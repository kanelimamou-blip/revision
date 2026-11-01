"use strict";
// Élémentaire (CE1 à CM2, programme CEB) : QCM à nombres et à mots nouveaux à chaque tirage,
// et exercices guidés (au moins 3 modèles par matière, donc des devoirs types neufs).
// Les titres de chapitres sont ceux de contenu/primaire_<classe>.py.
(() => {
  const { ri, pick } = GH;
  const mix = (r, a) => a.map((x) => [r(), x]).sort((p, q) => p[0] - q[0]).map((p) => p[1]);
  const autres = (r, pool, ok, n = 3) => mix(r, [...new Set(pool.map(String))].filter((x) => x !== String(ok))).slice(0, n);
  const NOUV = [];
  const fr = (t) => String(t).replace(/\bde le /g, "du ").replace(/\bde les /g, "des ").replace(/\bà le /g, "au ").replace(/\bà les /g, "aux ").replace(/\bde ([aeéiouh])/gi, "d'$1").replace(/\bde ([AEÉIOU])/g, "d'$1");
  const add = (sid, ch, f) => { const it = [ch, f]; (GEN[sid] = GEN[sid] || []).push(it); NOUV.push(it); };
  const F = (x) => Math.round(x).toLocaleString("fr-FR");
  const D = (x, d = 2) => Number(x.toFixed(d)).toLocaleString("fr-FR");
  const S = (q, ok, faux, e, pts = 1) => ({ q, ok: String(ok), faux: faux.map(String), e, pts });
  const ex = (sid, t, make) => (EXGEN[sid] = EXGEN[sid] || []).push({ t, make });
  const near = (v, ds) => ds.map((d) => v + d).filter((x) => x >= 0 && x !== v);
  const num = (r, ok, ds, fmt = F, u = "") => autres(r, near(ok, ds).map((x) => fmt(x) + u), fmt(ok) + u);
  // paire de faits : [a, b] → « a ? » → b, et l'inverse si les a sont distincts
  const paire = (sid, ch, rows, aVersB, bVersA) => {
    if (new Set(rows.map((x) => x[1])).size >= 4) add(sid, ch, (r) => { const [a, b] = pick(r, rows); return { q: aVersB(a), ok: b, faux: autres(r, rows.map((x) => x[1]), b), e: `${a} : ${b}.` }; });
    if (bVersA && new Set(rows.map((x) => x[0])).size >= 4) add(sid, ch, (r) => { const [a, b] = pick(r, rows); return { q: bVersA(b), ok: a, faux: autres(r, rows.map((x) => x[0]), a), e: `${a} : ${b}.` }; });
  };
  const an = (d) => String(d);
  const chrono = (sid, ch, rows) => {
    add(sid, ch, (r) => { const [d, ev] = pick(r, rows); return { q: `En quelle année : ${ev} ?`, ok: an(d), faux: autres(r, rows.map((x) => an(x[0])).concat([an(d + 10), an(d - 10), an(d + 1)]), an(d)), e: `${ev} : ${an(d)}.` }; });
    add(sid, ch, (r) => { const [d, ev] = pick(r, rows); return { q: `Quel événement date de ${an(d)} ?`, ok: ev, faux: autres(r, rows.filter((x) => x[0] !== d).map((x) => x[1]), ev), e: `${an(d)} : ${ev}.` }; });
    add(sid, ch, (r) => { const xs = mix(r, rows).slice(0, 4); if (new Set(xs.map((x) => x[0])).size < 4) return null; const ok = xs.reduce((a, b) => (a[0] <= b[0] ? a : b));
      return { q: "Lequel de ces événements est le plus ancien ?", ok: ok[1], faux: xs.filter((x) => x !== ok).map((x) => x[1]), e: xs.slice().sort((a, b) => a[0] - b[0]).map((x) => `${x[0]} : ${x[1]}`).join(" ; ") + "." }; });
  };
  // exercice guidé de 4 faits tirés d'une ou plusieurs tables [question, réponse, explication?]
  const exFaits = (sid, t, ctx, rows) => ex(sid, t, (r) => { const xs = mix(r, rows).slice(0, 4);
    return { context: ctx, steps: xs.map(([q, ok, e], i) => S(fr(q), ok, autres(r, rows.map((x) => x[1]), ok), e || `${ok}.`, i < 2 ? 1 : 1.5)) }; });
  const exChrono = (sid, t, rows) => ex(sid, t, (r) => { const xs = mix(r, rows).slice(0, 4).sort((a, b) => a[0] - b[0]); if (new Set(xs.map((x) => x[0])).size < 4) return null; const d = xs[3][0] - xs[0][0];
    return { context: `Frise à compléter : ${mix(r, xs).map((x) => `${x[1]} (${x[0]})`).join(" ; ")}.`, steps: [
      S("Événement le plus ancien :", xs[0][1], xs.slice(1).map((x) => x[1]), `${xs[0][0]} : ${xs[0][1]}.`, 1),
      S("Événement le plus récent :", xs[3][1], xs.slice(0, 3).map((x) => x[1]), `${xs[3][0]} : ${xs[3][1]}.`, 1),
      S("Nombre d'années entre le premier et le dernier :", String(d), autres(r, [d + 1, d - 1, d + 10, d * 2].filter((x) => x > 0), d), `${xs[3][0]} − ${xs[0][0]} = ${d} ans.`, 1.5),
      S(`En quelle année : ${xs[1][1]} ?`, String(xs[1][0]), autres(r, xs.map((x) => x[0]).filter((x) => x !== xs[1][0]).concat([xs[1][0] + 10]), xs[1][0]), `${xs[1][1]} : ${xs[1][0]}.`, 1.5)] }; });

  // =====================================================================================================
  // CALCUL commun, réglé par classe
  // =====================================================================================================
  const PRENOMS = ["Awa", "Moussa", "Fatou", "Ibrahima", "Khady", "Modou", "Aïssatou", "Ousmane", "Bineta", "Cheikh", "Ndèye", "Lamine", "Mariama", "Abdou"];
  const OBJ = [["mangue", "mangues"], ["cahier", "cahiers"], ["bonbon", "bonbons"], ["crayon", "crayons"], ["orange", "oranges"], ["bille", "billes"], ["œuf", "œufs"], ["livre", "livres"]];
  const calcul = (sid, chNum, chAdd, chMul, chDiv, max) => {
    add(sid, chNum, (r) => { const n = ri(r, 10, max - 1), k = pick(r, max > 10000 ? [1, 10, 100, 1000] : max > 1000 ? [1, 10, 100] : [1, 10]), u = { 1: "unités", 10: "dizaines", 100: "centaines", 1000: "milliers" }[k], c = Math.floor(n / k) % 10;
      return { q: `Dans ${F(n)}, quel est le chiffre des ${u} ?`, ok: String(c), faux: autres(r, String(n).split("").concat(["0", "5", "9"]), c), e: `${F(n)} : le chiffre des ${u} est ${c}.` }; });
    add(sid, chNum, (r) => { const xs = [...new Set(Array.from({ length: 6 }, () => ri(r, 10, max - 1)))].slice(0, 4); if (xs.length < 4) return null; const big = r() < 0.5, ok = big ? Math.max(...xs) : Math.min(...xs);
      return { q: `Quel est le plus ${big ? "grand" : "petit"} nombre ?`, ok: F(ok), faux: xs.filter((x) => x !== ok).map(F), e: `On compare d'abord le nombre de chiffres, puis les chiffres de gauche à droite : ${F(ok)}.` }; });
    add(sid, chNum, (r) => { const n = ri(r, 10, max - 2), s = r() < 0.5; const ok = s ? n + 1 : n - 1;
      return { q: `Quel nombre vient juste ${s ? "après" : "avant"} ${F(n)} ?`, ok: F(ok), faux: num(r, ok, [2, -2, 10, -10, s ? -2 : 2]), e: `${F(n)} ${s ? "+" : "−"} 1 = ${F(ok)}.` }; });
    add(sid, chAdd, (r) => { const a = ri(r, 10, Math.floor(max / 2)), b = ri(r, 10, Math.floor(max / 2)); return { q: `${F(a)} + ${F(b)} =`, ok: F(a + b), faux: num(r, a + b, [10, -10, 1, -1, 100, -100]), e: `${F(a)} + ${F(b)} = ${F(a + b)}.` }; });
    add(sid, chAdd, (r) => { const a = ri(r, 20, max - 1), b = ri(r, 5, a - 1); return { q: `${F(a)} − ${F(b)} =`, ok: F(a - b), faux: num(r, a - b, [10, -10, 1, -1, 100]), e: `${F(a)} − ${F(b)} = ${F(a - b)}. Vérification : ${F(a - b)} + ${F(b)} = ${F(a)}.` }; });
    add(sid, chAdd, (r) => { const p = pick(r, PRENOMS), [, o] = pick(r, OBJ), a = ri(r, 12, Math.min(500, max / 2)), b = ri(r, 3, a - 2), plus = r() < 0.5;
      return { q: `${p} a ${a} ${o}. ${plus ? `On lui en donne ${b}` : `Il en donne ${b}`}. Combien en a-t-il maintenant ?`, ok: String(plus ? a + b : a - b), faux: autres(r, near(plus ? a + b : a - b, [1, -1, 10, -10]).concat([plus ? a - b : a + b]), plus ? a + b : a - b), e: `${a} ${plus ? "+" : "−"} ${b} = ${plus ? a + b : a - b}.` }; });
    const tm = max > 1000 ? 12 : 10;
    add(sid, chMul, (r) => { const a = ri(r, 2, tm), b = ri(r, 2, tm); return { q: `${a} × ${b} =`, ok: String(a * b), faux: autres(r, [a * b + a, a * b - b, a + b, a * (b + 1), (a + 1) * b].filter((x) => x > 0), a * b), e: `${a} × ${b} = ${a * b}.` }; });
    add(sid, chMul, (r) => { const a = ri(r, 11, max > 1000 ? 999 : 99), b = ri(r, 2, 9); return { q: `${F(a)} × ${b} =`, ok: F(a * b), faux: num(r, a * b, [b, -b, 10, -10, a]), e: `${F(a)} × ${b} = ${F(a * b)}.` }; });
    add(sid, chMul, (r) => { const p = pick(r, PRENOMS), n = ri(r, 2, 9), q = ri(r, 3, 12), [, o] = pick(r, OBJ);
      return { q: `${p} a ${n} sachets de ${q} ${o}. Combien de ${o} en tout ?`, ok: String(n * q), faux: autres(r, [n + q, n * q + q, n * q - n, n * (q + 1)], n * q), e: `${n} × ${q} = ${n * q}.` }; });
    add(sid, chDiv, (r) => { const d = ri(r, 2, tm), q = ri(r, 2, max > 1000 ? 99 : 10), n = d * q; return { q: `${F(n)} ÷ ${d} =`, ok: F(q), faux: num(r, q, [1, -1, 2, 10]), e: `${d} × ${q} = ${F(n)}, donc ${F(n)} ÷ ${d} = ${q}.` }; });
    add(sid, chDiv, (r) => { const d = ri(r, 2, 9), q = ri(r, 2, 15), rest = ri(r, 1, d - 1), n = d * q + rest, [, o] = pick(r, OBJ);
      return { q: `On partage ${n} ${o} entre ${d} enfants. Combien en reste-t-il ?`, ok: String(rest), faux: autres(r, [0, rest + 1, q, d - rest, rest + 2].filter((x) => x >= 0 && x !== rest), rest), e: `${n} = ${d} × ${q} + ${rest} : chacun a ${q} ${o}, il en reste ${rest}.` }; });
  };
  calcul("ce1-maths", "Les nombres jusqu'à 1 000", "L'addition et la soustraction", "La multiplication et les tables", "Le partage et la division", 1000);
  calcul("ce2-maths", "Les nombres jusqu'à 100 000", "Addition et soustraction posées", "La multiplication", "La division", 100000);
  calcul("cm1-maths", "Les grands nombres", "Les quatre opérations", "Les quatre opérations", "Les quatre opérations", 10000000);
  calcul("cm2-maths", "Nombres entiers et opérations", "Nombres entiers et opérations", "Nombres entiers et opérations", "Nombres entiers et opérations", 100000000);

  // mesures
  const LONG = [["km", 1000], ["hm", 100], ["dam", 10], ["m", 1], ["dm", 0.1], ["cm", 0.01], ["mm", 0.001]];
  const MASS = [["t", 1000000], ["kg", 1000], ["hg", 100], ["dag", 10], ["g", 1], ["dg", 0.1], ["cg", 0.01]];
  const CAPA = [["hl", 100], ["dal", 10], ["l", 1], ["dl", 0.1], ["cl", 0.01], ["ml", 0.001]];
  const conv = (sid, ch, tabs, simple) => add(sid, ch, (r) => { const T = pick(r, tabs), i = ri(r, 0, T.length - 2), j = simple ? Math.min(T.length - 1, i + 1 + ri(r, 0, 1)) : ri(r, 0, T.length - 1); if (i === j) return null;
    const [u1, f1] = T[i], [u2, f2] = T[j], v = simple ? ri(r, 2, 50) : ri(r, 2, 999) / pick(r, [1, 10]), res = (v * f1) / f2; if (res > 1e7 || res < 0.001) return null;
    const ok = `${D(res, 4)} ${u2}`; return { q: `${D(v, 2)} ${u1} = … ${u2}`, ok, faux: autres(r, [res * 10, res / 10, res * 100, res / 100].map((x) => `${D(x, 4)} ${u2}`), ok), e: `1 ${u1} = ${D(f1 / f2, 4)} ${u2}, donc ${D(v, 2)} ${u1} = ${ok}.` }; });
  conv("ce1-maths", "Mesurer des longueurs", [[["m", 100], ["dm", 10], ["cm", 1]]], true);
  conv("ce2-maths", "Longueurs et périmètres", [LONG.slice(0, 6)], true);
  conv("ce2-maths", "Masses, capacités et monnaie", [MASS.slice(1, 5), CAPA.slice(2)], true);
  conv("cm1-maths", "Les mesures de longueur, de masse et de capacité", [LONG, MASS, CAPA], false);
  conv("cm2-maths", "Les mesures : longueurs, masses, capacités, surfaces agraires", [LONG, MASS, CAPA], false);
  add("cm2-maths", "Les mesures : longueurs, masses, capacités, surfaces agraires", (r) => { const k = pick(r, [0, 1, 2]), v = ri(r, 2, 95) / pick(r, [1, 10]);
    const [q, res, u] = [[`${D(v)} ha = … a`, v * 100, "a"], [`${D(v)} ha = … m²`, v * 10000, "m²"], [`${D(v)} a = … m²`, v * 100, "m²"]][k], ok = `${D(res)} ${u}`;
    return { q, ok, faux: autres(r, [res * 10, res / 10, res * 100, res / 100].map((x) => `${D(x, 4)} ${u}`), ok), e: "1 ha = 100 a = 10 000 m² ; 1 a = 100 m² ; 1 ca = 1 m²." }; });
  add("cm2-maths", "Les mesures : longueurs, masses, capacités, surfaces agraires", (r) => { const s = ri(r, 2, 12) / 2, rd = ri(r, 4, 12) * 100, ok = s * rd;
    return { q: `Un champ de ${D(s)} ha a un rendement de ${F(rd)} kg/ha. Production ?`, ok: `${F(ok)} kg`, faux: autres(r, [ok / 10, ok * 10, s + rd, rd].map((x) => `${F(x)} kg`), `${F(ok)} kg`), e: `${D(s)} × ${F(rd)} = ${F(ok)} kg.` }; });

  // monnaie
  add("ce1-maths", "Les masses, les capacités et la monnaie", (r) => { const a = ri(r, 1, 9) * 25, b = ri(r, 1, 8) * 25, B = Math.ceil((a + b) / 100) * 100 + pick(r, [0, 100, 400]); const ok = B - a - b;
    return { q: `${pick(r, PRENOMS)} achète un pain à ${a} F et un sachet de lait à ${b} F. Il paie avec ${B} F. Monnaie rendue ?`, ok: `${ok} F`, faux: autres(r, [ok + 25, ok + 50, a + b, Math.abs(ok - 25)].map((x) => `${x} F`), `${ok} F`), e: `${a} + ${b} = ${a + b} F ; ${B} − ${a + b} = ${ok} F.` }; });
  add("ce2-maths", "Masses, capacités et monnaie", (r) => { const n = ri(r, 2, 9), p = ri(r, 2, 20) * 50, B = Math.ceil((n * p) / 1000) * 1000 + pick(r, [0, 1000]), ok = B - n * p;
    return { q: `${n} cahiers à ${p} F l'un. On paie avec ${F(B)} F. Monnaie ?`, ok: `${F(ok)} F`, faux: autres(r, [ok + 50, ok + 100, n * p, Math.abs(ok - 50)].map((x) => `${F(x)} F`), `${F(ok)} F`), e: `${n} × ${p} = ${F(n * p)} F ; ${F(B)} − ${F(n * p)} = ${F(ok)} F.` }; });

  // temps et durées
  const hm = (m) => `${Math.floor(m / 60) % 24} h ${String(m % 60).padStart(2, "0")}`;
  const duree = (sid, ch, pas) => {
    add(sid, ch, (r) => { const d = ri(r, 6 * 60 / pas, 18 * 60 / pas) * pas, t = ri(r, 1, 30) * pas, ok = hm(d + t);
      return { q: `Il est ${hm(d)}. Quelle heure sera-t-il dans ${t >= 60 ? `${Math.floor(t / 60)} h ${t % 60 ? t % 60 + " min" : ""}` : t + " min"} ?`.replace(/ +\?/, " ?"), ok, faux: autres(r, [hm(d + t + pas), hm(d + t - pas), hm(d + t + 60), hm(d + Math.max(pas, t - 60))], ok), e: `${hm(d)} + ${t} min = ${ok}.` }; });
    add(sid, ch, (r) => { const [u, v, w, k] = pick(r, [["jours", "semaine", 7, 1], ["mois", "année", 12, 1], ["minutes", "heure", 60, 1], ["heures", "jour", 24, 1], ["jours", "semaines", 7, 0], ["mois", "années", 12, 0]]), n = k ? 1 : ri(r, 2, 5);
      return { q: `Combien de ${u} dans ${n === 1 ? "une" : n} ${v} ?`, ok: String(n * w), faux: autres(r, [n * w + 1, n * w - 1, n * 10, n * (w === 7 ? 30 : w === 12 ? 10 : w === 60 ? 100 : 12), n * w + w], n * w), e: `1 ${v.replace(/s$/, "")} = ${w} ${u} ; ${n} × ${w} = ${n * w}.` }; });
  };
  duree("ce1-maths", "Le temps : l'heure, les jours et les mois", 15);
  duree("ce2-maths", "Les durées et le calendrier", 5);
  duree("cm1-maths", "Les durées et les vitesses", 5);
  duree("cm2-maths", "Durées, vitesses et distances", 5);
  const vit = (sid, ch) => {
    add(sid, ch, (r) => { const v = ri(r, 3, 12) * 10, t = pick(r, [0.5, 1, 1.5, 2, 2.5, 3, 4]), d = v * t; return { q: `Un car roule à ${v} km/h pendant ${D(t)} h. Distance parcourue ?`, ok: `${D(d)} km`, faux: autres(r, [d + v, v / t, d / 2, v + t].map((x) => `${D(x)} km`), `${D(d)} km`), e: `d = v × t = ${v} × ${D(t)} = ${D(d)} km.` }; });
    add(sid, ch, (r) => { const v = ri(r, 3, 12) * 10, t = pick(r, [1, 2, 3, 4, 5]), d = v * t; return { q: `${d} km parcourus en ${t} h. Vitesse moyenne ?`, ok: `${v} km/h`, faux: autres(r, [d * t, v + 10, d - t, v - 10].map((x) => `${x} km/h`), `${v} km/h`), e: `v = d ÷ t = ${d} ÷ ${t} = ${v} km/h.` }; });
    add(sid, ch, (r) => { const v = ri(r, 3, 12) * 10, t = pick(r, [0.5, 1, 1.5, 2, 2.5, 3]), d = v * t, ok = `${Math.floor(t)} h ${t % 1 ? "30 min" : ""}`.trim(); return { q: `${D(d)} km à ${v} km/h : durée du trajet ?`, ok, faux: autres(r, [t + 0.5, t + 1, Math.max(0.5, t - 0.5), t * 2].map((x) => `${Math.floor(x)} h ${x % 1 ? "30 min" : ""}`.trim()), ok), e: `t = d ÷ v = ${D(d)} ÷ ${v} = ${D(t)} h = ${ok}.` }; });
  };
  vit("cm1-maths", "Les durées et les vitesses");
  vit("cm2-maths", "Durées, vitesses et distances");

  // fractions et décimaux
  const frac = (sid, ch, avance) => {
    add(sid, ch, (r) => { const d = pick(r, [2, 3, 4, 5, 6, 8, 10]), k = ri(r, 2, 12), n = ri(r, 1, d - 1), T = d * k, ok = n * k;
      return { q: `Combien valent les ${n}/${d} de ${T} ?`, ok: String(ok), faux: autres(r, [k, T - ok, ok + k, T / n | 0].filter((x) => x > 0), ok), e: `${T} ÷ ${d} = ${k} ; ${k} × ${n} = ${ok}.` }; });
    if (avance) {
      add(sid, ch, (r) => { const d = pick(r, [2, 4, 5, 8, 10, 20, 25]), n = ri(r, 1, d - 1), v = n / d, ok = D(v, 3); return { q: `${n}/${d} en écriture décimale :`, ok, faux: autres(r, [`${n},${d}`, D(d / n, 3), D(v * 10, 3), D(v / 10, 3)], ok), e: `${n} ÷ ${d} = ${ok}.` }; });
      add(sid, ch, (r) => { const d = pick(r, [6, 8, 9, 10, 12, 15, 16, 18, 20, 24]), divs = [2, 3, 4, 5, 6].filter((k) => d % k === 0), k = pick(r, divs), n = k * ri(r, 1, d / k - 1), g = (a, b) => (b ? g(b, a % b) : a), p = g(n, d), ok = `${n / p}/${d / p}`;
        if (p === 1) return null; return { q: `Simplifie ${n}/${d} au maximum :`, ok, faux: autres(r, [`${n / k}/${d}`, `${n}/${d / k}`, `${d / p}/${n / p}`, `${n / p + 1}/${d / p}`], ok), e: `On divise ${n} et ${d} par ${p} : ${ok}.` }; });
      add(sid, ch, (r) => { const a = ri(r, 1, 999) / 100, b = ri(r, 1, 999) / 100; if (a === b) return null; const ok = D(Math.max(a, b)); return { q: `Le plus grand : ${D(a)} ou ${D(b)} ?`, ok, faux: autres(r, [D(Math.min(a, b)), "Ils sont égaux", D(Math.max(a, b) / 10)], ok), e: `On compare les parties entières, puis les dixièmes et les centièmes : ${ok}.` }; });
    }
  };
  frac("ce2-maths", "Les fractions simples", false);
  frac("cm1-maths", "Les fractions", true);
  frac("cm2-maths", "Fractions et nombres décimaux", true);
  const dec = (sid, ch) => {
    add(sid, ch, (r) => { const a = ri(r, 11, 999) / 10, b = ri(r, 11, 999) / 100, s = r() < 0.5, ok = s ? a + b : a - b; if (ok <= 0) return null;
      return { q: `${D(a)} ${s ? "+" : "−"} ${D(b)} =`, ok: D(ok), faux: autres(r, [ok + 1, ok + 0.1, ok - 0.01, s ? a - b : a + b].filter((x) => x > 0).map((x) => D(x)), D(ok)), e: `On aligne les virgules : ${D(a)} ${s ? "+" : "−"} ${D(b)} = ${D(ok)}.` }; });
    add(sid, ch, (r) => { const a = ri(r, 11, 999) / 100, k = pick(r, [10, 100, 1000]), m = r() < 0.5, ok = m ? a * k : a / k;
      return { q: `${D(a)} ${m ? "×" : "÷"} ${F(k)} =`, ok: D(ok, 5), faux: autres(r, [m ? a / k : a * k, ok * 10, ok / 10, a + k].map((x) => D(x, 5)), D(ok, 5)), e: `${m ? "× " + F(k) + " : la virgule avance" : "÷ " + F(k) + " : la virgule recule"} de ${String(k).length - 1} rang(s).` }; });
    add(sid, ch, (r) => { const a = ri(r, 11, 99) / 10, b = ri(r, 2, 9), ok = a * b; return { q: `${D(a)} × ${b} =`, ok: D(ok), faux: autres(r, [ok * 10, ok / 10, ok + b, a + b].map((x) => D(x)), D(ok)), e: `${Math.round(a * 10)} × ${b} = ${Math.round(ok * 10)}, une décimale : ${D(ok)}.` }; });
  };
  dec("cm1-maths", "Les nombres décimaux");
  dec("cm2-maths", "Opérations sur les nombres décimaux");

  // proportionnalité, pourcentages, commerce, moyenne
  const prop = (sid, ch) => add(sid, ch, (r) => { const n1 = ri(r, 2, 6), p1 = ri(r, 2, 30) * 50 * n1, n2 = ri(r, 2, 12); if (n1 === n2) return null; const u = p1 / n1, ok = u * n2;
    return { q: `${n1} kg de sucre coûtent ${F(p1)} F. Prix de ${n2} kg ?`, ok: `${F(ok)} F`, faux: autres(r, [u, p1 + n2, ok + u, p1 * n2].map((x) => `${F(x)} F`), `${F(ok)} F`), e: `Prix d'1 kg : ${F(p1)} ÷ ${n1} = ${F(u)} F ; ${n2} × ${F(u)} = ${F(ok)} F.` }; });
  prop("cm1-maths", "Proportionnalité et règle de trois");
  prop("cm2-maths", "Proportionnalité, pourcentages et échelles");
  add("cm2-maths", "Proportionnalité, pourcentages et échelles", (r) => { const p = pick(r, [5, 10, 15, 20, 25, 30, 40, 50]), P = ri(r, 2, 60) * 1000, ok = (P * p) / 100;
    return { q: `${p} % de ${F(P)} F =`, ok: `${F(ok)} F`, faux: autres(r, [ok * 10, ok / 10, P - ok, p * 100].map((x) => `${F(x)} F`), `${F(ok)} F`), e: `${F(P)} × ${p} ÷ 100 = ${F(ok)} F.` }; });
  add("cm2-maths", "Proportionnalité, pourcentages et échelles", (r) => { const p = pick(r, [10, 20, 25, 30, 40, 50]), P = ri(r, 2, 40) * 1000, ok = P - (P * p) / 100;
    return { q: `Article à ${F(P)} F, remise de ${p} %. Prix payé ?`, ok: `${F(ok)} F`, faux: autres(r, [(P * p) / 100, P + (P * p) / 100, P - p, ok - 500].map((x) => `${F(x)} F`), `${F(ok)} F`), e: `Remise : ${F((P * p) / 100)} F ; ${F(P)} − ${F((P * p) / 100)} = ${F(ok)} F.` }; });
  add("cm2-maths", "Proportionnalité, pourcentages et échelles", (r) => { const e = pick(r, [100, 200, 500, 1000, 10000, 50000, 100000, 1000000]), c = ri(r, 2, 15), m = (c * e) / 100, ok = m >= 1000 ? `${D(m / 1000, 3)} km` : `${D(m, 2)} m`;
    return { q: `Échelle 1/${F(e)} : ${c} cm sur la carte représentent …`, ok, faux: autres(r, [m * 10, m / 10, m * 100, m / 100].map((x) => (x >= 1000 ? `${D(x / 1000, 3)} km` : `${D(x, 2)} m`)), ok), e: `${c} × ${F(e)} = ${F(c * e)} cm = ${ok}.` }; });
  add("cm2-maths", "Prix d'achat, de revient, de vente, bénéfice et perte", (r) => { const A = ri(r, 10, 200) * 500, f = ri(r, 1, 20) * 500, V = A + f + ri(r, -10, 30) * 500, R = A + f, b = V - R; if (!b) return null;
    const ok = b > 0 ? `bénéfice de ${F(b)} F` : `perte de ${F(-b)} F`;
    return { q: `Achat ${F(A)} F, frais ${F(f)} F, vente ${F(V)} F. Résultat ?`, ok, faux: autres(r, [b > 0 ? `perte de ${F(b)} F` : `bénéfice de ${F(-b)} F`, `bénéfice de ${F(Math.abs(V - A))} F`, `perte de ${F(Math.abs(V - A) + f)} F`, `bénéfice de ${F(Math.abs(b) + f)} F`], ok), e: `Prix de revient : ${F(A)} + ${F(f)} = ${F(R)} F ; ${F(V)} − ${F(R)} = ${b > 0 ? "" : "−"}${F(Math.abs(b))} F.` }; });
  add("cm2-maths", "Prix d'achat, de revient, de vente, bénéfice et perte", (r) => { const C = ri(r, 2, 50) * 10000, t = ri(r, 2, 9), n = ri(r, 1, 4), ok = (C * t * n) / 100;
    return { q: `Intérêt de ${F(C)} F placés à ${t} % pendant ${n} an${n > 1 ? "s" : ""} :`, ok: `${F(ok)} F`, faux: autres(r, [(C * t) / 100, ok * 10, ok / 10, C + ok].map((x) => `${F(x)} F`), `${F(ok)} F`), e: `${F(C)} × ${t} × ${n} ÷ 100 = ${F(ok)} F.` }; });
  add("cm2-maths", "Partages égaux et inégaux, moyenne", (r) => { const xs = Array.from({ length: ri(r, 3, 5) }, () => ri(r, 4, 18)), s = xs.reduce((a, b) => a + b, 0); if (s % xs.length) return null; const ok = s / xs.length;
    return { q: `Moyenne de ${xs.join(" ; ")} :`, ok: String(ok), faux: autres(r, [s, ok + 1, ok - 1, Math.max(...xs)], ok), e: `(${xs.join(" + ")}) ÷ ${xs.length} = ${s} ÷ ${xs.length} = ${ok}.` }; });
  add("cm2-maths", "Partages égaux et inégaux, moyenne", (r) => { const p = ri(r, 2, 40) * 500, d = ri(r, 1, 20) * 500, S0 = 2 * p + d, g = r() < 0.5;
    return { q: `Deux parts : somme ${F(S0)} F, différence ${F(d)} F. ${g ? "Grande" : "Petite"} part ?`, ok: `${F(g ? p + d : p)} F`, faux: autres(r, [g ? p : p + d, S0 / 2, S0 - d, p + 2 * d].map((x) => `${F(x)} F`), `${F(g ? p + d : p)} F`), e: `Petite part : (${F(S0)} − ${F(d)}) ÷ 2 = ${F(p)} F ; grande part : ${F(p + d)} F.` }; });

  // géométrie : périmètres, aires, volumes
  const peri = (sid, ch, aires) => {
    add(sid, ch, (r) => { const c = r() < 0.4, L = ri(r, 3, 40), l = c ? L : ri(r, 2, L - 1), ok = 2 * (L + l);
      return { q: c ? `Périmètre d'un carré de ${L} m de côté :` : `Périmètre d'un rectangle de ${L} m sur ${l} m :`, ok: `${ok} m`, faux: autres(r, [L + l, L * l, ok + 2, 4 * L + (c ? 2 : 0)].map((x) => `${x} m`), `${ok} m`), e: c ? `P = 4 × ${L} = ${ok} m.` : `P = 2 × (${L} + ${l}) = ${ok} m.` }; });
    if (aires) {
      add(sid, ch, (r) => { const c = r() < 0.4, L = ri(r, 3, 40), l = c ? L : ri(r, 2, L - 1), ok = L * l;
        return { q: c ? `Aire d'un carré de ${L} m de côté :` : `Aire d'un rectangle de ${L} m sur ${l} m :`, ok: `${ok} m²`, faux: autres(r, [2 * (L + l), L + l, ok + L, ok * 2].map((x) => `${x} m²`), `${ok} m²`), e: `A = ${L} × ${l} = ${ok} m².` }; });
      add(sid, ch, (r) => { const b = ri(r, 2, 30), h = ri(r, 2, 20), ok = (b * h) / 2; return { q: `Aire d'un triangle de base ${b} cm et de hauteur ${h} cm :`, ok: `${D(ok)} cm²`, faux: autres(r, [b * h, b + h, ok + b, 2 * (b + h)].map((x) => `${D(x)} cm²`), `${D(ok)} cm²`), e: `A = ${b} × ${h} ÷ 2 = ${D(ok)} cm².` }; });
    }
  };
  peri("ce2-maths", "Longueurs et périmètres", false);
  peri("cm1-maths", "Périmètres et aires", true);
  peri("cm2-maths", "Périmètres et aires des figures", true);
  add("cm2-maths", "Périmètres et aires des figures", (r) => { const R = ri(r, 1, 20), dsk = r() < 0.5, ok = dsk ? R * R * 3.14 : 2 * R * 3.14;
    return { q: dsk ? `Aire d'un disque de rayon ${R} m (π ≈ 3,14) :` : `Périmètre d'un cercle de rayon ${R} m (π ≈ 3,14) :`, ok: `${D(ok)} ${dsk ? "m²" : "m"}`, faux: autres(r, (dsk ? [2 * R * 3.14, R * 3.14, 4 * R * R * 3.14, R * R] : [R * 3.14, R * R * 3.14, 4 * R * 3.14, 2 * R]).map((x) => `${D(x)} ${dsk ? "m²" : "m"}`), `${D(ok)} ${dsk ? "m²" : "m"}`), e: dsk ? `A = ${R} × ${R} × 3,14 = ${D(ok)} m².` : `P = diamètre × 3,14 = ${2 * R} × 3,14 = ${D(ok)} m.` }; });
  add("cm2-maths", "Périmètres et aires des figures", (r) => { const B = ri(r, 6, 30), b = ri(r, 2, B - 2), h = ri(r, 2, 20), ok = ((B + b) * h) / 2;
    return { q: `Aire d'un trapèze : grande base ${B} m, petite base ${b} m, hauteur ${h} m :`, ok: `${D(ok)} m²`, faux: autres(r, [(B + b) * h, B * b, ok + h, B * h].map((x) => `${D(x)} m²`), `${D(ok)} m²`), e: `A = (${B} + ${b}) × ${h} ÷ 2 = ${D(ok)} m².` }; });
  add("cm2-maths", "Les volumes", (r) => { const L = ri(r, 2, 12), l = ri(r, 1, L), h = ri(r, 1, 6), ok = L * l * h;
    return { q: `Volume d'un pavé de ${L} m × ${l} m × ${h} m :`, ok: `${ok} m³`, faux: autres(r, [L * l, 2 * (L + l) * h, L + l + h, ok * 10].map((x) => `${x} m³`), `${ok} m³`), e: `V = ${L} × ${l} × ${h} = ${ok} m³.` }; });
  add("cm2-maths", "Les volumes", (r) => { const v = ri(r, 2, 90) / pick(r, [1, 10]), k = pick(r, [0, 1, 2]), [q, res, u] = [[`${D(v)} m³ = … l`, v * 1000, "l"], [`${D(v)} dm³ = … cm³`, v * 1000, "cm³"], [`${D(v)} m³ = … dm³`, v * 1000, "dm³"]][k], ok = `${F(res)} ${u}`;
    return { q, ok, faux: autres(r, [res / 10, res * 10, res / 100, res / 1000].map((x) => `${D(x, 3)} ${u}`), ok), e: "Chaque unité de volume vaut 1 000 fois la suivante ; 1 dm³ = 1 l." }; });

  // =====================================================================================================
  // FRANÇAIS : conjugaison, accords, homophones, vocabulaire
  // =====================================================================================================
  const PRO = ["je", "tu", "il", "nous", "vous", "ils"], PRO_F = ["je", "tu", "elle", "nous", "vous", "elles"];
  const ER = ["chanter", "parler", "jouer", "danser", "marcher", "regarder", "aimer", "écouter", "travailler", "porter", "laver", "donner", "fermer", "sauter", "compter", "chercher", "dessiner", "aider", "planter", "cultiver"];
  const TERM = { present: ["e", "es", "e", "ons", "ez", "ent"], imparfait: ["ais", "ais", "ait", "ions", "iez", "aient"], futur: ["ai", "as", "a", "ons", "ez", "ont"], ps: ["ai", "as", "a", "âmes", "âtes", "èrent"] };
  const AVOIR = { present: ["ai", "as", "a", "avons", "avez", "ont"], imparfait: ["avais", "avais", "avait", "avions", "aviez", "avaient"], futur: ["aurai", "auras", "aura", "aurons", "aurez", "auront"], ps: ["eus", "eus", "eut", "eûmes", "eûtes", "eurent"] };
  const IRR = {
    être: { present: ["suis", "es", "est", "sommes", "êtes", "sont"], imparfait: ["étais", "étais", "était", "étions", "étiez", "étaient"], futur: ["serai", "seras", "sera", "serons", "serez", "seront"], ps: ["fus", "fus", "fut", "fûmes", "fûtes", "furent"] },
    avoir: AVOIR,
    aller: { present: ["vais", "vas", "va", "allons", "allez", "vont"], imparfait: ["allais", "allais", "allait", "allions", "alliez", "allaient"], futur: ["irai", "iras", "ira", "irons", "irez", "iront"], ps: ["allai", "allas", "alla", "allâmes", "allâtes", "allèrent"] },
    faire: { present: ["fais", "fais", "fait", "faisons", "faites", "font"], imparfait: ["faisais", "faisais", "faisait", "faisions", "faisiez", "faisaient"], futur: ["ferai", "feras", "fera", "ferons", "ferez", "feront"], ps: ["fis", "fis", "fit", "fîmes", "fîtes", "firent"] },
    finir: { present: ["finis", "finis", "finit", "finissons", "finissez", "finissent"], imparfait: ["finissais", "finissais", "finissait", "finissions", "finissiez", "finissaient"], futur: ["finirai", "finiras", "finira", "finirons", "finirez", "finiront"], ps: ["finis", "finis", "finit", "finîmes", "finîtes", "finirent"] },
    venir: { present: ["viens", "viens", "vient", "venons", "venez", "viennent"], imparfait: ["venais", "venais", "venait", "venions", "veniez", "venaient"], futur: ["viendrai", "viendras", "viendra", "viendrons", "viendrez", "viendront"], ps: ["vins", "vins", "vint", "vînmes", "vîntes", "vinrent"] },
    prendre: { present: ["prends", "prends", "prend", "prenons", "prenez", "prennent"], imparfait: ["prenais", "prenais", "prenait", "prenions", "preniez", "prenaient"], futur: ["prendrai", "prendras", "prendra", "prendrons", "prendrez", "prendront"], ps: ["pris", "pris", "prit", "prîmes", "prîtes", "prirent"] },
    dire: { present: ["dis", "dis", "dit", "disons", "dites", "disent"], imparfait: ["disais", "disais", "disait", "disions", "disiez", "disaient"], futur: ["dirai", "diras", "dira", "dirons", "direz", "diront"], ps: ["dis", "dis", "dit", "dîmes", "dîtes", "dirent"] },
    pouvoir: { present: ["peux", "peux", "peut", "pouvons", "pouvez", "peuvent"], imparfait: ["pouvais", "pouvais", "pouvait", "pouvions", "pouviez", "pouvaient"], futur: ["pourrai", "pourras", "pourra", "pourrons", "pourrez", "pourront"], ps: ["pus", "pus", "put", "pûmes", "pûtes", "purent"] },
  };
  const PP = { être: ["été", "avoir"], avoir: ["eu", "avoir"], aller: ["allé", "être"], faire: ["fait", "avoir"], finir: ["fini", "avoir"], venir: ["venu", "être"], prendre: ["pris", "avoir"], dire: ["dit", "avoir"], pouvoir: ["pu", "avoir"] };
  const ETRE_PR = IRR.être.present;
  const conj = (v, t, p) => {
    if (t === "pc") { const [pp, aux] = PP[v] || [v.slice(0, -2) + "é", "avoir"]; const a = (aux === "être" ? ETRE_PR : AVOIR.present)[p]; return `${a} ${pp}${aux === "être" && p >= 3 ? "s" : ""}`; }
    if (IRR[v]) return IRR[v][t][p];
    const rad = t === "futur" ? v : v.slice(0, -2); return rad + TERM[t][p];
  };
  const sujet = (v, t, p) => { const f = conj(v, t, p), s = PRO[p]; return s === "je" && /^[aeéèêiouh]/i.test(f) ? `j'${f}` : `${s} ${f}`; };
  const TNOM = { present: "présent", imparfait: "imparfait", futur: "futur simple", pc: "passé composé", ps: "passé simple" };
  const conjQ = (sid, ch, temps, verbes) => add(sid, ch, (r) => { const v = pick(r, verbes), t = pick(r, temps), p = ri(r, 0, 5), ok = sujet(v, t, p);
    const pool = [0, 1, 2, 3, 4, 5].filter((k) => k !== p).map((k) => `${PRO[p] === "je" ? "je" : PRO[p]} ${conj(v, t, k)}`.replace(/^je ([aeéèêiouh])/i, "j'$1"))
      .concat(Object.keys(TNOM).filter((x) => x !== t && (x !== "ps" || temps.includes("ps"))).map((x) => sujet(v, x, p)));
    return { q: `Conjugue « ${v} » au ${TNOM[t]} avec « ${PRO[p]} » :`, ok, faux: autres(r, pool, ok), e: `${TNOM[t][0].toUpperCase() + TNOM[t].slice(1)} de ${v} : ${ok}.` }; });
  const tempsQ = (sid, ch, temps, verbes) => add(sid, ch, (r) => { const v = pick(r, verbes), t = pick(r, temps), p = ri(r, 0, 5), f = sujet(v, t, p), ok = TNOM[t];
    return { q: `« ${f} » : à quel temps est le verbe ?`, ok, faux: autres(r, temps.map((x) => TNOM[x]).concat(["présent", "imparfait", "futur simple", "passé composé"]), ok), e: `${f} : ${ok} de ${v}.` }; });
  const BASE = ["être", "avoir", "aller", "faire"];
  conjQ("ce1-francais", "Le présent : être, avoir et les verbes en -er", ["present"], ER.concat(["être", "avoir"]));
  tempsQ("ce1-francais", "Passé, présent, futur", ["present", "futur", "pc"], ER.slice(0, 10).concat(["être", "avoir"]));
  conjQ("ce2-francais", "Le présent des verbes", ["present"], ER.concat(BASE, ["finir", "venir", "prendre", "dire", "pouvoir"]));
  conjQ("ce2-francais", "L'imparfait et le futur simple", ["imparfait", "futur"], ER.concat(BASE, ["finir", "venir"]));
  conjQ("ce2-francais", "Le passé composé", ["pc"], ER.concat(BASE, ["finir", "venir", "prendre", "dire"]));
  conjQ("cm1-francais", "Révision des temps de l'indicatif", ["present", "imparfait", "futur", "pc"], ER.concat(Object.keys(IRR)));
  tempsQ("cm1-francais", "Révision des temps de l'indicatif", ["present", "imparfait", "futur", "pc", "ps"], ER.concat(Object.keys(IRR)));
  conjQ("cm1-francais", "Le passé simple", ["ps"], ER.concat(Object.keys(IRR)));
  conjQ("cm2-francais", "Les temps de l'indicatif", ["present", "imparfait", "futur", "pc", "ps"], ER.concat(Object.keys(IRR)));
  tempsQ("cm2-francais", "Les temps de l'indicatif", ["present", "imparfait", "futur", "pc", "ps"], ER.concat(Object.keys(IRR)));

  // pluriel et féminin
  const PLUR = [["un cheval", "des chevaux"], ["un journal", "des journaux"], ["un animal", "des animaux"], ["un bijou", "des bijoux"], ["un genou", "des genoux"], ["un caillou", "des cailloux"], ["un chou", "des choux"], ["un hibou", "des hiboux"], ["un jeu", "des jeux"], ["un bateau", "des bateaux"], ["un oiseau", "des oiseaux"], ["un gâteau", "des gâteaux"], ["un pneu", "des pneus"], ["un clou", "des clous"], ["un trou", "des trous"], ["un nez", "des nez"], ["une souris", "des souris"], ["un travail", "des travaux"], ["un œil", "des yeux"], ["un cheveu", "des cheveux"], ["un tableau", "des tableaux"], ["un bal", "des bals"], ["un sou", "des sous"], ["un prix", "des prix"]];
  const plurQ = (sid, ch) => add(sid, ch, (r) => { const [s, p] = pick(r, PLUR), base = s.replace(/^une? /, ""), ok = p;
    const v = [`des ${base}s`, `des ${base}x`, `des ${base.replace(/(al|ail)$/, "aux")}`, `des ${base}`].filter((x) => x !== ok);
    return { q: `Le pluriel de « ${s} » :`, ok, faux: autres(r, v.concat([`des ${base}es`]), ok), e: `${s} → ${ok}.` }; });
  const FEM = [["un acteur", "une actrice"], ["un chanteur", "une chanteuse"], ["un lion", "une lionne"], ["un boulanger", "une boulangère"], ["un maître", "une maîtresse"], ["un coq", "une poule"], ["un roi", "une reine"], ["un neveu", "une nièce"], ["un directeur", "une directrice"], ["un vendeur", "une vendeuse"], ["un paysan", "une paysanne"], ["un oncle", "une tante"], ["un taureau", "une vache"], ["un bélier", "une brebis"], ["un cousin", "une cousine"], ["un élève", "une élève"], ["un instituteur", "une institutrice"], ["un garçon", "une fille"]];
  const femQ = (sid, ch) => add(sid, ch, (r) => { const [m, f] = pick(r, FEM), base = m.replace(/^un /, "");
    return { q: `Le féminin de « ${m} » :`, ok: f, faux: autres(r, [`une ${base}e`, `une ${base}euse`, `une ${base}esse`, `une ${base}rice`, `une ${base}`].filter((x) => x !== f).concat(FEM.map((x) => x[1])), f), e: `${m} → ${f}.` }; });
  plurQ("ce1-francais", "Masculin, féminin, singulier et pluriel"); femQ("ce1-francais", "Masculin, féminin, singulier et pluriel");
  plurQ("ce2-francais", "Les accords"); femQ("ce2-francais", "Le groupe nominal : nom, déterminant, adjectif");
  plurQ("cm1-francais", "Les accords dans la phrase"); femQ("cm1-francais", "Les accords dans la phrase");
  plurQ("cm2-francais", "Orthographe d'usage et homophones");

  // homophones : [phrase avec ___, bonne réponse, [choix de la série]]
  const H = {
    aa: [["a", "à"], ["Awa ___ un beau cahier.", "a"], ["Il va ___ l'école.", "à"], ["Moussa ___ faim.", "a"], ["Nous allons ___ Thiès.", "à"], ["Mon frère ___ dix ans.", "a"], ["Elle joue ___ la balle.", "à"], ["Le maître ___ corrigé les cahiers.", "a"], ["Je pense ___ toi.", "à"]],
    et: [["et", "est"], ["Le ciel ___ bleu.", "est"], ["Fatou ___ Awa jouent.", "et"], ["Mon père ___ pêcheur.", "est"], ["J'achète du pain ___ du lait.", "et"], ["La mangue ___ mûre.", "est"], ["Il chante ___ il danse.", "et"], ["L'école ___ fermée le dimanche.", "est"]],
    son: [["son", "sont"], ["Les élèves ___ en classe.", "sont"], ["Ali range ___ cartable.", "son"], ["Mes amis ___ gentils.", "sont"], ["Elle prend ___ livre.", "son"], ["Les mangues ___ sucrées.", "sont"], ["Le chat dort dans ___ panier.", "son"]],
    on: [["on", "ont"], ["Les enfants ___ faim.", "ont"], ["___ va au marché.", "On"], ["Ils ___ gagné le match.", "ont"], ["Demain, ___ ira à la plage.", "on"], ["Mes parents ___ une voiture.", "ont"], ["___ entend les oiseaux.", "On"]],
    ces: [["ces", "ses"], ["Moussa range ___ affaires.", "ses"], ["Regarde ___ beaux oiseaux là-bas !", "ces"], ["Fatou aime ___ sœurs.", "ses"], ["___ mangues sont mûres.", "Ces"], ["Le paysan soigne ___ bœufs.", "ses"], ["J'aime ___ chansons.", "ces"]],
    ou: [["ou", "où"], ["___ vas-tu ?", "Où"], ["Veux-tu du thé ___ du café ?", "ou"], ["La ville ___ je suis né est Kaolack.", "où"], ["Viens lundi ___ mardi.", "ou"], ["Je sais ___ il habite.", "où"], ["Rouge ___ vert ?", "ou"]],
    ce: [["ce", "se"], ["Il ___ lave les mains.", "se"], ["___ livre est à moi.", "Ce"], ["Elles ___ promènent.", "se"], ["___ matin, il pleut.", "Ce"], ["Le chat ___ cache.", "se"], ["J'aime ___ quartier.", "ce"]],
    leur: [["leur", "leurs"], ["Je ___ donne un conseil.", "leur"], ["Ils ont pris ___ sacs.", "leurs"], ["Le maître ___ parle.", "leur"], ["Elles aiment ___ parents.", "leurs"], ["Les élèves rangent ___ cahiers.", "leurs"], ["Dis-___ de venir.", "leur"]],
    cest: [["c'est", "s'est"], ["___ mon meilleur ami.", "C'est"], ["Il ___ levé tôt.", "s'est"], ["___ l'heure de manger.", "C'est"], ["Elle ___ blessée au genou.", "s'est"], ["Moussa ___ endormi.", "s'est"], ["___ beau, le fleuve !", "C'est"]],
  };
  const homQ = (sid, ch, keys) => add(sid, ch, (r) => { const k = pick(r, keys), [opts, ...rows] = H[k], [ph, ok] = pick(r, rows), cap = (s) => s[0].toUpperCase() + s.slice(1);
    const choix = opts.map((o) => (/^___/.test(ph) ? cap(o) : o)), all = [...new Set(choix.concat(Object.values(H).flatMap((x) => x[0]).map((o) => (/^___/.test(ph) ? cap(o) : o))))];
    return { q: `Complète : « ${ph} »`, ok, faux: autres(r, choix.filter((x) => x !== ok).concat(mix(r, all)), ok).slice(0, 3), e: `« ${ph.replace("___", ok)} » (${opts.join(" ou ")}).` }; });
  homQ("ce1-francais", "Les sons et les lettres", ["aa", "et"]);
  homQ("ce2-francais", "Les homophones grammaticaux", ["aa", "et", "son", "on"]);
  homQ("cm1-francais", "Les homophones grammaticaux", ["aa", "et", "son", "on", "ces", "ou", "ce"]);
  homQ("cm2-francais", "Orthographe d'usage et homophones", ["ces", "ou", "ce", "leur", "cest", "son", "on"]);

  // vocabulaire
  const SYN = [["content", "joyeux"], ["triste", "malheureux"], ["rapide", "vite"], ["commencer", "débuter"], ["maison", "habitation"], ["courageux", "brave"], ["beau", "joli"], ["peur", "frayeur"], ["regarder", "observer"], ["finir", "terminer"], ["grand", "immense"], ["aider", "secourir"], ["ami", "camarade"], ["parler", "discuter"], ["calme", "tranquille"]];
  const ANT = [["grand", "petit"], ["chaud", "froid"], ["jour", "nuit"], ["propre", "sale"], ["ouvrir", "fermer"], ["monter", "descendre"], ["riche", "pauvre"], ["gagner", "perdre"], ["entrer", "sortir"], ["rapide", "lent"], ["honnête", "malhonnête"], ["possible", "impossible"], ["augmenter", "diminuer"], ["toujours", "jamais"], ["fort", "faible"]];
  const ALPHA = ["arachide", "baobab", "case", "école", "fleuve", "gazelle", "hibiscus", "igname", "jardin", "lion", "mangue", "niébé", "oignon", "pirogue", "quartier", "riz", "savane", "tamarin", "village", "zébu"];
  const vocab = (sid, chS, chA) => {
    add(sid, chS, (r) => { const [a, b] = pick(r, SYN); return { q: `Un synonyme de « ${a} » :`, ok: b, faux: autres(r, ANT.flatMap((x) => x).concat(SYN.map((x) => x[1])).filter((x) => x !== a), b), e: `${a} et ${b} ont un sens proche.` }; });
    add(sid, chS, (r) => { const [a, b] = pick(r, ANT), inv = r() < 0.5, [x, y] = inv ? [b, a] : [a, b]; return { q: `Le contraire de « ${x} » :`, ok: y, faux: autres(r, SYN.flatMap((s) => s).concat(ANT.map((s) => (inv ? s[0] : s[1]))).filter((s) => s !== x), y), e: `${x} ≠ ${y}.` }; });
    if (chA) add(sid, chA, (r) => { const xs = mix(r, ALPHA).slice(0, 4), ok = xs.slice().sort((p, q) => p.localeCompare(q, "fr"))[0]; return { q: `Dans le dictionnaire, quel mot vient en premier : ${xs.join(", ")} ?`, ok, faux: xs.filter((x) => x !== ok), e: `Ordre alphabétique : ${xs.slice().sort((p, q) => p.localeCompare(q, "fr")).join(", ")}.` }; });
  };
  vocab("ce1-francais", "Synonymes, contraires et familles de mots", "L'ordre alphabétique et le dictionnaire");
  vocab("ce2-francais", "Le vocabulaire : dictionnaire, préfixes, suffixes", "Le vocabulaire : dictionnaire, préfixes, suffixes");
  vocab("cm1-francais", "Le vocabulaire : familles, sens propre et figuré");
  vocab("cm2-francais", "Le vocabulaire : synonymes, antonymes, homonymes, niveaux de langue");
  // nature des mots
  const NAT = { nom: ["maison", "fleuve", "Dakar", "enfant", "mangue", "école", "pirogue"], verbe: ["courir", "mange", "chantons", "dormait", "finira", "lisez"], adjectif: ["grand", "belle", "rapide", "rouges", "heureux", "propre"], déterminant: ["le", "une", "des", "mon", "ces", "leur"], adverbe: ["vite", "toujours", "souvent", "rapidement", "hier", "beaucoup"], pronom: ["il", "nous", "elles", "lui", "vous", "on"] };
  const natQ = (sid, ch, ks) => add(sid, ch, (r) => { const k = pick(r, ks), ok = pick(r, NAT[k]); return { q: `Lequel de ces mots est un ${k} ?`, ok, faux: mix(r, ks.filter((x) => x !== k)).slice(0, 3).map((x) => pick(r, NAT[x])), e: `« ${ok} » est un ${k}.` }; });
  natQ("ce1-francais", "Le nom et le déterminant", ["nom", "verbe", "déterminant", "adjectif"]);
  natQ("ce2-francais", "Le groupe nominal : nom, déterminant, adjectif", ["nom", "verbe", "déterminant", "adjectif", "pronom"]);
  natQ("cm1-francais", "La nature des mots", Object.keys(NAT));
  natQ("cm2-francais", "Les natures et les fonctions", Object.keys(NAT));

  // participe passé (CM2)
  const PPA = [["Les filles sont (partir).", "parties", ["parti", "partis", "partie"]], ["Les garçons sont (arriver).", "arrivés", ["arrivé", "arrivées", "arrivée"]], ["Elle est (tomber).", "tombée", ["tombé", "tombés", "tombées"]], ["Ils ont (manger) du riz.", "mangé", ["mangés", "mangées", "mangée"]], ["Elles ont (chanter).", "chanté", ["chantées", "chantés", "chantée"]], ["La lettre que j'ai (écrire).", "écrite", ["écrit", "écrits", "écrites"]], ["Les mangues qu'il a (cueillir).", "cueillies", ["cueilli", "cueillis", "cueillie"]], ["Les livres que tu as (lire).", "lus", ["lu", "lues", "lue"]], ["Ma sœur est (venir).", "venue", ["venu", "venus", "venues"]], ["Nous avons (finir) nos devoirs.", "fini", ["finis", "finies", "finie"]], ["Ces robes, je les ai (acheter).", "achetées", ["acheté", "achetés", "achetée"]], ["Des portes (ouvrir).", "ouvertes", ["ouvert", "ouverts", "ouverte"]]];
  add("cm2-francais", "L'accord du participe passé", (r) => { const [ph, ok, f] = pick(r, PPA); return { q: `Accorde le participe : « ${ph} »`, ok, faux: f, e: /sont|est/.test(ph) ? "Avec être, accord avec le sujet." : /qu.|que|les ai/.test(ph) ? "Avec avoir, accord avec le COD placé avant." : /ont|avons/.test(ph) ? "Avec avoir, pas d'accord avec le sujet." : "Sans auxiliaire, accord comme un adjectif." }; });

  // =====================================================================================================
  // SCIENCES, HISTOIRE, GÉOGRAPHIE, VIVRE ENSEMBLE : tables de faits (tirées des leçons)
  // =====================================================================================================
  const QD = (t) => `Quel est ${t} ?`;
  // CE1
  const SENS = [["la vue", "les yeux"], ["l'ouïe", "les oreilles"], ["l'odorat", "le nez"], ["le goût", "la langue"], ["le toucher", "la peau"]];
  paire("ce1-sciences", "Le corps humain et les cinq sens", SENS, (a) => `Organe du sens de ${a} :`, (b) => `Sens dont l'organe est ${b} :`);
  const ANIM = [["la vache", "herbivore"], ["le lion", "carnivore"], ["la chèvre", "herbivore"], ["le chat", "carnivore"], ["la poule", "omnivore"], ["le mouton", "herbivore"], ["l'épervier", "carnivore"], ["le porc", "omnivore"], ["l'âne", "herbivore"], ["le chacal", "carnivore"]];
  const DEPL = [["le poisson", "il nage"], ["l'oiseau", "il vole"], ["le serpent", "il rampe"], ["le cheval", "il marche et court"], ["la grenouille", "elle saute"], ["le criquet", "il saute et vole"]];
  paire("ce1-sciences", "Les animaux autour de nous", ANIM, (a) => `Régime alimentaire de ${a} :`);
  paire("ce1-sciences", "Les animaux autour de nous", DEPL, (a) => `Comment se déplace ${a} ?`, (b) => `Quel animal : ${b} ?`);
  const ALIM = [["le riz", "aliment énergétique"], ["le mil", "aliment énergétique"], ["le poisson", "aliment de construction"], ["la viande", "aliment de construction"], ["l'œuf", "aliment de construction"], ["la mangue", "aliment de protection"], ["le chou", "aliment de protection"], ["l'orange", "aliment de protection"], ["le niébé", "aliment de construction"], ["l'huile", "aliment énergétique"]];
  paire("ce1-sciences", "Les aliments et les repas", ALIM, (a) => `À quel groupe appartient ${a} ?`);
  const PLANTE = [["la racine", "puise l'eau dans le sol"], ["la tige", "porte les feuilles et conduit la sève"], ["la feuille", "fabrique la nourriture de la plante"], ["la fleur", "donne le fruit"], ["le fruit", "contient les graines"], ["la graine", "donne une nouvelle plante"]];
  paire("ce1-sciences", "Les plantes", PLANTE, (a) => `Rôle de ${a} :`, (b) => `Quelle partie de la plante ${b} ?`);
  const HYG = [["se laver les mains", "avant de manger et après les toilettes"], ["se brosser les dents", "matin et soir après les repas"], ["se couper les ongles", "chaque semaine"], ["prendre une douche", "chaque jour"], ["laver les fruits", "avant qu’on les mange"]];
  paire("ce1-sciences", "L'hygiène du corps et des dents", HYG, (a) => `Quand faut-il ${a} ?`, (b) => `Que faut-il faire ${b} ?`);
  const FAMILLE = [["le père de mon père", "mon grand-père"], ["la sœur de ma mère", "ma tante"], ["le frère de mon père", "mon oncle"], ["le fils de mon oncle", "mon cousin"], ["la mère de ma mère", "ma grand-mère"], ["la fille de ma tante", "ma cousine"]];
  paire("ce1-histoire", "Ma famille et mes ancêtres", FAMILLE, (a) => `Qui est ${a} ?`, (b) => `${b[0].toUpperCase() + b.slice(1)}, c'est :`);
  const JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"], MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];
  add("ce1-histoire", "Se repérer dans le temps", (r) => { const L = r() < 0.5 ? JOURS : MOIS, i = ri(r, 0, L.length - 1), s = r() < 0.5, ok = L[(i + (s ? 1 : L.length - 1)) % L.length]; return { q: `Quel ${L === JOURS ? "jour" : "mois"} vient juste ${s ? "après" : "avant"} ${L[i]} ?`, ok, faux: autres(r, L.filter((x) => x !== L[i]), ok), e: `${L.join(", ")}.` }; });
  const METIERS = [["le pêcheur", "attrape des poissons"], ["le cultivateur", "travaille la terre"], ["le forgeron", "travaille le fer"], ["le cordonnier", "répare les chaussures"], ["le maçon", "construit les maisons"], ["l'infirmier", "soigne les malades"], ["le tailleur", "coud les vêtements"], ["le boulanger", "fait le pain"], ["l'éleveur", "garde les troupeaux"], ["le menuisier", "travaille le bois"]];
  paire("ce1-histoire", "Les métiers d'autrefois et d'aujourd'hui", METIERS, (a) => `Que fait ${a} ?`, (b) => `Qui ${b} ?`);
  paire("ce1-geo", "S'orienter et se repérer", [["le soleil se lève", "à l'est"], ["le soleil se couche", "à l'ouest"], ["en face de l'est, on a", "l'ouest"], ["opposé au nord", "le sud"]], (a) => `${a[0].toUpperCase() + a.slice(1)} :`);
  const SAISON = [["la saison des pluies", "hivernage (juillet à octobre)"], ["la saison sèche", "novembre à juin"], ["l'harmattan", "vent chaud et sec venant du désert"], ["l'alizé", "vent frais venant de la mer"]];
  paire("ce1-geo", "Le temps qu'il fait et les saisons", SAISON, (a) => `Que désigne ${a} ?`, (b) => `Quel mot correspond à : ${b} ?`);
  const ROUTE = [["feu rouge", "je m'arrête"], ["feu vert", "je peux passer"], ["passage pour piétons", "je traverse ici"], ["feu orange", "je ralentis et je m'arrête"]];
  paire("ce1-civique", "La sécurité sur la route", ROUTE, (a) => `Que fais-je au ${a.startsWith("feu") ? a : "niveau du " + a} ?`, (b) => `Où ou quand : « ${b} » ?`);
  const POLI = [["quand on arrive", "bonjour"], ["quand on demande", "s'il te plaît"], ["quand on reçoit", "merci"], ["quand on bouscule quelqu'un", "pardon"], ["quand on part", "au revoir"]];
  paire("ce1-civique", "La politesse et le respect", POLI, (a) => `Que dit-on ${a} ?`, (b) => `Quand dit-on « ${b} » ?`);

  // CE2
  const RESP = [["l'air entre par", "le nez et la bouche"], ["l'air passe par", "la trachée"], ["les échanges se font dans", "les poumons"], ["le gaz rejeté est", "le gaz carbonique"], ["le gaz utile est", "l'oxygène"]];
  paire("ce2-sciences", "La respiration", RESP, (a) => `Respiration : ${a} …`);
  const DIG = [["la bouche", "les dents broient les aliments"], ["l'œsophage", "conduit les aliments à l'estomac"], ["l'estomac", "malaxe les aliments"], ["l'intestin grêle", "les nutriments passent dans le sang"], ["le gros intestin", "forme les déchets"]];
  paire("ce2-sciences", "La digestion", DIG, (a) => `Rôle de ${a} :`, (b) => `Organe où ${b} :`);
  const NAISS = [["la poule", "ovipare"], ["la vache", "vivipare"], ["le crocodile", "ovipare"], ["la chèvre", "vivipare"], ["le canard", "ovipare"], ["la chienne", "vivipare"], ["la tortue", "ovipare"], ["la brebis", "vivipare"]];
  add("ce2-sciences", "La naissance des animaux", (r) => { const [a, b] = pick(r, NAISS); return { q: `${a[0].toUpperCase() + a.slice(1)} est :`, ok: b, faux: [b === "ovipare" ? "vivipare" : "ovipare", "ni ovipare ni vivipare", "ovipare et vivipare à la fois"], e: `${a} : ${b}.` }; });
  const MAL = [["le paludisme", "la piqûre du moustique anophèle"], ["la diarrhée", "l'eau et les aliments sales"], ["la carie", "le sucre et le manque de brossage"], ["la conjonctivite", "les mains sales portées aux yeux"], ["la tuberculose", "la toux d'un malade"]];
  paire("ce2-sciences", "Les maladies et leur prévention", MAL, (a) => `Comment attrape-t-on ${a} ?`, (b) => `Maladie transmise par ${b} :`);
  const SIECLE = (y) => ["", "Ier", "IIe", "IIIe", "IVe", "Ve", "VIe", "VIIe", "VIIIe", "IXe", "Xe", "XIe", "XIIe", "XIIIe", "XIVe", "XVe", "XVIe", "XVIIe", "XVIIIe", "XIXe", "XXe", "XXIe"][Math.floor((y - 1) / 100) + 1];
  add("ce2-histoire", "Mesurer le temps : siècle et frise", (r) => { const y = ri(r, 101, 2030), s = SIECLE(y), ok = `${s} siècle`; return { q: `L'année ${y} appartient au :`, ok, faux: autres(r, [SIECLE(y + 100), SIECLE(Math.max(1, y - 100)), SIECLE(Math.max(1, y - 200)), SIECLE(Math.min(2030, y + 200))].map((x) => `${x} siècle`), ok), e: `Le ${s} siècle va de ${(Math.floor((y - 1) / 100)) * 100 + 1} à ${(Math.floor((y - 1) / 100) + 1) * 100}.` }; });
  add("ce2-histoire", "Mesurer le temps : siècle et frise", (r) => { const [u, v, n] = pick(r, [["ans", "un siècle", 100], ["ans", "une décennie", 10], ["siècles", "un millénaire", 10], ["ans", "un millénaire", 1000]]); return { q: `Combien de ${u} dans ${v} ?`, ok: String(n), faux: autres(r, [10, 100, 1000, 12, 50], n), e: `${v} = ${n} ${u}.` }; });
  const SYMB = [["la devise du Sénégal", "Un Peuple, Un But, Une Foi"], ["l'hymne national", "Le Lion rouge"], ["les couleurs du drapeau", "vert, or, rouge avec une étoile verte"], ["l'emblème (armoiries)", "un lion et un baobab"], ["la fête de l'indépendance", "le 4 avril"], ["la capitale", "Dakar"]];
  paire("ce2-civique", "Les symboles de la Nation", SYMB, (a) => `Au Sénégal, ${a} :`, (b) => `« ${b} », c'est :`);
  const DROITS = [["aller à l'école", "droit à l'éducation"], ["être soigné", "droit à la santé"], ["avoir un nom", "droit à l'identité"], ["jouer", "droit aux loisirs"], ["être protégé de la violence", "droit à la protection"], ["donner son avis", "droit d'expression"]];
  paire("ce2-civique", "Les droits et les devoirs de l'enfant", DROITS, (a) => `« ${a[0].toUpperCase() + a.slice(1)} » correspond au :`, (b) => `Le ${b}, c'est le droit de :`);
  const CARTE = [["le haut de la carte", "le nord"], ["le bas de la carte", "le sud"], ["la droite de la carte", "l'est"], ["la gauche de la carte", "l'ouest"]];
  paire("ce2-geo", "Lire une carte", CARTE, (a) => `Sur une carte orientée, ${a} indique :`, (b) => `${b[0].toUpperCase() + b.slice(1)} est représenté par :`);
  const ACTI = [["Kayar", "la pêche"], ["les Niayes", "le maraîchage"], ["le Ferlo", "l'élevage"], ["Kaolack", "l'arachide et le sel"], ["Richard-Toll", "la canne à sucre"], ["Kédougou", "l'or"], ["la Casamance", "le riz pluvial"]];
  paire("ce2-geo", "Les activités des hommes", ACTI, (a) => `Activité principale de ${a} :`, (b) => `Où pratique-t-on surtout ${b} ?`);
  const FLEUVES = [["le fleuve Sénégal", "Saint-Louis"], ["le fleuve Gambie", "Kédougou et Tambacounda"], ["le fleuve Casamance", "Ziguinchor"], ["le Saloum", "Kaolack"]];
  paire("ce2-geo", "Le relief et les cours d'eau", FLEUVES, (a) => `Ville ou région traversée par ${a} :`, (b) => `Cours d'eau de ${b} :`);

  // CM1
  const EMP = [[300, "naissance de l'empire du Ghana (vers)"], [1076, "les Almoravides prennent Koumbi Saleh"], [1235, "bataille de Kirina, victoire de Soundiata Keïta"], [1324, "pèlerinage de Kankou Moussa à La Mecque"], [1464, "Sonni Ali Ber devient roi du Songhaï"], [1591, "bataille de Tondibi, fin de l'empire Songhaï"], [1659, "fondation de Saint-Louis"], [1848, "abolition de l'esclavage dans les colonies françaises"]];
  chrono("cm1-histoire", "L'empire du Mali", EMP);
  const ROIS = [["Soundiata Keïta", "fondateur de l'empire du Mali"], ["Kankou Moussa", "empereur du Mali célèbre pour son pèlerinage"], ["Sonni Ali Ber", "roi conquérant du Songhaï"], ["Askia Mohammed", "empereur Songhaï qui développe Tombouctou"], ["Ndiadiane Ndiaye", "fondateur légendaire du Djolof"], ["Koli Tenguella", "fondateur de la dynastie des Déniankés du Fouta"]];
  paire("cm1-histoire", "Les royaumes du Sénégal", ROIS, (a) => `Qui était ${a} ?`, (b) => `Qui fut le ${b} ?`);
  const CAP = [["l'empire du Ghana", "Koumbi Saleh"], ["l'empire du Mali", "Niani"], ["l'empire Songhaï", "Gao"]];
  add("cm1-histoire", "L'empire Songhaï", (r) => { const [a, b] = pick(r, CAP); return { q: `Capitale de ${a} :`, ok: b, faux: autres(r, CAP.map((x) => x[1]).concat(["Tombouctou", "Dakar"]), b), e: `${a} : ${b}.` }; });
  const OS = [["le crâne", "protège le cerveau"], ["les côtes", "protègent le cœur et les poumons"], ["la colonne vertébrale", "soutient le corps"], ["le fémur", "os de la cuisse, le plus long"], ["les muscles", "font bouger les os"], ["les articulations", "permettent de plier les membres"]];
  paire("cm1-sciences", "Le squelette et les muscles", OS, (a) => `Rôle de ${a} :`, (b) => `Qu'est-ce qui ${b.replace(/^os /, "est l'os ")} ?`);
  const SANG = [["le cœur", "pompe le sang"], ["les artères", "conduisent le sang du cœur vers les organes"], ["les veines", "ramènent le sang vers le cœur"], ["les globules rouges", "transportent l'oxygène"], ["les globules blancs", "défendent le corps contre les microbes"], ["les plaquettes", "arrêtent les saignements"]];
  paire("cm1-sciences", "La circulation du sang", SANG, (a) => `Rôle de ${a} :`, (b) => `Qu'est-ce qui ${b} ?`);
  const ELEC = [["la pile", "générateur"], ["la lampe", "récepteur"], ["l'interrupteur", "ouvre ou ferme le circuit"], ["le fil de cuivre", "conducteur"], ["le plastique", "isolant"], ["le bois sec", "isolant"], ["la clé en fer", "conducteur"]];
  paire("cm1-sciences", "L'électricité", ELEC, (a) => `Dans un circuit, ${a} est :`);
  const LIM = [["au nord", "la Mauritanie"], ["à l'est", "le Mali"], ["au sud", "la Guinée et la Guinée-Bissau"], ["à l'ouest", "l'océan Atlantique"], ["enclavée dans le Sénégal", "la Gambie"]];
  paire("cm1-geo", "La situation et les limites du Sénégal", LIM, (a) => `Limite du Sénégal ${a} :`, (b) => `Où se trouve ${b} par rapport au Sénégal ?`);
  const REG = [["Dakar", "Dakar"], ["Thiès", "Thiès"], ["Diourbel", "Diourbel"], ["Ziguinchor", "Ziguinchor"], ["Kaolack", "Kaolack"], ["Saint-Louis", "Saint-Louis"], ["Louga", "Louga"], ["Fatick", "Fatick"], ["Kolda", "Kolda"], ["Matam", "Matam"], ["Tambacounda", "Tambacounda"], ["Kaffrine", "Kaffrine"], ["Kédougou", "Kédougou"], ["Sédhiou", "Sédhiou"]];
  add("cm1-geo", "Les régions administratives", (r) => { const n = 14; return { q: "Combien de régions administratives compte le Sénégal ?", ok: String(n), faux: autres(r, [10, 11, 12, 13, 15, 16], n), e: "Le Sénégal compte 14 régions depuis 2008." }; });
  add("cm1-geo", "Les régions administratives", (r) => { const ok = pick(r, REG)[0]; return { q: "Laquelle de ces villes est un chef-lieu de région ?", ok, faux: mix(r, ["Mbour", "Touba", "Rufisque", "Richard-Toll", "Joal", "Bignona", "Podor", "Bakel", "Kayar"]).slice(0, 3), e: `${ok} est le chef-lieu de la région du même nom. Les autres villes sont des chefs-lieux de département ou des communes.` }; });
  const INST = [["le Président de la République", "élu pour 5 ans au suffrage universel"], ["l'Assemblée nationale", "vote les lois"], ["le gouvernement", "dirigé par le Premier ministre"], ["les juges", "rendent la justice"], ["le Conseil constitutionnel", "veille au respect de la Constitution"]];
  paire("cm1-civique", "Les institutions de la République", INST, (a) => `${a[0].toUpperCase() + a.slice(1)} :`, (b) => `Qui ${b.replace(/^élu/, "est élu").replace(/^dirigé/, "est dirigé")} ?`);

  // CM2
  const COLO = [[1659, "fondation de Saint-Louis"], [1854, "Faidherbe devient gouverneur"], [1857, "création des tirailleurs sénégalais"], [1885, "chemin de fer Dakar–Saint-Louis"], [1886, "mort de Lat Dior à Dékhelé"], [1895, "création de l'AOF"], [1902, "Dakar capitale de l'AOF"], [1914, "Blaise Diagne élu député"], [1944, "massacre de Thiaroye"], [1960, "indépendance du Sénégal"], [2000, "première alternance politique"], [2001, "nouvelle Constitution"]];
  chrono("cm2-histoire", "La pénétration coloniale", COLO);
  const RESIST = [["Lat Dior", "Cayor"], ["Alboury Ndiaye", "Djolof"], ["Maba Diakhou Ba", "Rip (Saloum)"], ["Aline Sitoé Diatta", "Casamance"], ["El Hadji Omar Tall", "Fouta et vallée du fleuve"], ["Cheikh Ahmadou Bamba", "Baol"]];
  paire("cm2-histoire", "Les résistances à la colonisation", RESIST, (a) => `Région de résistance de ${a} :`, (b) => `Quel résistant est associé à : ${b} ?`);
  const PRES = [["Léopold Sédar Senghor", "1960-1980"], ["Abdou Diouf", "1981-2000"], ["Abdoulaye Wade", "2000-2012"], ["Macky Sall", "2012-2024"], ["Bassirou Diomaye Faye", "depuis 2024"]];
  paire("cm2-histoire", "Le Sénégal indépendant", PRES, (a) => `Période de présidence de ${a} :`, (b) => `Président du Sénégal ${b.startsWith("depuis") ? b : "de " + b.replace("-", " à ")} :`);
  const ORG = [["l'ONU", "New York"], ["l'Union africaine", "Addis-Abeba"], ["la CEDEAO", "Abuja"], ["la BCEAO", "Dakar"], ["l'UEMOA", "Ouagadougou"]];
  paire("cm2-histoire", "Les organisations africaines et internationales", ORG, (a) => `Siège de ${a} :`, (b) => `Organisation qui a son siège à ${b} :`);
  const NUT = [["l'appareil digestif", "transforme les aliments en nutriments"], ["l'appareil respiratoire", "apporte l'oxygène au sang"], ["l'appareil circulatoire", "transporte les nutriments et l'oxygène"], ["l'appareil excréteur", "élimine les déchets (urine)"]];
  paire("cm2-sciences", "Les appareils de la nutrition", NUT, (a) => `Rôle de ${a} :`, (b) => `Quel appareil ${b} ?`);
  const MAL2 = [["le paludisme", "dormir sous une moustiquaire imprégnée"], ["la bilharziose", "éviter de se baigner dans les eaux stagnantes"], ["le VIH/sida", "se faire dépister et se protéger"], ["la rougeole", "se faire vacciner"], ["le choléra", "boire de l'eau potable et se laver les mains"], ["le diabète", "manger moins sucré et faire du sport"]];
  paire("cm2-sciences", "Les maladies et la santé publique", MAL2, (a) => `Comment se protéger contre ${a} ?`, (b) => `« ${b[0].toUpperCase() + b.slice(1)} » protège surtout contre :`);
  const ENER = [["le soleil", "renouvelable"], ["le vent", "renouvelable"], ["l'eau des barrages", "renouvelable"], ["le pétrole", "non renouvelable"], ["le gaz naturel", "non renouvelable"], ["le charbon", "non renouvelable"]];
  add("cm2-sciences", "Énergie et environnement", (r) => { const k = r() < 0.5 ? "renouvelable" : "non renouvelable", ok = pick(r, ENER.filter((x) => x[1] === k))[0]; return { q: `Quelle source d'énergie est ${k} ?`, ok, faux: mix(r, ENER.filter((x) => x[1] !== k).map((x) => x[0])).slice(0, 3), e: `${ok} : énergie ${k}.` }; });
  const CHAINE = [["mil", "criquet", "poule", "chacal"], ["herbe", "gazelle", "lion", "vautour"], ["plancton", "sardinelle", "thiof", "requin"], ["feuille", "chenille", "oiseau", "serpent"]];
  add("cm2-sciences", "Les chaînes alimentaires et l'équilibre de la nature", (r) => { const c = pick(r, CHAINE), ok = c.join(" → "); return { q: "Quelle chaîne alimentaire est correcte ?", ok, faux: [c.slice().reverse().join(" → "), [c[1], c[0], c[2], c[3]].join(" → "), [c[0], c[2], c[1], c[3]].join(" → ")], e: "La flèche va du mangé vers le mangeur ; la chaîne commence par une plante." }; });
  const AGRI = [["l'arachide", "le bassin arachidier (Kaolack, Diourbel)"], ["le riz irrigué", "la vallée du fleuve Sénégal"], ["les légumes", "les Niayes"], ["l'élevage", "le Ferlo"], ["le coton", "Tambacounda et Kolda"], ["la canne à sucre", "Richard-Toll"]];
  paire("cm2-geo", "L'agriculture et l'élevage au Sénégal", AGRI, (a) => `Zone principale de production de ${a} :`, (b) => `Principale production de cette zone : ${b}`);
  const CAPAF = [["le Mali", "Bamako"], ["la Mauritanie", "Nouakchott"], ["la Guinée", "Conakry"], ["la Gambie", "Banjul"], ["la Guinée-Bissau", "Bissau"], ["la Côte d'Ivoire", "Yamoussoukro"], ["le Burkina Faso", "Ouagadougou"], ["le Niger", "Niamey"], ["le Nigeria", "Abuja"], ["le Ghana", "Accra"], ["le Maroc", "Rabat"], ["l'Égypte", "Le Caire"]];
  paire("cm2-geo", "L'Afrique : relief, climats, pays", CAPAF, (a) => `Capitale de ${a} :`, (b) => `${b} est la capitale de :`);
  const MONDE = [["l'océan Pacifique", "le plus grand océan"], ["l'Asie", "le plus grand continent"], ["l'Antarctique", "le continent glacé inhabité"], ["l'océan Atlantique", "l'océan qui borde le Sénégal"], ["l'Océanie", "le continent de l'Australie"], ["l'océan Indien", "l'océan entre l'Afrique et l'Australie"]];
  paire("cm2-geo", "Le monde : continents et océans", MONDE, (a) => `Qu'est-ce que ${a} ?`, (b) => `Quel est ${b} ?`);
  const INST2 = [["le pouvoir exécutif", "le Président et le gouvernement"], ["le pouvoir législatif", "l'Assemblée nationale"], ["le pouvoir judiciaire", "les cours et tribunaux"]];
  add("cm2-civique", "La Constitution et les institutions", (r) => { const [a, b] = pick(r, INST2); return { q: `Qui exerce ${a} ?`, ok: b, faux: autres(r, INST2.map((x) => x[1]).concat(["le maire", "le gouverneur"]), b), e: `${a} : ${b}.` }; });
  const VOTE = [["l'urne", "boîte où l'on dépose son bulletin"], ["l'isoloir", "lieu où l'on choisit son bulletin en secret"], ["le bulletin", "papier qui porte le choix de l'électeur"], ["l'encre indélébile", "empêche de voter deux fois"], ["la liste électorale", "registre des personnes qui peuvent voter"]];
  paire("cm2-civique", "Les élections et la démocratie", VOTE, (a) => `Qu'est-ce que ${a} ?`, (b) => `Quel mot désigne : ${b} ?`);
  const VAL = [["la teranga", "l'hospitalité"], ["le jom", "la dignité, l'honneur"], ["le kersa", "la retenue, la pudeur"], ["le mbokk", "la parenté, la solidarité familiale"], ["la tontine", "l'épargne collective"]];
  paire("cm2-civique", "La paix, la sécurité et la solidarité", VAL, (a) => `Que signifie ${a} ?`, (b) => `Quel mot désigne ${b} ?`);

  // =====================================================================================================
  // EXERCICES GUIDÉS (au moins 3 par matière)
  // =====================================================================================================
  // maths : 4 modèles par classe, nombres adaptés
  const exMaths = (sid, max, opts) => {
    ex(sid, "Achats à la boutique", (r) => { const p1 = ri(r, 2, max > 1000 ? 30 : 8) * 25, n1 = ri(r, 2, 6), p2 = ri(r, 2, max > 1000 ? 20 : 6) * 25, n2 = ri(r, 2, 5), T = p1 * n1 + p2 * n2, B = Math.ceil(T / 500) * 500 + pick(r, [0, 500]);
      return { context: `${pick(r, PRENOMS)} achète ${n1} paquets de biscuits à ${p1} F et ${n2} jus à ${p2} F. ${B > T ? `Il paie avec ${F(B)} F.` : ""}`, steps: [
        S("Prix des biscuits :", `${F(p1 * n1)} F`, [`${F(p1 + n1)} F`, `${F(p1 * (n1 + 1))} F`, `${F(p1)} F`], `${n1} × ${p1} = ${F(p1 * n1)} F.`, 1.5),
        S("Prix des jus :", `${F(p2 * n2)} F`, [`${F(p2 + n2)} F`, `${F(p2 * (n2 + 1))} F`, `${F(p2)} F`], `${n2} × ${p2} = ${F(p2 * n2)} F.`, 1.5),
        S("Dépense totale :", `${F(T)} F`, [`${F(T + 25)} F`, `${F(p1 + p2)} F`, `${F(T - p2)} F`], `${F(p1 * n1)} + ${F(p2 * n2)} = ${F(T)} F.`, 1),
        S("Monnaie rendue :", `${F(B - T)} F`, [`${F(B - T + 25)} F`, `${F(B + T)} F`, `${F(T)} F`], `${F(B)} − ${F(T)} = ${F(B - T)} F.`, 1)].filter((s) => B > T || !/Monnaie/.test(s.q)) }; });
    ex(sid, "Le jardin de l'école", (r) => { const L = ri(r, 6, 30), l = ri(r, 3, L - 1), pz = ri(r, 2, 8) * (max > 1000 ? 100 : 25);
      return { context: `Le jardin de l'école est un rectangle de ${L} m de long et ${l} m de large. On veut l'entourer d'un grillage à ${pz} F le mètre.`, steps: [
        S("Longueur + largeur :", `${L + l} m`, [`${L * l} m`, `${L - l} m`, `${2 * L} m`], `${L} + ${l} = ${L + l} m.`, 1),
        S("Périmètre du jardin :", `${2 * (L + l)} m`, [`${L + l} m`, `${L * l} m`, `${4 * L} m`], `2 × (${L} + ${l}) = ${2 * (L + l)} m.`, 1.5),
        S(opts.aires ? "Aire du jardin :" : "Nombre de mètres de grillage :", opts.aires ? `${L * l} m²` : `${2 * (L + l)} m`, opts.aires ? [`${2 * (L + l)} m²`, `${L + l} m²`, `${L * l * 2} m²`] : [`${L + l} m`, `${L * l} m`, `${2 * (L + l) + 2} m`], opts.aires ? `${L} × ${l} = ${L * l} m².` : "On grillage tout le tour.", 1),
        S("Prix du grillage :", `${F(2 * (L + l) * pz)} F`, [`${F((L + l) * pz)} F`, `${F(L * l * pz)} F`, `${F(2 * (L + l) + pz)} F`], `${2 * (L + l)} × ${pz} = ${F(2 * (L + l) * pz)} F.`, 1.5)] }; });
    ex(sid, "Le partage des fournitures", (r) => { const e = ri(r, 3, 9), c = ri(r, 3, max > 1000 ? 25 : 9), rest = ri(r, 1, e - 1), N = e * c + rest;
      return { context: `Le maître a ${N} crayons à partager entre les ${e} rangées de la classe, de façon égale.`, steps: [
        S("Opération à faire :", `${N} ÷ ${e}`, [`${N} × ${e}`, `${N} + ${e}`, `${N} − ${e}`], "Partager en parts égales, c'est diviser.", 1),
        S("Crayons par rangée :", String(c), [String(c + 1), String(c - 1), String(N - e)], `${e} × ${c} = ${e * c} ≤ ${N} < ${e * (c + 1)}.`, 1.5),
        S("Crayons restants :", String(rest), [String(rest + 1), "0", String(e)], `${N} − ${e * c} = ${rest}.`, 1.5),
        S("Vérification :", `${e} × ${c} + ${rest} = ${N}`, [`${e} × ${c} = ${N}`, `${e} + ${c} + ${rest} = ${N}`, `${c} × ${rest} = ${N}`], "Dividende = diviseur × quotient + reste.", 1)] }; });
    if (opts.trajet) ex(sid, "Le voyage en car", (r) => { const v = ri(r, 5, 9) * 10, t = pick(r, [2, 3, 4, 5]), h0 = ri(r, 6, 10), d = v * t;
      return { context: `Un car quitte Dakar à ${h0} h et roule à ${v} km/h de moyenne pendant ${t} h.`, steps: [
        S("Distance parcourue :", `${d} km`, [`${d + v} km`, `${v + t} km`, `${d - v} km`], `${v} × ${t} = ${d} km.`, 1.5),
        S("Heure d'arrivée :", `${h0 + t} h`, [`${h0 + t + 1} h`, `${h0 + t - 1} h`, `${t} h`], `${h0} h + ${t} h = ${h0 + t} h.`, 1),
        S("Distance en 1 h 30 min :", `${D(v * 1.5)} km`, [`${D(v * 1.3)} km`, `${v} km`, `${D(v * 3)} km`], `1 h 30 = 1,5 h ; ${v} × 1,5 = ${D(v * 1.5)} km.`, 1.5),
        S(`Durée pour ${d + v} km à la même vitesse :`, `${t + 1} h`, [`${t} h`, `${t + 2} h`, `${t - 1} h`], `${d + v} ÷ ${v} = ${t + 1} h.`, 1)] }; });
    else ex(sid, "Les heures de classe", (r) => { const h0 = 8, m0 = pick(r, [0, 15, 30]), dur = pick(r, [90, 105, 120, 150]), rec = pick(r, [15, 20, 30]);
      return { context: `La classe commence à ${hm(h0 * 60 + m0)}. Après ${dur} minutes de cours, c'est la récréation, qui dure ${rec} minutes.`, steps: [
        S("Durée du cours en heures et minutes :", `${Math.floor(dur / 60)} h ${String(dur % 60).padStart(2, "0")}`, [`${Math.floor(dur / 60) + 1} h 00`, `${dur} h`, `${Math.floor(dur / 60)} h ${String((dur % 60) + 10).padStart(2, "0")}`], `${dur} min = ${Math.floor(dur / 60)} h ${dur % 60} min.`, 1.5),
        S("Début de la récréation :", hm(h0 * 60 + m0 + dur), [hm(h0 * 60 + m0 + dur + 15), hm(h0 * 60 + m0 + dur - 15), hm(h0 * 60 + dur)], `${hm(h0 * 60 + m0)} + ${dur} min.`, 1.5),
        S("Fin de la récréation :", hm(h0 * 60 + m0 + dur + rec), [hm(h0 * 60 + m0 + dur), hm(h0 * 60 + m0 + dur + rec + 10), hm(h0 * 60 + m0 + rec)], `+ ${rec} min.`, 1),
        S("Minutes dans une heure :", "60", ["100", "30", "24"], "1 h = 60 min.", 1)] }; });
  };
  exMaths("ce1-maths", 1000, { aires: false, trajet: false });
  exMaths("ce2-maths", 100000, { aires: false, trajet: false });
  exMaths("cm1-maths", 1e7, { aires: true, trajet: true });
  exMaths("cm2-maths", 1e8, { aires: true, trajet: true });
  ex("cm2-maths", "Le commerce du commerçant", (r) => { const n = ri(r, 10, 60), a = ri(r, 4, 20) * 500, f = ri(r, 2, 20) * 1000, v = a + ri(r, 1, 6) * 500, A = n * a, R = A + f, V = n * v, B = V - R; if (B <= 0) return null;
    return { context: `Un commerçant achète ${n} sacs à ${F(a)} F l'un. Le transport coûte ${F(f)} F. Il revend chaque sac ${F(v)} F.`, steps: [
      S("Prix d'achat :", `${F(A)} F`, [`${F(A + f)} F`, `${F(n + a)} F`, `${F(V)} F`], `${n} × ${F(a)} = ${F(A)} F.`, 1),
      S("Prix de revient :", `${F(R)} F`, [`${F(A)} F`, `${F(A - f)} F`, `${F(V)} F`], `${F(A)} + ${F(f)} = ${F(R)} F.`, 1.5),
      S("Prix de vente :", `${F(V)} F`, [`${F(R)} F`, `${F(n * a)} F`, `${F(V + v)} F`], `${n} × ${F(v)} = ${F(V)} F.`, 1),
      S("Bénéfice :", `${F(B)} F`, [`${F(V - A)} F`, `${F(B * 2)} F`, `${F(Math.abs(B - 500))} F`], `${F(V)} − ${F(R)} = ${F(B)} F.`, 1.5)] }; });
  ex("cm2-maths", "La citerne du quartier", (r) => { const L = ri(r, 2, 6), l = ri(r, 1, L), h = ri(r, 1, 3), V = L * l * h, q = pick(r, [100, 200, 250, 500]);
    return { context: `Une citerne a la forme d'un pavé de ${L} m de long, ${l} m de large et ${h} m de haut. Chaque famille reçoit ${q} l par jour.`, steps: [
      S("Volume :", `${V} m³`, [`${L * l} m³`, `${L + l + h} m³`, `${V * 10} m³`], `${L} × ${l} × ${h} = ${V} m³.`, 1.5),
      S("Volume en litres :", `${F(V * 1000)} l`, [`${F(V * 100)} l`, `${F(V * 10)} l`, `${F(V)} l`], "1 m³ = 1 000 l.", 1),
      S("Familles servies en un jour :", String((V * 1000) / q), [String((V * 1000) / q + 10), String((V * 100) / q), String(V * q)], `${F(V * 1000)} ÷ ${q} = ${(V * 1000) / q}.`, 1.5),
      S("Citerne remplie à moitié, en litres :", `${F(V * 500)} l`, [`${F(V * 1000)} l`, `${F(V * 250)} l`, `${F(V * 50)} l`], `${F(V * 1000)} ÷ 2.`, 1)] }; });

  // français : conjugaison, accords, homophones
  const exConj = (sid, temps, verbes) => ex(sid, "Conjuguer un verbe", (r) => { const v = pick(r, verbes), t = pick(r, temps), ps = mix(r, [0, 1, 2, 3, 4, 5]).slice(0, 4);
    return { context: `Conjugue le verbe « ${v} » au ${TNOM[t]}.`, steps: ps.map((p, i) => { const ok = sujet(v, t, p); return S(`Avec « ${PRO[p]} » :`, ok, autres(r, [0, 1, 2, 3, 4, 5].filter((k) => k !== p).map((k) => `${PRO[p]} ${conj(v, t, k)}`.replace(/^je ([aeéèêiouh])/i, "j'$1")).concat(Object.keys(TNOM).filter((x) => x !== t).map((x) => sujet(v, x, p))), ok), `${ok}.`, i < 2 ? 1 : 1.5); }) }; });
  const exHom = (sid, keys) => ex(sid, "Les homophones", (r) => { const rows = keys.flatMap((k) => H[k].slice(1).map((x) => [...x, H[k][0]])), xs = mix(r, rows).slice(0, 4);
    return { context: "Complète chaque phrase avec le mot qui convient.", steps: xs.map(([ph, ok, opts], i) => { const cap = (s) => (/^___/.test(ph) ? s[0].toUpperCase() + s.slice(1) : s), c = opts.map(cap); return S(`« ${ph} »`, ok, autres(r, c.concat(keys.flatMap((k) => H[k][0]).map(cap)), ok), `« ${ph.replace("___", ok)} ».`, i < 2 ? 1 : 1.5); }) }; });
  const exAcc = (sid) => ex(sid, "Singulier, pluriel, masculin, féminin", (r) => { const [s1, p1] = pick(r, PLUR), [s2, p2] = pick(r, PLUR.filter((x) => x[0] !== s1)), [m1, f1] = pick(r, FEM), [m2, f2] = pick(r, FEM.filter((x) => x[0] !== m1));
    const fp = (s) => { const b = s.replace(/^une? /, ""); return [`des ${b}s`, `des ${b}x`, `des ${b}`, `des ${b.replace(/(al|ail)$/, "aux")}`, `des ${b}es`, `des ${b}aux`, `les ${b}e`]; };
    const ff = (m) => { const b = m.replace(/^un /, ""); return [`une ${b}e`, `une ${b}euse`, `une ${b}esse`, `une ${b}`]; };
    return { context: "Écris chaque groupe de mots au pluriel ou au féminin.", steps: [
      S(`Pluriel de « ${s1} » :`, p1, autres(r, fp(s1), p1), `${s1} → ${p1}.`, 1), S(`Pluriel de « ${s2} » :`, p2, autres(r, fp(s2), p2), `${s2} → ${p2}.`, 1),
      S(`Féminin de « ${m1} » :`, f1, autres(r, ff(m1).concat(FEM.map((x) => x[1])), f1), `${m1} → ${f1}.`, 1.5), S(`Féminin de « ${m2} » :`, f2, autres(r, ff(m2).concat(FEM.map((x) => x[1])), f2), `${m2} → ${f2}.`, 1.5)] }; });
  const exVoc = (sid) => ex(sid, "Synonymes et contraires", (r) => { const s = mix(r, SYN).slice(0, 2), a = mix(r, ANT).slice(0, 2), pool = SYN.flatMap((x) => x).concat(ANT.flatMap((x) => x));
    return { context: "Trouve le synonyme ou le contraire de chaque mot.", steps: [
      ...s.map(([x, y]) => S(`Synonyme de « ${x} » :`, y, autres(r, pool.filter((w) => w !== x), y), `${x} ≈ ${y}.`, 1)),
      ...a.map(([x, y]) => S(`Contraire de « ${x} » :`, y, autres(r, pool.filter((w) => w !== x), y), `${x} ≠ ${y}.`, 1.5))] }; });
  exConj("ce1-francais", ["present"], ER.concat(["être", "avoir"])); exAcc("ce1-francais"); exHom("ce1-francais", ["aa", "et"]); exVoc("ce1-francais");
  exConj("ce2-francais", ["present", "imparfait", "futur", "pc"], ER.concat(BASE, ["finir"])); exAcc("ce2-francais"); exHom("ce2-francais", ["aa", "et", "son", "on"]); exVoc("ce2-francais");
  exConj("cm1-francais", ["present", "imparfait", "futur", "pc", "ps"], ER.concat(Object.keys(IRR))); exAcc("cm1-francais"); exHom("cm1-francais", ["son", "on", "ces", "ou", "ce"]); exVoc("cm1-francais");
  exConj("cm2-francais", ["imparfait", "futur", "pc", "ps"], ER.concat(Object.keys(IRR))); exHom("cm2-francais", ["ces", "ce", "leur", "cest", "ou"]); exVoc("cm2-francais");
  ex("cm2-francais", "Accorder le participe passé", (r) => { const xs = mix(r, PPA).slice(0, 4); return { context: "Accorde correctement chaque participe passé entre parenthèses.", steps: xs.map(([ph, ok, f], i) => S(`« ${ph} »`, ok, f, /sont|est/.test(ph) ? "Avec être : accord avec le sujet." : /qu.|que|les ai/.test(ph) ? "Avec avoir : accord avec le COD placé avant." : /ont|avons/.test(ph) ? "Avec avoir et COD après : pas d'accord." : "Sans auxiliaire : accord comme un adjectif.", i < 2 ? 1 : 1.5)) }; });

  // matières de faits : chaque table devient des questions [q, réponse, explication]
  const T = (rows, stem) => rows.map(([a, b]) => [stem(a), b, `${a} : ${b}.`]);
  const exF = (sid, t, ctx, ...tables) => exFaits(sid, t, ctx, tables.flat());
  exF("ce1-sciences", "Mon corps et mes sens", "Réponds à partir de ta leçon sur le corps et l'hygiène.", T(SENS, (a) => `Organe du sens de ${a} :`), T(HYG, (a) => `Quand faut-il ${a} ?`));
  exF("ce1-sciences", "Les animaux", "Observe les animaux de ton village et réponds.", T(ANIM, (a) => `Régime de ${a} :`), T(DEPL, (a) => `Comment se déplace ${a} ?`));
  exF("ce1-sciences", "Les plantes et les aliments", "Réponds à partir de tes leçons sur les plantes et les aliments.", T(PLANTE, (a) => `Rôle de ${a} :`), T(ALIM, (a) => `Groupe de ${a} :`));
  exF("ce1-histoire", "Ma famille", "Réponds sur ta famille.", T(FAMILLE, (a) => `Qui est ${a} ?`));
  exF("ce1-histoire", "Les métiers", "Associe chaque métier à son travail.", T(METIERS, (a) => `Que fait ${a} ?`));
  ex("ce1-histoire", "Les jours et les mois", (r) => { const i = ri(r, 0, 6), j = ri(r, 0, 11);
    return { context: `Aujourd'hui, nous sommes ${JOURS[i]}, au mois de ${MOIS[j]}.`, steps: [
      S("Quel jour sera-t-il demain ?", JOURS[(i + 1) % 7], autres(r, JOURS.filter((x) => x !== JOURS[i]), JOURS[(i + 1) % 7]), `Après ${JOURS[i]} vient ${JOURS[(i + 1) % 7]}.`, 1),
      S("Quel jour était-ce hier ?", JOURS[(i + 6) % 7], autres(r, JOURS.filter((x) => x !== JOURS[i]), JOURS[(i + 6) % 7]), `Avant ${JOURS[i]} vient ${JOURS[(i + 6) % 7]}.`, 1),
      S("Quel sera le mois prochain ?", MOIS[(j + 1) % 12], autres(r, MOIS.filter((x) => x !== MOIS[j]), MOIS[(j + 1) % 12]), `Après ${MOIS[j]} vient ${MOIS[(j + 1) % 12]}.`, 1.5),
      S("Combien de jours dans une semaine ?", "7", ["5", "10", "12"], "Lundi à dimanche : 7 jours.", 1.5)] }; });
  exF("ce1-geo", "S'orienter", "Le soleil t'aide à t'orienter.", T([["le soleil se lève", "à l'est"], ["le soleil se couche", "à l'ouest"], ["en face de l'est, on a", "l'ouest"], ["opposé au nord", "le sud"]], (a) => `${a[0].toUpperCase() + a.slice(1)} :`), T(SAISON, (a) => `Que désigne ${a} ?`));
  exF("ce1-geo", "Les saisons", "Réponds sur le temps qu'il fait au Sénégal.", T(SAISON, (a) => `Que désigne ${a} ?`));
  exF("ce1-geo", "Les activités de mon pays", "Réponds sur les activités des hommes.", T(ACTI, (a) => `Activité principale de ${a} :`));
  exF("ce1-civique", "La politesse", "Choisis la bonne formule de politesse.", T(POLI, (a) => `Que dit-on ${a} ?`));
  exF("ce1-civique", "Sur la route", "Réponds sur la sécurité routière.", T(ROUTE, (a) => `Que fais-je au ${a.startsWith("feu") ? a : "niveau du " + a} ?`), T(POLI.slice(0, 2), (a) => `Que dit-on ${a} ?`));
  exF("ce1-civique", "Mes droits", "Réponds sur les droits de l'enfant.", T(DROITS, (a) => `« ${a[0].toUpperCase() + a.slice(1)} » correspond au :`));
  exF("ce2-sciences", "Respirer et digérer", "Réponds sur la respiration et la digestion.", T(RESP, (a) => `Respiration : ${a} …`), T(DIG, (a) => `Rôle de ${a} :`));
  ex("ce2-sciences", "La naissance des animaux", (r) => ({ context: "Classe chaque animal : ovipare (il naît d'un œuf pondu) ou vivipare (il naît du ventre de sa mère).", steps: mix(r, NAISS).slice(0, 4).map(([a, b], i) => S(`${a[0].toUpperCase() + a.slice(1)} est :`, b, [b === "ovipare" ? "vivipare" : "ovipare", "ni ovipare ni vivipare", "ovipare et vivipare à la fois"], `${a} : ${b}.`, i < 2 ? 1 : 1.5)) }));
  exF("ce2-sciences", "Se protéger des maladies", "Réponds sur les maladies.", T(MAL, (a) => `Comment attrape-t-on ${a} ?`));
  exF("ce2-histoire", "Siècles et dates", "Réponds sur les siècles.", Array.from({ length: 12 }, (_, k) => { const y = [1235, 1324, 1659, 1789, 1848, 1885, 1902, 1914, 1960, 2000, 2024, 1076][k]; return [`L'année ${y} appartient au :`, `${SIECLE(y)} siècle`, `${y} : ${SIECLE(y)} siècle.`]; }));
  exF("ce2-histoire", "Les symboles et l'histoire", "Réponds sur les symboles du Sénégal.", T(SYMB, (a) => `Au Sénégal, ${a} :`));
  exChrono("ce2-histoire", "La frise du temps", EMP.concat(COLO.slice(7)));
  exF("ce2-geo", "Lire une carte", "Une carte est orientée avec le nord en haut.", T(CARTE, (a) => `${a[0].toUpperCase() + a.slice(1)} indique :`), T(LIM.slice(0, 4), (a) => `Limite du Sénégal ${a} :`));
  exF("ce2-geo", "Les activités et les fleuves", "Réponds sur les régions du Sénégal.", T(ACTI, (a) => `Activité principale de ${a} :`), T(FLEUVES, (a) => `Ville traversée par ${a} :`));
  exF("ce2-geo", "Les fleuves du Sénégal", "Réponds sur les cours d'eau.", T(FLEUVES, (a) => `Ville ou région traversée par ${a} :`), T(SAISON, (a) => `Que désigne ${a} ?`));
  exF("ce2-civique", "Les symboles de la Nation", "Réponds sur les symboles du Sénégal.", T(SYMB, (a) => `Au Sénégal, ${a} :`));
  exF("ce2-civique", "Droits et devoirs", "Réponds sur les droits de l'enfant.", T(DROITS, (a) => `« ${a[0].toUpperCase() + a.slice(1)} » correspond au :`));
  exF("ce2-civique", "Circuler en sécurité", "Réponds sur la sécurité routière et la politesse.", T(ROUTE, (a) => `Que fais-je au ${a.startsWith("feu") ? a : "niveau du " + a} ?`), T(POLI, (a) => `Que dit-on ${a} ?`));
  exF("cm1-sciences", "Le squelette et le sang", "Réponds sur le corps humain.", T(OS, (a) => `Rôle de ${a} :`), T(SANG, (a) => `Rôle de ${a} :`));
  exF("cm1-sciences", "Le circuit électrique", "Réponds sur l'électricité.", T(ELEC, (a) => `Dans un circuit, ${a} est :`));
  exF("cm1-sciences", "La santé", "Réponds sur les maladies.", T(MAL, (a) => `Comment attrape-t-on ${a} ?`), T(MAL2.slice(0, 3), (a) => `Comment se protéger contre ${a} ?`));
  exChrono("cm1-histoire", "La frise des empires", EMP);
  exF("cm1-histoire", "Les grands rois", "Réponds sur les empires et les royaumes.", T(ROIS, (a) => `Qui était ${a} ?`), T(CAP, (a) => `Capitale de ${a} :`));
  exF("cm1-histoire", "Les capitales des empires", "Réponds sur les empires.", T(CAP, (a) => `Capitale de ${a} :`), T(ROIS.slice(0, 4), (a) => `Qui était ${a} ?`));
  exF("cm1-geo", "Les limites du Sénégal", "Réponds sur la situation du Sénégal.", T(LIM, (a) => `Limite du Sénégal ${a} :`));
  exF("cm1-geo", "Les activités et les fleuves", "Réponds sur la géographie du Sénégal.", T(ACTI, (a) => `Activité principale de ${a} :`), T(FLEUVES, (a) => `Ville ou région traversée par ${a} :`));
  exF("cm1-geo", "Le climat", "Réponds sur le climat du Sénégal.", T(SAISON, (a) => `Que désigne ${a} ?`), T(LIM.slice(0, 2), (a) => `Limite du Sénégal ${a} :`));
  exF("cm1-civique", "Les institutions", "Réponds sur les institutions de la République.", T(INST, (a) => `${a[0].toUpperCase() + a.slice(1)} :`));
  exF("cm1-civique", "Les symboles de la Nation", "Réponds sur la Nation.", T(SYMB, (a) => `Au Sénégal, ${a} :`));
  exF("cm1-civique", "Les droits de l'enfant", "Réponds sur les droits de l'enfant.", T(DROITS, (a) => `« ${a[0].toUpperCase() + a.slice(1)} » correspond au :`));
  exF("cm2-sciences", "La nutrition", "Réponds sur les appareils de la nutrition.", T(NUT, (a) => `Rôle de ${a} :`), T(DIG.slice(2), (a) => `Rôle de ${a} :`));
  exF("cm2-sciences", "Santé publique", "Réponds sur la prévention des maladies.", T(MAL2, (a) => `Comment se protéger contre ${a} ?`));
  exF("cm2-sciences", "Énergie et électricité", "Réponds sur l'énergie et l'électricité.", T(ENER, (a) => `${a[0].toUpperCase() + a.slice(1)} est une énergie :`), T(ELEC.slice(0, 3), (a) => `Dans un circuit, ${a} est :`));
  exChrono("cm2-histoire", "La frise de la colonisation à l'indépendance", COLO);
  exF("cm2-histoire", "Les résistants", "Réponds sur les résistances à la colonisation.", T(RESIST, (a) => `Région de résistance de ${a} :`));
  exF("cm2-histoire", "Les présidents et les organisations", "Réponds sur le Sénégal indépendant.", T(PRES, (a) => `Période de présidence de ${a} :`), T(ORG, (a) => `Siège de ${a} :`));
  exF("cm2-geo", "L'économie du Sénégal", "Réponds sur les productions du Sénégal.", T(AGRI, (a) => `Zone principale de production de ${a} :`));
  exF("cm2-geo", "Les capitales africaines", "Réponds sur les pays d'Afrique.", T(CAPAF, (a) => `Capitale de ${a} :`));
  exF("cm2-geo", "Le monde", "Réponds sur les continents et les océans.", T(MONDE, (a) => `Qu'est-ce que ${a} ?`));
  exF("cm2-civique", "Les élections", "Réponds sur le déroulement d'un vote.", T(VOTE, (a) => `Qu'est-ce que ${a} ?`));
  exF("cm2-civique", "Les institutions", "Réponds sur la Constitution.", T(INST2, (a) => `Qui exerce ${a} ?`), T(INST.slice(0, 3), (a) => `${a[0].toUpperCase() + a.slice(1)} :`));
  exF("cm2-civique", "Les valeurs de solidarité", "Réponds sur les valeurs sénégalaises.", T(VAL, (a) => `Que signifie ${a} ?`));

  // garde-fou commun
  for (const it of NOUV) { const f = it[1]; it[1] = (r) => { for (let i = 0; i < 12; i++) { let o; try { o = f(r); } catch (er) { continue; }
    if (!o || o.ok == null || /NaN|undefined|Infinity/.test(JSON.stringify(o))) continue; o = GH.fix(GH.clean({ ...o, q: fr(o.q) })); if (o && new Set([o.ok, ...o.faux]).size === 4) return o; } return null; }; }
})();
