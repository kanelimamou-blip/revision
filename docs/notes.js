"use strict";
// Mes notes : l'élève saisit ses notes de devoirs et de compositions. L'appli calcule ses moyennes, prévoit la moyenne
// de fin de trimestre (tendance des notes + maîtrise des chapitres dans l'appli), la compare à l'objectif, réajuste la
// trajectoire (les matières qui rapportent le plus de points passent en tête) et propose des pistes d'orientation.
(() => {
  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  const nf = (x, d = 2) => (Math.round(x * 10 ** d) / 10 ** d).toLocaleString("fr-FR");
  const TYPES = ["Devoir", "Composition", "Interrogation", "Exposé"];
  const subsN = () => subjectsOf(S.level).filter((s) => !/annales/.test(s.id));
  const trimestre = () => { const m = new Date().getMonth(); return m >= 8 || m === 0 ? 1 : m <= 3 ? 2 : 3; };
  const cle = (n) => n.sid || "x:" + n.nom;
  const nomDe = (k) => (k.startsWith("x:") ? k.slice(2) : subjName(k));
  // coefficients officiels du BAC par série (Office du BAC), repris en 1re ; l'élève peut les changer
  const COEF = { S1: { francais: 3, philo: 2, hg: 2, anglais: 2, maths: 8, pc: 8, svt: 2 }, S2: { francais: 3, philo: 2, hg: 2, anglais: 2, maths: 5, pc: 6, svt: 6 },
    S3: { francais: 3, philo: 2, anglais: 2, maths: 8, pc: 8 }, S4: { francais: 3, philo: 2, hg: 2, anglais: 2, maths: 5, pc: 5, svt: 5 }, S5: { francais: 3, philo: 2, hg: 2, anglais: 2, maths: 5, pc: 5, svt: 5 },
    L1a: { francais: 6, philo: 6, hg: 2, anglais: 2, maths: 2 }, L1b: { francais: 6, philo: 6, hg: 2, anglais: 3, maths: 2, espagnol: 2 }, "L'": { francais: 6, philo: 4, hg: 2, anglais: 4, maths: 2, espagnol: 4 },
    L2: { francais: 5, philo: 6, hg: 6, anglais: 4, maths: 2, espagnol: 2, svt: 2 }, G: { francais: 3, eco: 6, philo: 2, hg: 2, maths: 5, anglais: 3, compta: 6 } };
  const famille = (k) => (k.match(/maths|pc|svt|francais|philo|hg|anglais|espagnol|eco|compta/) || [])[0];
  const officiel = (k) => { const t = COEF[String(S.level).split(" ")[1]]; return t && /^(1ère|Tle)/.test(S.level) ? t[famille(k)] : undefined; };
  const coef = (k) => (S.coefs || {})[k] ?? officiel(k) ?? 2;
  const sur20 = (n) => (20 * n.n) / (n.sur || 20);
  const notesDe = (k, tr) => (S.notes || []).filter((n) => cle(n) === k && n.l === S.level && (!tr || n.tr === tr)).sort((a, b) => a.d.localeCompare(b.d));

  // moyenne d'une matière sur le trimestre : moyenne des devoirs, puis (devoirs + composition) / 2 quand la composition est là
  function moyMatiere(k, tr) {
    const l = notesDe(k, tr); if (!l.length) return null;
    const dev = l.filter((n) => n.t !== "Composition"), comp = l.filter((n) => n.t === "Composition");
    const m = (a) => a.reduce((s, n) => s + sur20(n), 0) / a.length;
    return dev.length && comp.length ? (m(dev) + m(comp)) / 2 : m(dev.length ? dev : comp);
  }
  // prévision : tendance des dernières notes, rapprochée de la maîtrise des chapitres travaillés dans l'appli
  function prevision(k) {
    const l = notesDe(k).map(sur20), moy = moyMatiere(k, trimestre());
    if (moy === null && !l.length) return null;
    let pente = 0;
    if (l.length >= 2) { const n = l.length, xm = (n - 1) / 2, ym = l.reduce((a, b) => a + b, 0) / n; pente = l.reduce((a, y, x) => a + (x - xm) * (y - ym), 0) / l.reduce((a, y, x) => a + (x - xm) ** 2, 0); }
    let p = (moy ?? l[l.length - 1]) + Math.max(-2, Math.min(2, pente));
    const qs = k.startsWith("x:") ? [] : qsOf(k).filter((q) => S.stats[q.id]);
    if (qs.length >= 10) p = 0.75 * p + 0.25 * (20 * qs.filter((q) => S.stats[q.id].last).length) / qs.length;
    return Math.max(0, Math.min(20, p));
  }
  const matieresNotees = () => [...new Set((S.notes || []).filter((n) => n.l === S.level).map(cle))];
  function generale(f) { let s = 0, c = 0; for (const k of matieresNotees()) { const m = f(k); if (m !== null) { s += m * coef(k); c += coef(k); } } return c ? s / c : null; }
  // points de moyenne générale à gagner en remontant une matière jusqu'à l'objectif : sert à réajuster la trajectoire
  globalThis.notesPriorite = () => {
    const obj = S.objectif || 12, tot = matieresNotees().reduce((a, k) => a + coef(k), 0) || 1, out = {};
    for (const k of matieresNotees()) { const p = prevision(k); if (p !== null && !k.startsWith("x:")) out[k] = Math.max(0, ((obj - p) * coef(k)) / tot); }
    return out;
  };

  // pistes d'orientation : grandes familles de matières, à discuter avec le professeur principal
  const FAM = [["sciences", "🔬 Sciences", /maths|pc|svt/, "Série S ; après le BAC : médecine, pharmacie, écoles d'ingénieurs, informatique, agronomie, sciences à l'université."],
    ["lettres", "📚 Lettres et sciences humaines", /francais|philo|hg|anglais|espagnol/, "Série L ; après le BAC : droit, journalisme, langues, lettres, histoire, enseignement, sciences politiques."],
    ["gestion", "💼 Économie et gestion", /eco|compta|maths/, "Série G ; après le BAC : gestion, comptabilité, banque, commerce, logistique, écoles de commerce."]];
  function orientation() {
    const r = FAM.map(([id, nom, rx, txt]) => { const ks = matieresNotees().filter((k) => rx.test(k)); const ms = ks.map((k) => prevision(k)).filter((x) => x !== null); return { id, nom, txt, n: ms.length, m: ms.length ? ms.reduce((a, b) => a + b, 0) / ms.length : null }; }).filter((f) => f.m !== null && f.n >= 2);
    if (!r.length) return `<p class="small muted">Ajoute des notes dans au moins deux matières d'une même famille (sciences, lettres, gestion) pour voir tes pistes.</p>`;
    r.sort((a, b) => b.m - a.m);
    return r.map((f, i) => `<div style="padding:6px 0;border-bottom:1px solid var(--line)"><div class="row small"><b>${i === 0 ? "⭐ " : ""}${f.nom}</b><span>${nf(f.m, 1)} / 20</span></div><div class="bar"><i style="width:${f.m * 5}%"></i></div>${i === 0 ? `<p class="small">${esc(f.txt)}</p>` : ""}</div>`).join("") +
      `<p class="small muted">Ce sont des pistes d'après tes notes, pas une décision : parles-en avec ton professeur principal et ta famille, et regarde aussi ce qui te plaît.</p>`;
  }

  function viewNotes(arg) {
    S.notes = S.notes || []; S.coefs = S.coefs || {};
    if (arg === "coefs") return coefs();
    const tr = trimestre(), obj = S.objectif || 12, ks = matieresNotees(), gen = generale((k) => moyMatiere(k, tr)), prev = generale(prevision);
    const prio = Object.entries(notesPriorite()).filter(([, v]) => v > 0.05).sort((a, b) => b[1] - a[1]).slice(0, 3);
    const subs = subsN(), dernier = S.notes.filter((n) => n.l === S.level).slice(-1)[0] || {};
    $view.innerHTML = `<h1>📒 Mes notes</h1><p class="muted">Note chaque devoir et chaque composition : l'appli calcule ta moyenne, la prévoit pour la fin du trimestre et adapte ta trajectoire.</p>
      <div class="card"><div class="row"><div><p class="small muted">Moyenne ${tr}${tr === 1 ? "er" : "e"} trimestre</p><p class="count">${gen === null ? "–" : nf(gen)}</p></div><div style="text-align:right"><p class="small muted">Prévision fin de trimestre</p><p class="count">${prev === null ? "–" : nf(prev, 1)}</p></div></div>
        ${prev === null ? "" : `<p class="${prev >= obj ? "msg-ok" : "msg-ko"}">${prev >= obj ? `🎯 Au niveau de ton objectif (${obj}/20). Garde le rythme.` : `🎯 Objectif ${obj}/20 : il manque ${nf(obj - prev, 1)} point${obj - prev >= 2 ? "s" : ""}.`}</p>`}
        ${prio.length ? `<p class="small"><b>Là où tu gagnes le plus de points :</b> ${prio.map(([k]) => esc(nomDe(k))).join(", ")}. Ta trajectoire les met en tête de tes séances.</p><a class="btn alt small" href="#trajectoire">Voir ma trajectoire</a>` : ""}</div>
      <div class="card"><h2>➕ Ajouter une note</h2>
        <label class="small">Matière</label><select id="nm">${subs.map((s) => `<option value="${s.id}"${dernier.sid === s.id ? " selected" : ""}>${esc(s.name)}</option>`).join("")}<option value="autre">Autre matière…</option></select>
        <input id="nautre" placeholder="Nom de la matière (ex. : EPS)" hidden maxlength="40">
        <div class="row" style="gap:8px"><label class="small" style="flex:1">Type<select id="nt">${TYPES.map((t) => `<option>${t}</option>`).join("")}</select></label><label class="small" style="width:5.5rem">Trimestre<select id="ntr">${[1, 2, 3].map((t) => `<option${t === tr ? " selected" : ""}>${t}</option>`).join("")}</select></label></div>
        <div class="row" style="gap:8px"><label class="small" style="flex:1">Note<input id="nn" type="number" min="0" step="0.25" inputmode="decimal" placeholder="ex. 13,5"></label><label class="small" style="width:5.5rem">Sur<input id="ns" type="number" min="1" value="20"></label></div>
        <p class="small msg-ko" id="nmsg"></p><button class="btn" id="nadd">Enregistrer la note</button></div>
      ${ks.length ? `<h2>Par matière</h2>${ks.map((k) => { const m = moyMatiere(k, tr), p = prevision(k), l = notesDe(k);
        return `<div class="card"><div class="row"><b>${esc(nomDe(k))}</b><span class="small muted">coef. ${coef(k)}</span></div>
          <div class="row small"><span>Moyenne : <b>${m === null ? "–" : nf(m)}</b></span><span>Prévision : <b>${p === null ? "–" : nf(p, 1)}</b>${p !== null && m !== null ? (p > m + 0.2 ? " ↗" : p < m - 0.2 ? " ↘" : " →") : ""}</span></div>
          <div class="bar"><i style="width:${(p ?? m ?? 0) * 5}%"></i></div>
          <p class="small muted">${l.map((n) => `<span title="${esc(n.t)}">${n.t === "Composition" ? "🅲 " : ""}${nf(n.n, 2)}${n.sur && n.sur !== 20 ? "/" + n.sur : ""} <a href="#" class="nrm" data-i="${S.notes.indexOf(n)}" aria-label="Supprimer">✕</a></span>`).join(" · ")}</p>
          ${!k.startsWith("x:") && p !== null && p < obj ? `<a class="btn alt small" href="#devoir/${k}">🎯 Préparer le prochain devoir</a>` : ""}</div>`; }).join("")}
        <a class="btn alt" href="#notes/coefs">Régler les coefficients</a>` : `<div class="card"><p class="small muted">Aucune note pour l'instant. Ajoute ta dernière note de devoir pour commencer.</p></div>`}
      <h2>🧭 Pistes d'orientation</h2><div class="card">${orientation()}</div>
      <a class="btn alt" href="#accueil">Retour à l'accueil</a>`;
    const nm = document.getElementById("nm"), au = document.getElementById("nautre");
    nm.onchange = () => { au.hidden = nm.value !== "autre"; };
    document.getElementById("nadd").onclick = () => {
      const n = parseFloat(String(document.getElementById("nn").value).replace(",", ".")), sur = parseFloat(document.getElementById("ns").value) || 20, msg = document.getElementById("nmsg");
      if (isNaN(n) || n < 0 || n > sur) { msg.textContent = `Écris une note entre 0 et ${sur}.`; return; }
      if (nm.value === "autre" && !au.value.trim()) { msg.textContent = "Écris le nom de la matière."; return; }
      const rec = { n, sur, t: document.getElementById("nt").value, tr: +document.getElementById("ntr").value, d: today(), l: S.level, ...(nm.value === "autre" ? { nom: au.value.trim() } : { sid: nm.value }) };
      S.notes = [...S.notes, rec].slice(-300); store.save(); if (typeof markDone === "function") markDone("notes"); viewNotes();
    };
    $view.querySelectorAll(".nrm").forEach((a) => a.onclick = (e) => { e.preventDefault(); S.notes.splice(+a.dataset.i, 1); store.save(); viewNotes(); });
  }
  function coefs() {
    const ks = [...new Set([...subsN().map((s) => s.id), ...matieresNotees()])];
    $view.innerHTML = `<h1>Coefficients</h1><p class="muted">${COEF[String(S.level).split(" ")[1]] && /^(1ère|Tle)/.test(S.level) ? `Déjà réglés sur les coefficients officiels du BAC ${esc(String(S.level).split(" ")[1])}.` : "Mets les coefficients de ta classe (2 par défaut)."} Ton établissement peut en utiliser d'autres en classe : change-les si besoin. Ils servent à ta moyenne générale et à savoir où tu gagnes le plus de points.</p>
      <div class="card">${ks.map((k) => `<div class="row" style="gap:8px;padding:4px 0"><span style="flex:1">${esc(nomDe(k))}${officiel(k) !== undefined ? ` <span class="small muted">(BAC : ${officiel(k)})</span>` : ""}</span><input type="number" min="0" max="10" class="cf" data-k="${esc(k)}" value="${coef(k)}" style="width:64px"></div>`).join("")}</div>
      <a class="btn" href="#notes">Enregistrer</a><button class="btn alt" id="cfreset">Revenir aux coefficients officiels</button>`;
    document.getElementById("cfreset").onclick = () => { S.coefs = {}; store.save(); coefs(); };
    $view.querySelectorAll(".cf").forEach((x) => x.oninput = () => { S.coefs[x.dataset.k] = Math.max(0, +x.value || 0); store.save(); });
  }
  globalThis.notesCard = () => {
    const ks = matieresNotees();
    if (!ks.length) return `<a class="card lib-card" href="#notes"><b>📒 Mes notes</b><span class="small muted">Note tes devoirs : l'appli calcule ta moyenne, la prévoit et adapte ta trajectoire.</span></a>`;
    const g = generale((k) => moyMatiere(k, trimestre())), p = generale(prevision);
    return `<a class="card lib-card" href="#notes"><b>📒 Mes notes : moyenne ${g === null ? "–" : nf(g)}${p !== null ? ` · prévision ${nf(p, 1)}` : ""}</b><span class="small muted">Ajoute ta dernière note pour réajuster ta trajectoire.</span></a>`;
  };
  ROUTES.notes = viewNotes;
})();
