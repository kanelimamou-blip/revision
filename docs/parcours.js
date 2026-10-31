"use strict";
// Parcours propre à chaque élève.
// 1) Mémoire de ce qu'il a déjà vu, y compris les questions et exercices générés : on ne les lui repropose pas
//    tant qu'il reste du neuf (empreinte courte de chaque énoncé, gardée sur le téléphone et dans son compte).
// 2) Choix du chapitre pondéré : chapitre que la classe voit en ce moment, cours du lendemain dans son emploi du temps,
//    devoir ou composition à venir, chapitres faibles, notes loin de l'objectif. Deux élèves n'ont donc pas le même tirage.
// 3) Les réponses aux questions générées comptent dans la maîtrise de chaque chapitre (courbe de progression).
// 4) Part de questions générées selon la classe : Terminale d'abord, puis Première et Troisième, puis les autres.
(() => {
  const MAX_VU = 4000;
  const emp = (t) => { let h = 2166136261; for (let i = 0; i < t.length; i++) { h ^= t.charCodeAt(i); h = Math.imul(h, 16777619); } return (h >>> 0).toString(36); };
  let cache = null;
  const vus = () => { if (!cache) cache = new Set(S.vu || []); return cache; };
  globalThis.empreinte = emp;
  globalThis.dejaVu = (texte) => vus().has(emp(texte));
  globalThis.marquerVu = (texte) => {
    const k = emp(texte), set = vus(); if (set.has(k)) return;
    set.add(k); (S.vu = S.vu || []).push(k);
    if (S.vu.length > MAX_VU) { S.vu.splice(0, S.vu.length - MAX_VU); cache = new Set(S.vu); }
  };

  // Part de questions générées dans un QCM, selon la classe (pondération voulue : Tle > 1re = 3e > autres)
  globalThis.partGeneree = () => { const c = String(S.level || "").split(" ")[0]; return c === "Tle" ? 0.5 : c === "1ère" || c === "3e" ? 0.45 : 0.35; };

  const idx = (sid, ch) => (typeof ch === "number" ? ch : ((DATA.programmes || {})[sid] || []).indexOf(ch));
  const demain = () => { const d = new Date(); if (d.getHours() >= 17) d.setDate(d.getDate() + 1); return d.getDay(); };
  // matières de l'emploi du temps des 24 prochaines heures, et devoirs à venir (7 jours)
  function contexte() {
    const jour = demain(), edt = new Set(((S.edt || {})[jour] || []).map((c) => c.sid).filter(Boolean));
    const dev = {}; for (const t of S.todo || []) { if (t.done || !t.sid) continue; const n = Math.round((new Date(t.date + "T12:00") - Date.now()) / 864e5); if (n >= -1 && n <= 7) dev[t.sid] = Math.min(dev[t.sid] ?? 99, n); }
    return { edt, dev };
  }
  let ctxCache = null, ctxT = 0;
  const ctx = () => { if (!ctxCache || Date.now() - ctxT > 6e4) { ctxCache = contexte(); ctxT = Date.now(); } return ctxCache; };

  // Poids d'un chapitre pour l'élève (plus il est grand, plus le chapitre sort souvent)
  globalThis.poidsChapitre = (sid, ch) => {
    const i = idx(sid, ch); if (i < 0) return 1;
    let w = 1;
    const enc = typeof chEnCours === "function" ? chEnCours(sid) : null;
    if (enc !== null) { if (i === enc) w *= 3; else if (i === enc - 1) w *= 2; else if (i < enc) w *= 1.4; else if (i > enc + 1) w *= 0.35; }
    const m = typeof maitriseCh === "function" ? maitriseCh(sid, i) : null;
    w *= m === null ? 1.6 : 1 + (100 - m) / 50; // jamais travaillé ou faible : plus souvent
    const c = ctx();
    if (c.edt.has(sid) && enc !== null && Math.abs(i - enc) <= 1) w *= 2; // cours demain : on prépare le chapitre en cours
    if (c.dev[sid] !== undefined && enc !== null && i <= enc && i >= enc - 2) w *= 2.5; // devoir proche : chapitres récents
    const pr = typeof notesPriorite === "function" ? notesPriorite()[sid] || 0 : 0;
    return w * (1 + Math.min(pr, 3) / 3);
  };

  // Réponse à une question générée : maîtrise du chapitre et mémoire
  globalThis.noterGen = (q, ok) => {
    if (q && q.q) marquerVu(q.q);
    if (!q || !q.s || q.chTitle === undefined) return;
    const i = idx(q.s, q.chTitle); if (i < 0) return;
    const k = `${q.s}~${i}`, st = (S.genCh = S.genCh || {})[k] || { ok: 0, ko: 0, r: [] };
    st[ok ? "ok" : "ko"]++; st.r = (st.r || []).concat(ok ? 1 : 0).slice(-10); st.t = Date.now(); S.genCh[k] = st;
  };
  // Maîtrise « générée » d'un chapitre : part de bonnes réponses sur les 10 dernières
  globalThis.maitriseGen = (sid, i) => { const st = (S.genCh || {})[`${sid}~${i}`]; if (!st || !st.r || st.r.length < 3) return null; return { m: Math.round((100 * st.r.reduce((a, b) => a + b, 0)) / st.r.length), n: st.r.length }; };

  // Exercices et sujets générés : on garde l'énoncé vu, et on en refait un autre s'il a déjà été vu
  if (typeof genExercise === "function") {
    const g0 = genExercise;
    globalThis.genExercise = function (sid, k, r = Math.random) { let e = null; for (let i = 0; i < 6; i++) { e = g0(sid, k, r); if (!e || !dejaVu(e.guided[0].context)) break; } if (e) marquerVu(e.guided[0].context); return e; };
  }

  // Pour l'élève et pour Est : ce qu'il a déjà vu et ce qu'il reste
  globalThis.bilanParcours = () => ({ vus: (S.vu || []).length, base: Object.keys(S.stats || {}).length, genCh: Object.keys(S.genCh || {}).length });
})();
