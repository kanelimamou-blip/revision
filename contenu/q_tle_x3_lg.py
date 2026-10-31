# QCM de terminale L et G, volume ×3 : exercices calculés (maths L, maths G).
import math
from fractions import Fraction as Fr
from q_tle_x3_calc import calc, n, poly, stat
from q_g_x3 import f as F, nb

L = {}
L["Fonctions : dérivée et variations"] = calc(
    [(f"Dérivée de f(x) = {poly(a, b, c)} :", f"f'(x) = {poly(2 * a, b)}", f"f'(x) = {poly(a, b)}", f"f'(x) = {poly(2 * a, b, c)}", f"f'(x) = {poly(2 * a, 0)}" if b else f"f'(x) = {poly(a, 0)}", "(ax² + bx + c)' = 2ax + b.") for a, b, c in [(3, -2, 5), (1, 4, -7), (-2, 6, 1), (5, 0, 3), (4, -8, 2), (-1, 3, 0)]]
    + [(f"f(x) = {poly(a, b, c)}. f'({x}) =", n(2 * a * x + b), n(a * x * x + b * x + c), n(2 * a + b), n(a * x + b), f"f'(x) = {poly(2 * a, b)}.") for a, b, c, x in [(2, 1, 0, 3), (1, -6, 4, 2), (-3, 2, 1, 1), (4, 0, -5, -1), (1, 5, 2, 0)]]
    + [(f"f(x) = {poly(a, b, c)}. f est croissante sur :", f"[{n(Fr(-b, 2 * a))} ; +∞[" if a > 0 else f"]−∞ ; {n(Fr(-b, 2 * a))}]", f"]−∞ ; {n(Fr(-b, 2 * a))}]" if a > 0 else f"[{n(Fr(-b, 2 * a))} ; +∞[", "ℝ", f"[{n(Fr(b, 2 * a))} ; +∞[",
        f"f'(x) = {poly(2 * a, b)} s'annule en {n(Fr(-b, 2 * a))}.") for a, b, c in [(1, -4, 3), (-1, 6, 0), (2, 8, 1), (-3, -6, 2), (1, 2, -8)]]
    + [(f"f(x) = {poly(a, b, c)}. Valeur de l'extremum :", n(c - Fr(b * b, 4 * a)), n(c), n(Fr(-b, 2 * a)), n(c + Fr(b * b, 4 * a)), "On calcule f(−b/(2a)).") for a, b, c in [(1, -4, 3), (-1, 6, 0), (2, 8, 1), (1, -10, 30)]]
    + [(f"f(x) = {poly(a, b, c)}. Équation de la tangente en x = {x} :", f"y = {poly(2 * a * x + b, c - a * x * x)}", f"y = {poly(2 * a * x + b, a * x * x + b * x + c)}", f"y = {poly(a * x + b, c)}", f"y = {poly(2 * a, b)}", "y = f'(x₀)(x − x₀) + f(x₀).") for a, b, c, x in [(1, 0, 2, 1), (1, -2, 0, 3), (2, 1, -1, 1), (-1, 4, 0, 1)]]
    + [(f"Le signe de f'(x) = {poly(a, b)} est positif pour :", f"x > {n(Fr(-b, a))}" if a > 0 else f"x < {n(Fr(-b, a))}", f"x < {n(Fr(-b, a))}" if a > 0 else f"x > {n(Fr(-b, a))}", f"x > {n(Fr(b, a))}", "tout réel x", "Signe d'une fonction affine.") for a, b in [(2, -6), (-3, 9), (5, 10), (-1, -4), (4, 2)]]
)
L["Suites arithmétiques et géométriques"] = calc(
    [(f"Suite arithmétique : u₀ = {u}, raison {r}. u₁₀ =", n(u + 10 * r), n(u + 9 * r), n(u * r ** 10) if abs(r) < 4 else n(u + 11 * r), n(10 * r), "uₙ = u₀ + nr.") for u, r in [(4, 3), (20, -2), (1, 7), (100, -5), (0, 6)]]
    + [(f"Suite géométrique : u₀ = {u}, raison {q}. u₄ =", n(u * q ** 4), n(u * q ** 3), n(u + 4 * q), n(u * 4 * q), "uₙ = u₀qⁿ.") for u, q in [(3, 2), (1, 3), (5, 2), (2, 5), (64, Fr(1, 2))]]
    + [(f"Suite arithmétique : u₁ = {a} et u₅ = {b}. La raison est :", n(Fr(b - a, 4), 4), n(Fr(b - a, 5)), n(b - a), n(Fr(b, a)), "u₅ = u₁ + 4r.") for a, b in [(3, 23), (10, -2), (7, 15), (1, 3)]]
    + [(f"Suite géométrique : u₀ = {a} et u₂ = {a * q * q} (raison positive). La raison est :", n(q), n(q * q), n(Fr(q, 2)), n(a * q), "u₂ = u₀q².") for a, q in [(2, 3), (5, 2), (1, 4), (3, 5)]]
    + [(f"Somme 1 + 2 + 3 + … + {k} =", n(k * (k + 1) // 2), n(k * k), n(k * (k - 1) // 2), n(k * (k + 1)), "n(n + 1)/2.") for k in [10, 20, 50, 100]]
    + [(f"Somme 1 + {q} + {q}² + … + {q}^{k} =", n((q ** (k + 1) - 1) // (q - 1)), n(q ** k), n((q ** k - 1) // (q - 1)), n(q ** (k + 1)), "(qⁿ⁺¹ − 1)/(q − 1).") for q, k in [(2, 5), (3, 4), (2, 9)]]
    + [(f"Une population de {p} habitants augmente de {t} % par an. Après 1 an :", nb(p * (1 + t / 100)), f"{round(p * t / 100):,}".replace(",", " "), f"{p + t:,}".replace(",", " "), f"{round(p * (1 + t / 10)):,}".replace(",", " "), f"Multiplier par 1 + {t}/100.") for p, t in [(10000, 3), (25000, 2), (8000, 5)]]
)
L["Logarithme et exponentielle"] = calc(
    [(f"Simplifier ln({a}) + ln({b}) − ln({c}) :", f"ln {n(Fr(a * b, c))}", f"ln {a + b - c}", f"ln {a * b * c}", f"ln {n(Fr(a, b * c))}", "Propriétés algébriques du logarithme.") for a, b, c in [(4, 6, 3), (10, 5, 2), (9, 2, 6), (8, 3, 4)]]
    + [(f"3 ln {a} est égal à :", f"ln {a ** 3}", f"ln {3 * a}", f"ln {a + 3}", f"(ln {a})³", "n ln a = ln aⁿ.") for a in [2, 5, 10]]
    + [(f"Résoudre e^x = e^{k} :", f"x = {k}", f"x = e^{k}", f"x = ln {k}", "pas de solution", "exp est strictement croissante donc injective.") for k in [3, 7]]
    + [(f"Résoudre ln({a}x) = ln {b} :", f"x = {n(Fr(b, a))}", f"x = {b - a}", f"x = {a * b}", f"x = {n(Fr(a, b))}", f"{a}x = {b}.") for a, b in [(2, 10), (3, 12), (5, 4)]]
    + [(f"Valeur approchée de ln {k} (à 0,01 près) :", n(round(math.log(k), 2)), n(round(math.log10(k), 2)), n(round(math.exp(k) / 100, 2)), n(round(math.log(k) + 1, 2)), "À la calculatrice : touche ln.") for k in [2, 3, 5, 10]]
    + [(f"Valeur approchée de e^{k} (à 0,1 près) :", n(round(math.exp(k), 1)), n(round(k * math.e, 1)), n(round(math.log(k), 1)) if k > 1 else "0", n(round(math.exp(k) + 1, 1)), "À la calculatrice : touche e^x.") for k in [1, 2, 3]]
    + [(f"Résoudre e^x > {k} :", f"x > ln {k}", f"x < ln {k}", f"x > e^{k}", f"x > {k}", "On applique ln, fonction croissante.") for k in [2, 5, 10]]
    + [(f"Résoudre ln x < {k} :", f"0 < x < e^{k}", f"x < e^{k}", f"x > e^{k}", f"0 < x < {k}", "Ne pas oublier x > 0.") for k in [1, 2, 3]]
    + [(f"Dérivée de f(x) = {a} ln x :", f"{a}/x", f"{a} ln x", f"1/({a}x)", f"{a}x", "(ln x)' = 1/x.") for a in [3, 5]]
    + [(f"Dérivée de f(x) = {a}e^x + {b}x :", f"{a}e^x + {b}", f"{a}e^x", f"{a}xe^x + {b}", f"e^x + {b}", "(e^x)' = e^x.") for a, b in [(2, 3), (4, 7)]]
)
L["Dénombrement et probabilités"] = calc(
    [(f"Nombre de façons de choisir un comité de {k} élèves dans une classe de {nn} :", n(math.comb(nn, k)), n(math.perm(nn, k)), n(nn * k), n(nn ** k), "Combinaisons : l'ordre ne compte pas.") for nn, k in [(30, 2), (25, 3), (12, 4), (40, 2)]]
    + [(f"Nombre de façons d'élire un président, un secrétaire et un trésorier parmi {nn} membres :", n(math.perm(nn, 3)), n(math.comb(nn, 3)), n(nn ** 3), n(3 * nn), "Arrangements : l'ordre (les postes) compte.") for nn in [10, 15, 20]]
    + [(f"Nombre de codes de {k} chiffres (0 à 9, répétition permise) :", n(10 ** k), n(math.perm(10, k)), n(math.comb(10, k)), n(10 * k), "p-listes : 10ᵏ.") for k in [3, 4, 6]]
    + [(f"{k}! =", n(math.factorial(k)), n(k * k), n(math.factorial(k - 1)), n(k * (k + 1) // 2), "Produit 1 × 2 × … × n.") for k in [4, 5, 6, 7]]
    + [(f"Une urne contient {r} boules rouges et {b} noires. On en tire une au hasard. P(rouge) =", n(Fr(r, r + b)), n(Fr(b, r + b)), n(Fr(r, b)), n(Fr(1, r + b)), "Cas favorables / cas possibles.") for r, b in [(3, 7), (5, 3), (4, 8), (6, 9)]]
    + [(f"Urne de {r} rouges et {b} noires. On tire 2 boules simultanément. P(2 rouges) =", n(Fr(math.comb(r, 2), math.comb(r + b, 2))), n(Fr(r, r + b) ** 2), n(Fr(2 * r, r + b)), n(Fr(math.comb(b, 2), math.comb(r + b, 2))), "C(r, 2) / C(r + b, 2).") for r, b in [(3, 2), (4, 6), (5, 5)]]
    + [(f"P(A) = {n(a)}. P(non A) =", n(round(1 - a, 2)), n(a), "1", n(round(a / 2, 3)), "P(Ā) = 1 − P(A).") for a in [0.35, 0.65, 0.12]]
    + [(f"A et B incompatibles, P(A) = {n(a)}, P(B) = {n(b)}. P(A ∪ B) =", n(round(a + b, 2)), n(round(a * b, 3)), n(round(a + b - a * b, 3)), "1", "Incompatibles : P(A ∪ B) = P(A) + P(B).") for a, b in [(0.2, 0.5), (0.35, 0.4), (0.1, 0.25)]]
)
L["Statistiques à deux variables"] = calc(
    [(f"Série : x = {', '.join(map(str, xs))} ; y = {', '.join(map(str, ys))}. x̄ =", n(round(stat(xs, ys)[0], 2)), n(round(stat(xs, ys)[1], 2)), n(sum(xs)), n(max(xs) - min(xs)), "Moyenne des xᵢ.") for xs, ys in [([2, 4, 6, 8, 10], [5, 9, 12, 16, 18]), ([1, 2, 3, 4, 5, 6], [12, 15, 19, 22, 24, 30]), ([10, 20, 30], [3, 7, 8])]]
    + [(f"Série : x = {', '.join(map(str, xs))} ; y = {', '.join(map(str, ys))}. ȳ =", n(round(stat(xs, ys)[1], 2)), n(round(stat(xs, ys)[0], 2)), n(sum(ys)), n(max(ys)), "Moyenne des yᵢ.") for xs, ys in [([2, 4, 6, 8, 10], [5, 9, 12, 16, 18]), ([1, 2, 3, 4, 5, 6], [12, 15, 19, 22, 24, 30]), ([10, 20, 30], [3, 7, 8])]]
    + [(f"Série : x = {', '.join(map(str, xs))} ; y = {', '.join(map(str, ys))}. V(x) =", n(round(stat(xs, ys)[3], 2)), n(round(math.sqrt(stat(xs, ys)[3]), 2)), n(round(stat(xs, ys)[2], 2)), n(round(stat(xs, ys)[3] * len(xs), 2)), "Moyenne des carrés des écarts.") for xs, ys in [([2, 4, 6, 8, 10], [5, 9, 12, 16, 18]), ([1, 2, 3, 4, 5, 6], [12, 15, 19, 22, 24, 30]), ([10, 20, 30], [3, 7, 8])]]
    + [(f"Droite d'ajustement y = {n(a)}x + {n(b)}. Estimation de y pour x = {x} :", n(round(a * x + b, 2)), n(round(a + b * x, 2)), n(round(a * x, 2)), n(round((x - b) / a, 2)), "On remplace x dans l'équation.") for a, b, x in [(2.5, 3, 12), (1.8, 10, 20), (0.6, 4, 15), (3, -2, 9)]]
    + [(f"Droite d'ajustement y = {n(a)}x + {n(b)}. Pour atteindre y = {y}, il faut x ≈", n(round((y - b) / a, 2)), n(round(a * y + b, 2)), n(round(y / a, 2)), n(round((y + b) / a, 2)), "On résout ax + b = y.") for a, b, y in [(2.5, 3, 53), (1.8, 10, 46), (4, 0, 10)]]
    + [(f"Série : x = {', '.join(map(str, xs))} ; y = {', '.join(map(str, ys))}. Méthode de Mayer : point moyen du premier groupe :", f"G₁({n(sum(xs[:len(xs) // 2]) / (len(xs) // 2))} ; {n(sum(ys[:len(ys) // 2]) / (len(ys) // 2))})", f"G₁({n(sum(xs) / len(xs))} ; {n(sum(ys) / len(ys))})", f"G₁({xs[0]} ; {ys[0]})", f"G₁({n(sum(ys[:len(ys) // 2]) / (len(ys) // 2))} ; {n(sum(xs[:len(xs) // 2]) / (len(xs) // 2))})",
        "On partage la série en deux groupes de même effectif.") for xs, ys in [([1, 2, 3, 4], [10, 14, 17, 21]), ([2, 4, 6, 8, 10, 12], [3, 4, 6, 7, 9, 10]), ([5, 10, 15, 20], [40, 34, 30, 22])]]
    + [(f"Mayer : G₁({a} ; {b}) et G₂({c} ; {d}). Coefficient directeur de la droite :", n(round((d - b) / (c - a), 2)), n(round((c - a) / (d - b), 2)), n(d - b), n(round(d / c, 2)), "(y₂ − y₁)/(x₂ − x₁).") for a, b, c, d in [(1.5, 12, 3.5, 19), (4, 4.33, 10, 8.67), (7.5, 37, 17.5, 26)]]
)
GG = {}
GG["Intérêts composés"] = calc(
    [(f"Capital de {F(c)} placé à {t} % par an, intérêts composés, pendant {k} ans. Valeur acquise :", F(c * (1 + t / 100) ** k), F(c * (1 + k * t / 100)), F(c * (1 + t / 100) ** (k - 1)), F(c * t / 100 * k), f"Cₙ = C₀(1 + i)ⁿ = {F(c)} × {n(1 + t / 100, 4)}^{k}.") for c, t, k in [(1000000, 5, 3), (500000, 4, 5), (2000000, 6, 2), (750000, 3, 4), (1500000, 8, 3), (300000, 10, 2)]]
    + [(f"Valeur acquise {F(v)} après {k} ans à {t} % composés. Capital placé :", F(v / (1 + t / 100) ** k), F(v * (1 + t / 100) ** k), F(v / (1 + k * t / 100)), F(v - v * t / 100 * k), "C₀ = Cₙ(1 + i)⁻ⁿ.") for v, t, k in [(1157625, 5, 3), (1210000, 10, 2), (2249728, 4, 3), (1124864, 4, 3)]]
    + [(f"{F(c)} placés à {t} % composés. Intérêts produits en {k} ans :", F(c * ((1 + t / 100) ** k - 1)), F(c * t / 100 * k), F(c * (1 + t / 100) ** k), F(c * t / 100), "I = Cₙ − C₀.") for c, t, k in [(1000000, 5, 2), (400000, 10, 3), (2500000, 6, 2)]]
    + [(f"Taux semestriel équivalent à un taux annuel de {t} % (intérêts composés) :", f"{n(round(((1 + t / 100) ** 0.5 - 1) * 100, 3), 3)} %", f"{n(t / 2)} %", f"{n(round(((1 + t / 100) ** 2 - 1) * 100, 2))} %", f"{n(t)} %", "(1 + iₛ)² = 1 + iₐ.") for t in [8, 10, 6]]
    + [(f"Un capital double en combien d'années à {t} % composés (arrondi à l'année supérieure) ?", f"{math.ceil(math.log(2) / math.log(1 + t / 100))} ans", f"{round(100 / t)} ans", f"{math.ceil(math.log(2) / math.log(1 + t / 100)) + 3} ans", f"{t} ans", "(1 + i)ⁿ ≥ 2 ⇔ n ≥ ln 2 / ln(1 + i).") for t in [5, 8, 12, 4]]
    + [(f"Valeur actuelle d'un effet de {F(v)} payable dans {k} ans au taux de {t} % composés :", F(v / (1 + t / 100) ** k), F(v * (1 - k * t / 100)), F(v * (1 + t / 100) ** k), F(v - v * t / 100), "Actualisation : V₀ = V(1 + i)⁻ⁿ.") for v, t, k in [(1000000, 5, 2), (5000000, 8, 3), (800000, 6, 1)]]
)
GG["Suites et annuités"] = calc(
    [(f"Annuités constantes de {F(a)} versées en fin d'année pendant {k} ans à {t} %. Valeur acquise :", F(a * ((1 + t / 100) ** k - 1) / (t / 100)), F(a * k), F(a * k * (1 + t / 100)), F(a * ((1 + t / 100) ** k)), "Vₙ = a[(1 + i)ⁿ − 1]/i.") for a, t, k in [(100000, 5, 4), (250000, 6, 5), (500000, 4, 3), (50000, 10, 6)]]
    + [(f"Annuités de {F(a)} pendant {k} ans à {t} %. Valeur actuelle (à l'origine) :", F(a * (1 - (1 + t / 100) ** -k) / (t / 100)), F(a * k), F(a * k / (1 + t / 100)), F(a * ((1 + t / 100) ** k - 1) / (t / 100)), "V₀ = a[1 − (1 + i)⁻ⁿ]/i.") for a, t, k in [(100000, 5, 4), (200000, 8, 3), (1000000, 6, 5)]]
    + [(f"Emprunt de {F(c)} remboursé par {k} annuités constantes au taux de {t} %. Annuité :", F(c * (t / 100) / (1 - (1 + t / 100) ** -k)), F(c / k), F(c / k * (1 + t / 100)), F(c * t / 100), "a = C × i / [1 − (1 + i)⁻ⁿ].") for c, t, k in [(1000000, 10, 2), (5000000, 8, 5), (2000000, 6, 4), (3000000, 5, 3)]]
    + [(f"Emprunt de {F(c)} à {t} %. Intérêt compris dans la première annuité :", F(c * t / 100), F(c * t / 100 / 2), F(c / 10), F(c * (1 + t / 100)), "I₁ = C × i.") for c, t in [(1000000, 10), (5000000, 8), (2000000, 6)]]
    + [(f"Une épargne de {F(a)} par mois augmente de {F(r)} chaque mois. Le {k}ᵉ versement vaut :", F(a + (k - 1) * r), F(a + k * r), F(a * k), F(a + (k - 2) * r), "Suite arithmétique : uₖ = u₁ + (k − 1)r.") for a, r, k in [(10000, 2000, 12), (25000, 5000, 6), (5000, 1000, 24)]]
    + [(f"Un loyer de {F(a)} augmente de {t} % par an. Loyer de la {k}ᵉ année :", F(a * (1 + t / 100) ** (k - 1)), F(a * (1 + t / 100) ** k), F(a * (1 + (k - 1) * t / 100)), F(a * k), "Suite géométrique de raison 1 + i.") for a, t, k in [(100000, 5, 4), (60000, 10, 3), (150000, 4, 5)]]
    + [(f"Emprunt de {F(c)} remboursé par amortissements constants sur {k} ans. Amortissement annuel :", F(c / k), F(c / (k + 1)), F(c * k / 10), F(c / k * 1.1), "A = C / n.") for c, k in [(6000000, 5), (1200000, 4), (900000, 3)]]
)
GG["Fonctions économiques : coût, recette, bénéfice"] = calc(
    [(f"Coût total C(q) = {poly(a, b, c)} (en milliers de F). Coût marginal Cm(q) =", poly(2 * a, b), poly(a, b), poly(2 * a, b, c), poly(2 * a, 0), "Cm = C'(q).") for a, b, c in [(2, 10, 500), (1, 40, 900), (3, 6, 200), (0.5, 20, 1000)]]
    + [(f"Prix de vente unitaire {p} F, coût C(q) = {poly(a, b, c)}. Bénéfice B(q) =", poly(-a, p - b, -c), poly(a, b - p, c), poly(-a, p + b, -c), poly(p - a, -b, -c), "B = R − C avec R = pq.") for p, a, b, c in [(100, 1, 20, 1200), (60, 2, 10, 200), (500, 5, 100, 3000)]]
    + [(f"B(q) = {poly(-a, b, -c)}. Le bénéfice est maximal pour q =", n(Fr(b, 2 * a)), n(Fr(b, a)), n(Fr(c, b)), n(b), "B'(q) = 0.") for a, b, c in [(1, 80, 1200), (2, 50, 200), (5, 400, 3000), (1, 30, 125)]]
    + [(f"Coût fixe {F(cf)}, coût variable unitaire {F(cv)}, prix unitaire {F(p)}. Seuil de rentabilité (quantité) :", f"{nb(math.ceil(cf / (p - cv)))} unités", f"{nb(math.ceil(cf / p))} unités", f"{nb(math.ceil(cf / cv))} unités", f"{nb(math.ceil((cf + cv) / p))} unités", "Q* = CF / (p − cv).") for cf, cv, p in [(600000, 2000, 5000), (1500000, 300, 800), (2400000, 1500, 3500)]]
    + [(f"C(q) = {poly(a, b, c)}. Coût moyen pour q = {q} :", n(round((a * q * q + b * q + c) / q, 2)), n(a * q * q + b * q + c), n(2 * a * q + b), n(round(c / q, 2)), "CM = C(q)/q.") for a, b, c, q in [(1, 10, 400, 20), (2, 5, 800, 10), (0.5, 30, 1250, 50)]]
    + [(f"Demande d(p) = {a} − {b}p. Recette pour p = {p} :", nb(p * (a - b * p)), nb(a - b * p), nb(p * a), nb(p * (a + b * p)), "R = p × d(p).") for a, b, p in [(1000, 20, 30), (500, 5, 40), (2000, 10, 100)]]
    + [(f"Demande d(p) = {a} − {b}p. Élasticité au prix p = {p} : e = −bp/d(p) ≈", n(round(-b * p / (a - b * p), 2)), n(round(b * p / (a - b * p), 2)), n(round(-b * (a - b * p) / p, 2)), n(-b), "e = d'(p) × p / d(p).") for a, b, p in [(1000, 20, 30), (500, 5, 40), (2000, 10, 100)]]
)
GG["Statistiques à deux variables"] = calc(
    [(f"Ventes (millions F) : année 1 → {ys[0]}, … (rang x = 1 à {len(ys)} : {', '.join(map(str, ys))}). Ventes moyennes :", n(round(sum(ys) / len(ys), 2)), n(sum(ys)), n(round((ys[0] + ys[-1]) / 2, 2)), n(max(ys)), "ȳ = somme / effectif.") for ys in [[12, 15, 17, 20, 23], [40, 42, 47, 51], [8, 9, 11, 14, 15, 17]]]
    + [(f"Rang x = 1 à {len(ys)}, ventes y = {', '.join(map(str, ys))}. Coefficient a de l'ajustement par moindres carrés :", n(round(stat(list(range(1, len(ys) + 1)), ys)[2] / stat(list(range(1, len(ys) + 1)), ys)[3], 2)), n(round(stat(list(range(1, len(ys) + 1)), ys)[2], 2)), n(round(stat(list(range(1, len(ys) + 1)), ys)[3], 2)), n(round(sum(ys) / len(ys), 2)),
        "a = cov(x, y)/V(x).") for ys in [[12, 15, 17, 20, 23], [40, 42, 47, 51], [8, 9, 11, 14, 15, 17]]]
    + [(f"Tendance y = {n(a)}x + {n(b)} (x = rang de l'année). Prévision pour l'année de rang {x} :", n(round(a * x + b, 2)), n(round(a * (x - 1) + b, 2)), n(round(a * x, 2)), n(round(b * x + a, 2)), "On remplace x par le rang.") for a, b, x in [(2.7, 9.3, 7), (3.8, 35.5, 6), (1.9, 5.9, 8), (5, 120, 10)]]
    + [(f"Coefficient de corrélation : cov = {c}, σx = {sx}, σy = {sy}. r =", n(round(c / (sx * sy), 3), 3), n(round(c / sx, 3), 3), n(round(sx * sy / c, 3), 3), n(round(c / (sx + sy), 3), 3), "r = cov / (σx σy).") for c, sx, sy in [(5.4, 1.5, 3.7), (12, 2, 6.5), (-8, 2.5, 3.4)]]
    + [(f"Prix x (F) : {', '.join(map(str, xs))} ; quantités y : {', '.join(map(str, ys))}. Point moyen :", f"G({n(round(sum(xs) / len(xs), 2))} ; {n(round(sum(ys) / len(ys), 2))})", f"G({n(round(sum(ys) / len(ys), 2))} ; {n(round(sum(xs) / len(xs), 2))})", f"G({n(sum(xs))} ; {n(sum(ys))})", f"G({xs[-1]} ; {ys[-1]})", "Moyennes des deux séries.") for xs, ys in [([100, 150, 200, 250], [80, 66, 50, 36]), ([500, 600, 700], [30, 25, 17]), ([50, 60, 70, 80, 90], [210, 190, 175, 150, 130])]]
    + [(f"Indice simple : prix {F(a)} en année de base, {F(b)} l'année suivante. Indice (base 100) :", n(round(b / a * 100, 1)), n(round(a / b * 100, 1)), n(round((b - a) / a * 100, 1)), n(b - a), "I = Pₜ/P₀ × 100.") for a, b in [(2000, 2300), (50000, 47500), (1200, 1500)]]
)
GG["Probabilités"] = calc(
    [(f"Dans une entreprise, {a} % des produits viennent de l'atelier A (défaut {da} %) et le reste de B (défaut {db} %). P(défaut) =", f"{n(round(a * da / 100 + (100 - a) * db / 100, 2))} %", f"{n(round((da + db) / 2, 2))} %", f"{n(round(a * da / 100, 2))} %", f"{n(da + db)} %", "Probabilités totales.") for a, da, db in [(60, 2, 5), (70, 1, 4), (40, 3, 1), (50, 6, 2)]]
    + [(f"Un client achète avec une probabilité {n(p)}. Sur {k} clients indépendants, nombre moyen d'achats :", n(round(k * p, 2)), n(round(p, 2)), n(round(k * p * (1 - p), 2)), n(k), "Espérance d'une binomiale : np.") for p, k in [(0.3, 50), (0.15, 200), (0.6, 40), (0.05, 400)]]
    + [(f"Jeu : on gagne {g} F avec la probabilité {n(p)}, sinon on perd {l} F. Espérance de gain :", f"{n(round(g * p - l * (1 - p), 2))} F", f"{n(round(g * p, 2))} F", f"{n(round(g - l, 2))} F", f"{n(round(g * p + l * (1 - p), 2))} F", "E = Σ gᵢ pᵢ.") for g, p, l in [(1000, 0.2, 300), (5000, 0.1, 500), (200, 0.5, 100)]]
    + [(f"Sur {t} salariés, {a} parlent anglais, {b} wolof et {c} les deux. Probabilité qu'un salarié parle anglais ou wolof :", n(Fr(a + b - c, t)), n(Fr(a + b, t)), n(Fr(c, t)), n(Fr(a, t)), "P(A ∪ B) = P(A) + P(B) − P(A ∩ B).") for t, a, b, c in [(100, 40, 70, 25), (50, 20, 30, 10), (80, 30, 50, 20)]]
    + [(f"P(A) = {n(a)}, P(B) = {n(b)}, A et B indépendants. P(A ∩ B) =", n(round(a * b, 4), 4), n(round(a + b, 2)), n(round(a + b - a * b, 4), 4), n(round(a / b, 2)), "Indépendance : P(A ∩ B) = P(A)P(B).") for a, b in [(0.4, 0.3), (0.5, 0.8), (0.25, 0.6)]]
    + [(f"X suit B({k} ; {n(p)}). P(X = 0) =", n(round((1 - p) ** k, 4), 4), n(round(p ** k, 4), 4), "0", n(round(1 - (1 - p) ** k, 4), 4), "P(X = 0) = (1 − p)ⁿ.") for k, p in [(3, 0.2), (5, 0.1), (4, 0.5)]]
    + [(f"X suit B({k} ; {n(p)}). P(X ≥ 1) =", n(round(1 - (1 - p) ** k, 4), 4), n(round((1 - p) ** k, 4), 4), n(round(k * p, 4), 4), "1", "Événement contraire de X = 0.") for k, p in [(3, 0.2), (5, 0.1), (4, 0.5)]]
)
QCM_TLE_X3_LG = {"tle-maths-l": L, "tle-maths-g": GG}
