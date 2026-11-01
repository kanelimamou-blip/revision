"use strict";
// Piloter l'élémentaire avec l'emploi du temps de l'école (demande d'Est, CE2 de son fils).
// L'emploi du temps officiel de l'étape 2 (CE1/CE2, Curriculum de l'Éducation de Base) est pré-rempli en un clic,
// chaque créneau est relié à une matière ET à un domaine (numération, mesure, conjugaison…), donc aux bons chapitres.
// Le soir, l'appli propose 3 petites activités sur ce qui a été fait en classe dans la journée, en suivant le volume horaire,
// et la page #pilotage montre au parent l'équilibre de la semaine (heures en classe, maîtrise, temps conseillé dans l'appli).
(() => {
  // domaines → chapitres (titres exacts de contenu/primaire_<classe>.py)
  const DOM = {
    CE1: {
      num: ["maths", ["Les nombres jusqu'à 1 000", "L'addition et la soustraction", "La multiplication et les tables", "Le partage et la division"]],
      mes: ["maths", ["Mesurer des longueurs", "Les masses, les capacités et la monnaie", "Le temps : l'heure, les jours et les mois"]],
      geom: ["maths", ["Les lignes et les figures planes"]], pb: ["maths", ["Résoudre des problèmes"]],
      lect: ["francais", ["Lire et comprendre un texte", "Les sons et les lettres"]], voc: ["francais", ["L'ordre alphabétique et le dictionnaire", "Synonymes, contraires et familles de mots"]],
      gram: ["francais", ["La phrase et la ponctuation", "Le nom et le déterminant", "Le verbe et son sujet"]], orth: ["francais", ["Masculin, féminin, singulier et pluriel", "Les sons et les lettres"]],
      conj: ["francais", ["Le présent : être, avoir et les verbes en -er", "Passé, présent, futur"]], ecr: ["francais", ["La phrase et la ponctuation", "Lire et comprendre un texte"]],
    },
    CE2: {
      num: ["maths", ["Les nombres jusqu'à 100 000", "Addition et soustraction posées", "La multiplication", "La division", "Les fractions simples"]],
      mes: ["maths", ["Longueurs et périmètres", "Masses, capacités et monnaie", "Les durées et le calendrier"]],
      geom: ["maths", ["Géométrie : angles, figures et cercle"]], pb: ["maths", ["Résoudre des problèmes"]],
      lect: ["francais", ["Lire et comprendre un texte"]], voc: ["francais", ["Le vocabulaire : dictionnaire, préfixes, suffixes"]],
      gram: ["francais", ["Les types de phrases", "Le groupe nominal : nom, déterminant, adjectif", "Sujet, verbe et compléments", "Les pronoms personnels"]],
      orth: ["francais", ["Les accords", "Les homophones grammaticaux"]], conj: ["francais", ["Le présent des verbes", "L'imparfait et le futur simple", "Le passé composé"]],
      ecr: ["francais", ["Écrire : des phrases et un petit texte"]],
    },
  };
  // domaines communs à toutes les classes : toute la matière
  const TOUT = { ecrite: "francais", orale: "francais", ist: "sciences", hist: "histoire", geo: "geo", vdm: "geo", ve: "civique", ang: "anglais" };
  const LIB = { num: "Activités numériques", mes: "Activités de mesure", geom: "Activités géométriques", pb: "Résolution de problèmes", lect: "Lecture", voc: "Vocabulaire",
    gram: "Grammaire", orth: "Orthographe", conj: "Conjugaison", ecr: "Écriture", ecrite: "Communication écrite", orale: "Communication orale", poesie: "Poésie / récitation",
    ist: "Initiation scientifique et technologique", hist: "Histoire", geo: "Géographie", vdm: "Vivre dans son milieu", ve: "Vivre ensemble",
    ang: "Anglais", ar: "Arabe", rel: "Éducation religieuse", eps: "Éducation physique et sportive", art: "Arts plastiques", mus: "Éducation musicale", scen: "Arts scéniques", remed: "Remédiation" };
  const HORS = ["ar", "rel", "eps", "art", "mus", "scen", "poesie"];

  // emploi du temps de l'étape 2 (CE1/CE2), lu sur le document de l'école : 9 créneaux de 30 min, récréation de 11 h à 11 h 30,
  // remédiation l'après-midi. Les horaires exacts se corrigent dans l'agenda.
  const H = [["08:00", "08:30"], ["08:30", "09:00"], ["09:00", "09:30"], ["09:30", "10:00"], ["10:00", "10:30"], ["10:30", "11:00"], ["11:30", "12:00"], ["12:00", "12:30"], ["12:30", "13:00"]];
  const EDT_E2 = {
    1: ["orale", "num", "lect", "num", "ist", "art", "hist", "voc", "ecrite"],
    2: ["poesie", "mes", "gram", "mes", "orth", "mus", "vdm", "ecrite", "ecr"],
    3: ["rel", "num", "voc", "lect", "ar", "conj", "geo", "orth", "ecrite"],
    4: ["eps", "orale", "geom", "gram", "conj", "ve", "geom", "ang", null],
    5: ["orale", "pb", "voc", "pb", "ist", "ang", "scen", "lect", null],
  };
  const REMED = { 2: ["15:00", "16:30"], 4: ["15:00", "16:30"] };

  const lv = () => S.level, pre = () => String(S.level || "").toLowerCase();
  const sidDe = (k) => { const d = (DOM[lv()] || {})[k]; const m = d ? d[0] : TOUT[k]; return m ? `${pre()}-${m}` : null; };
  const chapsDe = (k) => { const sid = sidDe(k), titres = (DATA.programmes || {})[sid] || [], d = (DOM[lv()] || {})[k];
    return d ? d[1].map((t) => titres.indexOf(t)).filter((i) => i >= 0) : titres.map((_, i) => i); };
  const minutes = (c) => { const [a, b] = [c.d, c.f || c.d].map((t) => { const [h, m] = t.split(":").map(Number); return h * 60 + m; }); return Math.max(0, b - a) || 30; };

  globalThis.installerEdtCEB = () => {
    S.edt = {};
    for (const [j, row] of Object.entries(EDT_E2)) {
      S.edt[j] = row.map((k, i) => (k ? { d: H[i][0], f: H[i][1], k, lib: LIB[k], ...(sidDe(k) && !HORS.includes(k) ? { sid: sidDe(k) } : { nom: LIB[k] }) } : null)).filter(Boolean);
      if (REMED[j]) S.edt[j].push({ d: REMED[j][0], f: REMED[j][1], k: "remed", lib: LIB.remed, nom: LIB.remed });
    }
    S.edtSrc = "ceb-e2"; store.save();
  };

  // maîtrise d'un chapitre : erreurs à corriger d'abord, sinon le moins travaillé
  const etatCh = (sid, ch) => { let ok = 0, ko = 0, err = 0, n = 0;
    for (const q of DATA.questions) { if (q.s !== sid || q.ch !== ch) continue; n++; const st = S.stats[q.id]; if (!st) continue; ok += st.ok; ko += st.ko; if (st.last === false) err++; }
    return { ok, ko, err, n, vu: ok + ko }; };
  const choisirCh = (k) => { const sid = sidDe(k), cs = chapsDe(k).map((ch) => ({ ch, ...etatCh(sid, ch) })).filter((c) => c.n);
    if (!cs.length) return null; const e = cs.slice().sort((a, b) => b.err - a.err)[0];
    const c = e.err ? e : cs.slice().sort((a, b) => a.vu - b.vu || a.ch - b.ch)[0];
    return { sid, ch: c.ch, raison: c.err ? `${c.err} erreur${c.err > 1 ? "s" : ""} à corriger` : c.vu ? "à consolider" : "pas encore travaillé" }; };
  globalThis.maitriseSid = (sid) => { let ok = 0, t = 0; for (const q of DATA.questions) { if (q.s !== sid) continue; const st = S.stats[q.id]; if (st) { ok += st.ok; t += st.ok + st.ko; } } return t ? Math.round((100 * ok) / t) : null; };

  // jour de classe à réviser : l'après-midi et le soir, celui d'aujourd'hui ; le matin, le précédent ; le week-end, toute la semaine
  const JOURS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];
  const cibleJour = () => { const d = new Date(), j = d.getDay(); if (j === 0 || j === 6) return null; if (d.getHours() >= 12) return j; return j === 1 ? null : j - 1; };
  const DUREE = { CE1: 15, CE2: 20, CM1: 25, CM2: 30 };
  const PRIO = ["num", "pb", "mes", "conj", "gram", "orth", "lect", "voc", "ecr", "geom", "ecrite", "orale", "ist", "hist", "geo", "vdm", "ve"];

  globalThis.planDuSoir = () => {
    const edt = S.edt || {}, j = cibleJour();
    const slots = j ? edt[j] || [] : Object.values(edt).flat();
    const poids = {};
    for (const c of slots) { const k = c.k || null; if (!k || HORS.includes(k) || k === "remed" || !sidDe(k)) continue; poids[k] = (poids[k] || 0) + minutes(c); }
    const ks = Object.keys(poids).sort((a, b) => poids[b] - poids[a] || PRIO.indexOf(a) - PRIO.indexOf(b));
    const out = [], vusSid = new Set();
    // 3 activités : la plus grosse de chaque matière d'abord (pas trois fois le français)
    for (const k of ks) { if (out.length >= 3) break; const c = choisirCh(k); if (!c || vusSid.has(c.sid + c.ch)) continue;
      if (out.filter((o) => o.sid === c.sid).length >= 2) continue; vusSid.add(c.sid + c.ch); out.push({ k, ...c }); }
    const remed = j ? (edt[j] || []).some((c) => c.k === "remed") : true;
    const nErr = DATA.questions.filter((q) => inLevel(q) && S.stats[q.id] && S.stats[q.id].last === false).length;
    return { j, out, remed: remed && nErr > 0, nErr, duree: DUREE[lv()] || 20, aEdt: Object.values(edt).some((l) => l.length) };
  };

  const fait = (cle) => ((S.planFait || {})[today()] || []).includes(cle);
  const marquer = (cle) => { S.planFait = { [today()]: [...new Set([...((S.planFait || {})[today()] || []), cle])] }; store.save(); };
  const ligne = (a) => { const titres = (DATA.programmes || {})[a.sid] || [], n = ((DATA.notions || {})[a.sid] || []).find((x) => +x.pch === a.ch), cle = `${a.sid}~${a.ch}`;
    return `<div class="plan-l${fait(cle) ? " fait" : ""}"><div><b>${fait(cle) ? "✅" : "▫️"} ${esc(LIB[a.k] || subjName(a.sid))}</b><span class="small">${esc(titres[a.ch] || "")} · ${a.raison}</span></div>
      <div class="kid-btns">${n ? `<a class="btn alt small" href="#notion/${n.id}">📖 Leçon</a>` : ""}<a class="btn small plan-go" data-c="${cle}" href="#quiz/${a.sid}/${a.ch}">🎮 10 questions</a></div></div>`; };

  globalThis.planSoirCard = (court) => {
    if (!["CE1", "CE2", "CM1", "CM2"].includes(lv())) return "";
    const p = planDuSoir();
    if (!p.aEdt) return `<div class="card plan"><h2>📅 Suivre l'emploi du temps de l'école</h2><p class="small">Ajoute l'emploi du temps de la classe : chaque soir, l'appli proposera de revoir ce qui a été fait en classe dans la journée.</p><a class="btn" href="#pilotage">Ajouter l'emploi du temps</a></div>`;
    const titre = p.j ? `Ce soir : ce qu'on a fait ${new Date().getDay() === p.j ? "aujourd'hui" : JOURS[p.j]}` : "Révision de la semaine";
    const html = `<div class="card plan"><h2>📅 ${titre}</h2><p class="small muted">Environ ${p.duree} minutes · d'après l'emploi du temps de la classe</p>
      ${p.out.map(ligne).join("") || `<p class="small">Pas de cours de maths ou de français ce jour-là : fais la question du jour !</p>`}
      ${p.remed ? `<div class="plan-l"><div><b>🔁 Remédiation</b><span class="small">${p.nErr} question${p.nErr > 1 ? "s" : ""} ratée${p.nErr > 1 ? "s" : ""} à refaire</span></div><a class="btn small" href="#erreurs/go">Refaire</a></div>` : ""}
      ${court ? `<a class="small" href="#pilotage">Voir toute la semaine ›</a>` : ""}</div>`;
    setTimeout(() => document.querySelectorAll(".plan-go").forEach((b) => b.addEventListener("click", () => marquer(b.dataset.c))), 0);
    return html;
  };

  // ---------- page parent : emploi du temps, équilibre de la semaine, plan
  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  ROUTES.pilotage = (arg) => {
    if (arg === "ceb") { const vide = !Object.values(S.edt || {}).some((l) => l.length);
      if (vide || confirm("Remplacer l'emploi du temps déjà saisi par celui de l'étape 2 (CE1/CE2) ?")) installerEdtCEB(); return go("pilotage"); }
    const edt = S.edt || {}, a = Object.values(edt).some((l) => l.length), e2 = ["CE1", "CE2"].includes(lv());
    const vol = {}, hors = {}; let tot = 0;
    for (const c of Object.values(edt).flat()) { const m = minutes(c); if (c.k === "remed") continue; tot += m;
      if (c.sid) vol[c.sid] = (vol[c.sid] || 0) + m; else hors[c.lib || c.nom] = (hors[c.lib || c.nom] || 0) + m; }
    const dom = {}; for (const c of Object.values(edt).flat()) if (c.sid && c.k && DOM[lv()] && DOM[lv()][c.k]) dom[c.sid] = { ...(dom[c.sid] || {}), [c.k]: ((dom[c.sid] || {})[c.k] || 0) + minutes(c) };
    const h = (m) => `${Math.floor(m / 60)} h${m % 60 ? ` ${m % 60}` : ""}`, semaine = (DUREE[lv()] || 20) * 5, totApp = Object.values(vol).reduce((x, y) => x + y, 0);
    const lignes = Object.entries(vol).sort((x, y) => y[1] - x[1]).map(([sid, m]) => { const mt = maitriseSid(sid), conseil = Math.max(5, Math.round((semaine * m) / totApp / 5) * 5);
      return `<tr><td><b>${esc(subjName(sid))}</b>${dom[sid] ? `<br><span class="small muted">${Object.entries(dom[sid]).map(([k, x]) => `${LIB[k]} ${h(x)}`).join(" · ")}</span>` : ""}</td><td>${h(m)}</td><td>${Math.round((100 * m) / tot)} %</td><td>${conseil} min</td><td>${mt === null ? "—" : mt + " %"}</td></tr>`; }).join("");
    $view.innerHTML = `<h1>📅 Piloter le ${esc(lv())} avec l'emploi du temps</h1>
      <p class="muted">L'appli suit l'emploi du temps de la classe : le soir, elle propose de revoir ce qui a été fait dans la journée, avec le temps donné à chaque matière à l'école.</p>
      ${a ? planSoirCard(false) : ""}
      <div class="card"><h2>L'emploi du temps</h2>
        ${a ? `<p class="small">${S.edtSrc === "ceb-e2" ? "Emploi du temps officiel de l'étape 2 (CE1/CE2) du Curriculum de l'Éducation de Base." : "Emploi du temps saisi pour la classe."} Les horaires et les cours se corrigent dans l'agenda.</p>` : `<p class="small">Choisis comment l'ajouter :</p>`}
        <div class="btns">${e2 ? `<a class="btn${a ? " alt" : ""}" href="#pilotage/ceb">📋 Emploi du temps officiel CE1/CE2 (étape 2)</a>` : ""}
          <a class="btn alt" href="#agenda">✏️ ${a ? "Modifier dans l'agenda" : "Le saisir moi-même"}</a><a class="btn alt" href="#agenda/importer">📷 Le prendre en photo</a></div></div>
      ${a ? `<div class="card"><h2>L'équilibre de la semaine</h2>
        <p class="small muted">Heures en classe, part de la semaine, temps conseillé dans l'appli (≈ ${semaine} min par semaine, réparti comme à l'école) et réussite aux questions.</p>
        <div class="tbl"><table><tr><th>Matière</th><th>En classe</th><th>Part</th><th>Appli</th><th>Réussite</th></tr>${lignes}</table></div>
        ${Object.keys(hors).length ? `<p class="small">Pas dans l'appli : ${Object.entries(hors).map(([n, m]) => `${esc(n)} (${h(m)})`).join(", ")}.</p>` : ""}</div>
      <div class="card"><h2>La semaine, jour par jour</h2>${[1, 2, 3, 4, 5].map((j) => { const l = (edt[j] || []).filter((c) => c.sid);
          const ks = [...new Set(l.map((c) => c.lib || subjName(c.sid)))]; return ks.length ? `<p><b>${JOURS[j][0].toUpperCase() + JOURS[j].slice(1)}</b> : ${ks.map(esc).join(", ")}</p>` : ""; }).join("")}</div>` : ""}
      <a class="btn alt" href="#accueil">↩ Retour</a>`;
  };
})();
