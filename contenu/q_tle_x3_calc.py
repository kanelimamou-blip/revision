# QCM de terminale, volume ×3 : exercices de calcul (maths S, maths L, maths G, physique-chimie).
# Chaque modèle est décliné sur plusieurs jeux de données fixes : la bonne réponse et les distracteurs sont calculés.
import math
from fractions import Fraction as Fr
import re
from q_g_x3 import calc as _calc, f as fcfa, nb


def fx(t):
    """Typographie : moins typographique, puissances négatives entre parenthèses, 1i -> i, e^1 -> e."""
    t = re.sub(r"(\d)\.(\d)", r"\1,\2", t)
    t = re.sub(r"([+−] )1t\b", r"\1t", t)
    t = re.sub(r"\^-(\d+)", r"^(−\1)", t)
    t = re.sub(r"(?<![\w)])-(?=\d)", "−", t)
    t = re.sub(r"(?<![\d,/])\b1i\b", "i", t)
    t = re.sub(r"e\^1(?![\d,])", "e", t)
    t = re.sub(r"(?<![\w(])(\d+/\d+)([a-zuxyz])", r"(\1)\2", t)
    return t


def _num(t):
    m = re.fullmatch(r"(−?)(\d+)", t)
    return int(m.group(2)) * (-1 if m.group(1) else 1) if m else None


NUM = re.compile(r"^(−?\d+(?:,\d+)?)( [^\d×].*)?$")


def _val(t):
    m = NUM.match(t)
    return (float(m.group(1).replace(",", ".").replace("−", "-")), m.group(2) or "") if m else None


def _plausible(d, ok):
    """Écarte les distracteurs absurdes (0, ou mille fois trop grands/petits) quand la réponse est un nombre."""
    a, b = _val(ok), _val(d)
    if not a or not b or a[1] != b[1] or a[0] == 0:
        return True
    if b[0] == 0 or len(d) > 14:
        return False
    r = abs(b[0] / a[0])
    return 1e-3 <= r <= 1e3


def calc(lst):
    out = []
    for q, ok, a, b, c, e in lst:
        q, ok, a, b, c, e = map(fx, (q, ok, a, b, c, e))
        ds = [x for x in dict.fromkeys([a, b, c]) if x != ok and _plausible(x, ok)]
        vu = _val(ok)
        if vu and vu[0]:
            for k in (2, 0.5, 10, 0.1, 1.5):
                if len(ds) >= 3:
                    break
                w = n(round(vu[0] * k, 3), 3) + vu[1]
                if w not in ds and w != ok:
                    ds.append(w)
        v = _num(ok)
        if v is not None:
            for w in (v + 1, v - 1, 2 * v, -v, v + 2):
                if len(ds) >= 3:
                    break
                w = n(w)
                if w not in ds and w != ok:
                    ds.append(w)
        while len(ds) < 3:
            ds.append(ok)
        out += _calc([(q, ok, *ds[:3], e)])
    return out


def pi(r):
    """Fraction de π : π/2, 2π/3, π."""
    r = Fr(r)
    num = "π" if abs(r.numerator) == 1 else f"{abs(r.numerator)}π"
    num = ("−" if r < 0 else "") + num
    return num if r.denominator == 1 else f"{num}/{r.denominator}"


def n(x, d=2):
    """Nombre à la française : 3,14 ; entier sans virgule."""
    if isinstance(x, Fr):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x))).replace("-", "−")
    s = f"{x:.{d}f}".rstrip("0").rstrip(".").replace(".", ",")
    return s.replace("-", "−")


def sg(x):
    """Coefficient avec son signe pour écrire une expression : + 3 / − 3."""
    return f"+ {n(x)}" if x >= 0 else f"− {n(-x)}"


def poly(*c):
    """poly(a, b, c) -> « ax² + bx + c » lisible."""
    deg = len(c) - 1
    out = []
    for i, a in enumerate(c):
        p = deg - i
        if a == 0:
            continue
        mono = ("x" if p == 1 else f"x{'²³⁴⁵'[p - 2]}" if p > 1 else "")
        coef = n(abs(a)) if (abs(a) != 1 or p == 0) else ""
        sign = "−" if a < 0 else "+"
        out.append((sign, coef + mono))
    if not out:
        return "0"
    s = ("−" if out[0][0] == "−" else "") + out[0][1]
    for sign, t in out[1:]:
        s += f" {sign} {t}"
    return s


M = {}
# ---------- 0. Limites
M["Limites de fonctions"] = calc(
    [(f"lim ({poly(a, 0, b)}) / ({poly(c, 0, d)}) quand x → +∞ =", n(Fr(a, c)), n(Fr(b, d)), "+∞", "0", f"Quotient des termes de plus haut degré : {n(a)}x² / {n(c)}x² = {n(Fr(a, c))}.")
     for a, b, c, d in [(3, 1, 2, 5), (-4, 7, 6, 1), (5, -2, 10, 3), (1, 9, 4, -1)]]
    + [(f"lim ({poly(1, 0, -k * k)}) / (x − {k}) quand x → {k} =", n(2 * k), "0", n(k), "+∞", f"x² − {k * k} = (x − {k})(x + {k}) ; on simplifie : limite {k} + {k} = {2 * k}.") for k in [2, 3, 5, 7]]
    + [(f"lim (√(x + {a * a}) − {a}) / x quand x → 0 =", n(Fr(1, 2 * a)), n(Fr(1, a)), "0", "+∞", f"Quantité conjuguée : 1 / (√(x + {a * a}) + {a}) → 1/{2 * a}.") for a in [1, 2, 3, 5]]
    + [(f"lim ({poly(a, b, c)}) quand x → −∞ =", "+∞" if a > 0 else "−∞", "−∞" if a > 0 else "+∞", n(a), "0", f"Terme dominant {n(a)}x² de signe {'positif' if a > 0 else 'négatif'}.") for a, b, c in [(2, -5, 1), (-3, 4, 7), (1, 100, -3)]]
    + [(f"lim ({poly(a, b)}) / ({poly(1, 0, c)}) quand x → +∞ =", "0", n(a), "+∞", n(Fr(b, c)), "Degré du dénominateur supérieur : la limite est 0.") for a, b, c in [(3, 1, 2), (-5, 4, 9), (7, -2, 1)]]
)
# ---------- 1. Continuité, TVI
def tvi(p, q):
    fx = lambda x: x ** 3 + p * x - q
    k = 0
    while fx(k + 1) < 0:
        k += 1
    return k, fx


