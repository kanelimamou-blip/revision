"use strict";
// Espace « Jeux » du CE1 au CM2 : on joue avec le programme de sa classe.
// Calcul éclair, Vrai ou faux, Memory des leçons, Écoute l'anglais, Le bon ordre, Le grand défi (toutes matières).
// Les questions viennent des générateurs (GEN, FAITS, VOCAB_EN) : elles changent à chaque partie. Records gardés dans S.jeux.
(() => {
  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  const R = Math.random, pick = (a) => a[Math.floor(R() * a.length)], mel = (a) => shuffle(a);
  const cap = (s) => s.charAt(0).toUpperCase() + s.slice(1);
  const fill = (t, a, b) => t.replace(/\{a\}/g, a).replace(/\{b\}/g, b).replace(/\{A\}/g, cap(a)).replace(/\{B\}/g, cap(b));
  const lv = () => String(S.level || "CE2"), lvi = () => ["CE1", "CE2", "CM1", "CM2"].indexOf(lv());
  const J = () => (S.jeux = S.jeux || { best: {}, parties: 0, trophees: 0 });
  let tick = null, partie = 0; const stop = () => { if (tick) clearInterval(tick); tick = null; partie++; };
  // chaque partie a son numéro : un délai resté d'une partie précédente ne doit rien écrire sur la suivante
  const garde = (f) => { const n = partie; return (...a) => (n === partie ? f(...a) : null); };
  window.addEventListener("hashchange", stop);

  const JEUX = [
    { id: "calcul", ico: "⚡", t: "Calcul éclair", d: "60 secondes pour faire un maximum de calculs.", libre: true },
    { id: "vraifaux", ico: "✅", t: "Vrai ou faux ?", d: "Des phrases de tes leçons : vrai ou faux ? Vite !", libre: true },
    { id: "memory", ico: "🃏", t: "Memory des leçons", d: "Retourne les cartes et retrouve les paires." },
    { id: "ecoute", ico: "🎧", t: "Écoute l'anglais", d: "Écoute le mot anglais et trouve ce qu'il veut dire." },
    { id: "ordre", ico: "🔢", t: "Le bon ordre", d: "Touche les nombres du plus petit au plus grand." },
    { id: "defi", ico: "🏆", t: "Le grand défi", d: "Toutes les matières mélangées, 90 secondes. Le jeu des champions !" },
  ];
  const ouvert = (j) => j.libre || isPremium();

  const fin = (id, score, unite, rejouer) => {
    const st = J(), avant = st.best[id] || 0, record = score > avant;
    st.parties++; if (record) { st.best[id] = score; if (avant) st.trophees++; }
    const n = score >= 15 ? 3 : score >= 8 ? 2 : score > 0 ? 1 : 0; 
    store.save();
    $view.innerHTML = `<div class="card jeu-fin"><p class="kid-etoiles">${"⭐".repeat(n)}${"☆".repeat(3 - n)}</p>
      <p class="kid-big">${score} ${unite}</p>
      ${record ? `<p class="jeu-record">🏆 Nouveau record !${avant ? ` (avant : ${avant})` : ""}</p>` : `<p class="muted">Ton record : <b>${avant}</b>. Tu peux le battre !</p>`}
      <div class="kid-btns"><button class="btn" id="rejoue">🔄 Rejouer</button><a class="btn alt" href="#jeux">🎮 Autres jeux</a></div></div>`;
    $view.querySelector("#rejoue").onclick = () => { stop(); rejouer(); };
  };
  const entete = (t, extra = "") => `<div class="jeu-haut"><a class="btn alt petit" href="#jeux">✖</a><b>${t}</b><span class="jeu-chrono" id="chrono"></span><span class="jeu-score" id="score">${extra}</span></div>`;
  const chrono = (sec, onEnd) => { if (tick) clearInterval(tick); let t = sec; const el = () => $view.querySelector("#chrono");
    const aff = () => { if (el()) { el().textContent = `⏱️ ${t}`; el().classList.toggle("urgent", t <= 10); } };
    aff(); tick = setInterval(() => { t--; aff(); if (t <= 0) { stop(); onEnd(); } }, 1000); };
  const flash = (ok) => { const b = document.createElement("div"); b.className = "jeu-flash " + (ok ? "ok" : "ko"); b.textContent = ok ? "✔" : "✖"; document.body.appendChild(b); setTimeout(() => b.remove(), 450); };

  // ---------- question à 4 choix générique (calcul, défi)
  const qcm4 = (titre, sec, fab, id, unite) => () => {
    let score = 0, serie = 0;
    const suivante = garde(() => { const g = fab(); if (!g) return suivante();
      const c = mel([g.ok, ...g.faux.slice(0, 3)]);
      $view.querySelector("#zone").innerHTML = `<p class="jeu-q">${esc(g.q)}</p>${g.sub ? `<p class="small muted">${esc(g.sub)}</p>` : ""}<div class="jeu-choix">${c.map((x) => `<button class="choice jeu-c">${esc(x)}</button>`).join("")}</div>`;
      $view.querySelectorAll(".jeu-c").forEach((b, k) => (b.onclick = () => { const ok = c[k] === g.ok; flash(ok);
        if (ok) { serie++; score += serie >= 5 ? 2 : 1; } else serie = 0;
        $view.querySelector("#score").textContent = `${score} pt${score > 1 ? "s" : ""}${serie >= 3 ? ` · 🔥${serie}` : ""}`; suivante(); })); });
    $view.innerHTML = `${entete(titre, "0 pt")}<div class="card" id="zone"></div><p class="small muted">5 bonnes réponses de suite : chaque bonne réponse rapporte 2 points.</p>`;
    suivante(); chrono(sec, () => fin(id, score, "points", qcm4(titre, sec, fab, id, unite)));
  };

  // ---------- calcul mental adapté à la classe
  const ent = (a, b) => a + Math.floor(R() * (b - a + 1));
  const proches = (n, pas = 1) => { const s = new Set(); while (s.size < 3) { const d = ent(1, 3) * pas * (R() < 0.5 ? -1 : 1); if (n + d >= 0 && n + d !== n) s.add(n + d); } return [...s]; };
  const fmt = (x) => String(Math.round(x * 100) / 100).replace(".", ",");
  const calcul = () => {
    const i = lvi(), k = pick(i === 0 ? ["+", "+", "-"] : i === 1 ? ["+", "-", "×", "×"] : i === 2 ? ["+", "-", "×", "×", ":"] : ["×", ":", "+d", "%", "-", "×10"]);
    let q, r;
    if (k === "+") { const m = [20, 100, 1000, 10000][i], a = ent(1, m / 2), b = ent(1, m / 2); q = `${a} + ${b}`; r = a + b; }
    else if (k === "-") { const m = [20, 100, 1000, 10000][i], a = ent(m / 4, m), b = ent(1, a); q = `${a} − ${b}`; r = a - b; }
    else if (k === "×") { const a = ent(2, i < 2 ? 10 : 12), b = ent(2, i === 1 ? 5 + 5 * (R() < 0.5) : 10); q = `${a} × ${b}`; r = a * b; }
    else if (k === ":") { const b = ent(2, 10), r0 = ent(2, 10); q = `${b * r0} : ${b}`; r = r0; }
    else if (k === "+d") { const a = ent(1, 99) / 10, b = ent(1, 99) / 10; q = `${fmt(a)} + ${fmt(b)}`; r = Math.round((a + b) * 10) / 10;
      return { q, ok: fmt(r), faux: [fmt(r + 1), fmt(r - 0.1 > 0 ? r - 0.1 : r + 0.2), fmt(r + 0.1)] }; }
    else if (k === "%") { const p = pick([10, 25, 50, 20]), n = pick([100, 200, 400, 1000, 500, 2000]); q = `${p} % de ${n}`; r = (p * n) / 100; return { q, ok: String(r), faux: proches(r, r >= 100 ? 10 : 5).map(String) }; }
    else { const a = ent(2, 99), m = pick([10, 100, 1000]); q = `${a} × ${m}`; r = a * m; return { q, ok: String(r), faux: [a * m * 10, a * (m / 10 || 1), a + m].filter((x) => x !== r).concat([r + 1]).slice(0, 3).map(String) }; }
    return { q: q + " = ?", ok: String(r), faux: proches(r, r > 50 && R() < 0.4 ? 10 : 1).map(String) };
  };

  // ---------- grand défi : questions générées de toutes les matières de la classe
  const defi = () => { const subs = subjectsOf(S.level).filter((s) => (GEN[s.id] || []).length); const s = pick(subs); if (!s) return calcul();
    const g = genQuestions(s.id, 1)[0]; if (!g) return null; return { q: g.q, sub: s.name, ok: g.c[g.a], faux: g.c.filter((_, k) => k !== g.a) }; };

  // ---------- faits des leçons (sciences, histoire, géo, vivre ensemble)
  const tables = () => (typeof FAITS === "undefined" ? [] : Object.entries(FAITS).filter(([sid]) => sid.startsWith(lv().toLowerCase() + "-")).flatMap(([sid, chs]) => chs.map((c) => ({ sid, ch: c[0], ph: c[3], rows: c[4].map((l) => l.split("|")) }))));
  const phrase = () => { const t = pick(tables()); if (!t) return null; const [a, b] = pick(t.rows);
    if (R() < 0.5) return { txt: fill(t.ph, a, b) + ".", vrai: true, juste: fill(t.ph, a, b) + ".", ch: t.ch };
    const autres = t.rows.filter((x) => x[1] !== b); if (!autres.length) return null; const [, b2] = pick(autres);
    return { txt: fill(t.ph, a, b2) + ".", vrai: false, juste: fill(t.ph, a, b) + ".", ch: t.ch }; };
  const vraifaux = () => {
    let score = 0, serie = 0;
    const suivante = garde(() => { const p = phrase(); if (!p) return go("jeux");
      $view.querySelector("#zone").innerHTML = `<p class="small muted">${esc(p.ch)}</p><p class="jeu-q">${esc(p.txt)}</p>
        <div class="jeu-vf"><button class="jeu-v" data-v="1">✅ Vrai</button><button class="jeu-f" data-v="0">❌ Faux</button></div><p class="small" id="corr"></p>`;
      $view.querySelectorAll("[data-v]").forEach((b) => (b.onclick = () => { const ok = (b.dataset.v === "1") === p.vrai; flash(ok);
        if (ok) { serie++; score += serie >= 5 ? 2 : 1; } else { serie = 0; }
        $view.querySelector("#score").textContent = `${score} pt${score > 1 ? "s" : ""}${serie >= 3 ? ` · 🔥${serie}` : ""}`;
        if (!ok && !p.vrai) { $view.querySelector("#corr").innerHTML = `C'était faux : <b>${esc(p.juste)}</b>`; setTimeout(suivante, 1400); } else suivante(); })); });
    $view.innerHTML = `${entete("Vrai ou faux ?", "0 pt")}<div class="card" id="zone"></div>`;
    suivante(); chrono(60, () => fin("vraifaux", score, "points", vraifaux));
  };

  // ---------- memory : 6 paires d'une leçon (ou de mots anglais)
  const memory = (src) => {
    if (!src) { const ts = tables(), en = typeof VOCAB_EN !== "undefined" ? (VOCAB_EN[lv()] || []).filter((c) => !c.forme) : [];
      $view.innerHTML = `${entete("Memory des leçons")}<p class="muted">Choisis une leçon :</p><div class="kid-grille">
        ${en.length ? `<button class="kid-tuile" data-m="en"><span class="kid-ico">🇬🇧</span><b>Mots anglais</b></button>` : ""}
        ${ts.map((t, k) => `<button class="kid-tuile" data-m="${k}"><span class="kid-ico">🃏</span><b>${esc(t.ch)}</b></button>`).join("")}</div>`;
      $view.querySelectorAll("[data-m]").forEach((b) => (b.onclick = () => memory(b.dataset.m))); return; }
    let paires;
    if (src === "en") { const c = pick((VOCAB_EN[lv()] || []).filter((x) => !x.forme)); paires = mel(c.mots).slice(0, 6); }
    else { const t = tables()[+src]; const vus = new Set(); paires = mel(t.rows).filter(([a, b]) => !vus.has(b) && vus.add(b)).slice(0, 6); }
    const cartes = mel(paires.flatMap(([a, b], k) => [{ k, t: cap(a), en: src === "en" }, { k, t: cap(b) }]));
    let ouvertes = [], trouvees = 0, coups = 0, bloque = false, t0 = Date.now();
    $view.innerHTML = `${entete("Memory", "0 coup")}<div class="memory">${cartes.map((c, i) => `<button class="mem" data-i="${i}"><span>${esc(c.t)}</span></button>`).join("")}</div>
      <p class="small muted">Retrouve chaque mot et ce qui va avec.${src === "en" ? " Les mots anglais sont lus à voix haute." : ""}</p>`;
    $view.querySelectorAll(".mem").forEach((b) => (b.onclick = () => { const i = +b.dataset.i, c = cartes[i];
      if (bloque || b.classList.contains("vu") || ouvertes.includes(i)) return;
      b.classList.add("vu"); ouvertes.push(i); if (c.en && globalThis.kidParler) kidParler([[c.t, "en"]]);
      if (ouvertes.length < 2) return;
      coups++; $view.querySelector("#score").textContent = `${coups} coup${coups > 1 ? "s" : ""}`;
      const [x, y] = ouvertes.map((j) => cartes[j]);
      if (x.k === y.k) { ouvertes.forEach((j) => $view.querySelector(`[data-i="${j}"]`).classList.add("ok")); ouvertes = []; trouvees++; flash(true);
        if (trouvees === paires.length) setTimeout(() => fin("memory", Math.max(1, 20 - Math.max(0, coups - paires.length)), "points (moins tu fais de coups, plus tu gagnes)", () => memory(src)), 600); }
      else { bloque = true; setTimeout(() => { ouvertes.forEach((j) => $view.querySelector(`[data-i="${j}"]`).classList.remove("vu")); ouvertes = []; bloque = false; }, 900); } }));
  };

  // ---------- écoute l'anglais : 10 mots entendus
  const ecoute = () => {
    const chs = typeof VOCAB_EN !== "undefined" ? (VOCAB_EN[lv()] || []).filter((c) => !c.forme) : []; if (!chs.length) return go("jeux");
    const tous = chs.flatMap((c) => c.mots); let n = 0, score = 0, mot = null;
    const dire = () => (globalThis.kidParler ? kidParler([[mot[0], "en"]]) : null);
    const suivante = garde(() => { if (n >= 10) return fin("ecoute", score, "bonnes réponses sur 10", ecoute);
      n++; const c = pick(chs); mot = pick(c.mots); const faux = mel([...new Set(tous.map((x) => x[1]))].filter((x) => x !== mot[1])).slice(0, 3), ch = mel([mot[1], ...faux]);
      $view.querySelector("#zone").innerHTML = `<p class="small muted">Mot ${n} sur 10 · ${esc(c.t)}</p><button class="jeu-ecoute" id="re">🔊 Écouter le mot</button>
        <p class="small muted">Tu n'entends rien ? Monte le son ou touche <a href="#" id="voir">voir le mot</a>.</p><div class="jeu-choix">${ch.map((x) => `<button class="choice jeu-c">${esc(x)}</button>`).join("")}</div>`;
      $view.querySelector("#re").onclick = dire; $view.querySelector("#voir").onclick = (e) => { e.preventDefault(); e.target.outerHTML = `<b>${esc(mot[0])}</b>`; };
      $view.querySelectorAll(".jeu-c").forEach((b, k) => (b.onclick = () => { const ok = ch[k] === mot[1]; flash(ok); if (ok) score++;
        $view.querySelector("#score").textContent = `${score} ⭐`;
        if (!ok) { $view.querySelector("#zone").insertAdjacentHTML("beforeend", `<p>« ${esc(mot[0])} » veut dire <b>${esc(mot[1])}</b>.</p>`); setTimeout(suivante, 1500); } else setTimeout(suivante, 300); }));
      setTimeout(dire, 250); });
    $view.innerHTML = `${entete("Écoute l'anglais", "0 ⭐")}<div class="card" id="zone"></div>`; suivante();
  };

  // ---------- le bon ordre : ranger 5 nombres (ou dates) du plus petit au plus grand
  const ordre = () => {
    let score = 0;
    const serie = garde(() => { const i = lvi(), m = [100, 1000, 100000, 1000000][i], s = new Set();
      const dec = i === 3 && R() < 0.4; while (s.size < 5) s.add(dec ? ent(1, 999) / 100 : ent(1, m));
      const ns = [...s], tri = ns.slice().sort((a, b) => a - b); let pos = 0;
      $view.querySelector("#zone").innerHTML = `<p class="jeu-q">Du plus petit au plus grand :</p><div class="jeu-ordre">${mel(ns).map((x) => `<button class="choice jeu-n" data-n="${x}">${dec ? fmt(x) : x.toLocaleString("fr-FR")}</button>`).join("")}</div>`;
      $view.querySelectorAll(".jeu-n").forEach((b) => (b.onclick = () => { if (+b.dataset.n === tri[pos]) { b.classList.add("ok"); b.disabled = true; pos++;
        if (pos === 5) { score++; flash(true); $view.querySelector("#score").textContent = `${score} série${score > 1 ? "s" : ""}`; setTimeout(serie, 250); } }
        else { flash(false); b.classList.add("ko"); setTimeout(() => b.classList.remove("ko"), 400); } })); });
    $view.innerHTML = `${entete("Le bon ordre", "0 série")}<div class="card" id="zone"></div>`; serie(); chrono(60, () => fin("ordre", score, "séries rangées", ordre));
  };

  const LANCE = { calcul: qcm4("Calcul éclair", 60, calcul, "calcul"), defi: qcm4("Le grand défi", 90, defi, "defi"), vraifaux, memory: () => memory(), ecoute, ordre };
  ROUTES.jeux = (id) => {
    stop();
    const j = JEUX.find((x) => x.id === id);
    if (j && ouvert(j)) return LANCE[id]();
    const st = J();
    $view.innerHTML = `<div class="kid-titre" style="background:#ffe9a8"><span class="kid-ico">🎮</span><h1>Les jeux</h1></div>
      <p class="muted">On joue avec les leçons du ${esc(lv())}. Les questions changent à chaque partie : bats tes records !</p>
      <p>🏅 Parties jouées : <b>${st.parties}</b> · 🏆 Records battus : <b>${st.trophees}</b></p>
      <div class="kid-grille">${JEUX.filter((x) => x.id !== "ecoute" || typeof VOCAB_EN !== "undefined").map((x) => `<a class="kid-tuile jeu-tuile" href="#jeux/${x.id}"><span class="kid-ico">${x.ico}</span><b>${x.t}${ouvert(x) ? "" : " 🔒"}</b>
        <small>${x.d}</small>${st.best[x.id] ? `<small class="jeu-best">Record : ${st.best[x.id]}</small>` : ""}</a>`).join("")}</div>
      ${!isPremium() ? `<p class="small muted">🔒 Les autres jeux s'ouvrent quand un parent débloque l'appli.</p>` : ""}
      <a class="btn alt" href="#accueil">↩ Retour</a>`;
    if (j && !ouvert(j)) $view.insertAdjacentHTML("afterbegin", `<a class="trial" href="#premium">🔒 Ce jeu s'ouvre quand l'appli est débloquée. Demande à un parent.</a>`);
  };
})();
