"use strict";
// Volume ×5 (demande d'Est du 2026-11-05, CE2 et 2nde) : à partir des modèles de QCM de chaque chapitre,
// des exercices guidés par chapitre (entraînement, contrôle, révision de deux chapitres)
// et des devoirs types ciblés (trois chapitres qui se suivent, trimestres, composition).
// Chaque exercice tire des questions toutes différentes ; les nombres et les faits changent à chaque essai.
const DEVGEN = {};
(() => {
  if (typeof GEN === "undefined" || typeof EXGEN === "undefined") return;
  const CIBLE = /^(ce2|2nde)-/;
  const progs = () => (typeof DATA !== "undefined" && DATA.programmes) || null;
  const mix = (r, a) => a.map((x) => [r(), x]).sort((p, q) => p[0] - q[0]).map((p) => p[1]);
  // n questions distinctes tirées des modèles fournis, en faisant tourner les modèles
  const tirer = (r, gens, n, vus = new Set()) => {
    const out = [];
    let ordre = mix(r, gens);
    for (let essai = 0; out.length < n && essai < n * 12; essai++) {
      if (!ordre.length) ordre = mix(r, gens);
      const f = ordre.shift();
      let o = null;
      try { o = f(r); } catch (e) { o = null; }
      if (!o || o.ok == null || !Array.isArray(o.faux) || o.faux.length < 3) continue;
      const cle = String(o.q).replace(/\d+/g, "#") + "|" + o.ok;
      if (vus.has(o.q) || (vus.has(cle) && essai < n * 6)) continue;
      if (new Set([String(o.ok), ...o.faux.slice(0, 3).map(String)]).size < 4) continue;
      vus.add(o.q); vus.add(cle);
      out.push(o);
    }
    return out.length === n ? out : null;
  };
  const step = (o, pts) => ({ q: o.q, ok: String(o.ok), faux: o.faux.slice(0, 3).map(String), e: o.e || "", pts });
  const parChapitre = (sid) => {
    const m = new Map();
    for (const [ch, f] of GEN[sid] || []) { if (!m.has(ch)) m.set(ch, []); m.get(ch).push(f); }
    const P = (progs() || {})[sid];
    const titres = P ? P.filter((t) => m.has(t)) : [...m.keys()];
    return titres.map((t) => [t, m.get(t)]);
  };
  const bareme = (n) => [...Array(n)].map((_, i) => (i < Math.ceil(n / 2) ? 1 : 1.5));
  const exo = (sid, t, make) => (EXGEN[sid] = EXGEN[sid] || []).push({ t, make, x5: true });

  let fait = false;
  function installer() {
    if (fait || !progs()) return;
    fait = true;
    for (const sid of Object.keys(GEN).filter((s) => CIBLE.test(s))) {
      const chs = parChapitre(sid);
      const R = (() => { let x = 7; return () => ((x = (x * 16807) % 2147483647) - 1) / 2147483646; })();
      const assez = (gens, n) => [0, 1, 2, 3, 4].filter(() => tirer(R, gens, n)).length >= 4;
      chs.forEach(([ch, gens], i) => {
        if (!assez(gens, 4)) return;
        exo(sid, `Entraînement : ${ch}`, (r) => { const qs = tirer(r, gens, 4); return qs && { context: `Chapitre : ${ch}. Quatre questions pour vérifier que la leçon est comprise.`, steps: qs.map((o, k) => step(o, bareme(4)[k])) }; });
        if (assez(gens, 6)) exo(sid, `Contrôle : ${ch}`, (r) => { const qs = tirer(r, gens, 6); return qs && { context: `Contrôle sur le chapitre « ${ch} » : six questions, de la plus simple à la plus difficile.`, steps: qs.map((o, k) => step(o, bareme(6)[k])) }; });
        if (i > 0 && assez(chs[i - 1][1], 3)) {
          const [ch0, g0] = chs[i - 1];
          exo(sid, `Révision : ${ch0} et ${ch}`, (r) => { const v = new Set(), a = tirer(r, g0, 3, v), b = a && tirer(r, gens, 3, v); return a && b && { context: `On révise deux chapitres qui se suivent : « ${ch0} » puis « ${ch} ».`, steps: [...a, ...b].map((o, k) => step(o, k % 3 === 2 ? 1.5 : 1)) }; });
        }
      });
      // devoirs types ciblés : trois chapitres qui se suivent, puis trimestres, puis composition
      const D = (DEVGEN[sid] = []);
      const ok6 = chs.filter(([, g]) => assez(g, 6));
      // interrogation écrite par chapitre, puis devoir sur deux chapitres qui se suivent
      ok6.filter(([, g]) => assez(g, 8)).forEach((c) => D.push({ t: `Interrogation écrite : ${c[0]}`, chs: [c] }));
      for (let i = 0; i + 1 < ok6.length; i++) D.push({ t: `Devoir sur ${ok6[i][0]} et ${ok6[i + 1][0]}`, chs: ok6.slice(i, i + 2) });
      for (let i = 0; i + 2 < ok6.length; i++) D.push({ t: `Devoir sur ${ok6[i][0]}, ${ok6[i + 1][0]} et ${ok6[i + 2][0]}`, chs: ok6.slice(i, i + 3) });
      if (ok6.length >= 3) {
        const tiers = Math.ceil(ok6.length / 3);
        ["1er", "2e", "3e"].forEach((tri, k) => { const part = ok6.slice(k * tiers, (k + 1) * tiers); if (part.length) D.push({ t: `Devoir du ${tri} trimestre`, chs: part }); });
        for (let i = 0; i + 3 < ok6.length; i++) D.push({ t: `Devoir surveillé : de ${ok6[i][0]} à ${ok6[i + 3][0]}`, chs: ok6.slice(i, i + 4) });
        const moitie = Math.ceil(ok6.length / 2);
        D.push({ t: "Devoir de synthèse du 1er semestre", chs: ok6.slice(0, moitie) });
        D.push({ t: "Devoir de synthèse du 2nd semestre", chs: ok6.slice(moitie) });
        D.push({ t: "Composition de fin d'année (tout le programme)", chs: ok6 });
      }
    }
  }
  globalThis.installerX5 = installer;

  // devoir type ciblé, noté sur 20 : un exercice par chapitre (quatre au plus), questions toutes différentes
  globalThis.genDevoir = (sid, k, r = Math.random) => {
    installer();
    const d = (DEVGEN[sid] || [])[k], subj = (DATA.subjects || []).find((s) => s.id === sid);
    if (!d || !subj) return null;
    const pris = d.chs.length > 4 ? mix(r, d.chs).slice(0, 4) : d.chs;
    const ordre = (progs()[sid] || []);
    pris.sort((a, b) => ordre.indexOf(a[0]) - ordre.indexOf(b[0]));
    const nq = pris.length >= 4 ? 4 : pris.length === 3 ? 5 : pris.length === 2 ? 6 : 8;
    const parts = [], v = new Set();
    for (const [ch, gens] of pris) {
      const qs = tirer(r, gens, nq, v);
      if (!qs) return null;
      const steps = qs.map((o) => {
        const f = GH.fix(GH.clean({ q: o.q, ok: String(o.ok), faux: o.faux.slice(0, 3).map(String), e: o.e || "" }));
        if (!f) return null;
        const order = [0, 1, 2, 3].sort(() => r() - 0.5), c = [f.ok, ...f.faux];
        return { q: f.q, c: order.map((i) => c[i]), a: order.indexOf(0), e: f.e, pts: 1 };
      });
      if (steps.includes(null)) return null;
      parts.push({ title: `Exercice ${parts.length + 1} : ${ch}`, context: "", steps });
    }
    const tot = parts.reduce((a, p) => a + p.steps.length, 0);
    parts.forEach((p) => p.steps.forEach((s) => (s.pts = Math.round((20 / tot) * 4) / 4)));
    const sum = parts.reduce((x, p) => x + p.steps.reduce((y, s) => y + s.pts, 0), 0), last = parts[parts.length - 1].steps;
    last[last.length - 1].pts = Math.round((last[last.length - 1].pts + 20 - sum) * 100) / 100;
    const prim = /^(ce|cm)/.test(sid);
    return { id: `gs-${sid}~${k}`, levels: subj.levels, exam: "Devoir", year: "type", subject: subj.name, title: d.t, gen: true, duration: prim ? "1 h" : "2 h", guided: parts };
  };
  globalThis.devoirsX5 = (sid) => { installer(); return (DEVGEN[sid] || []).map((d, k) => ({ id: `gs-${sid}~${k}`, t: d.t })); };
})();