M["Continuité et théorème des valeurs intermédiaires"] = calc(
    [(f"f(x) = {poly(1, 0, p, -q)} est continue et strictement croissante. La solution α de f(x) = 0 se trouve dans :", f"[{tvi(p, q)[0]} ; {tvi(p, q)[0] + 1}]", f"[{tvi(p, q)[0] + 1} ; {tvi(p, q)[0] + 2}]",
      f"[−{tvi(p, q)[0] + 1} ; −{tvi(p, q)[0]}]" if tvi(p, q)[0] else "[−1 ; 0]", "[10 ; 11]", f"f({tvi(p, q)[0]}) = {n(tvi(p, q)[1](tvi(p, q)[0]))} < 0 et f({tvi(p, q)[0] + 1}) = {n(tvi(p, q)[1](tvi(p, q)[0] + 1))} > 0.")
     for p, q in [(1, 5), (2, 20), (3, 1), (1, 40), (4, 60)]]
    + [(f"f continue sur [{a} ; {b}] avec f({a}) = {fa} et f({b}) = {fb}. L'équation f(x) = {k} :", "a au moins une solution dans l'intervalle", "n'a aucune solution", "a exactement deux solutions", "n'a de solution que si f est dérivable",
        f"{k} est compris entre {fa} et {fb} : théorème des valeurs intermédiaires.") for a, b, fa, fb, k in [(0, 2, -3, 5, 1), (1, 4, 10, 2, 7), (-1, 1, -8, 8, 0), (2, 6, 0, 12, 5)]]
    + [(f"g(x) = (x² − {k * k}) / (x − {k}) pour x ≠ {k}. Pour que g soit continue en {k}, on pose g({k}) =", n(2 * k), "0", n(k), n(k * k), f"lim g = {2 * k} en {k} : prolongement par continuité.") for k in [1, 4, 6]]
)
# ---------- 2. Dérivées
M["Dérivabilité et calcul de dérivées"] = calc(
    [(f"f(x) = {poly(a, b, c, d)}. f'({x0}) =", n(3 * a * x0 ** 2 + 2 * b * x0 + c), n(a * x0 ** 3 + b * x0 ** 2 + c * x0 + d), n(3 * a * x0 ** 2 + b * x0 + c), n(6 * a * x0 + 2 * b),
      f"f'(x) = {poly(3 * a, 2 * b, c)}, donc f'({x0}) = {n(3 * a * x0 ** 2 + 2 * b * x0 + c)}.") for a, b, c, d, x0 in [(1, -2, 3, 1, 2), (2, 0, -5, 4, 1), (-1, 3, 0, 2, 3), (1, 1, 1, 1, -1), (3, -1, 2, 0, 2)]]
    + [(f"La dérivée de f(x) = ({poly(a, b)})^{k} est :", f"{n(k * a)}({poly(a, b)})^{k - 1}", f"{k}({poly(a, b)})^{k - 1}", f"{n(a)}({poly(a, b)})^{k}", f"({poly(a, b)})^{k - 1}",
        f"(uⁿ)' = n u' uⁿ⁻¹ avec u' = {n(a)}.") for a, b, k in [(2, 1, 3), (3, -1, 4), (5, 2, 2), (4, -3, 5)]]
    + [(f"La dérivée de f(x) = ln({poly(a, b)}) est :", f"{n(a)} / ({poly(a, b)})", f"1 / ({poly(a, b)})", f"ln({n(a)})", f"{n(a)}·ln({poly(a, b)})", "(ln u)' = u'/u.") for a, b in [(2, 1), (3, -5), (5, 4)]]
    + [(f"La dérivée de f(x) = e^({poly(a, b)}) est :", f"{n(a)}e^({poly(a, b)})", f"e^({poly(a, b)})", f"{n(a)}e^{n(a)}", f"({poly(a, b)})e^({poly(a, b) if b else poly(a, 0)})", "(e^u)' = u'e^u.") for a, b in [(2, -1), (-3, 0), (5, 2)]]
    + [(f"Tangente à y = {poly(1, b, c)} au point d'abscisse {x0} :", f"y = {poly(2 * x0 + b, -(x0 ** 2) + c)}", f"y = {poly(2 * x0 + b, x0 ** 2 + b * x0 + c)}", f"y = {poly(x0 + b, c)}", f"y = {poly(2 * x0, c)}",
        f"f'({x0}) = {2 * x0 + b}, f({x0}) = {x0 ** 2 + b * x0 + c} ; y = f'({x0})(x − {x0}) + f({x0}).") for b, c, x0 in [(0, 1, 2), (-2, 3, 1), (4, 0, -1), (1, -2, 3)]]
)
# ---------- 3. Étude de fonctions
M["Étude complète d'une fonction"] = calc(
    [(f"f(x) = {poly(a, b, c)}. Son extremum est atteint en x =", n(Fr(-b, 2 * a)), n(Fr(b, 2 * a)), n(Fr(-b, a)), n(Fr(-c, b)) if b else "0", f"f'(x) = {poly(2 * a, b)} s'annule en −b/(2a).") for a, b, c in [(1, -6, 2), (2, 8, -1), (-1, 4, 3), (3, -12, 5)]]
    + [(f"f(x) = {poly(a, b)} + {c}/(x − {d}). Asymptote oblique en +∞ :", f"y = {poly(a, b)}", f"y = {poly(a, 0)}", f"x = {d}", f"y = {n(c)}", f"{c}/(x − {d}) → 0, donc f(x) − ({poly(a, b)}) → 0.") for a, b, c, d in [(1, 2, 3, 1), (2, -1, 5, 2), (-1, 4, 1, 3)]]
    + [(f"f(x) = {poly(a, b)} + {c}/(x − {d}). Asymptote verticale :", f"x = {d}", f"x = −{d}", f"y = {d}", f"x = {c}", f"Le dénominateur s'annule en {d}.") for a, b, c, d in [(1, 2, 3, 1), (2, -1, 5, 2), (-1, 4, 1, 3)]]
    + [(f"f(x) = ({poly(a, b)}) / ({poly(1, -d)}). Son centre de symétrie est :", f"Ω({d} ; {n(a)})", f"Ω({n(a)} ; {d})", f"Ω(−{d} ; {n(a)})", "Ω(0 ; 0)", "Intersection des asymptotes x = {d} et y = {a}.".format(d=d, a=n(a))) for a, b, d in [(2, 1, 1), (3, -2, 2), (-1, 5, 4)]]
    + [(f"f(x) = {poly(1, 0, -3 * k * k, 0)}. Ses extremums locaux sont en x =", f"−{k} et {k}", f"0 et {k}", f"−{3 * k} et {3 * k}", f"{k * k}", f"f'(x) = 3x² − {3 * k * k} = 3(x − {k})(x + {k}).") for k in [1, 2, 3]]
)
# ---------- 4. Logarithme
M["Fonction logarithme népérien"] = calc(
    [(f"ln {a} + ln {b} =", f"ln {a * b}", f"ln {a + b}", f"(ln {a})(ln {b})", f"ln {Fr(a, b) if a % b == 0 else a + b + 1}", "ln a + ln b = ln(ab).") for a, b in [(2, 5), (3, 4), (6, 7), (10, 10)]]
    + [(f"ln {a} − ln {b} =", f"ln {n(Fr(a, b))}", f"ln {a - b}", f"ln {a} / ln {b}", f"ln {a * b}", "ln a − ln b = ln(a/b).") for a, b in [(12, 3), (20, 4), (7, 2)]]
    + [(f"ln({a}^{k}) =", f"{k} ln {a}", f"(ln {a})^{k}", f"ln {a * k}", f"{a} ln {k}", "ln(aⁿ) = n ln a.") for a, k in [(2, 5), (3, 4), (10, 3)]]
    + [(f"La solution de ln x = {k} est :", f"e^{k}" if k not in (0, 1) else ("1" if k == 0 else "e"), f"{k}", f"ln {k}" if k > 0 else "aucune", f"{k}e", "ln x = k ⇔ x = e^k.") for k in [2, 3, -1, 1]]
    + [(f"La solution de ln({poly(a, b)}) = 0 est x =", n(Fr(1 - b, a)), n(Fr(-b, a)), n(Fr(1, a)), "e", f"{poly(a, b)} = 1.") for a, b in [(2, -3), (3, 4), (5, 1)]]
    + [(f"L'ensemble de définition de f(x) = ln({poly(a, b)}) est :", f"]{n(Fr(-b, a))} ; +∞[" if a > 0 else f"]−∞ ; {n(Fr(-b, a))}[", f"[{n(Fr(-b, a))} ; +∞[", "ℝ", f"]−∞ ; {n(Fr(-b, a))}[" if a > 0 else f"]{n(Fr(-b, a))} ; +∞[",
        f"Il faut {poly(a, b)} > 0.") for a, b in [(2, -4), (-1, 3), (3, 6)]]
    + [(f"ln(e^{k}) =", n(k), f"e^{k}", "1", f"ln {k}" if k > 0 else "0", "ln et exp sont réciproques.") for k in [3, -2, 5]]
)
# ---------- 5. Exponentielle
M["Fonction exponentielle et fonctions puissances"] = calc(
    [(f"e^{a} × e^{b} =", f"e^{a + b}", f"e^{a * b}", f"e^{a - b}", f"{a + b}e", "e^a × e^b = e^(a+b).") for a, b in [(2, 3), (5, -2), (-1, 4), (3, 3)]]
    + [(f"(e^{a})^{b} =", f"e^{a * b}", f"e^{a + b}", f"e^{a ** b}", f"{b}e^{a}", "(e^a)^b = e^(ab).") for a, b in [(2, 3), (4, 2), (-1, 5)]]
    + [(f"La solution de e^({poly(a, b)}) = 1 est x =", n(Fr(-b, a)), n(Fr(1 - b, a)), "0", "1", f"e^u = 1 ⇔ u = 0, soit {poly(a, b)} = 0.") for a, b in [(2, -6), (3, 1), (-1, 4)]]
    + [(f"La solution de e^x = {k} est :", f"ln {k}", f"e^{k}", f"{k}/e", "aucune", "e^x = k (k > 0) ⇔ x = ln k.") for k in [2, 5, 10]]
    + [(f"L'équation e^(2x) − {a + b}e^x + {a * b} = 0 a pour solutions :", f"ln {a} et ln {b}", f"{a} et {b}", f"e^{a} et e^{b}", f"−ln {a} et −ln {b}", f"On pose X = e^x : X² − {a + b}X + {a * b} = 0, X = {a} ou X = {b}.") for a, b in [(2, 3), (3, 4), (2, 5)]]
    + [(f"lim x^{k}e^(−x) quand x → +∞ =", "0", "+∞", "1", f"{k}", "Croissances comparées : l'exponentielle l'emporte.") for k in [2, 5, 10]]
    + [(f"{a}^x = e^(…) :", f"x ln {a}", f"{a} ln x", f"ln({a}x)", f"x + ln {a}", "aˣ = e^(x ln a).") for a in [2, 3, 10]]
)
# ---------- 6. Suites
M["Suites numériques"] = calc(
    [(f"uₙ₊₁ = ({n(a)})uₙ + {b}. La limite éventuelle ℓ (point fixe) vaut :", n(Fr(b) / (1 - Fr(a))), n(b), n(Fr(b) / (1 + Fr(a))), "+∞", f"ℓ = ({n(a)})ℓ + {b} ⇔ ℓ = {b} / (1 − {n(a)}).") for a, b in [(Fr(1, 2), 3), (Fr(1, 3), 4), (Fr(2, 5), 6), (Fr(3, 4), 1)]]
    + [(f"(uₙ) géométrique, u₀ = {u0}, q = {q}. u₀ + u₁ + … + u₅ =", n(u0 * (q ** 6 - 1) // (q - 1)), n(u0 * q ** 5), n(u0 * (q ** 5 - 1) // (q - 1)), n(6 * u0 * q), f"u₀(q⁶ − 1)/(q − 1).") for u0, q in [(1, 2), (2, 3), (5, 2), (3, 4)]]
    + [(f"(uₙ) arithmétique, u₀ = {u0}, r = {r}. u₀ + u₁ + … + u₉ =", n(10 * u0 + 45 * r), n(u0 + 9 * r), n(10 * (u0 + 9 * r)), n(10 * u0 + 90 * r), "10 termes × (u₀ + u₉)/2.") for u0, r in [(2, 3), (10, -1), (1, 5), (7, 2)]]
    + [(f"lim ({n(q)})ⁿ quand n → +∞ =", "0" if abs(q) < 1 else "+∞", "+∞" if abs(q) < 1 else "0", "1", n(q), "|q| < 1 : qⁿ → 0 ; q > 1 : qⁿ → +∞.") for q in [Fr(2, 3), Fr(5, 4), Fr(9, 10), 3]]
    + [(f"uₙ = ({poly(a, b)}) / ({poly(c, d)}) avec x remplacé par n. lim uₙ =", n(Fr(a, c)), n(Fr(b, d)), "0", "+∞", "Rapport des coefficients de n.") for a, b, c, d in [(3, 1, 2, 5), (1, -4, 4, 1), (6, 2, 3, -1)]]
)
# ---------- 7. Primitives
M["Primitives"] = calc(
    [(f"Une primitive de f(x) = {n(a)}x^{k} est :", f"{n(Fr(a, k + 1))}x^{k + 1}", f"{n(a * k)}x^{k - 1}", f"{n(a)}x^{k + 1}", f"{n(Fr(a, k))}x^{k}", "Primitive de xⁿ : xⁿ⁺¹/(n + 1).") for a, k in [(6, 2), (4, 3), (10, 4), (3, 5)]]
    + [(f"Une primitive de f(x) = e^({n(a)}x) est :", f"(1/{n(a)})e^({n(a)}x)" if a != 1 else "e^x", f"{n(a)}e^({n(a)}x)", f"e^({n(a)}x)", f"x e^({n(a)}x)", "Primitive de e^(ax) : e^(ax)/a.") for a in [2, 3, 5, -1]]
    + [(f"Une primitive de f(x) = 1/({poly(a, b)}) sur un intervalle où {poly(a, b)} > 0 est :", f"(1/{n(a)}) ln({poly(a, b)})" if a != 1 else f"ln({poly(a, b)})", f"ln({poly(a, b)})" if a != 1 else f"2 ln({poly(a, b)})", f"{n(a)} ln({poly(a, b)})" if a != 1 else f"−1/({poly(a, b)})²", f"−1/({poly(a, b)})²" if a != 1 else f"x ln({poly(a, b)})",
        "Primitive de u'/u : ln|u|.") for a, b in [(2, 1), (3, -2), (1, 4)]]
    + [(f"Une primitive de f(x) = cos({n(a)}x) est :", f"(1/{n(a)}) sin({n(a)}x)", f"{n(a)} sin({n(a)}x)", f"−(1/{n(a)}) sin({n(a)}x)", f"sin({n(a)}x)", "Primitive de cos(ax) : sin(ax)/a.") for a in [2, 3, 4]]
    + [(f"La primitive de f(x) = {2 * a}x qui s'annule en 0 et vaut … en x = {x0} :", n(a * x0 * x0), n(2 * a * x0), n(a * x0), n(2 * a * x0 * x0), f"F(x) = {a}x², donc F({x0}) = {a * x0 * x0}.") for a, x0 in [(1, 3), (3, 2), (2, 5)]]
)
# ---------- 8. Intégrales
M["Calcul intégral et aires"] = calc(
    [(f"∫ de 0 à {k} de ({poly(a, b)}) dx =", n(Fr(a * k * k, 2) + b * k), n(a * k + b), n(a * k * k + b * k), n(Fr(a * k * k, 2)), f"[{n(Fr(a, 2))}x² + {b}x] de 0 à {k}.") for a, b, k in [(2, 1, 3), (4, -1, 2), (6, 0, 1), (1, 3, 4)]]
    + [(f"∫ de 0 à 1 de x^{k} dx =", n(Fr(1, k + 1)), n(Fr(1, k)), "1", n(k + 1), f"[x^{k + 1}/{k + 1}] de 0 à 1.") for k in [2, 3, 4, 9]]
    + [(f"∫ de 0 à ln {k} de e^x dx =", n(k - 1), n(k), f"ln {k}", n(k + 1), f"[e^x] de 0 à ln {k} = {k} − 1.") for k in [2, 3, 5]]
    + [(f"∫ de 1 à e^{k} de (1/x) dx =", n(k), f"e^{k}", "1", f"1/e^{k}", f"[ln x] de 1 à e^{k} = {k}.") for k in [1, 2, 3]]
    + [(f"Valeur moyenne de f(x) = {n(a)}x sur [0 ; {k}] :", n(Fr(a * k, 2)), n(a * k), n(Fr(a * k * k, 2)), n(a), f"(1/{k}) × ∫ = (1/{k}) × {n(Fr(a * k * k, 2))}.") for a, k in [(2, 4), (6, 2), (3, 6)]]
    + [(f"L'aire entre la courbe de x² et l'axe des abscisses, de 0 à {k} (en u.a.) :", n(Fr(k ** 3, 3)), n(k * k), n(Fr(k * k, 2)), n(k ** 3), f"∫ x² dx = [x³/3] de 0 à {k}.") for k in [3, 6]]
)
# ---------- 9. Équations différentielles
M["Équations différentielles"] = calc(
    [(f"Les solutions de y' = {n(a)}y sont :", f"y = Ce^({n(a)}x)", f"y = Ce^(x/{n(a)})" if a != 1 else "y = Cx", f"y = {n(a)}x + C", f"y = Ce^(−{n(a)}x)" if a > 0 else "y = Ce^x", "y' = ay ⇔ y = Ce^(ax).") for a in [2, -3, Fr(1, 2), 5]]
    + [(f"y' = {n(a)}y et y(0) = {k}. Alors y(x) =", f"{k}e^({n(a)}x)", f"e^({n(a)}x) + {k}", f"{k}e^x", f"{n(a)}e^({k}x)", f"C = y(0) = {k}.") for a, k in [(2, 3), (-1, 5), (4, 2)]]
    + [(f"y' = {n(a)}y + {b}. Solution constante :", f"y = {n(Fr(-b) / a)}", f"y = {n(b)}", f"y = {n(Fr(b) / a)}", "y = 0", f"y' = 0 donne y = −{b}/{n(a)}.") for a, b in [(2, 6), (-3, 9), (5, -10)]]
    + [(f"y'' + {w * w}y = 0 : la période des solutions est :", f"2π/{w}" if w != 1 else "2π", f"{w}π", f"π/{w * w}", f"2π × {w}", f"Solutions A cos({w}x) + B sin({w}x), ω = {w}.") for w in [2, 3, 5]]
    + [(f"y'' + {w * w}y = 0, y(0) = {a}, y'(0) = 0. Alors y(x) =", f"{a} cos({w}x)", f"{a} sin({w}x)", f"{a}e^({w}x)", f"cos({a}x)", f"A = {a}, B = 0.") for w, a in [(2, 3), (4, 5), (3, 2)]]
)
# ---------- 10. Complexes forme algébrique
M["Nombres complexes : forme algébrique et équations"] = calc(
    [(f"({a} {sg(b)}i)({c} {sg(d)}i) =", f"{n(a * c - b * d)} {sg(a * d + b * c)}i", f"{n(a * c + b * d)} {sg(a * d + b * c)}i", f"{n(a * c)} {sg(b * d)}i", f"{n(a * c - b * d)} {sg(a * d - b * c)}i", "On développe avec i² = −1.") for a, b, c, d in [(2, 3, 1, -1), (1, 2, 3, 4), (4, -1, 2, 5), (3, 3, 1, -2)]]
    + [(f"Le module de {a} {sg(b)}i est :", n(int(math.hypot(a, b))), n(a + b), n(a * a + b * b), n(abs(a - b)), f"√({a}² + {b}²).") for a, b in [(12, 5), (5, -12), (6, 8), (8, 15)]]
    + [(f"Le conjugué de {a} {sg(b)}i est :", f"{a} {sg(-b)}i", f"{n(-a)} {sg(b)}i", f"{n(-a)} {sg(-b)}i", f"{b} {sg(a)}i", "On change le signe de la partie imaginaire.") for a, b in [(2, 5), (-3, 1), (7, -4)]]
    + [(f"Les solutions de z² = −{k * k} sont :", f"{k}i et −{k}i", f"{k} et −{k}", f"{k * k}i et −{k * k}i", "aucune", f"z² = ({k}i)².") for k in [2, 3, 5]]
    + [(f"Les solutions de z² {sg(-2 * a)}z + {a * a + b * b} = 0 sont :", f"{a} + {b}i et {a} − {b}i", f"{a} + {b} et {a} − {b}", f"−{a} + {b}i et −{a} − {b}i", f"{b} + {a}i et {b} − {a}i", f"Δ = −{4 * b * b} = ({2 * b}i)².") for a, b in [(1, 2), (2, 1), (3, 4)]]
    + [(f"1/({a} + {b}i) =", f"{n(Fr(a, a * a + b * b))} − {n(Fr(b, a * a + b * b))}i", f"{n(Fr(1, a))} + {n(Fr(1, b))}i", f"{a} − {b}i", f"{n(Fr(a, a * a + b * b))} + {n(Fr(b, a * a + b * b))}i", "On multiplie par le conjugué.") for a, b in [(1, 1), (3, 4), (1, 2)]]
)
# ---------- 11. Forme trigonométrique
ARG = {(1, 1): "π/4", (1, -1): "−π/4", (-1, 1): "3π/4", (0, 1): "π/2", (0, -1): "−π/2", (-1, 0): "π"}
M["Nombres complexes : forme trigonométrique, exponentielle et géométrie"] = calc(
    [(f"Un argument de z = {k} + {k}i est :", "π/4", "π/2", "π/3", "−π/4", "z = k(1 + i), k > 0 : argument de 1 + i.") for k in [1, 2, 5]]
    + [(f"Le module de ({a} + {a}i)^{m} est :", f"{n(round((a * math.sqrt(2)) ** m, 4))}" if m % 2 == 0 else f"{n(a ** m)}(√2)^{m}", n(2 * a * m), f"{n(a ** m)}", f"{n(2 ** m)}", f"|1 + i| = √2, le module est élevé à la puissance {m}.") for a, m in [(1, 4), (1, 6), (2, 2)]]
    + [(f"(1 + i)^{m} =", {2: "2i", 4: "−4", 8: "16", 6: "−8i"}[m], {2: "2", 4: "4", 8: "−16", 6: "8i"}[m], {2: "−2i", 4: "4i", 8: "16i", 6: "−8"}[m], {2: "0", 4: "−4i", 8: "8", 6: "8"}[m], f"1 + i = √2 e^(iπ/4) ; on élève à la puissance {m}.") for m in [2, 4, 6, 8]]
    + [(f"e^(iπ/{k}) en forme algébrique :", {2: "i", 3: "1/2 + i√3/2", 6: "√3/2 + i/2", 4: "√2/2 + i√2/2"}[k], {2: "1", 3: "√3/2 + i/2", 6: "1/2 + i√3/2", 4: "1 + i"}[k], {2: "−i", 3: "−1/2 + i√3/2", 6: "−√3/2 + i/2", 4: "√2 + i√2"}[k], {2: "−1", 3: "1/2 − i√3/2", 6: "√3/2 − i/2", 4: "√2/2 − i√2/2"}[k], "e^(iθ) = cos θ + i sin θ.") for k in [2, 3, 4, 6]]
    + [(f"|z₁| = {a}, |z₂| = {b}, arg z₁ = π/{p}, arg z₂ = π/{q}. Le module et un argument de z₁z₂ :", f"{a * b} et {pi(Fr(1, p) + Fr(1, q))}", f"{a + b} et {pi(Fr(1, p) + Fr(1, q))}", f"{a * b} et {pi(Fr(1, p * q))}", f"{a + b} et π/{p * q}", "Modules multipliés, arguments ajoutés.") for a, b, p, q in [(2, 3, 3, 6), (4, 5, 4, 4), (1, 7, 2, 3)]]
)
# ---------- 12. Similitudes
M["Transformations du plan : similitudes"] = calc(
    [(f"z' = ({a} {sg(b)}i)z + {c}. Le rapport de la similitude est :", n(math.hypot(a, b)) if math.hypot(a, b) == int(math.hypot(a, b)) else f"√{a * a + b * b}", n(a * a + b * b), n(abs(a) + abs(b) + 1), "1", f"Rapport = |{a} {sg(b)}i|.") for a, b, c in [(3, 4, 1), (1, 1, 2), (0, 2, -1), (1, -1, 3)]]
    + [(f"z' = {k}iz + b : l'angle de la similitude est :", "π/2" if k > 0 else "−π/2", "π" , "0", "π/4", f"arg({k}i) = {'π/2' if k > 0 else '−π/2'}.") for k in [2, 3, -1]]
    + [(f"z' = {a}z + {b} (a réel ≠ 1). Le centre de cette homothétie a pour affixe :", n(Fr(b, 1 - a)), n(b), n(Fr(b, a)), n(Fr(-b, 1 - a)), f"ω = b/(1 − a) = {b}/(1 − {a}).") for a, b in [(2, 3), (3, -4), (-1, 6)]]
    + [(f"z' = iz + {k}. C'est :", f"la rotation d'angle π/2 et de centre d'affixe {n(Fr(k, 2))} + {n(Fr(k, 2))}i", "une translation", "une homothétie de rapport 2", "une symétrie axiale", f"|i| = 1 ; centre ω = {k}/(1 − i).") for k in [2, 4, 6]]
    + [(f"Une similitude de rapport {r} multiplie les aires par :", n(r * r), n(r), n(2 * r), n(r ** 3), "Les aires sont multipliées par k².") for r in [2, 5, Fr(1, 2)]]
)
# ---------- 13. Dénombrement
M["Dénombrement"] = calc(
    [(f"C({nn}, {k}) =", n(math.comb(nn, k)), n(math.perm(nn, k)), n(nn * k), n(math.comb(nn, k - 1)), "Nombre de façons de choisir k objets parmi n sans ordre.") for nn, k in [(8, 3), (10, 4), (12, 2), (6, 3), (9, 5)]]
    + [(f"Nombre d'arrangements A({nn}, {k}) :", n(math.perm(nn, k)), n(math.comb(nn, k)), n(nn ** k), n(math.factorial(k)), "n!/(n − k)!.") for nn, k in [(7, 3), (10, 2), (5, 5)]]
    + [(f"Nombre d'anagrammes du mot « {w} » :", n(math.factorial(len(w)) // math.prod(math.factorial(w.count(c)) for c in set(w))), n(math.factorial(len(w))), n(len(w) ** 2), n(len(set(w))), "n! divisé par les factorielles des lettres répétées.") for w in ["DAKAR", "THIES", "LOUGA", "KAOLACK"]]
    + [(f"On tire simultanément {k} boules dans une urne de {nn} boules. Nombre de tirages :", n(math.comb(nn, k)), n(math.perm(nn, k)), n(nn ** k), n(nn * k), "Tirage simultané : combinaisons.") for nn, k in [(10, 3), (15, 2), (20, 4)]]
    + [(f"On tire successivement avec remise {k} boules parmi {nn}. Nombre de tirages :", n(nn ** k), n(math.comb(nn, k)), n(math.perm(nn, k)), n(nn * k), "p-listes : nᵏ.") for nn, k in [(5, 3), (4, 4), (10, 2)]]
)
# ---------- 14. Probabilités
def binom(nn, k, p):
    return math.comb(nn, k) * p ** k * (1 - p) ** (nn - k)


M["Probabilités et variables aléatoires"] = calc(
    [(f"X suit la loi binomiale B({nn} ; {n(p)}). P(X = {k}) ≈", n(round(binom(nn, k, p), 4), 4), n(round(p ** k, 4), 4), n(round(math.comb(nn, k) * p ** k, 4), 4), n(round(1 - binom(nn, k, p), 4), 4), f"C({nn},{k}) × {n(p)}^{k} × {n(1 - p)}^{nn - k}.") for nn, k, p in [(5, 2, 0.5), (4, 1, 0.2), (6, 3, 0.5), (10, 0, 0.1)]]
    + [(f"X suit B({nn} ; {n(p)}). E(X) =", n(nn * p), n(nn * p * (1 - p)), n(p), n(nn), "E(X) = np.") for nn, p in [(20, 0.3), (50, 0.1), (12, 0.25), (100, 0.04)]]
    + [(f"X suit B({nn} ; {n(p)}). V(X) =", n(nn * p * (1 - p)), n(nn * p), n(math.sqrt(nn * p * (1 - p))), n(nn * (1 - p)), "V(X) = np(1 − p).") for nn, p in [(20, 0.5), (50, 0.2), (10, 0.1)]]
    + [(f"P(A) = {n(a)}, P(B|A) = {n(b)}. P(A ∩ B) =", n(a * b), n(a + b), n(b / a), n(a + b - a * b), "P(A ∩ B) = P(A) × P_A(B).") for a, b in [(0.4, 0.5), (0.3, 0.2), (0.6, 0.75)]]
    + [(f"P(A ∩ B) = {n(c)} et P(A) = {n(a)}. P_A(B) =", n(c / a), n(c * a), n(a - c), n(c + a), "P_A(B) = P(A ∩ B)/P(A).") for c, a in [(0.12, 0.4), (0.15, 0.5), (0.06, 0.3)]]
    + [(f"X prend les valeurs {x1}, {x2}, {x3} avec les probabilités {n(p1)}, {n(p2)}, {n(round(1 - p1 - p2, 2))}. E(X) =", n(round(x1 * p1 + x2 * p2 + x3 * (1 - p1 - p2), 4)), n((x1 + x2 + x3) / 3), n(x3), n(round(x1 * p1 + x2 * p2, 4)), "Somme des xᵢpᵢ.") for x1, x2, x3, p1, p2 in [(0, 10, 50, 0.5, 0.3), (-2, 1, 4, 0.2, 0.5), (1, 2, 3, 0.25, 0.25)]]
)
# ---------- 15. Statistiques à deux variables
def stat(xs, ys):
    k = len(xs); mx = sum(xs) / k; my = sum(ys) / k
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / k
    vx = sum((x - mx) ** 2 for x in xs) / k
    return mx, my, cov, vx


SER = [([1, 2, 3, 4], [3, 5, 7, 9]), ([2, 4, 6, 8], [1, 2, 4, 5]), ([1, 3, 5, 7, 9], [2, 3, 5, 6, 9]), ([0, 2, 4], [10, 7, 4])]
M["Statistiques à deux variables"] = calc(
    [(f"x : {', '.join(map(str, xs))} ; y : {', '.join(map(str, ys))}. Le point moyen G est :", f"G({n(stat(xs, ys)[0])} ; {n(stat(xs, ys)[1])})", f"G({n(stat(xs, ys)[1])} ; {n(stat(xs, ys)[0])})", f"G({n(sum(xs))} ; {n(sum(ys))})", f"G({n(max(xs))} ; {n(max(ys))})", "Moyennes de x et de y.") for xs, ys in SER]
    + [(f"x : {', '.join(map(str, xs))} ; y : {', '.join(map(str, ys))}. cov(x, y) =", n(stat(xs, ys)[2]), n(stat(xs, ys)[3]), n(stat(xs, ys)[2] * 2), n(-stat(xs, ys)[2]), "Moyenne des produits des écarts.") for xs, ys in SER]
    + [(f"x : {', '.join(map(str, xs))} ; y : {', '.join(map(str, ys))}. Coefficient directeur a de la droite de régression de y en x :", n(stat(xs, ys)[2] / stat(xs, ys)[3]), n(stat(xs, ys)[3] / stat(xs, ys)[2]), n(stat(xs, ys)[2]), n(stat(xs, ys)[1] / stat(xs, ys)[0]), "a = cov(x, y) / V(x).") for xs, ys in SER]
    + [(f"Un coefficient de corrélation r = {n(r)} indique :", d, *o, "|r| proche de 1 : ajustement affine justifié.") for r, d, o in [(0.98, "une forte corrélation positive", ("une absence de corrélation", "une forte corrélation négative", "une erreur de calcul")),
        (-0.95, "une forte corrélation négative", ("une forte corrélation positive", "une absence de corrélation", "une erreur de calcul")), (0.12, "une corrélation très faible", ("une forte corrélation positive", "une forte corrélation négative", "une corrélation parfaite"))]]
)
# ---------- 16. Arithmétique
M["Arithmétique (séries S1 et S3)"] = calc(
    [(f"PGCD({a}, {b}) =", n(math.gcd(a, b)), n(math.lcm(a, b)), n(min(a, b)), n(abs(a - b)), "Algorithme d'Euclide.") for a, b in [(84, 36), (120, 45), (252, 198), (91, 65)]]
    + [(f"PPCM({a}, {b}) =", n(math.lcm(a, b)), n(math.gcd(a, b)), n(a * b), n(a + b), "PPCM × PGCD = a × b.") for a, b in [(12, 18), (15, 20), (8, 14)]]
    + [(f"Le reste de la division de {a}^{k} par {m} est :", n(pow(a, k, m)), n((a * k) % m), n((pow(a, k, m) + 1) % m), n(m - 1 if pow(a, k, m) != m - 1 else 0), f"Calcul par congruences modulo {m}.") for a, k, m in [(2, 10, 7), (3, 20, 5), (5, 12, 6), (7, 100, 4)]]
    + [(f"L'équation {a}x + {b}y = {c} a des solutions entières :", "oui" if c % math.gcd(a, b) == 0 else "non", "non" if c % math.gcd(a, b) == 0 else "oui", "seulement x = 0", "une infinité de solutions réelles seulement", f"PGCD({a}, {b}) = {math.gcd(a, b)} {'divise' if c % math.gcd(a, b) == 0 else 'ne divise pas'} {c} (Bézout).") for a, b, c in [(6, 9, 15), (4, 10, 7), (5, 3, 1)]]
    + [(f"{p} est-il premier ?", "oui" if all(p % d for d in range(2, int(p ** 0.5) + 1)) else f"non ({min(d for d in range(2, p) if p % d == 0)} le divise)", "non" if all(p % d for d in range(2, int(p ** 0.5) + 1)) else "oui", "on ne peut pas savoir", "seulement s'il est pair", f"On teste les diviseurs jusqu'à √{p}.") for p in [97, 91, 113, 221]]
)
# ---------- 17. Espace
def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def lin(a, b, c, d):
    """Équation de plan lisible : 2x − y + z − 3 = 0."""
    t = poly(a, 0) if a else ""
    for k, var in ((b, "y"), (c, "z")):
        if k:
            m = "" if abs(k) == 1 else n(abs(k))
            t += (f" {'−' if k < 0 else '+'} " if t else ("−" if k < 0 else "")) + m + var
    if d:
        t += f" {'−' if d < 0 else '+'} {n(abs(d))}"
    return t + " = 0"



M["Géométrie dans l'espace"] = calc(
    [(f"A({a[0]} ; {a[1]} ; {a[2]}) et B({b[0]} ; {b[1]} ; {b[2]}). AB =", n(math.dist(a, b)), n(sum(abs(x - y) for x, y in zip(a, b))), n(sum((x - y) ** 2 for x, y in zip(a, b))), n(math.dist(a, b) + 1), "√((xB − xA)² + (yB − yA)² + (zB − zA)²).") for a, b in [((1, 2, 3), (3, 5, 9)), ((0, 0, 0), (2, 3, 6)), ((1, -1, 2), (5, 3, 4)), ((2, 1, 0), (4, 5, 4))]]
    + [(f"u({u[0]} ; {u[1]} ; {u[2]}) · v({v[0]} ; {v[1]} ; {v[2]}) =", n(sum(x * y for x, y in zip(u, v))), n(sum(x + y for x, y in zip(u, v))), n(u[0] * v[0]), n(-sum(x * y for x, y in zip(u, v))), "xx' + yy' + zz'.") for u, v in [((1, 2, 3), (4, -1, 2)), ((2, 0, -1), (3, 5, 6)), ((1, 1, 1), (2, -3, 1))]]
    + [(f"Le plan passant par A({a[0]} ; {a[1]} ; {a[2]}) de vecteur normal n({u[0]} ; {u[1]} ; {u[2]}) a pour équation :", lin(*u, -dot(u, a)), lin(*a, -dot(u, a)), lin(*u, dot(u, a)), lin(*u, 0) if dot(u, a) else lin(*u, 1),
        "ax + by + cz + d = 0 avec d trouvé en remplaçant par A.") for a, u in [((1, 2, 3), (2, -1, 1)), ((0, 1, -1), (1, 1, 2)), ((2, 0, 1), (3, 2, -1))]]
    + [(f"Le milieu de [AB] avec A({a[0]} ; {a[1]} ; {a[2]}) et B({b[0]} ; {b[1]} ; {b[2]}) est :", f"({n(Fr(a[0] + b[0], 2))} ; {n(Fr(a[1] + b[1], 2))} ; {n(Fr(a[2] + b[2], 2))})", f"({b[0] - a[0]} ; {b[1] - a[1]} ; {b[2] - a[2]})", f"({a[0] + b[0]} ; {a[1] + b[1]} ; {a[2] + b[2]})", f"({a[0]} ; {b[1]} ; {a[2]})", "Moyenne des coordonnées.") for a, b in [((1, 2, 3), (3, 6, 7)), ((0, -2, 4), (6, 2, 0))]]
    + [(f"Distance du point O(0 ; 0 ; 0) au plan {lin(a, b, c, d)} :", n(abs(d) / math.sqrt(a * a + b * b + c * c)), n(abs(d)), n(abs(d) / (a * a + b * b + c * c)), n(math.sqrt(a * a + b * b + c * c)), "|d| / √(a² + b² + c²).") for a, b, c, d in [(1, 2, 2, -6), (2, 3, 6, 14), (0, 3, 4, 10)]]
)
# ---------- 18. Coniques
M["Coniques (série S1)"] = calc(
    [(f"Ellipse x²/{a * a} + y²/{b * b} = 1. Sa distance focale c vaut :", n(math.sqrt(a * a - b * b)), n(math.sqrt(a * a + b * b)), n(a - b), n(a * a - b * b), "c² = a² − b².") for a, b in [(5, 3), (13, 5), (10, 6)]]
    + [(f"Ellipse x²/{a * a} + y²/{b * b} = 1. Son excentricité vaut :", n(Fr(int(math.sqrt(a * a - b * b)), a)), n(Fr(b, a)), n(Fr(a, int(math.sqrt(a * a - b * b)))), "1", "e = c/a < 1.") for a, b in [(5, 3), (13, 5), (10, 6)]]
    + [(f"Parabole y² = {2 * p}x. Son foyer est :", f"F({n(Fr(p, 2))} ; 0)", f"F({p} ; 0)", f"F(0 ; {n(Fr(p, 2))})", f"F({2 * p} ; 0)", f"y² = 2px avec p = {p} : F(p/2 ; 0).") for p in [2, 4, 6]]
    + [(f"Hyperbole x²/{a * a} − y²/{b * b} = 1. Ses asymptotes sont :", f"y = ±{n(Fr(b, a))}x", f"y = ±{n(Fr(a, b))}x", f"y = ±{b}x", f"x = ±{a}", "y = ±(b/a)x.") for a, b in [(2, 3), (4, 1), (3, 6)]]
    + [(f"Hyperbole x²/{a * a} − y²/{b * b} = 1. Son excentricité :", n(math.sqrt(a * a + b * b) / a), n(math.sqrt(abs(a * a - b * b)) / a), n(Fr(b, a)), "1", "c² = a² + b², e = c/a > 1.") for a, b in [(3, 4), (5, 12)]]
)
QCM_TLE_X3_CALC = {"tle-maths": {k: v for k, v in M.items() if v}}
