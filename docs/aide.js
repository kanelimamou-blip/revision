"use strict";
// « Je bloque sur un exercice » : l'élève tape, colle, dicte ou photographie l'énoncé. L'appli retrouve le chapitre
// (même moteur de recherche que l'assistant) et donne une aide en 3 niveaux : un indice, la méthode pas à pas,
// puis un exercice semblable entièrement corrigé. Tout reste sur le téléphone, gratuit, sans IA :
// l'appli ne résout pas l'exercice exact de l'élève, elle l'amène à le résoudre lui-même.
(() => {
  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  let IX = null, IXL = null;
  // exercices et sujets guidés de la classe, découpés partie par partie pour trouver le plus proche
  function indexExos() {
    if (IX && IXL === S.level) return IX;
    const subs = subjectsOf(S.level), docs = [];
    for (const e of [...exercisesOf(S.level), ...annalesOf(S.level)]) (e.guided || []).forEach((p, k) => {
      const sid = (subs.find((s) => s.name === e.subject) || {}).id;
      docs.push({ e, k, p, sid, text: [e.title || "", p.title, p.context || "", ...p.steps.map((s) => `${s.q} ${s.c[s.a]} ${s.e}`)].join(" ") });
    });
    const df = new Map();
    for (const d of docs) { d.tf = new Map(); for (const w of tokens(d.text)) d.tf.set(w, (d.tf.get(w) || 0) + 1); d.len = [...d.tf.values()].reduce((a, b) => a + b, 0) || 1; for (const w of d.tf.keys()) df.set(w, (df.get(w) || 0) + 1); }
    IX = { docs, df, n: docs.length, avg: docs.reduce((a, d) => a + d.len, 0) / (docs.length || 1) }; IXL = S.level;
    return IX;
  }
  function proche(texte, sid) {
    const ix = indexExos(), qt = [...new Set(tokens(texte))];
    return ix.docs.map((d) => [score(ix, d, qt) * (sid && d.sid !== sid ? 0.5 : 1), d]).filter(([s]) => s > 1).sort((a, b) => b[0] - a[0]).slice(0, 2).map(([, d]) => d);
  }

  function viewAide() {
    $view.innerHTML = `<h1>🆘 Je bloque sur un exercice</h1>
      <p class="muted">Écris, colle, dicte ou prends en photo ton exercice. Je retrouve le chapitre et je t'aide en 3 niveaux : un indice, la méthode, puis un exercice semblable corrigé. Essaie toujours le niveau 1 avant le suivant !</p>
      <form id="ask" class="card"><textarea id="ain" rows="5" maxlength="1500" placeholder="Ex. : Soit f(x) = x³ − 3x + 1. Étudier les variations de f et donner l'équation de la tangente en 0."></textarea>
        <div class="row" style="gap:8px"><label class="btn alt" style="flex:1;text-align:center">📸 Photo<input type="file" id="aph" accept="image/*" capture="environment" hidden></label><button class="btn" style="flex:2">M'aider</button></div>
        <p class="small" id="amsg"></p></form><div id="ares"></div>`;
    const input = document.getElementById("ain"), msg = document.getElementById("amsg");
    const go = (t) => { if (!t.trim()) { msg.textContent = "Écris ou photographie d'abord ton exercice."; return; } msg.textContent = ""; aider(t); };
    document.getElementById("ask").onsubmit = (e) => { e.preventDefault(); go(input.value); };
    if (typeof assistVoice === "function") { assistVoice(input, (t) => go(t)); }
    document.getElementById("aph").onchange = async (e) => {
      const f = e.target.files[0]; if (!f) return;
      try {
        msg.className = "small"; msg.textContent = "Lecture de la photo…";
        const im = await EDT_IMPORT.reduire(f, 2000), { texte } = await EDT_IMPORT.ocr(EDT_IMPORT.nettoyer(im), (t) => (msg.textContent = t));
        input.value = texte.replace(/\n{2,}/g, "\n").trim(); msg.textContent = "Vérifie le texte lu (corrige si besoin), puis touche « M'aider ».";
      } catch (err) { msg.className = "small msg-ko"; msg.textContent = "Lecture impossible : écris l'énoncé ou ses mots importants."; }
    };
  }

  function aider(texte) {
    const r = answer(texte), box = document.getElementById("ares");
    if (r.empty || r.none) { box.innerHTML = `<div class="card"><p>Je n'ai pas reconnu le chapitre. Ajoute les mots importants de l'énoncé (« dérivée », « pH », « dissertation », « présent perfect »…) ou le nom de la matière.</p></div>`; return; }
    const m = r.main, sid = m.sid, fiche = m.kind === "fiche" ? m : null, p = fiche ? m.p : m.pch;
    const meth = r.meth || (fiche && fiche.lines.find((l) => l[0] === "methode")), ex = proche(texte, sid);
    const q0 = r.qcm && r.qcm[0] ? remix(r.qcm[0]) : null, indice = r.keys[0], rappels = r.keys.slice(1, 3);
    if (typeof markDone === "function") markDone("assistant");
    box.innerHTML = `<div class="card"><p class="small muted">Chapitre reconnu</p><h2>${esc(m.sname)} · ${esc(m.title)}</h2></div>
      <details class="card niv" open><summary><b>💡 Niveau 1 : un indice</b></summary><p>Pense à ceci :</p><p><b>${esc(indice || "")}</b></p>
        <p class="small muted">Relis l'énoncé : quelle donnée te permet d'utiliser ce point du cours ? Écris la première ligne de ta réponse avant d'ouvrir le niveau 2.</p></details>
      <details class="card niv"><summary><b>🛠️ Niveau 2 : la méthode pas à pas</b></summary>
        ${meth ? `<p><b>${esc(meth[1])}</b></p><ol class="steps">${meth[2].map((l) => `<li>${esc(l)}</li>`).join("")}</ol>` : `<ul class="steps">${[indice, ...rappels].filter(Boolean).map((k) => `<li>${esc(k)}</li>`).join("")}</ul>`}
        ${r.trap ? `<p>⚠️ <b>Piège :</b> ${esc(r.trap[1])}</p>` : ""}${rappels.length && meth ? `<p class="small"><b>Rappels du cours :</b> ${rappels.map(esc).join(" · ")}</p>` : ""}
        <p class="small muted">Applique chaque étape à TON exercice. Bloqué à une étape ? Ouvre le niveau 3.</p></details>
      <details class="card niv"><summary><b>✅ Niveau 3 : un exercice semblable corrigé</b></summary>
        ${ex.length ? ex.map((d) => `<p class="small muted">${esc(d.e.title || d.e.exam + " " + d.e.year)} · ${esc(d.p.title)}</p>${d.p.context ? `<p><b>${esc(d.p.context)}</b></p>` : ""}
          <ol class="steps">${d.p.steps.map((s) => `<li>${esc(s.q)}<br><span class="msg-ok">→ ${esc(s.c[s.a])}</span><br><span class="small muted">${esc(s.e)}</span></li>`).join("")}</ol>
          <a class="btn alt small" href="#sujet/${d.e.id}">Le refaire moi-même, noté${isPremium() || d.e.free ? "" : " 🔒"}</a>`).join("<hr>")
        : r.ex ? `<p><b>${esc(r.ex[1])}</b></p><ol class="steps">${r.ex[2].map((l) => `<li>${esc(l)}</li>`).join("")}</ol>` : `<p class="small">Pas encore d'exercice corrigé très proche : lis le cours détaillé ci-dessous, il contient un exemple corrigé.</p>`}
        ${r.ex && ex.length ? `<p class="small"><b>Autre exemple du cours :</b> ${esc(r.ex[1])}</p><ol class="steps small">${r.ex[2].map((l) => `<li>${esc(l)}</li>`).join("")}</ol>` : ""}</details>
      <div class="card"><h2>Ensuite</h2>
        ${q0 ? `<div class="mini" id="aq">${questionBlock(q0)}</div>` : ""}
        <div class="row wrap">${r.notion ? `<a class="btn alt small" href="#notion/${r.notion.id}">📖 Cours détaillé${isPremium() || r.notion.free ? "" : " 🔒"}</a>` : ""}${p !== undefined && p !== null ? `<a class="btn alt small" href="#quiz/${sid}/${p}">✏️ QCM sur ce chapitre</a>` : ""}<a class="btn alt small" href="#assistant/${encodeURIComponent(m.title)}">💬 Pose une question</a></div></div>`;
    const aq = document.getElementById("aq"); if (aq) bindQuestion(aq, q0, () => {});
    box.scrollIntoView({ block: "start" });
  }
  ROUTES.aide = viewAide;
})();
