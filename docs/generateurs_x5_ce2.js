"use strict";
// CE2 ×5 (demande d'Est du 2026-11-05) : nouveaux modèles de questions pour les chapitres de maths et de français,
// en priorité ceux qui n'en avaient pas (géométrie, problèmes, types de phrases, pronoms, lecture, écriture).
// Programme CEB, étape 2. Chaque tirage donne une question nouvelle avec la réponse calculée et l'explication.
(() => {
  if (typeof GEN === "undefined") return;
  const ri = (r, a, b) => a + Math.floor(r() * (b - a + 1));
  const pick = (r, a) => a[Math.floor(r() * a.length)];
  const mix = (r, a) => a.map((x) => [r(), x]).sort((p, q) => p[0] - q[0]).map((p) => p[1]);
  const F = (x) => Math.round(x).toLocaleString("fr-FR");
  const autres = (r, pool, ok, n = 3) => mix(r, [...new Set(pool.map(String))].filter((x) => x !== String(ok))).slice(0, n);
  const num = (r, ok, ds, u = "") => autres(r, ds.map((d) => ok + d).filter((x) => x >= 0 && x !== ok).map((x) => F(x) + u), F(ok) + u);
  const add = (sid, ch, f) => (GEN[sid] = GEN[sid] || []).push([ch, (r) => {
    for (let i = 0; i < 12; i++) { let o; try { o = f(r); } catch (e) { continue; }
      if (!o || o.ok == null || /NaN|undefined|Infinity/.test(JSON.stringify(o))) continue;
      o.ok = String(o.ok); o.faux = o.faux.map(String);
      if (o.faux.length >= 3 && new Set([o.ok, ...o.faux.slice(0, 3)]).size === 4) { o.faux = o.faux.slice(0, 3); return o; } }
    return null; }]);

  // ---------- nombres en lettres (jusqu'à 999 999), orthographe traditionnelle avec traits d'union
  const U = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"];
  const D = { 20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante", 60: "soixante" };
  const moins100 = (n) => {
    if (n <= 16) return U[n];
    if (n < 20) return "dix-" + U[n - 10];
    if (n < 70) { const d = Math.floor(n / 10) * 10, u = n % 10; return D[d] + (u === 0 ? "" : u === 1 ? " et un" : "-" + U[u]); }
    if (n < 80) return n === 71 ? "soixante et onze" : "soixante-" + moins100(n - 60);
    if (n === 80) return "quatre-vingts";
    return "quatre-vingt-" + moins100(n - 80);
  };
  const moins1000 = (n) => {
    const c = Math.floor(n / 100), rst = n % 100;
    const cent = c === 0 ? "" : c === 1 ? "cent" : U[c] + (rst === 0 ? " cents" : " cent");
    return [cent, rst ? moins100(rst) : ""].filter(Boolean).join(" ") || "zéro";
  };
  const lettres = (n) => {
    const m = Math.floor(n / 1000), rst = n % 1000;
    const mil = m === 0 ? "" : m === 1 ? "mille" : moins1000(m).replace(/cents$/, "cent").replace(/vingts$/, "vingt") + " mille";
    return [mil, rst ? moins1000(rst) : ""].filter(Boolean).join(" ") || "zéro";
  };
  const RANGS = [["unités", 1], ["dizaines", 10], ["centaines", 100], ["unités de mille", 1000], ["dizaines de mille", 10000]];

  // ======================= MATHÉMATIQUES =======================
  const M = "ce2-maths";
  const N1 = "Les nombres jusqu'à 100 000";
  add(M, N1, (r) => { const n = ri(r, 1001, 99999); return { q: `Écris en chiffres : « ${lettres(n)} ».`, ok: F(n), faux: num(r, n, [1000, -1000, 100, -100, 10, 9000, -90]), e: `${lettres(n)} = ${F(n)}.` }; });
  add(M, N1, (r) => { const n = ri(r, 1001, 99999), ok = lettres(n); return { q: `Comment s'écrit ${F(n)} en lettres ?`, ok, faux: autres(r, [n + 1000, n - 1000, n + 100, n + 10, n - 100].filter((x) => x > 0 && x < 100000).map(lettres), ok), e: `${F(n)} se lit « ${ok} ».` }; });
  add(M, N1, (r) => { const n = ri(r, 10000, 99999), [nom, v] = pick(r, RANGS), ch = Math.floor(n / v) % 10;
    return { q: `Dans ${F(n)}, quel est le chiffre des ${nom} ?`, ok: ch, faux: autres(r, String(n).split("").concat(["0", "1"]), ch), e: `${F(n)} : ${String(n).split("").map((c, i) => `${c} (${RANGS[4 - i][0]})`).join(", ")}.` }; });
  add(M, N1, (r) => { const n = ri(r, 10000, 99999), [nom, v] = pick(r, RANGS.slice(1)), ok = Math.floor(n / v);
    return { q: `Dans ${F(n)}, combien y a-t-il ${/^[aeiouéu]/.test(nom) ? "d'" : "de "}${nom} en tout ?`, ok: F(ok), faux: autres(r, [Math.floor(n / v) % 10, Math.floor(n / (v * 10)), Math.floor(n / (v / 10 || 1)), ok + 1].map(F), F(ok)), e: `On lit le nombre jusqu'au chiffre des ${nom} : ${F(ok)}.` }; });
  add(M, N1, (r) => { const xs = [...new Set([...Array(4)].map(() => ri(r, 10000, 99999)))]; if (xs.length < 4) return null; const g = pick(r, ["grand", "petit"]), ok = g === "grand" ? Math.max(...xs) : Math.min(...xs);
    return { q: `Quel est le plus ${g} nombre ?`, ok: F(ok), faux: xs.filter((x) => x !== ok).map(F), e: `On compare d'abord les dizaines de mille, puis les unités de mille, etc. Le plus ${g} est ${F(ok)}.` }; });
  add(M, N1, (r) => { const n = ri(r, 1000, 99999), [nom, v] = pick(r, [["à la dizaine la plus proche", 10], ["à la centaine la plus proche", 100], ["au millier le plus proche", 1000]]), ok = Math.round(n / v) * v; if (ok === n) return null;
    return { q: `Arrondis ${F(n)} ${nom}.`, ok: F(ok), faux: autres(r, [ok + v, ok - v, Math.floor(n / v) * v === ok ? Math.ceil(n / v) * v : Math.floor(n / v) * v, n].filter((x) => x >= 0).map(F), F(ok)), e: `${F(n)} est plus près de ${F(ok)}.` }; });
  add(M, N1, (r) => { const n = ri(r, 1000, 99998), s = pick(r, ["juste après", "juste avant"]), ok = s === "juste après" ? n + 1 : n - 1;
    return { q: `Quel nombre vient ${s} ${F(n)} ?`, ok: F(ok), faux: autres(r, [n, s === "juste après" ? n - 1 : n + 1, ok + 10, ok - 10, ok + 100].map(F), F(ok)), e: `${s === "juste après" ? "On ajoute" : "On enlève"} 1 : ${F(ok)}.` }; });
  add(M, N1, (r) => { const c = [ri(r, 1, 9), ri(r, 0, 9), ri(r, 0, 9), ri(r, 0, 9), ri(r, 0, 9)], n = +c.join("");
    const dec = c.map((x, i) => [x, 10 ** (4 - i)]).filter(([x]) => x).map(([x, v]) => `${x} × ${F(v)}`).join(" + ");
    return { q: `Combien font ${dec} ?`, ok: F(n), faux: autres(r, [n + 1000, n - 100, +c.slice().reverse().join("") || n + 1, n + 10].filter((x) => x > 0).map(F), F(n)), e: `On place chaque chiffre à son rang : ${F(n)}.` }; });
  add(M, N1, (r) => { const xs = [...new Set([...Array(4)].map(() => ri(r, 1000, 99999)))]; if (xs.length < 4) return null; const ok = xs.slice().sort((a, b) => a - b);
    const f = (a) => a.map(F).join(" < ");
    return { q: "Quel rangement est dans l'ordre croissant (du plus petit au plus grand) ?", ok: f(ok), faux: [f([ok[1], ok[0], ok[2], ok[3]]), f(ok.slice().reverse()), f([ok[0], ok[2], ok[1], ok[3]])], e: `Ordre croissant : ${f(ok)}.` }; });

  const ADD = "Addition et soustraction posées";
  add(M, ADD, (r) => { const a = ri(r, 1000, 49999), b = ri(r, 1000, 49999), s = a + b; return { q: `Pose et calcule : ${F(a)} + ${F(b)}.`, ok: F(s), faux: num(r, s, [10, -10, 100, 1000, -1000]), e: `On aligne les unités et on n'oublie pas les retenues : ${F(s)}.` }; });
  add(M, ADD, (r) => { const a = ri(r, 20000, 99999), b = ri(r, 1000, a - 1000), d = a - b; return { q: `Pose et calcule : ${F(a)} − ${F(b)}.`, ok: F(d), faux: num(r, d, [10, -10, 100, -100, 1000]), e: `${F(a)} − ${F(b)} = ${F(d)}. Vérifie : ${F(d)} + ${F(b)} = ${F(a)}.` }; });
  add(M, ADD, (r) => { const b = ri(r, 100, 9999), c = ri(r, b + 100, 99999), ok = c - b; return { q: `Complète : ${F(b)} + … = ${F(c)}.`, ok: F(ok), faux: num(r, ok, [b, 10, -10, 100]).concat(F(c + b)), e: `On calcule ${F(c)} − ${F(b)} = ${F(ok)}.` }; });
  add(M, ADD, (r) => { const [cible] = [pick(r, [1000, 10000, 100000])], a = ri(r, cible / 10, cible - 1), ok = cible - a; return { q: `Combien faut-il ajouter à ${F(a)} pour obtenir ${F(cible)} ?`, ok: F(ok), faux: num(r, ok, [10, -10, 100, 1, -1]), e: `${F(cible)} − ${F(a)} = ${F(ok)}.` }; });
  add(M, ADD, (r) => { const a = ri(r, 1000, 89999), k = pick(r, [9, 99, 999]), s = a + k; return { q: `Calcul malin : ${F(a)} + ${k}.`, ok: F(s), faux: num(r, s, [1, -1, 2, 10]), e: `Ajouter ${k}, c'est ajouter ${k + 1} puis enlever 1 : ${F(a + k + 1)} − 1 = ${F(s)}.` }; });
  add(M, ADD, (r) => { const nom = pick(r, ["Awa", "Moussa", "Fatou", "Ibrahima", "Khady", "Ousmane"]), a = ri(r, 50, 400) * 50, b = ri(r, 10, Math.floor(a / 50) - 5) * 50, ok = a - b;
    return { q: `${nom} a ${F(a)} F. ${["Awa", "Fatou", "Khady"].includes(nom) ? "Elle" : "Il"} achète un sac à ${F(b)} F. Combien lui reste-t-il ?`, ok: F(ok) + " F", faux: autres(r, [a + b, ok + 100, ok - 100, b].map((x) => F(x) + " F"), F(ok) + " F"), e: `Il reste ${F(a)} − ${F(b)} = ${F(ok)} F.` }; });

  const MUL = "La multiplication";
  add(M, MUL, (r) => { const a = ri(r, 101, 999), b = ri(r, 2, 9), p = a * b; return { q: `Pose et calcule : ${F(a)} × ${b}.`, ok: F(p), faux: num(r, p, [b, -b, 10, 100, a]), e: `${F(a)} × ${b} = ${F(p)}.` }; });
  add(M, MUL, (r) => { const a = ri(r, 11, 999), k = pick(r, [10, 100, 1000]), p = a * k; return { q: `Combien font ${F(a)} × ${F(k)} ?`, ok: F(p), faux: autres(r, [a * k * 10, a * k / 10, a + k, a * k + k].filter(Number.isInteger).map(F), F(p)), e: `Multiplier par ${F(k)}, c'est écrire ${String(k).length - 1} zéro${k > 10 ? "s" : ""} à droite : ${F(p)}.` }; });
  add(M, MUL, (r) => { const a = ri(r, 6, 9), b = ri(r, 6, 9), p = a * b; return { q: `Table de ${a} : ${a} × ${b} = ?`, ok: p, faux: autres(r, [p + a, p - a, p + b, p - 1, p + 1], p), e: `${a} × ${b} = ${p}.` }; });
  add(M, MUL, (r) => { const n = ri(r, 3, 9), k = ri(r, 12, 48), obj = pick(r, [["caisses", "mangues"], ["paquets", "biscuits"], ["rangées", "chaises"], ["sachets", "bonbons"]]), p = n * k;
    return { q: `Il y a ${n} ${obj[0]} de ${k} ${obj[1]}. Combien de ${obj[1]} en tout ?`, ok: F(p), faux: autres(r, [n + k, p + k, p - n, p + 10].map(F), F(p)), e: `${n} × ${k} = ${F(p)} ${obj[1]}.` }; });
  add(M, MUL, (r) => { const a = ri(r, 12, 499), [nom, k] = pick(r, [["le double", 2], ["le triple", 3]]), ok = a * k; return { q: `Quel est ${nom} de ${F(a)} ?`, ok: F(ok), faux: autres(r, [a * (5 - k), a + k, ok + a, ok - 1].map(F), F(ok)), e: `${nom} de ${F(a)} = ${F(a)} × ${k} = ${F(ok)}.` }; });
  add(M, MUL, (r) => { const a = ri(r, 2, 9), b = ri(r, 11, 99), c = ri(r, 2, 5), ok = a * b * c; return { q: `Calcule astucieusement : ${a} × ${b} × ${c}.`, ok: F(ok), faux: num(r, ok, [b, -b, a * c, 10]), e: `On peut commencer par ${a} × ${c} = ${a * c}, puis × ${b} : ${F(ok)}.` }; });

  const DIV = "La division";
  add(M, DIV, (r) => { const d = ri(r, 2, 9), q = ri(r, 11, 199), rst = ri(r, 0, d - 1), n = d * q + rst;
    return { q: `Dans la division de ${F(n)} par ${d}, quel est le quotient ?`, ok: F(q), faux: autres(r, [q + 1, q - 1, q + 10, rst, n - d].filter((x) => x >= 0).map(F), F(q)), e: `${F(n)} = ${d} × ${F(q)} + ${rst}. Le quotient est ${F(q)}.` }; });
  add(M, DIV, (r) => { const d = ri(r, 3, 9), q = ri(r, 11, 99), rst = ri(r, 1, d - 1), n = d * q + rst;
    return { q: `Dans la division de ${F(n)} par ${d}, quel est le reste ?`, ok: rst, faux: autres(r, [0, rst + 1, rst - 1, d, d - 1, q].filter((x) => x >= 0 && x !== rst), rst), e: `${d} × ${q} = ${F(d * q)} ; ${F(n)} − ${F(d * q)} = ${rst}. Le reste est toujours plus petit que ${d}.` }; });
  add(M, DIV, (r) => { const d = ri(r, 2, 9), q = ri(r, 12, 250), n = d * q, obj = pick(r, ["billes", "cahiers", "oranges", "crayons"]);
    return { q: `On partage ${F(n)} ${obj} entre ${d} enfants, chacun autant. Combien chacun en reçoit-il ?`, ok: F(q), faux: autres(r, [q + 1, q - 1, n - d, q * 2].map(F), F(q)), e: `${F(n)} ÷ ${d} = ${F(q)}.` }; });
  add(M, DIV, (r) => { const n = ri(r, 2, 400) * 4, [nom, k] = pick(r, [["la moitié", 2], ["le quart", 4]]), ok = n / k; return { q: `Quelle est ${nom} de ${F(n)} ?`, ok: F(ok), faux: autres(r, [n / (6 - k), n * k, ok + 1, ok - 2].filter(Number.isInteger).map(F), F(ok)), e: `${nom} de ${F(n)} = ${F(n)} ÷ ${k} = ${F(ok)}.` }; });
  add(M, DIV, (r) => { const a = ri(r, 3, 9), b = ri(r, 3, 9), p = a * b; return { q: `Combien de fois ${a} dans ${p} ?`, ok: b, faux: autres(r, [b + 1, b - 1, a, p - a], b), e: `${a} × ${b} = ${p}, donc ${p} ÷ ${a} = ${b}.` }; });
  add(M, DIV, (r) => { const p = ri(r, 2, 9), n = ri(r, 3, 6), places = n * p + ri(r, 1, p - 1), ok = Math.ceil(places / p);
    return { q: `${places} élèves partent en pirogue. Une pirogue prend ${p} élèves. Combien de pirogues faut-il au minimum ?`, ok, faux: autres(r, [ok - 1, ok + 1, Math.floor(places / p) + 2, p], ok), e: `${places} ÷ ${p} = ${Math.floor(places / p)} reste ${places % p} : il faut une pirogue de plus pour les ${places % p} derniers, soit ${ok}.` }; });

  const FR = "Les fractions simples";
  const FN = { 2: ["demi", "demis"], 3: ["tiers", "tiers"], 4: ["quart", "quarts"] };
  add(M, FR, (r) => { const d = pick(r, [2, 3, 4, 5, 6, 8, 10]), n = ri(r, 1, d - 1); return { q: `On partage une galette en ${d} parts égales et on en mange ${n}. Quelle fraction a-t-on mangée ?`, ok: `${n}/${d}`, faux: autres(r, [`${d}/${n}`, `${d - n}/${d}`, `${n}/${d + 1}`, `1/${d}`, `${n + 1}/${d}`], `${n}/${d}`), e: `${n} parts sur ${d} : ${n}/${d}.` }; });
  add(M, FR, (r) => { const d = pick(r, [2, 3, 4]), n = ri(r, 1, d - 1), ok = `${n}/${d}`, mot = `${lettres(n)} ${n > 1 ? FN[d][1] : FN[d][0]}`;
    return { q: `Comment écrit-on « ${mot} » ?`, ok, faux: autres(r, ["1/2", "1/3", "2/3", "1/4", "3/4", "4/3", "2/4"], ok), e: `« ${mot} » s'écrit ${ok}.` }; });
  add(M, FR, (r) => { const d = pick(r, [3, 4, 5, 6, 8]), xs = mix(r, [...Array(d - 1).keys()].map((i) => i + 1)).slice(0, 4); if (xs.length < 4) return null; const ok = Math.max(...xs);
    return { q: "Quelle fraction est la plus grande ?", ok: `${ok}/${d}`, faux: xs.filter((x) => x !== ok).map((x) => `${x}/${d}`), e: `Même dénominateur : la plus grande a le plus grand numérateur, ${ok}/${d}.` }; });
  add(M, FR, (r) => { const d = pick(r, [2, 3, 4, 5, 6, 8, 10]); return { q: "Quelle fraction est égale à une unité entière ?", ok: `${d}/${d}`, faux: [`1/${d}`, `${d - 1}/${d}`, `${d}/${d + 1}`], e: `${d}/${d} : on prend toutes les parts, c'est 1.` }; });
  add(M, FR, (r) => { const d = pick(r, [2, 3, 4, 5]), k = ri(r, 2, 30), n = ri(r, 1, d - 1), tot = d * k, ok = n * k;
    return { q: `Combien font les ${n}/${d} de ${tot} ?`, ok, faux: autres(r, [k, ok + k, tot - ok === ok ? ok + 2 : tot - ok, tot / n | 0], ok), e: `${tot} ÷ ${d} = ${k}, puis ${k} × ${n} = ${ok}.` }; });

  const LG = "Longueurs et périmètres";
  add(M, LG, (r) => { const [a, ua, k, ub] = pick(r, [[ri(r, 2, 90), "m", 100, "cm"], [ri(r, 2, 50), "km", 1000, "m"], [ri(r, 2, 90), "cm", 10, "mm"], [ri(r, 2, 9), "m", 1000, "mm"]]), ok = a * k;
    return { q: `${a} ${ua} = … ${ub}`, ok: F(ok), faux: autres(r, [a * k * 10, a * k / 10, a + k, a * 10].filter(Number.isInteger).map(F), F(ok)), e: `1 ${ua} = ${F(k)} ${ub}, donc ${a} ${ua} = ${F(ok)} ${ub}.` }; });
  add(M, LG, (r) => { const c = ri(r, 3, 60); return { q: `Périmètre d'un carré de ${c} m de côté :`, ok: `${4 * c} m`, faux: [`${c * c} m`, `${2 * c} m`, `${4 * c + 4} m`], e: `4 × ${c} = ${4 * c} m.` }; });
  add(M, LG, (r) => { const L = ri(r, 6, 80), l = ri(r, 2, L - 1); return { q: `Un champ rectangulaire mesure ${L} m de long et ${l} m de large. Quelle longueur de grillage pour en faire le tour ?`, ok: `${2 * (L + l)} m`, faux: [`${L + l} m`, `${L * l} m`, `${2 * L + l} m`], e: `Périmètre = 2 × (${L} + ${l}) = ${2 * (L + l)} m.` }; });
  add(M, LG, (r) => { const a = ri(r, 3, 30), b = ri(r, 3, 30), c = ri(r, Math.abs(a - b) + 1, a + b - 1); return { q: `Périmètre d'un triangle de côtés ${a} cm, ${b} cm et ${c} cm :`, ok: `${a + b + c} cm`, faux: autres(r, [a + b, a * b, a + b + c + 1, 3 * a].map((x) => `${x} cm`), `${a + b + c} cm`), e: `On additionne les trois côtés : ${a + b + c} cm.` }; });
  add(M, LG, (r) => { const m = ri(r, 1, 9), cm = ri(r, 1, 99), ok = m * 100 + cm; return { q: `${m} m ${cm} cm = … cm`, ok: F(ok), faux: autres(r, [m + cm, m * 10 + cm, m * 1000 + cm, ok + 100].map(F), F(ok)), e: `${m} m = ${m * 100} cm ; ${m * 100} + ${cm} = ${ok} cm.` }; });

  const MA = "Masses, capacités et monnaie";
  add(M, MA, (r) => { const [a, ua, k, ub] = pick(r, [[ri(r, 2, 50), "kg", 1000, "g"], [ri(r, 2, 20), "L", 100, "cL"], [ri(r, 2, 9), "L", 1000, "mL"], [ri(r, 2, 9), "t", 1000, "kg"]]), ok = a * k;
    return { q: `${a} ${ua} = … ${ub}`, ok: F(ok), faux: autres(r, [a * k * 10, a * k / 10, a + k, a * 10].filter(Number.isInteger).map(F), F(ok)), e: `1 ${ua} = ${F(k)} ${ub}, donc ${a} ${ua} = ${F(ok)} ${ub}.` }; });
  add(M, MA, (r) => { const p = ri(r, 2, 40) * 25, n = ri(r, 2, 9), b = Math.ceil((n * p) / 1000) * 1000, ok = b - n * p; if (ok === 0) return null;
    return { q: `${n} pains à ${F(p)} F. On paie avec ${F(b)} F. Combien le boutiquier rend-il ?`, ok: `${F(ok)} F`, faux: autres(r, [n * p, ok + p, ok + 100, b - p].filter((x) => x > 0).map((x) => `${F(x)} F`), `${F(ok)} F`), e: `${n} × ${F(p)} = ${F(n * p)} F ; ${F(b)} − ${F(n * p)} = ${F(ok)} F.` }; });
  add(M, MA, (r) => { const ps = [ri(r, 2, 20) * 50, ri(r, 2, 20) * 50, ri(r, 2, 20) * 50], s = ps[0] + ps[1] + ps[2];
    return { q: `Au marché : riz ${F(ps[0])} F, huile ${F(ps[1])} F, oignons ${F(ps[2])} F. Total ?`, ok: `${F(s)} F`, faux: num(r, s, [50, -50, 100, 500], " F"), e: `${F(ps[0])} + ${F(ps[1])} + ${F(ps[2])} = ${F(s)} F.` }; });
  add(M, MA, (r) => { const kg = ri(r, 1, 9), g = ri(r, 1, 9) * 100, ok = kg * 1000 + g; return { q: `${kg} kg ${g} g = … g`, ok: F(ok), faux: autres(r, [kg + g, kg * 100 + g, ok + 1000, kg * 10000 + g].map(F), F(ok)), e: `${kg} kg = ${F(kg * 1000)} g ; + ${g} = ${F(ok)} g.` }; });
  add(M, MA, (r) => { const [ok, b, n] = pick(r, [[500, 10000, 20], [500, 2000, 4], [250, 1000, 4], [200, 1000, 5], [100, 500, 5], [100, 1000, 10], [50, 200, 4], [25, 100, 4]]); return { q: `Combien de pièces de ${F(ok)} F faut-il pour faire ${F(b)} F ?`, ok: n, faux: autres(r, [n + 1, n * 2, n - 1, 3], n), e: `${F(b)} ÷ ${F(ok)} = ${n}.` }; });

  const DU = "Les durées et le calendrier";
  const hm = (m) => `${Math.floor(m / 60) % 24} h ${String(m % 60).padStart(2, "0")}`;
  add(M, DU, (r) => { const d = ri(r, 7, 17) * 60 + pick(r, [0, 15, 30, 45]), x = pick(r, [15, 30, 45, 50, 75, 90, 120]), ok = hm(d + x);
    return { q: `Il est ${hm(d)}. Quelle heure sera-t-il dans ${x} minutes ?`, ok, faux: autres(r, [hm(d + x + 10), hm(d + x - 15), hm(d + x + 60), hm(d - x)], ok), e: `${hm(d)} + ${x} min = ${ok}.` }; });
  add(M, DU, (r) => { const a = ri(r, 7, 12) * 60 + pick(r, [0, 15, 30]), x = ri(r, 2, 16) * 15, b = a + x;
    return { q: `Le cours commence à ${hm(a)} et finit à ${hm(b)}. Combien de temps dure-t-il ?`, ok: `${x} min`, faux: autres(r, [x + 15, x - 15, x + 60, x + 30].filter((y) => y > 0).map((y) => `${y} min`), `${x} min`), e: `De ${hm(a)} à ${hm(b)} : ${x} minutes${x >= 60 ? ` (${Math.floor(x / 60)} h ${x % 60} min)` : ""}.` }; });
  add(M, DU, (r) => { const [m, j] = pick(r, [["janvier", 31], ["février (année ordinaire)", 28], ["mars", 31], ["avril", 30], ["mai", 31], ["juin", 30], ["juillet", 31], ["août", 31], ["septembre", 30], ["octobre", 31], ["novembre", 30], ["décembre", 31]]);
    return { q: `Combien de jours compte le mois de ${m} ?`, ok: j, faux: autres(r, [28, 29, 30, 31, 32], j), e: `${m[0].toUpperCase() + m.slice(1)} compte ${j} jours.` }; });
  add(M, DU, (r) => { const s = ri(r, 2, 12), ok = s * 7; return { q: `Combien de jours dans ${s} semaines ?`, ok, faux: autres(r, [ok + 7, ok - 7, s * 5, s * 10], ok), e: `1 semaine = 7 jours ; ${s} × 7 = ${ok}.` }; });
  add(M, DU, (r) => { const h = ri(r, 2, 5), m = pick(r, [0, 15, 30, 45]), ok = h * 60 + m; return { q: `${h} h ${m} min = … min`, ok, faux: autres(r, [h * 100 + m, h + m, ok + 60, h * 60], ok), e: `${h} h = ${h * 60} min ; + ${m} = ${ok} min.` }; });
  const JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"];
  add(M, DU, (r) => { const i = ri(r, 0, 6), n = ri(r, 2, 20), ok = JOURS[(i + n) % 7]; return { q: `Aujourd'hui, c'est ${JOURS[i]}. Quel jour serons-nous dans ${n} jours ?`, ok, faux: autres(r, JOURS, ok), e: `${n} jours = ${Math.floor(n / 7)} semaine(s) et ${n % 7} jour(s) : ${ok}.` }; });

  const GEO = "Géométrie : angles, figures et cercle";
  const FIG = [["un triangle", 3], ["un carré", 4], ["un rectangle", 4], ["un losange", 4], ["un pentagone", 5], ["un hexagone", 6], ["un octogone", 8]];
  add(M, GEO, (r) => { const [f, n] = pick(r, FIG), w = pick(r, ["côtés", "sommets"]); return { q: `Combien de ${w} a ${f} ?`, ok: n, faux: autres(r, [3, 4, 5, 6, 8, n + 1], n), e: `${f[0].toUpperCase() + f.slice(1)} a ${n} côtés et ${n} sommets.` }; });
  add(M, GEO, (r) => { const [f, ok] = pick(r, [["un carré", "4 côtés égaux et 4 angles droits"], ["un rectangle", "4 angles droits, côtés opposés égaux"], ["un losange", "4 côtés égaux, pas forcément d'angle droit"], ["un triangle rectangle", "un angle droit"]]);
    return { q: `Quelle propriété décrit ${f} ?`, ok, faux: autres(r, ["4 côtés égaux et 4 angles droits", "4 angles droits, côtés opposés égaux", "4 côtés égaux, pas forcément d'angle droit", "un angle droit", "aucun côté égal"], ok), e: `${f[0].toUpperCase() + f.slice(1)} : ${ok}.` }; });
  add(M, GEO, (r) => { const d = ri(r, 2, 40) * 2, w = pick(r, ["rayon", "diamètre"]), ok = w === "rayon" ? d / 2 : d * 2, x = w === "rayon" ? d : d / 2;
    return { q: w === "rayon" ? `Un cercle a un diamètre de ${x} cm. Quel est son rayon ?` : `Un cercle a un rayon de ${x} cm. Quel est son diamètre ?`, ok: `${ok} cm`, faux: autres(r, [x, x * 4, x + 2, ok + 1].map((y) => `${y} cm`), `${ok} cm`), e: "Le diamètre est le double du rayon." }; });
  add(M, GEO, (r) => { const [a, ok] = pick(r, [["plus petit qu'un angle droit", "un angle aigu"], ["plus grand qu'un angle droit", "un angle obtus"], ["égal à l'angle du coin d'une feuille", "un angle droit"]]);
    return { q: `Un angle ${a} est :`, ok, faux: autres(r, ["un angle aigu", "un angle obtus", "un angle droit", "un angle plat"], ok), e: "On compare l'angle avec l'équerre (angle droit)." }; });
  add(M, GEO, (r) => { const [o, ok] = pick(r, [["vérifier un angle droit", "l'équerre"], ["tracer un cercle", "le compas"], ["tracer un trait droit et mesurer", "la règle graduée"], ["reporter une longueur sans la mesurer", "le compas"]]);
    return { q: `Quel instrument utilise-t-on pour ${o} ?`, ok, faux: autres(r, ["l'équerre", "le compas", "la règle graduée", "le rapporteur", "la gomme"], ok), e: `Pour ${o} : ${ok}.` }; });
  add(M, GEO, (r) => { const [f, ok] = pick(r, [["un carré", "4"], ["un rectangle (non carré)", "2"], ["un triangle équilatéral", "3"], ["un cercle", "une infinité"]]);
    return { q: `Combien d'axes de symétrie a ${f} ?`, ok, faux: autres(r, ["0", "1", "2", "3", "4", "une infinité"], ok), e: `${f[0].toUpperCase() + f.slice(1)} a ${ok} axe(s) de symétrie.` }; });

  const PB = "Résoudre des problèmes";
  const P1 = ["Awa", "Moussa", "Fatou", "Ibrahima", "Khady", "Ousmane", "Binta", "Lamine"];
  add(M, PB, (r) => { const n = pick(r, P1), il = ["Awa", "Fatou", "Khady", "Binta"].includes(n) ? "elle" : "il", a = ri(r, 10, 90), b = ri(r, 5, a - 1), ok = a - b; return { q: `${n} a ${a} billes. Son frère en a ${b}. Combien de billes ${n} a-t-${il} de plus que son frère ?`, ok, faux: autres(r, [a + b, ok + 1, ok - 1, b], ok), e: `« De plus » : on fait la différence, ${a} − ${b} = ${ok}.` }; });
  add(M, PB, (r) => { const ag = ri(r, 7, 12), d = ri(r, 20, 40), ok = ag + d; return { q: `Mamadou a ${ag} ans. Son père a ${d} ans de plus que lui. Quel âge a son père ?`, ok: `${ok} ans`, faux: autres(r, [d, d - ag, ok + 1, ag * 3].map((x) => `${x} ans`), `${ok} ans`), e: `${ag} + ${d} = ${ok} ans.` }; });
  add(M, PB, (r) => { const p = ri(r, 2, 12) * 50, n = ri(r, 3, 9), b = ri(r, 2, 6) * 1000; if (b <= n * p) return null; const ok = b - n * p;
    return { q: `Fatou achète ${n} cahiers à ${F(p)} F. Elle avait ${F(b)} F. Combien lui reste-t-il ?`, ok: `${F(ok)} F`, faux: autres(r, [n * p, b - p, ok + p, b + n * p].map((x) => `${F(x)} F`), `${F(ok)} F`), e: `D'abord ${n} × ${F(p)} = ${F(n * p)} F, puis ${F(b)} − ${F(n * p)} = ${F(ok)} F. (Deux étapes.)` }; });
  add(M, PB, (r) => { const g = ri(r, 3, 9), f = ri(r, 3, 9), cl = ri(r, 2, 6), ok = (g + f) * cl; return { q: `Dans chaque classe, il y a ${g} garçons et ${f} filles au premier rang. Combien d'élèves au premier rang dans ${cl} classes ?`, ok, faux: autres(r, [g + f + cl, g * f, ok + cl, (g + f) * (cl + 1)], ok), e: `(${g} + ${f}) × ${cl} = ${ok}.` }; });
  add(M, PB, (r) => { const tot = ri(r, 4, 20) * 6, n = pick(r, [2, 3, 6]), ok = tot / n; return { q: `Un car transporte ${tot} passagers en ${n} voyages identiques. Combien de passagers par voyage ?`, ok, faux: autres(r, [tot - n, ok + n, tot * n, ok - 1], ok), e: `${tot} ÷ ${n} = ${ok}.` }; });
  add(M, PB, (r) => { const op = pick(r, [["gagne", "+"], ["perd", "−"]]), a = ri(r, 20, 80), b = ri(r, 5, 19), c = ri(r, 2, 15), ok = op[1] === "+" ? a + b - c : a - b + c;
    return { q: `Au début du jeu, Lamine a ${a} points. Il ${op[0]} ${b} points, puis ${op[0] === "gagne" ? "perd" : "gagne"} ${c} points. Combien en a-t-il à la fin ?`, ok, faux: autres(r, [a + b + c, a - b - c, ok + 1, a], ok), e: `${a} ${op[1]} ${b} ${op[1] === "+" ? "−" : "+"} ${c} = ${ok}.` }; });

  // ======================= FRANÇAIS =======================
  const Fr = "ce2-francais";
  const TP = "Les types de phrases";
  const PHR = [["Le soleil se lève à l'est.", "déclarative"], ["Mon frère joue au football.", "déclarative"], ["La pluie tombe sur le village.", "déclarative"], ["Nous allons à l'école à pied.", "déclarative"],
    ["Où habites-tu ?", "interrogative"], ["Est-ce que tu as fini tes devoirs ?", "interrogative"], ["Quand part le car ?", "interrogative"], ["Aimes-tu le thiéboudienne ?", "interrogative"],
    ["Quelle belle journée !", "exclamative"], ["Comme tu as grandi !", "exclamative"], ["Que ce gâteau est bon !", "exclamative"], ["Quel bruit dans la cour !", "exclamative"],
    ["Ferme la porte, s'il te plaît.", "impérative"], ["Range ta chambre.", "impérative"], ["Lavez-vous les mains avant de manger.", "impérative"], ["Écoutez bien la maîtresse.", "impérative"]];
  add(Fr, TP, (r) => { const [p, t] = pick(r, PHR); return { q: `« ${p} » est une phrase :`, ok: t, faux: ["déclarative", "interrogative", "exclamative", "impérative"].filter((x) => x !== t), e: { déclarative: "Elle donne une information et finit par un point.", interrogative: "Elle pose une question et finit par un point d'interrogation.", exclamative: "Elle exprime un sentiment et finit par un point d'exclamation.", impérative: "Elle donne un ordre ou un conseil." }[t] }; });
  add(Fr, TP, (r) => { const t = pick(r, ["déclarative", "interrogative", "exclamative", "impérative"]), ok = pick(r, PHR.filter((x) => x[1] === t))[0];
    return { q: `Quelle phrase est ${t} ?`, ok, faux: ["déclarative", "interrogative", "exclamative", "impérative"].filter((x) => x !== t).map((u) => pick(r, PHR.filter((x) => x[1] === u))[0]), e: `${ok} : phrase ${t}.` }; });
  add(Fr, TP, (r) => { const [p, t] = pick(r, PHR.filter((x) => x[1] !== "impérative")), base = p.slice(0, -1).trim(), ok = { déclarative: ".", interrogative: "?", exclamative: "!" }[t];
    return { q: `Quel signe termine la phrase : « ${base} … » ?`, ok: ok === "." ? "un point (.)" : ok === "?" ? "un point d'interrogation (?)" : "un point d'exclamation (!)", faux: ["un point (.)", "un point d'interrogation (?)", "un point d'exclamation (!)", "une virgule (,)"].filter((x) => !x.includes(`(${ok})`)), e: `C'est une phrase ${t}.` }; });
  add(Fr, TP, (r) => { const [ok, d] = pick(r, [["Tu viens avec nous ?", "Tu viens avec nous."], ["Viens-tu avec nous ?", "Tu viens avec nous."], ["Est-ce que Fatou dort ?", "Fatou dort."], ["Pourquoi le chien aboie-t-il ?", "Le chien aboie."]]);
    return { q: `Quelle phrase transforme « ${d} » en question ?`, ok, faux: [d, d.replace(".", " !"), "Viens avec nous !"].filter((x) => x !== ok), e: "Une phrase interrogative pose une question : elle se termine par « ? »." }; });

  const SV = "Sujet, verbe et compléments";
  const SVP = [["Le chat", "boit", "du lait"], ["Les enfants", "jouent", "dans la cour"], ["Ma grand-mère", "prépare", "le repas"], ["Le pêcheur", "répare", "son filet"], ["Awa", "lit", "un livre"], ["Les oiseaux", "chantent", "le matin"], ["Mon père", "conduit", "le car"], ["La maîtresse", "écrit", "au tableau"], ["Le boulanger", "vend", "du pain"], ["Les élèves", "plantent", "des arbres"]];
  add(Fr, SV, (r) => { const [s, v, c] = pick(r, SVP); return { q: `Dans « ${s} ${v} ${c}. », quel est le sujet ?`, ok: s, faux: [v, c, `${v} ${c}`], e: `On demande « Qui est-ce qui ${v} ? » : ${s}.` }; });
  add(Fr, SV, (r) => { const [s, v, c] = pick(r, SVP); return { q: `Dans « ${s} ${v} ${c}. », quel est le verbe ?`, ok: v, faux: [s, c, s.split(" ").pop()], e: `Le verbe change avec le temps : hier, ${s.toLowerCase()} … ; le verbe est « ${v} ».` }; });
  add(Fr, SV, (r) => { const [s, v, c] = pick(r, SVP); return { q: `Dans « ${s} ${v} ${c}. », quel groupe est le complément ?`, ok: c, faux: [s, v, `${s} ${v}`], e: `« ${c} » complète le verbe « ${v} ».` }; });
  add(Fr, SV, (r) => { const [s, v] = pick(r, SVP), pl = /^(Les|Mes)/.test(s); return { q: `« ${s} » est un sujet au :`, ok: pl ? "pluriel" : "singulier", faux: [pl ? "singulier" : "pluriel", "féminin seulement", "verbe"], e: `« ${s} » : ${pl ? "plusieurs" : "un seul"}, donc ${pl ? "pluriel" : "singulier"} ; le verbe « ${v} » s'accorde.` }; });

  const PR = "Les pronoms personnels";
  const PRO = [["Les enfants", "ils"], ["Mes sœurs", "elles"], ["Le maître", "il"], ["La voiture", "elle"], ["Awa et moi", "nous"], ["Toi et ton frère", "vous"], ["Moussa", "il"], ["Fatou et Khady", "elles"], ["Le lion et la lionne", "ils"], ["Les filles", "elles"]];
  add(Fr, PR, (r) => { const [g, p] = pick(r, PRO); return { q: `Quel pronom peut remplacer « ${g} » ?`, ok: p, faux: autres(r, ["il", "elle", "ils", "elles", "nous", "vous"], p), e: `« ${g} » → ${p}.` }; });
  add(Fr, PR, (r) => { const [p, v] = pick(r, [["je", "chante"], ["tu", "chantes"], ["il", "chante"], ["nous", "chantons"], ["vous", "chantez"], ["ils", "chantent"]]); return { q: `Complète : … ${v} une chanson.`, ok: p === "il" ? "il" : p, faux: autres(r, ["je", "tu", "nous", "vous", "ils"].filter((x) => !(v === "chante" && ["je", "il"].includes(x))), p), e: `« ${v} » va avec « ${p} ».` }; });
  add(Fr, PR, (r) => { const [p, ok] = pick(r, [["je", "1re personne du singulier"], ["tu", "2e personne du singulier"], ["il", "3e personne du singulier"], ["nous", "1re personne du pluriel"], ["vous", "2e personne du pluriel"], ["elles", "3e personne du pluriel"]]);
    return { q: `« ${p} » est le pronom de la :`, ok, faux: autres(r, ["1re personne du singulier", "2e personne du singulier", "3e personne du singulier", "1re personne du pluriel", "2e personne du pluriel", "3e personne du pluriel"], ok), e: `${p} : ${ok}.` }; });
  add(Fr, PR, (r) => { const [s, p, v] = pick(r, [["Les pêcheurs partent en mer.", "Ils", "partent en mer."], ["Ma mère vend des légumes.", "Elle", "vend des légumes."], ["Mon ami et moi jouons.", "Nous", "jouons."], ["Les poules picorent.", "Elles", "picorent."], ["Le car arrive.", "Il", "arrive."]]);
    return { q: `Remplace le sujet par un pronom : « ${s} »`, ok: `${p} ${v}`, faux: autres(r, ["Il", "Elle", "Ils", "Elles", "Nous"].filter((x) => x !== p).map((x) => `${x} ${v}`), `${p} ${v}`), e: `Le sujet devient « ${p.toLowerCase()} ».` }; });

  const LC = "Lire et comprendre un texte";
  const TXT = [
    ["Ce matin, Awa va au marché de Tilène avec sa mère. Elles achètent du poisson et des légumes. Sur le chemin du retour, il commence à pleuvoir.", [["Qui va au marché ?", "Awa et sa mère", ["Awa et son père", "Le marchand", "Awa seule"]], ["Où vont-elles ?", "au marché de Tilène", ["à l'école", "à la plage", "chez la voisine"]], ["Quand cela se passe-t-il ?", "ce matin", ["ce soir", "hier", "la nuit"]], ["Que se passe-t-il au retour ?", "il pleut", ["il fait nuit", "elles se perdent", "le car tombe en panne"]]]],
    ["Le vieux pêcheur Ndiaga répare son filet sous le baobab. Demain, à l'aube, il partira en mer avec son fils Modou. Ils espèrent ramener beaucoup de sardinelles.", [["Que fait Ndiaga ?", "il répare son filet", ["il vend du poisson", "il dort", "il construit une pirogue"]], ["Avec qui partira-t-il ?", "avec son fils Modou", ["avec sa femme", "seul", "avec son voisin"]], ["Quand partira-t-il ?", "demain à l'aube", ["ce soir", "dans une semaine", "à midi"]], ["Que veulent-ils pêcher ?", "des sardinelles", ["des crevettes", "des requins", "des huîtres"]]]],
    ["À la récréation, Lamine tombe et se blesse au genou. La maîtresse nettoie la plaie et met un pansement. Lamine sourit : il n'a presque plus mal.", [["Qui se blesse ?", "Lamine", ["la maîtresse", "un camarade", "le directeur"]], ["Où est-il blessé ?", "au genou", ["à la main", "à la tête", "au pied"]], ["Qui le soigne ?", "la maîtresse", ["sa mère", "le docteur", "un ami"]], ["Comment se sent-il à la fin ?", "il va mieux", ["il pleure encore", "il a très mal", "il est fâché"]]]],
    ["Pendant l'hivernage, Binta aide son grand-père dans le champ de mil. Ils sèment les graines après la première pluie. Trois mois plus tard, ils feront la récolte.", [["Quand Binta aide-t-elle son grand-père ?", "pendant l'hivernage", ["pendant les vacances de Noël", "en saison sèche", "la nuit"]], ["Que cultivent-ils ?", "du mil", ["du riz", "des tomates", "du coton"]], ["Quand sèment-ils ?", "après la première pluie", ["avant la pluie", "en décembre", "le jour de la récolte"]], ["Dans combien de temps feront-ils la récolte ?", "trois mois", ["une semaine", "un an", "deux jours"]]]],
    ["Le car rapide part de la gare à huit heures. Il est plein : il y a des élèves, des commerçantes et un vieil homme avec une canne. Le chauffeur roule prudemment.", [["À quelle heure part le car ?", "à huit heures", ["à midi", "à six heures", "à dix heures"]], ["D'où part-il ?", "de la gare", ["du marché", "de l'école", "du port"]], ["Qui est dans le car ?", "des élèves, des commerçantes et un vieil homme", ["seulement des élèves", "personne", "des touristes seulement"]], ["Comment roule le chauffeur ?", "prudemment", ["très vite", "sans regarder", "en klaxonnant sans arrêt"]]]],
    ["Khady a planté un manguier devant la maison. Chaque soir, elle l'arrose avec l'eau du puits. Son petit frère l'aide à retirer les mauvaises herbes.", [["Qu'a planté Khady ?", "un manguier", ["un baobab", "des fleurs", "un citronnier"]], ["Où l'a-t-elle planté ?", "devant la maison", ["à l'école", "au marché", "dans la forêt"]], ["D'où vient l'eau ?", "du puits", ["du robinet", "de la mer", "de la pluie seulement"]], ["Qui l'aide ?", "son petit frère", ["sa mère", "son voisin", "personne"]]]],
  ];
  add(Fr, LC, (r) => { const [t, qs] = pick(r, TXT), [q, ok, f] = pick(r, qs); return { q: `Lis : « ${t} » ${q}`, ok, faux: f, e: "La réponse se trouve dans le texte : relis la phrase qui en parle." }; });
  add(Fr, LC, (r) => { const [t] = pick(r, TXT), titres = { 0: "Au marché", 1: "Le vieux pêcheur", 2: "Une chute à la récréation", 3: "Au champ de mil", 4: "Le car rapide", 5: "Le manguier de Khady" }, i = TXT.findIndex((x) => x[0] === t), ok = titres[i];
    return { q: `Lis : « ${t} » Quel est le meilleur titre ?`, ok, faux: autres(r, Object.values(titres), ok), e: "Le titre résume l'idée principale du texte." }; });

  const EC = "Écrire : des phrases et un petit texte";
  const ORD = [["le", "chat", "dort", "sur", "la", "natte"], ["les", "élèves", "chantent", "l'hymne", "national"], ["ma", "sœur", "lave", "les", "assiettes"], ["le", "berger", "garde", "ses", "moutons"], ["nous", "mangeons", "du", "riz", "au", "poisson"]];
  const phr = (ws) => ws[0][0].toUpperCase() + ws[0].slice(1) + " " + ws.slice(1).join(" ") + ".";
  add(Fr, EC, (r) => { const ws = pick(r, ORD), ok = phr(ws), m = ws.slice().sort((a, b) => a.localeCompare(b, "fr")); return { q: `Remets les mots dans l'ordre : ${m.join(" / ")}`, ok, faux: [phr([ws[1], ws[0], ...ws.slice(2)]), phr(ws.slice().reverse()), phr([...ws.slice(2), ws[0], ws[1]])], e: "Une phrase commence par une majuscule, suit l'ordre sujet, verbe, complément, et finit par un point." }; });
  add(Fr, EC, (r) => { const ws = pick(r, ORD), ok = phr(ws), s = ws.join(" "); return { q: "Quelle phrase est bien écrite ?", ok, faux: [s + ".", phr(ws).slice(0, -1), s[0].toUpperCase() + s.slice(1) + ","], e: "Majuscule au début, point à la fin." }; });
  add(Fr, EC, (r) => { const [a, b, ok] = pick(r, [["Il pleut", "nous restons à la maison", "donc"], ["Je voulais sortir", "il pleuvait", "mais"], ["Awa prend son sac", "elle part à l'école", "puis"], ["J'ai faim", "je n'ai pas encore mangé", "car"], ["Moussa lit", "son frère dessine", "et"]]);
    return { q: `Complète avec le bon mot : « ${a}, … ${b}. »`, ok, faux: autres(r, ["donc", "mais", "puis", "car", "et"], ok), e: `« ${ok} » relie bien les deux idées.` }; });
  add(Fr, EC, (r) => { const [d, ok] = pick(r, [["la maison", "La grande maison blanche"], ["un chien", "Un petit chien noir"], ["le marché", "Le marché animé"], ["une fille", "Une fille souriante"]]);
    return { q: `Quel groupe enrichit le mieux « ${d} » avec des adjectifs ?`, ok, faux: [d[0].toUpperCase() + d.slice(1), `${d} et ${d}`, `Le ${d}`], e: "On ajoute des adjectifs pour mieux décrire." }; });

  // compléments pour les chapitres qui n'avaient qu'un modèle
  add(Fr, "Les accords", (r) => { const [n, a] = pick(r, [["fille", "grande"], ["voiture", "rouge"], ["maison", "belle"], ["robe", "neuve"], ["chèvre", "noire"]]), [n2, a2] = pick(r, [["garçon", "grand"], ["vélo", "rouge"], ["arbre", "beau"], ["pantalon", "neuf"], ["bouc", "noir"]]);
    const k = pick(r, [0, 1]), ok = k ? `des ${n}s ${a}s` : `des ${n2}s ${a2 === "beau" ? "beaux" : a2 + "s"}`;
    return { q: `Mets au pluriel : « ${k ? `une ${n} ${a}` : `un ${n2} ${a2}`} »`, ok, faux: k ? [`des ${n}s ${a}`, `des ${n} ${a}s`, `des ${n} ${a}`] : [`des ${n2}s ${a2}`, `des ${n2} ${a2}s`, `des ${n2} ${a2}`], e: "Au pluriel, le nom ET l'adjectif prennent la marque du pluriel (souvent -s, parfois -x)." }; });
  add(Fr, "Le présent des verbes", (r) => { const v = pick(r, ["parler", "jouer", "chanter", "danser", "marcher", "regarder", "laver", "porter"]), [p, t] = pick(r, [["je", "e"], ["tu", "es"], ["il", "e"], ["nous", "ons"], ["vous", "ez"], ["ils", "ent"]]), b = v.slice(0, -2), ok = b + t;
    return { q: `Conjugue « ${v} » au présent avec « ${p} » :`, ok: `${p} ${ok}`, faux: autres(r, ["e", "es", "ons", "ez", "ent"].filter((x) => x !== t).map((x) => `${p} ${b}${x}`), `${p} ${ok}`), e: `Verbe en -er au présent : -e, -es, -e, -ons, -ez, -ent.` }; });
  add(Fr, "L'imparfait et le futur simple", (r) => { const v = pick(r, ["jouer", "chanter", "manger", "parler", "danser"]), tps = pick(r, ["imparfait", "futur"]), [p, i, f] = pick(r, [["je", "ais", "ai"], ["tu", "ais", "as"], ["il", "ait", "a"], ["nous", "ions", "ons"], ["vous", "iez", "ez"], ["ils", "aient", "ont"]]);
    const b = v === "manger" && tps === "imparfait" && !["nous", "vous"].includes(p) ? "mange" : v.slice(0, -2), ok = tps === "imparfait" ? `${p} ${b}${i}` : `${p} ${v}${f}`;
    return { q: `« ${v} » à l'${tps === "futur" ? "futur simple" : "imparfait"} avec « ${p} » :`, ok, faux: autres(r, [`${p} ${v}${f}`, `${p} ${b}${i}`, `${p} ${v.slice(0, -2)}${i}`, `${p} ${v.slice(0, -2)}e`, `${p} ${v}${i}`], ok), e: tps === "imparfait" ? "Imparfait : -ais, -ais, -ait, -ions, -iez, -aient." : "Futur : infinitif + -ai, -as, -a, -ons, -ez, -ont." }; });
  add(Fr, "Le passé composé", (r) => { const [v, pp] = pick(r, [["manger", "mangé"], ["finir", "fini"], ["prendre", "pris"], ["faire", "fait"], ["voir", "vu"], ["écrire", "écrit"]]), [p, a] = pick(r, [["j'", "ai"], ["tu", "as"], ["il", "a"], ["nous", "avons"], ["vous", "avez"], ["ils", "ont"]]), ok = `${p}${p.endsWith("'") ? "" : " "}${a} ${pp}`;
    return { q: `« ${v} » au passé composé avec « ${p.replace("'", "e")} » :`, ok, faux: autres(r, [`${p}${p.endsWith("'") ? "" : " "}${a} ${v}`, `${p}${p.endsWith("'") ? "" : " "}${a} ${pp}s`, `${p}${p.endsWith("'") ? "" : " "}suis ${pp}`, `${p}${p.endsWith("'") ? "" : " "}avait ${pp}`], ok), e: `Passé composé = avoir au présent + participe passé (${pp}).` }; });
  add(Fr, "Les homophones grammaticaux", (r) => { const [a, ok, f] = pick(r, [["Awa … une poupée.", "a", ["à", "as", "ah"]], ["Il va … l'école.", "à", ["a", "as", "ha"]], ["Le chat … le chien jouent.", "et", ["est", "es", "ait"]], ["Le ciel … bleu.", "est", ["et", "es", "ai"]], ["Moussa range … cartable.", "son", ["sont", "sons", "sa"]], ["Les enfants … contents.", "sont", ["son", "sons", "sonts"]], ["… mange du riz ce soir.", "On", ["Ont", "Om", "Ons"]], ["Ils … faim.", "ont", ["on", "onts", "om"]]]);
    return { q: `Complète : « ${a} »`, ok, faux: f, e: { a: "On peut dire « avait » : c'est le verbe avoir.", à: "On ne peut pas dire « avait » : c'est la préposition « à ».", et: "On peut dire « et puis ».", est: "On peut dire « était ».", son: "On peut dire « mon » : c'est un déterminant.", sont: "On peut dire « étaient ».", On: "On peut dire « il » : c'est un pronom.", ont: "On peut dire « avaient »." }[ok] }; });
})();
