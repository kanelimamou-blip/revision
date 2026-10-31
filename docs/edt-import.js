"use strict";
// Importer son emploi du temps : photo, capture d'écran, fichier texte ou texte collé (WhatsApp…).
// La lecture de l'image (Tesseract, logiciel libre et gratuit) se fait sur le téléphone : l'image n'est envoyée nulle part.
// L'appli propose un brouillon que l'élève vérifie et corrige avant d'enregistrer ; la photo reste visible pour s'aider,
// ce qui sert surtout quand l'emploi du temps est écrit à la main (la lecture automatique y est moins sûre).
(() => {
  const norm = (s) => String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[’']/g, " ");
  const JOUR_RX = [[/^lun/, 1], [/^mard?i?$|^mardi/, 2], [/^merc?r?e?d?i?$|^mercredi/, 3], [/^jeu/, 4], [/^vend?r?e?d?i?$|^vendredi/, 5], [/^sam/, 6], [/^dim/, 0]];
  const jourDe = (w) => { const x = norm(w).replace(/[^a-z]/g, ""); if (x.length < 3) return null; for (const [r, d] of JOUR_RX) if (r.test(x)) return d; return null; };
  // heures : 8h, 8 h 30, 08h00, 8:30, 8H, 14h-16h, 8h à 10h
  const HEURE = /(?<!\d)([01]?\d|2[0-3])\s*(?:h|H|:)\s*([0-5]\d)?(?![\d])/g;
  const hhmm = (h, m) => `${String(+h).padStart(2, "0")}:${m || "00"}`;
  const heures = (s) => [...String(s).matchAll(HEURE)].map((m) => ({ t: hhmm(m[1], m[2]), i: m.index, j: m.index + m[0].length }));

  // matières : abréviations des emplois du temps sénégalais, rapprochées des matières de la classe
  const SYN = [
    [/^(maths?|mathemat\w*|mathe|mth)$/, "maths"], [/^(pc|spc|sp|pct|physique\w*|chimie|sc\s*ph\w*|sciences?\s*phys\w*)$/, "pc"],
    [/^(svt|sciences?\s*(de la vie|naturelles?)|sn|biologie|bio)$/, "svt"], [/^(francais|fr|franc|fran)$/, "francais"], [/^(philo\w*)$/, "philo"],
    [/^(hg|h\s*g|h\/g|h-g|histoire\w*|geo\w*|hist\w*|histo\w*|histoire\s*(et\s*)?geo\w*)$/, "hg"], [/^(anglais|ang|angl|english|lv1)$/, "anglais"],
    [/^(espagnol|esp|lv2)$/, "espagnol"], [/^(eco\w*|economie\w*)$/, "eco"], [/^(compta\w*|techniques?\s*compta\w*|tc)$/, "compta"],
  ];
  const AUTRES = [[/^(eps|sport)$/, "EPS"], [/^(arabe|ar)$/, "Arabe"], [/^(ecm|ec|edd|education\s*civique|civisme)$/, "Éducation civique"], [/^(info\w*|tic)$/, "Informatique"],
    [/^(allemand|all)$/, "Allemand"], [/^(latin|lat)$/, "Latin"], [/^(portugais|port)$/, "Portugais"], [/^(italien)$/, "Italien"], [/^(russe)$/, "Russe"], [/^(ef|economie\s*familiale)$/, "Économie familiale"],
    [/^(dessin|arts?\s*plastiques?)$/, "Dessin"], [/^(musique)$/, "Musique"], [/^(tp|travaux\s*pratiques)$/, "TP"], [/^(etude|permanence|perm)$/, "Étude"]];
  const lev = (a, b) => { const m = a.length, n = b.length, d = Array.from({ length: m + 1 }, (_, i) => [i]); for (let j = 1; j <= n; j++) d[0][j] = j;
    for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++) d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); return d[m][n]; };
  const LONGS = [["mathematiques", "maths"], ["physique", "pc"], ["francais", "francais"], ["philosophie", "philo"], ["histoire", "hg"], ["geographie", "hg"], ["anglais", "anglais"], ["espagnol", "espagnol"], ["economie", "eco"], ["comptabilite", "compta"]];
  function sidDe(cle, subs) {
    const ok = subs.filter((s) => !/annales/.test(s.id));
    return (ok.find((s) => s.id.split("-").includes(cle)) || ok.find((s) => s.id.includes(cle)) || {}).id || null;
  }
  // « Maths », « PC », « Hist-Géo », « Mathématiques » mal lu… → { sid } ou { nom }, sinon null
  function matiere(txt, subs) {
    const t = norm(txt).replace(/[^a-z\/\- ]/g, " ").replace(/\s+/g, " ").trim();
    if (!t || t.length < 2) return null;
    const essais = [t, ...t.split(/[ \/-]/).filter((w) => w.length >= 2)];
    for (const e of essais) {
      for (const [r, cle] of SYN) if (r.test(e)) { const sid = sidDe(cle, subs); if (sid) return { sid }; }
      for (const [r, nom] of AUTRES) if (r.test(e)) return { nom };
    }
    for (const e of essais) if (e.length >= 4 && e.length <= 6) for (const [l, cle] of [["philo", "philo"], ["maths", "maths"], ["math", "maths"], ["franc", "francais"], ["angl", "anglais"], ["hist", "hg"], ["compta", "compta"]]) if (lev(e, l) <= 1) { const sid = sidDe(cle, subs); if (sid) return { sid }; }
    for (const e of essais) if (e.length >= 6) for (const [l, cle] of LONGS) if (lev(e.slice(0, l.length + 1), l) <= 2) { const sid = sidDe(cle, subs); if (sid) return { sid }; }
    return null;
  }

  // Lecture ligne par ligne : « Lundi : 8h-10h Maths, 10h-12h Français » ou « Lundi » puis « 8h-10h Maths » en dessous
  function parLignes(texte, subs) {
    const edt = {}; let jour = null;
    for (const brut of String(texte).split(/\n+/)) {
      let ligne = brut;
      const premier = ligne.trim().split(/[\s:,;.\-]+/)[0];
      if (jourDe(premier) !== null) { jour = jourDe(premier); ligne = ligne.trim().slice(premier.length); }
      if (jour === null) continue;
      const hs = heures(ligne);
      for (let k = 0; k < hs.length; k++) {
        const h = hs[k], suite = hs[k + 1], fin = suite && /^\s*(-|–|—|à|a|au)?\s*$/.test(ligne.slice(h.j, suite.i)) ? suite : null;
        if (fin) k++;
        const apres = ligne.slice((fin || h).j, hs[k + 1] ? hs[k + 1].i : ligne.length), avant = k - (fin ? 1 : 0) === 0 ? ligne.slice(0, h.i) : "";
        const m = matiere(apres, subs) || matiere(avant, subs);
        if (m) (edt[jour] = edt[jour] || []).push({ d: h.t, f: fin ? fin.t : "", ...m });
      }
    }
    return finir(edt);
  }

  // Lecture d'un tableau (jours en colonnes, heures à gauche) à partir de la position des mots trouvés sur l'image
  function parTableau(mots, subs) {
    const cx = (w) => (w.x0 + w.x1) / 2, cy = (w) => (w.y0 + w.y1) / 2;
    const jours = []; for (const w of mots) { const d = jourDe(w.text); if (d !== null && !jours.some((j) => j.d === d)) jours.push({ d, x: cx(w), y: cy(w), w }); }
    if (jours.length < 2) return null;
    const gauche = Math.min(...jours.map((j) => j.w.x0)), haut = Math.min(...jours.map((j) => j.w.y0));
    // repères d'heures dans la colonne de gauche, regroupés par hauteur
    const hmots = mots.filter((w) => w.x1 <= gauche + 5 && heures(w.text).length);
    const lignes = [];
    for (const w of hmots.sort((a, b) => cy(a) - cy(b))) {
      const l = lignes[lignes.length - 1], ht = w.y1 - w.y0;
      // « 10h- » puis « 11h » en dessous dans la même case : un seul repère 10 h – 11 h
      if (l && (Math.abs(l.y - cy(w)) < ht * 0.8 || (/[-–à]$/.test(l.der) && w.y0 - l.y1 < ht * 1.2))) { l.t.push(...heures(w.text).map((h) => h.t)); l.y = (l.y + cy(w)) / 2; l.y1 = w.y1; l.der = w.text; }
      else lignes.push({ y: cy(w), y1: w.y1, t: heures(w.text).map((h) => h.t), der: w.text });
    }
    if (lignes.length < 2) return null;
    const mn = (t) => +t.slice(0, 2) * 60 + +t.slice(3);
    lignes.forEach((l, k) => { l.d = l.t[0]; const n = lignes[k + 1] && lignes[k + 1].t[0];
      // une fin mal lue (« 12h » lu « 17h ») : on prend le début du créneau suivant, sinon une heure
      l.f = l.t[1] && mn(l.t[1]) > mn(l.d) && mn(l.t[1]) - mn(l.d) <= 240 && (!n || mn(l.t[1]) <= mn(n)) ? l.t[1] : n && mn(n) > mn(l.d) ? n : hhmm(+l.d.slice(0, 2) + 1, l.d.slice(3)); });
    const cases = {};
    for (const w of mots) {
      if (w.y1 <= haut + 2 || jourDe(w.text) !== null || hmots.includes(w) || w.x1 <= gauche) continue;
      const col = jours.reduce((a, b) => (Math.abs(cx(w) - b.x) < Math.abs(cx(w) - a.x) ? b : a));
      const lg = lignes.reduce((a, b) => (Math.abs(cy(w) - b.y) < Math.abs(cy(w) - a.y) ? b : a));
      const k = col.d + "|" + lignes.indexOf(lg); (cases[k] = cases[k] || []).push(w.text);
    }
    const edt = {};
    for (const [k, txt] of Object.entries(cases)) {
      const [d, i] = k.split("|"), m = matiere(txt.join(" "), subs); if (!m) continue;
      (edt[d] = edt[d] || []).push({ d: lignes[i].d, f: lignes[i].f, ...m });
    }
    return finir(edt);
  }

  // tri, et fusion de deux heures qui se suivent dans la même matière (8h-9h Maths + 9h-10h Maths = 8h-10h Maths)
  function finir(edt) {
    for (const j of Object.keys(edt)) {
      const l = edt[j].sort((a, b) => a.d.localeCompare(b.d)), out = [];
      for (const c of l) { const p = out[out.length - 1]; if (p && p.f === c.d && (p.sid || p.nom) === (c.sid || c.nom)) p.f = c.f; else if (!p || p.d !== c.d) out.push({ ...c }); }
      edt[j] = out;
    }
    return edt;
  }
  const nb = (edt) => Object.values(edt || {}).reduce((a, l) => a + l.length, 0);

  // ---------- Lecture de l'image sur le téléphone (chargée seulement à la demande : environ 5 Mo la première fois)
  let worker = null;
  async function ocr(img, prog) {
    if (!globalThis.Tesseract) await new Promise((ok, ko) => { const s = document.createElement("script"); s.src = "vendor/tesseract/tesseract.min.js"; s.onload = ok; s.onerror = ko; document.head.appendChild(s); });
    if (!worker) worker = await Tesseract.createWorker("fra", 1, { workerPath: "vendor/tesseract/worker.min.js", corePath: "vendor/tesseract/", langPath: "vendor/tesseract/",
      logger: (m) => prog(m.status === "recognizing text" ? `Lecture de l'image… ${Math.round(m.progress * 100)} %` : "Préparation de la lecture (la première fois, environ 5 Mo)…") });
    const { data } = await worker.recognize(img, {}, { text: true, blocks: true });
    const mots = [];
    for (const b of data.blocks || []) for (const p of b.paragraphs) for (const l of p.lines) for (const w of l.words) if (w.text.trim()) mots.push({ text: w.text, ...w.bbox });
    return { texte: data.text || "", mots };
  }
  // image réduite : plus rapide à lire, et une copie légère gardée sur le téléphone pour s'aider à corriger
  function reduire(file, max) {
    return new Promise((ok, ko) => {
      const im = new Image(); im.onerror = ko;
      im.onload = () => { const k = Math.min(max > 1500 ? 3 : 1, max / Math.max(im.width, im.height)), c = document.createElement("canvas"); c.width = Math.round(im.width * k); c.height = Math.round(im.height * k);
        const g = c.getContext("2d"); g.fillStyle = "#fff"; g.fillRect(0, 0, c.width, c.height); g.drawImage(im, 0, 0, c.width, c.height); URL.revokeObjectURL(im.src); ok(c); };
      im.src = URL.createObjectURL(file);
    });
  }
  // noir et blanc, et on efface les traits du tableau : la lecture des cases devient bien plus sûre
  function nettoyer(src) {
    const c = document.createElement("canvas"); c.width = src.width; c.height = src.height;
    const g = c.getContext("2d"); g.drawImage(src, 0, 0);
    const W = c.width, H = c.height, img = g.getImageData(0, 0, W, H), a = img.data, lum = new Float32Array(W * H);
    let sum = 0; for (let i = 0; i < W * H; i++) sum += lum[i] = a[i * 4] * 0.3 + a[i * 4 + 1] * 0.59 + a[i * 4 + 2] * 0.11;
    const seuil = (sum / (W * H)) * 0.75, noir = new Uint8Array(W * H), trait = new Uint8Array(W * H);
    for (let i = 0; i < W * H; i++) noir[i] = lum[i] < seuil ? 1 : 0;
    for (let y = 0; y < H; y++) { let r = 0; for (let x = 0; x <= W; x++) { if (x < W && noir[y * W + x]) r++; else { if (r > W * 0.15) for (let k = x - r; k < x; k++) trait[y * W + k] = 1; r = 0; } } }
    for (let x = 0; x < W; x++) { let r = 0; for (let y = 0; y <= H; y++) { if (y < H && noir[y * W + x]) r++; else { if (r > H * 0.15) for (let k = y - r; k < y; k++) trait[k * W + x] = 1; r = 0; } } }
    for (let i = 0; i < W * H; i++) { const v = noir[i] && !trait[i] ? 0 : 255; a[i * 4] = a[i * 4 + 1] = a[i * 4 + 2] = v; }
    g.putImageData(img, 0, 0); return c;
  }
  const PHOTO = "edt-photo";
  const photo = () => { try { return localStorage.getItem(PHOTO); } catch (e) { return null; } };

  // ---------- Écrans
  let brouillon = null;
  function viewImport() {
    const p = photo();
    $view.innerHTML = `<h1>📷 Importer mon emploi du temps</h1>
      <p class="muted">Prends en photo ton emploi du temps (même écrit à la main), choisis une capture d'écran, ou colle-le en texte. L'appli le lit sur ton téléphone, puis tu vérifies avant d'enregistrer.</p>
      <div class="card"><label class="btn" style="text-align:center">📸 Prendre une photo<input type="file" id="cam" accept="image/*" capture="environment" hidden></label>
        <label class="btn alt" style="text-align:center">🖼️ Choisir une image ou un fichier<input type="file" id="fic" accept="image/*,.txt,.csv,text/plain" hidden></label>
        <p class="small muted">Conseil : photo bien droite, à la lumière, tout le tableau visible.</p><p class="small" id="imsg"></p></div>
      <div class="card"><h2>✍️ Ou colle ton emploi du temps</h2><p class="small muted">Une ligne par jour, par exemple : « Lundi : 8h-10h Maths, 10h-12h Français, 15h-17h PC »</p>
        <textarea id="txt" rows="6" placeholder="Lundi : 8h-10h Maths, 10h-12h Français&#10;Mardi : 8h-9h Anglais, 9h-11h SVT"></textarea>
        <button class="btn alt" id="lire">Lire ce texte</button></div>
      ${p ? `<details class="card"><summary><b>📷 Ma dernière photo</b></summary><img src="${p}" alt="Photo de mon emploi du temps" style="width:100%;margin-top:.5rem"></details>` : ""}
      <a class="btn alt" href="#agenda">Retour à l'agenda</a>`;
    const msg = document.getElementById("imsg"), dire = (t, cls = "small") => { msg.className = cls; msg.textContent = t; };
    const subs = subjectsOf(S.level);
    async function fichier(f) {
      if (!f) return;
      if (/^text\/|\.(txt|csv)$/i.test(f.type + " " + f.name) && !/^image\//.test(f.type)) { const t = await f.text(); return montrer(parLignes(t.replace(/[;,\t]/g, " "), subs), null, "le fichier"); }
      if (!/^image\//.test(f.type)) return dire("Ce type de fichier ne se lit pas encore. Fais une capture d'écran du PDF et choisis-la ici.", "small msg-ko");
      try {
        dire("Préparation de l'image…");
        const [grand, petit] = await Promise.all([reduire(f, 2000), reduire(f, 1100)]);
        const vue = petit.toDataURL("image/jpeg", 0.7);
        try { localStorage.setItem(PHOTO, vue); } catch (e) {}
        let best = {};
        for (const im of [nettoyer(grand), grand]) {
          const { texte, mots } = await ocr(im, (t) => dire(t));
          for (const e of [parTableau(mots, subs), parLignes(texte, subs)]) if (nb(e) > nb(best)) best = e;
          if (nb(best) >= 4) break;
        }
        montrer(best, vue, "la photo");
      } catch (e) { dire("La lecture n'a pas marché sur ce téléphone. Tu peux remplir ton emploi du temps à la main en t'aidant de la photo.", "small msg-ko"); if (Compte.logError) Compte.logError("Import EDT : " + (e && e.message)); }
    }
    document.getElementById("cam").onchange = (e) => fichier(e.target.files[0]);
    document.getElementById("fic").onchange = (e) => fichier(e.target.files[0]);
    document.getElementById("lire").onclick = () => montrer(parLignes(document.getElementById("txt").value, subs), null, "le texte");
  }

  function montrer(edt, vue, source) {
    brouillon = edt || {};
    const subs = subjectsOf(S.level).filter((s) => !/annales/.test(s.id)), n = nb(brouillon);
    const opts = (c) => subs.map((s) => `<option value="${s.id}"${c.sid === s.id ? " selected" : ""}>${esc(s.name)}</option>`).join("") + `<option value="__nom"${c.nom ? " selected" : ""}>${esc(c.nom || "Autre cours")}</option>`;
    $view.innerHTML = `<h1>✅ Vérifie ton emploi du temps</h1>
      <p class="${n ? "muted" : "msg-ko"}">${n ? `J'ai trouvé ${n} cours dans ${esc(source)}. Corrige ce qui est faux, ajoute ce qui manque, puis enregistre.` : `Je n'ai pas réussi à lire les cours dans ${esc(source)}${vue ? " (c'est fréquent avec l'écriture à la main)" : ""}. Ajoute-les ci-dessous${vue ? " en t'aidant de la photo" : ""} : c'est rapide.`}</p>
      ${vue ? `<details class="card"${n ? "" : " open"}><summary><b>📷 Voir la photo</b></summary><img src="${vue}" alt="Photo de l'emploi du temps" style="width:100%;margin-top:.5rem"></details>` : ""}
      ${ORDRE_JOURS.map((d) => `<div class="card"><h2>${JOURS[d]}</h2>
        ${(brouillon[d] || []).map((c, k) => `<div class="row slot" data-d="${d}" data-k="${k}"><input type="time" class="bd" value="${c.d}" style="width:6.5rem"><input type="time" class="bf" value="${c.f || ""}" style="width:6.5rem"><select class="bm" style="flex:1">${opts(c)}</select><button class="btn alt small bx" aria-label="Retirer">✕</button></div>`).join("")}
        <button class="btn alt small bplus" data-d="${d}">＋ Ajouter un cours</button></div>`).join("")}
      <div class="card"><label class="row small"><span><input type="radio" name="mode" value="rem" checked> Remplacer mon emploi du temps actuel</span></label>
        <label class="row small"><span><input type="radio" name="mode" value="add"> Ajouter à mon emploi du temps actuel</span></label></div>
      <button class="btn hi-btn" id="save">Enregistrer</button><a class="btn alt" href="#agenda/importer">Recommencer</a>`;
    const lire = () => $view.querySelectorAll(".slot").forEach((r) => {
      const c = brouillon[r.dataset.d][+r.dataset.k], v = r.querySelector(".bm").value;
      c.d = r.querySelector(".bd").value; c.f = r.querySelector(".bf").value;
      if (v === "__nom") { delete c.sid; c.nom = c.nom || "Cours"; } else { delete c.nom; c.sid = v; }
    });
    $view.querySelectorAll(".bx").forEach((b) => b.onclick = () => { lire(); const r = b.closest(".slot"); brouillon[r.dataset.d].splice(+r.dataset.k, 1); montrer(brouillon, vue, source); });
    $view.querySelectorAll(".bplus").forEach((b) => b.onclick = () => { lire(); const d = b.dataset.d, l = (brouillon[d] = brouillon[d] || []), der = l[l.length - 1];
      l.push({ d: der && der.f ? der.f : "08:00", f: "", sid: (subs[0] || {}).id }); montrer(brouillon, vue, source); });
    document.getElementById("save").onclick = () => {
      lire();
      const rem = $view.querySelector('[name="mode"]:checked').value === "rem";
      S.edt = rem ? {} : S.edt || {};
      for (const [d, l] of Object.entries(brouillon)) { const ok = l.filter((c) => c.d); if (ok.length) S.edt[d] = finir({ x: [...(rem ? [] : S.edt[d] || []), ...ok] }).x; }
      store.save(); if (typeof markDone === "function") markDone("edt"); go("agenda");
    };
  }


  // ---------- Saisie guidée : on part de lundi 8 h ; pour chaque créneau libre l'élève choisit la matière (ou une pause) et
  // jusqu'à quelle heure, puis place d'un coup toutes les autres heures de cette matière dans la semaine.
  const H0 = 8 * 60, PAS = 30, NC = 22, JG = [1, 2, 3, 4, 5, 6];
  const tIdx = (t) => Math.round((+t.slice(0, 2) * 60 + +t.slice(3, 5) - H0) / PAS), idxT = (i) => hhmm(Math.floor((H0 + i * PAS) / 60), String((H0 + i * PAS) % 60).padStart(2, "0"));
  const lbl = (c) => (c.sid ? subjName(c.sid) : c.nom), meme = (a, b) => a && b && typeof a === "object" && typeof b === "object" && (a.sid || a.nom) === (b.sid || b.nom);
  let G = null, hist = [];
  function grilleDe(edt) {
    const g = {}; JG.forEach((d) => (g[d] = Array(NC).fill(undefined)));
    for (const d of JG) for (const c of (edt || {})[d] || []) { const a = tIdx(c.d), b = c.f ? tIdx(c.f) : a + 2; for (let i = Math.max(0, a); i < Math.min(NC, b); i++) g[d][i] = c.sid ? { sid: c.sid } : { nom: c.nom }; }
    return g;
  }
  function edtDe(g) {
    const edt = {};
    for (const d of JG) { const l = []; let i = 0;
      while (i < NC) { const c = g[d][i]; if (c && typeof c === "object") { let j = i; while (j < NC && meme(g[d][j], c)) j++; l.push({ d: idxT(i), f: idxT(j), ...c }); i = j; } else i++; }
      if (l.length) edt[d] = l; }
    return edt;
  }
  const libre = () => { for (const d of JG) for (let i = 0; i < NC; i++) if (G[d][i] === undefined) return [d, i]; return null; };
  const poser = (d, i, n, v) => { hist.push(structuredClone(G)); for (let k = i; k < i + n && k < NC && (G[d][k] === undefined || k === i); k++) G[d][k] = v; };
  const court = (c) => { const n = lbl(c); return n.length > 6 ? n.replace(/^(Mathématiques|Techniques comptables|Histoire-Géographie|Philosophie|Économie|Espagnol.*|Anglais|Français)$/, (m) => ({ "Mathématiques": "Maths", "Techniques comptables": "Compta", "Histoire-Géographie": "HG", "Philosophie": "Philo", "Économie": "Éco", "Anglais": "Ang.", "Français": "Fr." })[m] || "Esp.").slice(0, 6) : n; };
  const hFr = (i) => hh(idxT(i));

  function viewGuide(arg) {
    if (!G || arg === "zero") { G = grilleDe(arg === "zero" ? {} : S.edt); hist = []; if (arg === "zero") history.replaceState(null, "", "#agenda/guide"); }
    const p = libre(), n = nb(edtDe(G));
    if (!p) return fin();
    const [d, i] = p, subs = subjectsOf(S.level).filter((s) => !/annales/.test(s.id));
    $view.innerHTML = `<h1>🪄 Saisie guidée</h1><p class="small muted">${n} cours notés · une case = 30 min · <a href="#agenda/guide/zero">tout recommencer</a></p>
      <div class="card prog"><h2>${JOURS[d]} à ${hFr(i)} : quel cours ?</h2>
        <div class="grid">${subs.map((s) => `<button class="subj tile gm" data-s="${s.id}" style="min-height:0"><b>${esc(s.name)}</b></button>`).join("")}
          <button class="subj tile gp" style="min-height:0"><b>☕ Pause ou trou</b></button><button class="subj tile go-autre" style="min-height:0"><b>✏️ Autre cours</b><span class="small muted">EPS, arabe…</span></button></div>
        <input id="gautre" placeholder="Nom du cours (ex. : EPS)" maxlength="40" hidden>
        <div class="row"><button class="btn alt" id="gfj" style="flex:1">🏠 Fini pour le ${JOURS[d].toLowerCase()}</button>${i === 0 ? `<button class="btn alt" id="gpas" style="flex:1">Pas cours le ${JOURS[d].toLowerCase()}</button>` : ""}</div></div>
      ${apercu()}
      <div class="row">${hist.length ? `<button class="btn alt" id="gundo" style="flex:1">↩ Annuler</button>` : ""}<button class="btn" id="gfin" style="flex:1">Terminer</button></div>`;
    const choisir = (v) => duree(d, i, v);
    $view.querySelectorAll(".gm").forEach((b) => b.onclick = () => choisir({ sid: b.dataset.s }));
    $view.querySelector(".gp").onclick = () => duree(d, i, "libre");
    const au = document.getElementById("gautre");
    $view.querySelector(".go-autre").onclick = () => { if (au.hidden) { au.hidden = false; au.focus(); } else if (au.value.trim()) choisir({ nom: au.value.trim() }); };
    au.onkeydown = (e) => { if (e.key === "Enter" && au.value.trim()) choisir({ nom: au.value.trim() }); };
    document.getElementById("gfj").onclick = () => { hist.push(structuredClone(G)); for (let k = i; k < NC; k++) if (G[d][k] === undefined) G[d][k] = "fin"; viewGuide(); };
    const pas = document.getElementById("gpas"); if (pas) pas.onclick = () => { hist.push(structuredClone(G)); G[d] = G[d].map((c) => (c === undefined ? "fin" : c)); viewGuide(); };
    const u = document.getElementById("gundo"); if (u) u.onclick = () => { G = hist.pop(); viewGuide(); };
    document.getElementById("gfin").onclick = fin;
  }
  // jusqu'à quelle heure : propositions jusqu'au prochain cours déjà noté
  function duree(d, i, v) {
    let max = i; while (max < NC && (max === i || G[d][max] === undefined)) max++;
    const fins = []; for (let k = i + 1; k <= max && k - i <= 10; k++) fins.push(k);
    const nom = v === "libre" ? "☕ Pause" : esc(lbl(v));
    $view.innerHTML = `<h1>🪄 Saisie guidée</h1><div class="card prog"><h2>${nom} le ${JOURS[d].toLowerCase()} à ${hFr(i)}, jusqu'à :</h2>
      <div class="grid">${fins.map((k) => `<button class="subj tile gf" data-k="${k}" style="min-height:0"><b>${hFr(k)}</b><span class="small muted">${(k - i) * 30 >= 60 ? `${Math.floor((k - i) / 2)} h${(k - i) % 2 ? " 30" : ""}` : "30 min"}</span></button>`).join("")}</div></div>
      <button class="btn alt" id="gret">Retour</button>`;
    $view.querySelectorAll(".gf").forEach((b) => b.onclick = () => { const n = +b.dataset.k - i; poser(d, i, n, v); v === "libre" ? viewGuide() : autres(v, n, d, i); });
    document.getElementById("gret").onclick = () => viewGuide();
  }
  // toutes les autres heures de la même matière, en touchant la grille de la semaine
  function autres(v, n, d0, i0) {
    $view.innerHTML = `<h1>🪄 Saisie guidée</h1>
      <div class="card"><p class="msg-ok">✓ C'est noté : <b>${esc(lbl(v))}</b> le ${JOURS[d0].toLowerCase()} de ${hFr(i0)} à ${hFr(i0 + n)}.</p>
        <h2>Où sont les autres cours de ${esc(lbl(v))} cette semaine ?</h2><p class="small muted">Touche l'heure de début dans la grille : le cours est placé avec la durée choisie. Touche-le à nouveau pour l'enlever.</p>
        <div class="row">${[1, 2, 3, 4, 6].map((k) => `<button class="btn alt small gdu${k === n ? " on" : ""}" data-n="${k}" style="flex:1">${k * 30 >= 60 ? (k % 2 ? `${Math.floor(k / 2)}h30` : `${k / 2} h`) : "30 min"}</button>`).join("")}</div></div>
      <div id="gg">${grille(v)}</div>
      <button class="btn hi-btn" id="gnext">C'est tout pour ${esc(lbl(v))} : cours suivant ›</button>`;
    $view.querySelectorAll(".gdu").forEach((b) => b.onclick = () => { n = +b.dataset.n; $view.querySelectorAll(".gdu").forEach((x) => x.classList.toggle("on", x === b)); });
    document.getElementById("gg").onclick = (e) => {
      const td = e.target.closest("[data-c]"); if (!td) return;
      const [d, i] = td.dataset.c.split("|").map(Number);
      if (meme(G[d][i], v)) { hist.push(structuredClone(G)); let a = i, b = i; while (a > 0 && meme(G[d][a - 1], v)) a--; while (b < NC && meme(G[d][b], v)) G[d][b++] = undefined; for (let k = a; k < i; k++) G[d][k] = undefined; }
      else if (G[d][i] === undefined || G[d][i] === "fin") { if (G[d][i] === "fin") G[d][i] = undefined; poser(d, i, n, v); }
      document.getElementById("gg").innerHTML = grille(v);
    };
    document.getElementById("gnext").onclick = () => viewGuide();
  }
  // grille de la semaine par heure (deux demi-cases par heure)
  function grille(v) {
    const H = []; for (let i = 0; i < NC; i += 2) H.push(i);
    const cel = (d, i) => { const c = G[d][i]; const cls = v && meme(c, v) ? "g-on" : c && typeof c === "object" ? "g-pris" : c === "libre" ? "g-pause" : "";
      return `<td class="${cls}" data-c="${d}|${i}">${c && typeof c === "object" && !(i > 0 && meme(G[d][i - 1], c)) ? esc(court(c)) : c === "libre" && G[d][i - 1] !== "libre" ? "☕" : ""}</td>`; };
    return `<div class="card" style="overflow-x:auto;padding:.4rem"><table class="gtab"><tr><th></th>${JG.map((d) => `<th>${JOURS[d].slice(0, 3)}</th>`).join("")}</tr>
      ${H.map((i) => `<tr><th>${hFr(i)}</th>${JG.map((d) => cel(d, i)).join("")}</tr><tr class="demi"><th></th>${JG.map((d) => cel(d, i + 1)).join("")}</tr>`).join("")}</table></div>`;
  }
  const apercu = () => (nb(edtDe(G)) ? `<details><summary class="small">Voir ma semaine</summary>${grille(null)}</details>` : "");
  function fin() {
    const edt = edtDe(G), n = nb(edt);
    $view.innerHTML = `<h1>🪄 Ta semaine</h1><p class="muted">${n} cours notés. Vérifie, puis enregistre : chaque soir, l'appli te dira quoi réviser pour le lendemain.</p>${grille(null)}
      <button class="btn hi-btn" id="gsave"${n ? "" : " disabled"}>Enregistrer mon emploi du temps</button><button class="btn alt" id="gback">Continuer la saisie</button>`;
    document.getElementById("gsave").onclick = () => { S.edt = edt; store.save(); G = null; if (typeof markDone === "function") markDone("edt"); go("agenda"); };
    document.getElementById("gback").onclick = () => { for (const d of JG) G[d] = G[d].map((c) => (c === "fin" ? undefined : c)); const p = libre(); p ? viewGuide() : go("agenda"); };
  }

  globalThis.EDT_IMPORT = { ocr, nettoyer, reduire, viewGuide, edtDe, grilleDe, parLignes, parTableau, matiere, jourDe, heures, viewImport, photo };
})();
