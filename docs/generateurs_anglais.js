"use strict";
// Anglais du CE1 au CM2 : questions à mots nouveaux tirées du vocabulaire de chaque chapitre (VOCAB_EN, docs/vocab_en.js).
// Mots et phrases dans les deux sens, l'intrus, la phrase à remettre dans l'ordre ; un exercice guidé par chapitre.
(() => {
  if (typeof VOCAB_EN === "undefined") return;
  const { pick } = GH;
  const mix = (r, a) => a.map((x) => [r(), x]).sort((p, q) => p[0] - q[0]).map((p) => p[1]);
  const autres = (r, pool, ok, n = 3) => mix(r, [...new Set(pool.map(String))].filter((x) => x !== String(ok))).slice(0, n);
  const NOUV = [];
  const add = (sid, ch, f) => { const it = [ch, f]; (GEN[sid] = GEN[sid] || []).push(it); NOUV.push(it); };
  const S = (q, ok, faux, e, pts = 1) => ({ q, ok: String(ok), faux: faux.map(String), e, pts });
  const ex = (sid, t, make) => (EXGEN[sid] = EXGEN[sid] || []).push({ t, make });
  // dans « remets dans l'ordre », la majuscule du premier mot donnerait la réponse : on l'enlève (sauf noms propres et « I »)
  const PROPRE = /^(I|I'm|Moussa|Awa|Senegal|Dakar|Gambia|Ghana|Independence|Thieboudienne)$/;
  const bas = (w) => (PROPRE.test(w) ? w : w.charAt(0).toLowerCase() + w.slice(1));
  const melange = (r, phrase) => { const w = phrase.replace(/[.!?]$/, "").split(" ").map((x, i) => (i ? x : bas(x))); if (w.length < 3) return null;
    const fin = (phrase.match(/[.!?]$/) || [""])[0], out = new Set();
    for (let i = 0; i < 20 && out.size < 3; i++) { const m = mix(r, w).join(" ") + fin; if (m !== phrase) out.add(m); }
    return out.size === 3 ? [...out] : null; };

  for (const [lv, chs] of Object.entries(VOCAB_EN)) {
    const sid = `${lv.toLowerCase()}-anglais`, tousMots = chs.flatMap((c) => (c.forme ? [] : c.mots));
    for (const c of chs) {
      const M = c.mots, P = c.phrases, F = c.forme;
      if (F) {
        add(sid, c.t, (r) => { const [a, b] = pick(r, M); return { q: `${F} « ${a} » :`, ok: b, faux: autres(r, M.map((x) => x[1]).concat([a + "s", a + "ed", a + "er"]), b), e: `${a} → ${b}.` }; });
        add(sid, c.t, (r) => { const [a, b] = pick(r, M); return { q: `« ${b} » vient de :`, ok: a, faux: autres(r, M.map((x) => x[0]), a), e: `${a} → ${b}.` }; });
      } else {
        add(sid, c.t, (r) => { const [a, b] = pick(r, M); return { q: `Comment dit-on « ${b} » en anglais ?`, ok: a, faux: autres(r, M.map((x) => x[0]), a), e: `${b} = ${a}.` }; });
        add(sid, c.t, (r) => { const [a, b] = pick(r, M); return { q: `Que veut dire « ${a} » ?`, ok: b, faux: autres(r, M.map((x) => x[1]), b), e: `${a} = ${b}.` }; });
        // l'intrus : 3 mots du thème et 1 d'un autre thème
        add(sid, c.t, (r) => { const trois = mix(r, M).slice(0, 3).map((x) => x[0]), set = new Set(M.map((x) => x[0])), intr = pick(r, tousMots.filter((x) => !set.has(x[0])));
          if (!intr) return null; return { q: `Trouve l'intrus (le mot qui n'est pas du thème « ${c.t} ») :`, ok: intr[0], faux: trois, e: `« ${intr[0]} » veut dire « ${intr[1]} » : il n'est pas de ce thème.` }; });
      }
      add(sid, c.t, (r) => { const [a, b] = pick(r, P); return { q: `Que veut dire « ${a} » ?`, ok: b, faux: autres(r, P.map((x) => x[1]), b), e: `${a} = ${b}.` }; });
      add(sid, c.t, (r) => { const [a, b] = pick(r, P); return { q: `Comment dit-on en anglais : « ${b} » ?`, ok: a, faux: autres(r, P.map((x) => x[0]), a), e: `${b} = ${a}.` }; });
      add(sid, c.t, (r) => { const [a, b] = pick(r, P), f = melange(r, a); if (!f) return null; const w = a.split(" "); w[0] = bas(w[0]); return { q: `Remets les mots dans l'ordre (« ${b} ») :`, ok: w.join(" "), faux: f, e: `La phrase correcte : ${a}` }; });
      // exercice guidé du chapitre
      ex(sid, c.t, (r) => { const ps = mix(r, P).slice(0, 2), ms = mix(r, M).slice(0, 2);
        return { context: `Thème : ${c.t}. Lis (ou écoute) puis réponds.`, steps: [
          ...ps.map(([a, b]) => S(`« ${a} » veut dire :`, b, autres(r, P.map((x) => x[1]), b), `${a} = ${b}.`, 1)),
          ...ms.map(([a, b]) => F ? S(`${F} « ${a} » :`, b, autres(r, M.map((x) => x[1]), b), `${a} → ${b}.`, 1.5) : S(`En anglais, « ${b} » se dit :`, a, autres(r, M.map((x) => x[0]), a), `${b} = ${a}.`, 1.5))] }; });
    }
  }
  for (const it of NOUV) { const f = it[1]; it[1] = (r) => { for (let i = 0; i < 12; i++) { let o; try { o = f(r); } catch (er) { continue; }
    if (!o || o.ok == null || /NaN|undefined|Infinity/.test(JSON.stringify(o))) continue; o = GH.fix(GH.clean(o)); if (o && new Set([o.ok, ...o.faux]).size === 4) return o; } return null; }; }
})();
