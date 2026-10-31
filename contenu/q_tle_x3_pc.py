# QCM de physique-chimie de terminale, volume ×3 : applications numériques calculées sur des jeux de données fixes.
import math
from q_tle_x3_calc import calc, n

g = 9.8
e = 1.6e-19
me = 9.1e-31
h = 6.62e-34
c0 = 3e8


def sci(x, d=2):
    """Notation scientifique à la française : 1,6 × 10⁻¹⁹."""
    if x == 0:
        return "0"
    k = math.floor(math.log10(abs(x)))
    m = x / 10 ** k
    if round(m, d) >= 10:
        m, k = m / 10, k + 1
    if k in (0, 1, 2):
        return n(round(x, d), d)
    sup = str(k).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return f"{n(round(m, d), d)} × 10{sup}"


def u(x, unit, d=2):
    return f"{n(round(x, d), d)} {unit}"


M = {}
M["P1. Cinématique du point"] = calc(
    [(f"x(t) = {a}t² {'+' if b >= 0 else '−'} {abs(b)}t + {c} (SI). La vitesse à t = {t} s vaut :", u(2 * a * t + b, "m/s"), u(a * t * t + b * t + c, "m/s"), u(a * t + b, "m/s"), u(2 * a, "m/s"),
      f"v = dx/dt = {2 * a}t + {b}.") for a, b, c, t in [(2, 3, 1, 2), (1, -4, 5, 3), (3, 0, 2, 1), (5, 2, 0, 4), (0.5, 6, 1, 2)]]
    + [(f"x(t) = {a}t² + {b}t (SI). L'accélération vaut :", u(2 * a, "m/s²"), u(a, "m/s²"), u(b, "m/s²"), u(2 * a + b, "m/s²"), "a = d²x/dt² = 2 × coefficient de t².") for a, b in [(3, 1), (1.5, 4), (4, -2)]]
    + [(f"Un mobile part du repos avec a = {a} m/s². Distance parcourue en {t} s :", u(0.5 * a * t * t, "m"), u(a * t * t, "m"), u(a * t, "m"), u(0.5 * a * t, "m"), "d = ½at².") for a, t in [(2, 5), (4, 3), (1.5, 10), (3, 6)]]
    + [(f"Un véhicule passe de {v0} à {v1} m/s en {t} s. Son accélération moyenne :", u((v1 - v0) / t, "m/s²"), u((v1 + v0) / t, "m/s²"), u(v1 / t, "m/s²"), u((v1 - v0) * t, "m/s²"), "a = Δv/Δt.") for v0, v1, t in [(5, 25, 4), (0, 30, 10), (10, 22, 3), (20, 8, 6)]]
    + [(f"Mouvement circulaire uniforme : R = {r} m, v = {v} m/s. Accélération normale :", u(v * v / r, "m/s²"), u(v / r, "m/s²"), u(v * r, "m/s²"), u(v * v * r, "m/s²"), "aₙ = v²/R.") for r, v in [(2, 4), (5, 10), (0.5, 3)]]
    + [(f"Freinage : v₀ = {v} m/s, a = −{a} m/s². Distance d'arrêt :", u(v * v / (2 * a), "m"), u(v * v / a, "m"), u(v / a, "m"), u(v * a, "m"), "v² − v₀² = 2ad avec v = 0.") for v, a in [(20, 5), (30, 6), (10, 2), (15, 3)]]
)
M["P2. Bases de la dynamique et énergie"] = calc(
    [(f"Un solide de {m} kg subit une force résultante de {F} N. Son accélération :", u(F / m, "m/s²"), u(F * m, "m/s²"), u(m / F, "m/s²"), u(F / m * g, "m/s²"), "Deuxième loi de Newton : a = F/m.") for m, F in [(2, 10), (5, 30), (0.5, 4), (10, 25)]]
    + [(f"Énergie cinétique d'un corps de {m} kg à {v} m/s :", u(0.5 * m * v * v, "J"), u(m * v * v, "J"), u(0.5 * m * v, "J"), u(m * v, "J"), "Ec = ½mv².") for m, v in [(2, 3), (4, 5), (1000, 10), (0.2, 20)]]
    + [(f"Travail du poids d'un corps de {m} kg qui descend de {hh} m (g = 9,8 N/kg) :", u(m * g * hh, "J"), u(-m * g * hh, "J"), u(m * hh, "J"), u(m * g / hh, "J"), "W = mgh, positif à la descente.") for m, hh in [(2, 5), (10, 3), (0.5, 20)]]
    + [(f"Chute libre sans vitesse initiale d'une hauteur de {hh} m. Vitesse au sol (g = 9,8) :", u(math.sqrt(2 * g * hh), "m/s"), u(2 * g * hh, "m/s"), u(g * hh, "m/s"), u(math.sqrt(g * hh), "m/s"), "Conservation de l'énergie : v = √(2gh).") for hh in [5, 10, 20, 45]]
    + [(f"Quantité de mouvement d'une masse de {m} kg à {v} m/s :", u(m * v, "kg·m/s"), u(0.5 * m * v * v, "kg·m/s"), u(m / v, "kg·m/s"), u(m + v, "kg·m/s"), "p = mv.") for m, v in [(3, 4), (0.15, 40), (70, 2)]]
    + [(f"Une force de {F} N déplace son point d'application de {d} m dans sa direction en {t} s. Puissance moyenne :", u(F * d / t, "W"), u(F * d, "W"), u(F * t / d, "W"), u(F / t, "W"), "P = W/Δt = Fd/Δt.") for F, d, t in [(50, 10, 5), (200, 3, 2), (20, 30, 10)]]
)
M["P3. Mouvements dans les champs de pesanteur et électrique uniformes"] = calc(
    [(f"Projectile lancé à {v} m/s sous un angle de {a}° (g = 9,8). Flèche (hauteur maximale) :", u((v * math.sin(math.radians(a))) ** 2 / (2 * g), "m"), u(v * v / (2 * g), "m"), u(v * v * math.sin(math.radians(2 * a)) / g, "m"), u(v * math.sin(math.radians(a)) / g, "m"),
      "h = v₀² sin²α / (2g).") for v, a in [(20, 30), (10, 45), (30, 60), (15, 30)]]
    + [(f"Projectile lancé à {v} m/s sous un angle de {a}° (g = 9,8). Portée sur sol horizontal :", u(v * v * math.sin(math.radians(2 * a)) / g, "m"), u((v * math.sin(math.radians(a))) ** 2 / (2 * g), "m"), u(v * v / g * 2, "m"), u(v * math.cos(math.radians(a)), "m"),
        "d = v₀² sin 2α / g.") for v, a in [(20, 30), (10, 45), (30, 15)]]
    + [(f"Champ électrique entre deux plaques : U = {U} V, d = {d} cm. E =", u(U / (d / 100), "V/m"), u(U * d / 100, "V/m"), u(U / d, "V/m"), u(U * d, "V/m"), "E = U/d avec d en mètres.") for U, d in [(200, 2), (500, 5), (1000, 4), (120, 3)]]
    + [(f"Un électron (e = 1,6 × 10⁻¹⁹ C) est accéléré sous une tension de {U} V. Énergie cinétique acquise :", sci(e * U) + " J", sci(e / U) + " J", sci(e * U * 2) + " J", sci(e * U * 1000) + " J", "Ec = eU.") for U in [100, 500, 2000, 1500]]
    + [(f"Force électrique sur une charge de {q} nC dans un champ de {E} V/m :", sci(q * 1e-9 * E) + " N", sci(q * 1e-9 / E) + " N", sci(q * E) + " N", sci(q * 1e-9 * E * 10) + " N", "F = |q|E.") for q, E in [(2, 5000), (5, 2000), (8, 1000)]]
    + [(f"Lancer vertical vers le haut à {v} m/s (g = 9,8). Durée de montée :", u(v / g, "s"), u(2 * v / g, "s"), u(v * g, "s"), u(v / (2 * g), "s"), "v = v₀ − gt = 0 ⇒ t = v₀/g.") for v in [9.8, 19.6, 14.7]]
)
G = 6.67e-11
MT, RT = 5.98e24, 6.37e6
M["P4. Gravitation universelle et satellites"] = calc(
    [(f"Satellite à {hh} km d'altitude (R_T = 6 370 km, g₀ = 9,8 m/s²). L'intensité de la pesanteur à cette altitude :", u(9.8 * (6370 / (6370 + hh)) ** 2, "m/s²"), u(9.8, "m/s²"), u(9.8 * 6370 / (6370 + hh), "m/s²"), u(9.8 * (6370 / hh) ** 2, "m/s²"),
      "g = g₀ R²/(R + h)².") for hh in [400, 800, 20000, 6370]]
    + [(f"Satellite en orbite circulaire à {hh} km d'altitude. Sa vitesse (G M_T = 3,99 × 10¹⁴ SI, R_T = 6 370 km) :", u(math.sqrt(3.99e14 / ((6370 + hh) * 1e3)) / 1000, "km/s"), u(math.sqrt(3.99e14 / (hh * 1e3)) / 1000, "km/s"), u(3.99e14 / ((6370 + hh) * 1e3) / 1e10, "km/s"), u(math.sqrt(3.99e14 / ((6370 + hh) * 1e3)) / 2000, "km/s"),
        "v = √(GM/(R + h)).") for hh in [400, 1000, 36000]]
    + [(f"Force gravitationnelle entre deux masses de {m1} kg et {m2} kg distantes de {d} m (G = 6,67 × 10⁻¹¹) :", sci(G * m1 * m2 / d ** 2) + " N", sci(G * m1 * m2 / d) + " N", sci(G * (m1 + m2) / d ** 2) + " N", sci(G * m1 * m2 * d ** 2) + " N", "F = G m₁m₂/d².") for m1, m2, d in [(100, 200, 2), (1000, 1000, 10), (50, 80, 0.5)]]
    + [(f"Satellite : r = {r} km, période T = {T} h. Si r est multiplié par 4, la période devient :", u(T * 8, "h"), u(T * 4, "h"), u(T * 2, "h"), u(T * 16, "h"), "Troisième loi de Kepler : T² ∝ r³, donc T × 4^(3/2) = 8T.") for r, T in [(7000, 1.6), (10000, 2.8), (8000, 2)]]
    + [(f"Période d'un satellite de vitesse {v} km/s sur une orbite de rayon {r} km :", u(2 * math.pi * r / v / 3600, "h"), u(r / v / 3600, "h"), u(2 * math.pi * v / r, "h"), u(2 * math.pi * r * v / 3600, "h"), "T = 2πr/v.") for v, r in [(7.7, 6770), (3.07, 42200), (7.35, 7370)]]
)
M["P5. Particule chargée dans un champ magnétique"] = calc(
    [(f"Un électron de vitesse {sci(v)} m/s entre perpendiculairement dans B = {B} mT. Rayon de la trajectoire (m = 9,1 × 10⁻³¹ kg) :", u(me * v / (e * B * 1e-3) * 100, "cm"), u(me * v / (e * B) * 100, "cm"), u(e * B * 1e-3 / (me * v) / 100, "cm"), u(me * v * v / (e * B * 1e-3) * 100, "cm"),
      "R = mv/(|q|B).") for v, B in [(1e7, 1), (2e7, 2), (5e6, 0.5), (3e7, 4)]]
    + [(f"Force de Lorentz sur un proton (q = 1,6 × 10⁻¹⁹ C), v = {sci(v)} m/s ⟂ B = {B} T :", sci(e * v * B) + " N", sci(e * v / B) + " N", sci(e * B) + " N", sci(e * v * B * 1e3) + " N", "F = |q|vB sin α avec α = 90°.") for v, B in [(1e6, 0.5), (2e5, 1.2), (5e6, 0.1)]]
    + [(f"Dans un champ magnétique uniforme, si la vitesse de la particule est multipliée par {k}, le rayon est :", f"multiplié par {k}", f"divisé par {k}", f"multiplié par {k * k}", "inchangé", "R = mv/(qB) est proportionnel à v.") for k in [2, 3, 4]]
    + [(f"Spectrographe : deux ions de même charge et de masses m et {k}m, même vitesse. Rapport des rayons R₂/R₁ :", n(k), n(1 / k, 2), n(k * k), n(math.sqrt(k)), "R est proportionnel à m.") for k in [2, 3, 1.5]]
    + [(f"Période du mouvement circulaire d'un électron dans B = {B} mT :", sci(2 * math.pi * me / (e * B * 1e-3)) + " s", sci(me / (e * B * 1e-3)) + " s", sci(2 * math.pi * e * B * 1e-3 / me) + " s", sci(2 * math.pi * me / (e * B)) + " s", "T = 2πm/(|q|B), indépendante de v.") for B in [1, 2, 10]]
)
M["P6. Loi de Laplace"] = calc(
    [(f"Conducteur de {L} cm parcouru par {I} A dans B = {B} T, perpendiculaire à B. Force de Laplace :", u(I * L / 100 * B, "N", 3), u(I * L * B, "N", 3), u(I * B, "N", 3), u(I * L / 100 / B, "N", 3), "F = I L B sin α.") for L, I, B in [(10, 5, 0.2), (20, 3, 0.5), (5, 10, 0.1), (15, 4, 0.3)]]
    + [(f"Conducteur de {L} cm, I = {I} A, B = {B} T, angle de {a}° avec B. Force de Laplace :", u(I * L / 100 * B * math.sin(math.radians(a)), "N", 3), u(I * L / 100 * B, "N", 3), u(I * L / 100 * B * math.cos(math.radians(a)), "N", 3), u(I * L * B * math.sin(math.radians(a)), "N", 3),
        "F = ILB sin α.") for L, I, B, a in [(10, 5, 0.2, 30), (20, 2, 0.5, 30), (8, 5, 0.4, 90)]]
    + [(f"Si l'intensité du courant est multipliée par {k} dans la loi de Laplace, la force est :", f"multipliée par {k}", f"divisée par {k}", f"multipliée par {k * k}", "inchangée", "F proportionnelle à I.") for k in [2, 3]]
    + [(f"Rails de Laplace : barre de {L} cm, I = {I} A, B = {B} T, déplacement de {d} cm. Travail de la force :", u(I * L / 100 * B * d / 100, "J", 4), u(I * L * B * d, "J", 4), u(I * L / 100 * B, "J", 4), u(I * B * d / 100, "J", 4), "W = F × d.") for L, I, B, d in [(10, 4, 0.5, 20), (20, 5, 0.1, 50), (12, 10, 0.25, 40)]]
)
M["P7. Induction et auto-induction"] = calc(
    [(f"Le flux à travers une bobine varie de {f1} Wb à {f2} Wb en {t} s. f.é.m. induite moyenne :", u(-(f2 - f1) / t, "V", 3), u((f2 - f1) * t, "V", 3), u(f2 / t, "V", 3), u((f2 + f1) / t, "V", 3), "e = −ΔΦ/Δt.") for f1, f2, t in [(0.2, 0.8, 0.5), (1, 0.4, 0.2), (0, 0.06, 0.03), (0.5, 0, 0.1)]]
    + [(f"Flux à travers {N} spires de surface {S} cm² dans B = {B} T, normale parallèle à B :", u(N * S * 1e-4 * B, "Wb", 4), u(N * S * B, "Wb", 4), u(S * 1e-4 * B, "Wb", 4), u(N * S * 1e-4 / B, "Wb", 4), "Φ = N B S cos θ.") for N, S, B in [(100, 20, 0.5), (500, 10, 0.2), (200, 50, 0.1)]]
    + [(f"Bobine d'inductance L = {L} mH, le courant varie de {di} A en {t} ms. f.é.m. d'auto-induction (en valeur absolue) :", u(L * 1e-3 * di / (t * 1e-3), "V"), u(L * di * t, "V"), u(L * 1e-3 * di, "V"), u(di / (L * 1e-3 * t), "V"), "|e| = L |di/dt|.") for L, di, t in [(50, 2, 10), (200, 0.5, 5), (10, 4, 2)]]
    + [(f"Énergie magnétique stockée dans une bobine L = {L} mH parcourue par {I} A :", u(0.5 * L * 1e-3 * I * I, "J", 4), u(L * 1e-3 * I * I, "J", 4), u(0.5 * L * I * I, "J", 4), u(0.5 * L * 1e-3 * I, "J", 4), "E = ½LI².") for L, I in [(100, 2), (50, 4), (400, 0.5)]]
    + [(f"Barre de {L} cm glissant à {v} m/s sur des rails dans B = {B} T. f.é.m. induite :", u(B * L / 100 * v, "V", 3), u(B * L * v, "V", 3), u(B * v, "V", 3), u(B * L / 100 / v, "V", 3), "e = BLv.") for L, v, B in [(20, 5, 0.5), (10, 2, 1), (50, 4, 0.2)]]
)
M["P8. Dipôle RC"] = calc(
    [(f"R = {R} kΩ et C = {C} µF. Constante de temps τ :", u(R * C, "ms"), u(R * C * 1000, "ms"), u(R / C, "ms"), u(R * C / 1000, "ms"), "τ = RC ; kΩ × µF = ms.") for R, C in [(10, 100), (2, 470), (47, 10), (1, 2200), (5, 20)]]
    + [(f"Condensateur C = {C} µF chargé sous {U} V. Charge Q :", sci(C * 1e-6 * U) + " C", sci(C * 1e-6 / U) + " C", sci(C * U) + " C", sci(0.5 * C * 1e-6 * U * U) + " C", "Q = CU.") for C, U in [(100, 12), (470, 6), (10, 230)]]
    + [(f"Énergie stockée dans C = {C} µF sous {U} V :", sci(0.5 * C * 1e-6 * U * U) + " J", sci(C * 1e-6 * U * U) + " J", sci(C * 1e-6 * U) + " J", sci(0.5 * C * U * U) + " J", "E = ½CU².") for C, U in [(100, 12), (1000, 10), (22, 50)]]
    + [(f"Charge d'un condensateur sous E = {E} V. Tension uc à t = τ :", u(E * (1 - math.exp(-1)), "V", 1), u(E * math.exp(-1), "V", 1), u(E / 2, "V", 1), u(E, "V", 1), "uc = E(1 − e⁻¹) ≈ 0,63E.") for E in [10, 12, 6]]
    + [(f"Décharge d'un condensateur chargé à {U} V. Tension à t = {k}τ :", u(U * math.exp(-k), "V", 2), u(U * (1 - math.exp(-k)), "V", 2), u(U / k, "V", 2), u(U * math.exp(-1), "V", 2) if k != 1 else u(U / 2, "V"), "uc = U e^(−t/τ).") for U, k in [(10, 2), (12, 3), (20, 1)]]
)
M["P9. Oscillations électriques libres"] = calc(
    [(f"Circuit LC : L = {L} mH, C = {C} µF. Période propre T₀ :", u(2 * math.pi * math.sqrt(L * 1e-3 * C * 1e-6) * 1000, "ms", 3), u(math.sqrt(L * 1e-3 * C * 1e-6) * 1000, "ms", 3), u(2 * math.pi * L * 1e-3 * C * 1e-6 * 1000, "ms", 3), u(2 * math.pi / math.sqrt(L * 1e-3 * C * 1e-6) / 1000, "ms", 3),
      "T₀ = 2π√(LC).") for L, C in [(100, 10), (10, 47), (50, 2), (400, 1), (25, 4)]]
    + [(f"Circuit LC : L = {L} H, C = {C} µF. Fréquence propre f₀ :", u(1 / (2 * math.pi * math.sqrt(L * C * 1e-6)), "Hz", 1), u(1 / math.sqrt(L * C * 1e-6), "Hz", 1), u(2 * math.pi * math.sqrt(L * C * 1e-6), "Hz", 1), u(1 / (2 * math.pi * L * C * 1e-6), "Hz", 1), "f₀ = 1/(2π√(LC)).") for L, C in [(1, 10), (0.1, 1), (0.5, 8)]]
    + [(f"Si la capacité d'un circuit LC est multipliée par {k}, la période propre est :", f"multipliée par {n(math.sqrt(k))}", f"multipliée par {k}", f"divisée par {n(math.sqrt(k))}", "inchangée", "T₀ ∝ √C.") for k in [4, 9, 16]]
    + [(f"Circuit LC : C = {C} µF chargé initialement sous {U} V. Énergie totale de l'oscillateur :", sci(0.5 * C * 1e-6 * U * U) + " J", sci(C * 1e-6 * U * U) + " J", sci(0.5 * C * 1e-6 * U) + " J", sci(2 * C * 1e-6 * U * U) + " J", "E = ½CU² (conservée sans résistance).") for C, U in [(10, 12), (1, 100), (47, 6)]]
    + [(f"Circuit LC : C = {C} µF, U₀ = {U} V, L = {L} H. Intensité maximale :", u(U * math.sqrt(C * 1e-6 / L) * 1000, "mA", 2), u(U * C * 1e-6 / L * 1000, "mA", 2), u(U / L, "mA", 2), u(U * math.sqrt(L / (C * 1e-6)), "mA", 2), "½CU₀² = ½LI₀² ⇒ I₀ = U₀√(C/L).") for C, U, L in [(10, 12, 0.1), (100, 5, 1), (1, 20, 0.01)]]
)
M["P10. Oscillations électriques forcées (RLC)"] = calc(
    [(f"Circuit RLC série : L = {L} H, C = {C} µF. Fréquence de résonance :", u(1 / (2 * math.pi * math.sqrt(L * C * 1e-6)), "Hz", 1), u(1 / math.sqrt(L * C * 1e-6), "Hz", 1), u(math.sqrt(L * C * 1e-6), "Hz", 4), u(1 / (2 * math.pi * L * C * 1e-6), "Hz", 1), "N₀ = 1/(2π√(LC)).") for L, C in [(0.2, 10), (1, 1), (0.05, 5), (0.5, 8)]]
    + [(f"RLC série : U = {U} V efficace, R = {R} Ω. Intensité efficace à la résonance :", u(U / R, "A", 3), u(U * R, "A", 3), u(R / U, "A", 3), u(U / R * math.sqrt(2), "A", 3), "À la résonance Z = R.") for U, R in [(12, 50), (6, 20), (220, 100)]]
    + [(f"RLC série : R = {R} Ω, Lω = {XL} Ω, 1/(Cω) = {XC} Ω. Impédance Z :", u(math.hypot(R, XL - XC), "Ω", 1), u(R + XL + XC, "Ω", 1), u(R + XL - XC, "Ω", 1), u(math.hypot(R, XL + XC), "Ω", 1), "Z = √(R² + (Lω − 1/(Cω))²).") for R, XL, XC in [(30, 80, 40), (60, 100, 20), (40, 50, 80), (12, 21, 5)]]
    + [(f"RLC série : R = {R} Ω, Z = {Z} Ω. Facteur de puissance cos φ :", n(R / Z, 2), n(Z / R, 2), n(1 - R / Z, 2), "1", "cos φ = R/Z.") for R, Z in [(30, 50), (50, 100), (80, 100)]]
    + [(f"Résonance : N₀ = {N0} Hz, bande passante ΔN = {dN} Hz. Facteur de qualité Q :", n(N0 / dN, 1), n(dN / N0, 3), n(N0 * dN), n(N0 - dN), "Q = N₀/ΔN.") for N0, dN in [(500, 25), (1000, 40), (200, 50)]]
)
M["P11. Oscillateurs mécaniques"] = calc(
    [(f"Pendule élastique : m = {m} g, k = {k} N/m. Période propre :", u(2 * math.pi * math.sqrt(m / 1000 / k), "s", 3), u(2 * math.pi * math.sqrt(k / (m / 1000)), "s", 3), u(math.sqrt(m / 1000 / k), "s", 3), u(2 * math.pi * m / 1000 / k, "s", 3), "T₀ = 2π√(m/k).") for m, k in [(200, 20), (500, 80), (100, 40), (250, 10)]]
    + [(f"Pendule simple de longueur {L} m (g = 9,8). Période des petites oscillations :", u(2 * math.pi * math.sqrt(L / g), "s"), u(2 * math.pi * math.sqrt(g / L), "s"), u(math.sqrt(L / g), "s"), u(2 * math.pi * L / g, "s"), "T₀ = 2π√(ℓ/g).") for L in [1, 0.5, 2, 0.25]]
    + [(f"Oscillateur : k = {k} N/m, amplitude Xm = {x} cm. Énergie mécanique :", u(0.5 * k * (x / 100) ** 2, "J", 4), u(k * (x / 100) ** 2, "J", 4), u(0.5 * k * x * x, "J", 4), u(0.5 * k * x / 100, "J", 4), "E = ½kXm².") for k, x in [(20, 5), (50, 10), (100, 2)]]
    + [(f"Oscillateur : m = {m} kg, k = {k} N/m, Xm = {x} cm. Vitesse maximale :", u(x / 100 * math.sqrt(k / m), "m/s", 3), u(x / 100 * math.sqrt(m / k), "m/s", 3), u(x * math.sqrt(k / m), "m/s", 3), u(x / 100 * k / m, "m/s", 3), "Vm = ω₀Xm.") for m, k, x in [(0.2, 20, 5), (0.5, 50, 4), (1, 100, 10)]]
    + [(f"Si la masse d'un pendule élastique est multipliée par {q}, la période est :", f"multipliée par {n(math.sqrt(q))}", f"multipliée par {q}", f"divisée par {n(math.sqrt(q))}", "inchangée", "T₀ ∝ √m.") for q in [4, 9]]
    + [(f"Ressort : un allongement de {x} cm sous une masse de {m} g (g = 9,8). Raideur :", u(m / 1000 * g / (x / 100), "N/m", 1), u(m * g / x, "N/m", 1), u(m / 1000 / (x / 100), "N/m", 1), u(x / 100 / (m / 1000 * g), "N/m", 1), "À l'équilibre : kx = mg.") for x, m in [(5, 100), (2, 200), (10, 500)]]
)
M["P12. Interférences lumineuses"] = calc(
    [(f"Fentes d'Young : λ = {l} nm, a = {a} mm, D = {D} m. Interfrange i :", u(l * 1e-9 * D / (a * 1e-3) * 1000, "mm", 3), u(l * 1e-9 * a * 1e-3 / D * 1000, "mm", 3), u(l * 1e-9 * D / a * 1000, "mm", 3), u(a * 1e-3 * D / (l * 1e-9) / 1e6, "mm", 3), "i = λD/a.") for l, a, D in [(600, 1, 2), (500, 0.5, 1), (650, 2, 3), (550, 0.2, 1)]]
    + [(f"On mesure {k} interfranges sur {L} mm. Interfrange :", u(L / k, "mm", 3), u(L * k, "mm", 3), u(L / (k + 1), "mm", 3), u(k / L, "mm", 3), "i = longueur / nombre d'interfranges.") for k, L in [(10, 12), (5, 6.5), (8, 4)]]
    + [(f"Fentes d'Young : i = {i} mm, a = {a} mm, D = {D} m. Longueur d'onde :", u(i * 1e-3 * a * 1e-3 / D * 1e9, "nm", 0), u(i * D / a * 1e3, "nm", 0), u(i * 1e-3 * D / (a * 1e-3) * 1e9, "nm", 0), u(i * a / D, "nm", 0), "λ = ia/D.") for i, a, D in [(1.2, 1, 2), (2.5, 0.4, 2), (3, 0.5, 2.5)]]
    + [(f"Fréquence d'une radiation de longueur d'onde {l} nm (c = 3 × 10⁸ m/s) :", sci(c0 / (l * 1e-9)) + " Hz", sci(l * 1e-9 / c0) + " Hz", sci(c0 * l * 1e-9) + " Hz", sci(c0 / l) + " Hz", "ν = c/λ.") for l in [600, 450, 750]]
    + [(f"Si la distance D écran-fentes est multipliée par {k}, l'interfrange est :", f"multipliée par {k}", f"divisée par {k}", f"multipliée par {k * k}", "inchangée", "i = λD/a est proportionnelle à D.") for k in [2, 3]]
)
M["P13. Effet photoélectrique"] = calc(
    [(f"Énergie d'un photon de longueur d'onde {l} nm (h = 6,62 × 10⁻³⁴ J·s) :", u(h * c0 / (l * 1e-9) / e, "eV"), u(h * c0 / (l * 1e-9), "eV"), u(h / (l * 1e-9) / e, "eV"), u(h * c0 * l * 1e-9 / e * 1e30, "eV"), "E = hc/λ, puis division par 1,6 × 10⁻¹⁹.") for l in [400, 500, 620, 300, 250]]
    + [(f"Travail d'extraction W₀ = {W} eV. Longueur d'onde seuil :", u(h * c0 / (W * e) * 1e9, "nm", 0), u(W * e / (h * c0) * 1e-9, "nm", 0), u(h * c0 / W * 1e9, "nm", 0), u(h / (W * e) * 1e9 * 1e8, "nm", 0), "λ₀ = hc/W₀.") for W in [2.25, 1.9, 4.5, 3]]
    + [(f"Photon de {E} eV sur un métal de W₀ = {W} eV. Énergie cinétique maximale des électrons :", u(E - W, "eV"), u(E + W, "eV"), u(E / W, "eV"), u(W, "eV"), "Ec max = hν − W₀ (Einstein).") for E, W in [(3.1, 2.25), (4.9, 4.5), (2.8, 1.9), (5, 3.2)]]
    + [(f"Fréquence seuil d'un métal de travail d'extraction {W} eV :", sci(W * e / h) + " Hz", sci(h / (W * e)) + " Hz", sci(W / h) + " Hz", sci(W * e * h) + " Hz", "ν₀ = W₀/h.") for W in [2.25, 4.5, 1.9]]
    + [(f"Potentiel d'arrêt U₀ = {U} V. Énergie cinétique maximale des électrons :", u(U, "eV"), u(U * e, "eV"), u(2 * U, "eV"), u(U / 2, "eV"), "Ec max = eU₀.") for U in [0.85, 1.2, 0.4]]
)
M["P14. Niveaux d'énergie de l'atome"] = calc(
    [(f"Atome d'hydrogène, Eₙ = −13,6/n² eV. Énergie du niveau n = {k} :", u(-13.6 / k ** 2, "eV"), u(-13.6 / k, "eV"), u(13.6 / k ** 2, "eV"), u(-13.6 * k ** 2, "eV"), "Eₙ = −13,6/n².") for k in [2, 3, 4, 5]]
    + [(f"Hydrogène : transition du niveau {p} vers le niveau {q}. Énergie du photon émis :", u(13.6 * (1 / q ** 2 - 1 / p ** 2), "eV"), u(13.6 * (1 / q - 1 / p), "eV"), u(13.6 / (p - q) ** 2, "eV"), u(13.6 * (1 / q ** 2 + 1 / p ** 2), "eV"), "ΔE = Eₚ − E_q.") for p, q in [(3, 2), (2, 1), (4, 2), (5, 2), (3, 1)]]
    + [(f"Hydrogène : longueur d'onde émise lors de la transition {p} → {q} :", u(h * c0 / (13.6 * (1 / q ** 2 - 1 / p ** 2) * e) * 1e9, "nm", 0), u(h * c0 / (13.6 * (1 / q - 1 / p) * e) * 1e9, "nm", 0), u(13.6 * (1 / q ** 2 - 1 / p ** 2) * 100, "nm", 0), u(h * c0 / (13.6 / p ** 2 * e) * 1e9, "nm", 0), "λ = hc/ΔE.") for p, q in [(3, 2), (4, 2), (2, 1)]]
    + [("Énergie d'ionisation de l'atome d'hydrogène pris dans son état fondamental :", "13,6 eV", "−13,6 eV", "3,4 eV", "10,2 eV", "Passer de E₁ = −13,6 eV à E∞ = 0.")]
    + [(f"Énergie d'ionisation de l'hydrogène depuis le niveau n = {k} :", u(13.6 / k ** 2, "eV"), u(13.6, "eV"), u(13.6 / k, "eV"), u(-13.6 / k ** 2, "eV"), "E∞ − Eₙ = 13,6/n².") for k in [2, 3]]
)
M["P15. Réactions nucléaires"] = calc(
    [(f"Demi-vie T = {T} jours. Fraction de noyaux restant au bout de {k * T} jours :", n(1 / 2 ** k, 4), n(1 / (2 * k), 4), n(1 - 1 / 2 ** k, 4), n(1 / k, 4), f"{k} demi-vies : (1/2)^{k}.") for T, k in [(8, 2), (5, 3), (12, 4), (2, 1)]]
    + [(f"Constante radioactive d'un nucléide de demi-vie {T} jours :", sci(math.log(2) / (T * 86400)) + " s⁻¹", sci(T * 86400 / math.log(2)) + " s⁻¹", sci(1 / (T * 86400)) + " s⁻¹", sci(math.log(2) / T) + " s⁻¹", "λ = ln 2 / T, T en secondes.") for T in [8, 138, 3.8]]
    + [(f"Activité initiale A₀ = {A} Bq, demi-vie {T} ans. Activité après {k * T} ans :", u(A / 2 ** k, "Bq", 1), u(A / (2 * k), "Bq", 1), u(A * (1 - 1 / 2 ** k), "Bq", 1), u(A / k, "Bq", 1), "A = A₀/2ᵏ après k demi-vies.") for A, T, k in [(8000, 30, 3), (1200, 5, 2), (6400, 1600, 5)]]
    + [(f"Défaut de masse Δm = {dm} u (1 u ≈ 931,5 MeV/c²). Énergie libérée :", u(dm * 931.5, "MeV", 1), u(dm * 931.5 ** 2, "MeV", 1), u(dm / 931.5, "MeV", 4), u(dm * 3e8, "MeV", 1), "E = Δm c².") for dm in [0.2, 0.0189, 0.03]]
    + [(f"Désintégration α d'un noyau de nombre de masse {A} et de numéro atomique {Z}. Le noyau fils a :", f"A = {A - 4}, Z = {Z - 2}", f"A = {A - 2}, Z = {Z - 4}", f"A = {A}, Z = {Z + 1}", f"A = {A - 4}, Z = {Z + 2}", "On perd un noyau d'hélium ⁴₂He.") for A, Z in [(238, 92), (226, 88), (210, 84)]]
    + [(f"Désintégration β⁻ d'un noyau (A = {A}, Z = {Z}). Le noyau fils a :", f"A = {A}, Z = {Z + 1}", f"A = {A}, Z = {Z - 1}", f"A = {A - 1}, Z = {Z}", f"A = {A + 1}, Z = {Z + 1}", "Un neutron devient un proton : Z augmente de 1.") for A, Z in [(14, 6), (60, 27), (131, 53)]]
)
# ---------- Chimie
MOL = {"méthanol": 32, "éthanol": 46, "propan-1-ol": 60, "butan-1-ol": 74, "acide éthanoïque": 60, "acide méthanoïque": 46, "acide propanoïque": 74, "glycine": 75}
M["C1. Les alcools"] = calc(
    [(f"Masse molaire d'un alcool saturé à {k} atomes de carbone (CₙH₂ₙ₊₁OH) :", u(14 * k + 18, "g/mol", 0), u(14 * k + 16, "g/mol", 0), u(12 * k + 18, "g/mol", 0), u(14 * k + 2, "g/mol", 0), "M = 14n + 18.") for k in [1, 2, 3, 4, 5]]
    + [(f"Un alcool saturé a pour masse molaire {14 * k + 18} g/mol. Nombre d'atomes de carbone :", n(k), n(k + 1), n(k - 1), n(2 * k), "14n + 18 = M.") for k in [3, 4, 6]]
    + [(f"Masse de {nm} contenue dans {q} mol :", u(q * MOL[nm], "g", 1), u(MOL[nm] / q, "g", 1), u(q + MOL[nm], "g", 1), u(q * 18, "g", 1), f"m = nM avec M = {MOL[nm]} g/mol.") for nm, q in [("éthanol", 0.5), ("méthanol", 2), ("butan-1-ol", 0.1)]]
    + [(f"Combustion complète de {q} mol d'éthanol C₂H₆O. Quantité de CO₂ formée :", u(2 * q, "mol"), u(q, "mol"), u(3 * q, "mol"), u(q / 2, "mol"), "C₂H₆O + 3 O₂ → 2 CO₂ + 3 H₂O.") for q in [0.5, 1, 0.2]]
    + [(f"Estérification : {q} mol d'acide et {q} mol d'alcool primaire, rendement 67 %. Quantité d'ester obtenue :", u(0.67 * q, "mol"), u(q, "mol"), u(0.33 * q, "mol"), u(2 * q, "mol"), "n(ester) = 0,67 × n initiale.") for q in [1, 0.3, 0.6]]
)
M["C2. Amines et acides α-aminés"] = calc(
    [(f"Masse molaire d'une amine saturée à {k} atomes de carbone (CₙH₂ₙ₊₃N) :", u(14 * k + 17, "g/mol", 0), u(14 * k + 14, "g/mol", 0), u(12 * k + 17, "g/mol", 0), u(14 * k + 3, "g/mol", 0), "M = 14n + 17.") for k in [1, 2, 3, 4]]
    + [(f"Une amine saturée a une masse molaire de {14 * k + 17} g/mol. Formule brute :", f"C{k}H{2 * k + 3}N", f"C{k}H{2 * k + 1}N", f"C{k + 1}H{2 * k + 5}N", f"C{k}H{2 * k}N", "14n + 17 = M.") for k in [2, 3, 5]]
    + [(f"Un dipeptide formé de deux glycines (M = 75 g/mol). Sa masse molaire :", "132 g/mol", "150 g/mol", "168 g/mol", "57 g/mol", "2 × 75 − 18 (eau éliminée).")]
    + [(f"Nombre de dipeptides différents formés à partir de {k} acides α-aminés distincts (répétition permise) :", n(k * k), n(k * (k - 1)), n(2 * k), n(k), "Ordre important et répétition : k².") for k in [2, 3, 4]]
    + [(f"Dans {V} mL de solution à {C} mol/L d'éthylamine, la quantité d'amine :", sci(V / 1000 * C) + " mol", sci(V * C) + " mol", sci(C / V) + " mol", sci(V / 1000 / C) + " mol", "n = CV.") for V, C in [(20, 0.1), (50, 0.02), (10, 0.5)]]
)
M["C3. Acides carboxyliques et dérivés"] = calc(
    [(f"Masse molaire d'un acide carboxylique saturé à {k} atomes de carbone (CₙH₂ₙO₂) :", u(14 * k + 32, "g/mol", 0), u(14 * k + 18, "g/mol", 0), u(12 * k + 32, "g/mol", 0), u(14 * k + 16, "g/mol", 0), "M = 14n + 32.") for k in [1, 2, 3, 4]]
    + [(f"Un acide carboxylique saturé a pour masse molaire {14 * k + 32} g/mol. Nombre d'atomes de carbone :", n(k), n(k + 1), n(k - 1), n(2 * k), "14n + 32 = M.") for k in [2, 5, 6]]
    + [(f"Masse molaire de l'ester formé par un acide de M = {a} g/mol et un alcool de M = {b} g/mol :", u(a + b - 18, "g/mol", 0), u(a + b, "g/mol", 0), u(a + b + 18, "g/mol", 0), u(a - b, "g/mol", 0), "Une molécule d'eau est éliminée.") for a, b in [(60, 46), (46, 32), (74, 60)]]
    + [(f"Saponification de {q} mol d'un triester (corps gras). Quantité de soude nécessaire :", u(3 * q, "mol"), u(q, "mol"), u(q / 3, "mol"), u(2 * q, "mol"), "Trois fonctions ester : 3 OH⁻ par mole.") for q in [0.1, 0.5, 2]]
    + [(f"Estérification : n₀ = {q} mol d'acide et d'alcool, il reste {r} mol d'acide à l'équilibre. Rendement :", f"{n(round((q - r) / q * 100))} %", f"{n(round(r / q * 100))} %", f"{n(round((q - r) * 100))} %", "100 %", "η = n(ester) / n₀.") for q, r in [(1, 0.33), (0.5, 0.2), (2, 0.8)]]
)
M["C4. Cinétique chimique"] = calc(
    [(f"La concentration d'un réactif passe de {c1} à {c2} mol/L en {t} min. Vitesse moyenne de disparition :", u((c1 - c2) / t, "mol/(L·min)", 4), u((c1 + c2) / t, "mol/(L·min)", 4), u((c1 - c2) * t, "mol/(L·min)", 4), u(c2 / t, "mol/(L·min)", 4), "v = −Δ[R]/Δt.") for c1, c2, t in [(0.5, 0.3, 10), (1, 0.4, 20), (0.08, 0.02, 5), (0.2, 0.15, 2)]]
    + [(f"Réaction d'ordre 1, demi-vie {T} min. Fraction de réactif restant après {k * T} min :", n(1 / 2 ** k, 4), n(1 / (2 * k), 4), n(1 - 1 / 2 ** k, 4), n(1 / k, 4), "Après k temps de demi-réaction : (1/2)ᵏ.") for T, k in [(10, 2), (4, 3), (15, 1)]]
    + [(f"Avancement final x_f = {x} mol. Le temps de demi-réaction correspond à x =", u(x / 2, "mol", 4), u(x, "mol", 4), u(x / 4, "mol", 4), u(2 * x, "mol", 4), "t½ : x(t½) = x_f/2.") for x in [0.02, 0.1, 0.006]]
    + [(f"Une élévation de température de 10 °C multiplie environ la vitesse par 2. De 20 °C à {20 + 10 * k} °C, elle est multipliée par :", n(2 ** k), n(2 * k), n(k), n(10 * k), f"{k} paliers de 10 °C : 2^{k}.") for k in [2, 3, 4]]
    + [(f"[R] = {c} × e^(−{kk}t) (t en min). Constante de vitesse et temps de demi-réaction :", f"k = {n(kk)} min⁻¹ ; t½ = {n(round(math.log(2) / kk, 1))} min", f"k = {n(c)} min⁻¹ ; t½ = {n(round(math.log(2) / kk, 1))} min", f"k = {n(kk)} min⁻¹ ; t½ = {n(round(1 / kk, 1))} min", f"k = {n(kk)} min⁻¹ ; t½ = {n(round(kk * math.log(2), 2))} min",
        "t½ = ln 2 / k.") for c, kk in [(0.1, 0.05), (0.5, 0.2), (1, 0.01)]]
)
M["C5. Autoprotolyse de l'eau, pH et indicateurs"] = calc(
    [(f"[H₃O⁺] = 10^(−{p}) mol/L. pH =", n(p), n(-p), n(14 - p), n(10 ** -p, 6), "pH = −log[H₃O⁺].") for p in [3, 5, 8, 11]]
    + [(f"pH = {p} à 25 °C. [OH⁻] =", f"10^(−{14 - p}) mol/L", f"10^(−{p}) mol/L", f"10^(−{p + 1}) mol/L", f"{14 - p} mol/L", "[H₃O⁺][OH⁻] = 10⁻¹⁴.") for p in [3, 9, 12, 5]]
    + [(f"[H₃O⁺] = {m} × 10^(−{k}) mol/L. pH ≈", n(round(-math.log10(m * 10 ** -k), 1)), n(k), n(round(math.log10(m * 10 ** -k), 1)), n(round(14 + math.log10(m * 10 ** -k), 1)), "pH = −log[H₃O⁺].") for m, k in [(2, 3), (5, 4), (3, 9), (4, 11)]]
    + [(f"Une solution de pH = {p} à 25 °C est :", "acide" if p < 7 else ("basique" if p > 7 else "neutre"), "basique" if p < 7 else "acide", "neutre" if p != 7 else "acide", "amphotère", "pH < 7 acide, pH > 7 basique à 25 °C.") for p in [2.5, 7, 10.4, 6.2]]
    + [(f"On dilue {k} fois une solution d'acide fort de pH = {p}. Nouveau pH :", n(p + math.log10(k)), n(p - math.log10(k)), n(p * k), n(p), "Dilution par 10 : pH + 1 pour un acide fort.") for k, p in [(10, 2), (100, 3), (1000, 1)]]
)
M["C6. Acides forts et bases fortes"] = calc(
    [(f"Solution d'acide chlorhydrique à {sci(c)} mol/L. pH =", n(round(-math.log10(c), 1)), n(round(14 + math.log10(c), 1)), n(round(-math.log10(c / 2), 1)), n(round(math.log10(c), 1)), "Acide fort : pH = −log C.") for c in [0.01, 0.001, 0.05, 2e-4]]
    + [(f"Solution de soude à {sci(c)} mol/L à 25 °C. pH =", n(round(14 + math.log10(c), 1)), n(round(-math.log10(c), 1)), n(round(7 + math.log10(c), 1)), n(round(14 - math.log10(c), 1)), "Base forte : pH = 14 + log C.") for c in [0.01, 0.1, 0.005, 1e-3]]
    + [(f"Dosage de {Va} mL d'HCl par la soude à {Cb} mol/L : équivalence à {Ve} mL. Concentration de l'acide :", u(Cb * Ve / Va, "mol/L", 4), u(Cb * Va / Ve, "mol/L", 4), u(Cb * Ve, "mol/L", 4), u(Va / (Cb * Ve), "mol/L", 4), "À l'équivalence CaVa = CbVe.") for Va, Cb, Ve in [(20, 0.1, 15), (10, 0.05, 12.5), (25, 0.2, 10), (20, 0.01, 18)]]
    + [(f"On mélange {V1} mL d'HCl à {c} mol/L et {V2} mL de soude à {c} mol/L. Le mélange est :", "acide" if V1 > V2 else ("basique" if V2 > V1 else "neutre"), "basique" if V1 > V2 else "acide", "neutre" if V1 != V2 else "basique", "tampon", "On compare les quantités de H₃O⁺ et OH⁻.") for V1, V2, c in [(20, 10, 0.1), (10, 15, 0.1), (25, 25, 0.05)]]
    + [(f"Masse de soude NaOH (40 g/mol) pour préparer {V} mL de solution à {c} mol/L :", u(c * V / 1000 * 40, "g", 3), u(c * V * 40, "g", 3), u(c * V / 1000, "g", 3), u(40 / (c * V / 1000), "g", 1), "m = CVM.") for V, c in [(250, 0.1), (500, 0.02), (100, 1)]]
)
M["C7. Acides faibles, bases faibles et pKa"] = calc(
    [(f"Couple de pKa = {pk}. À pH = {p}, l'espèce prédominante est :", "la base" if p > pk else "l'acide", "l'acide" if p > pk else "la base", "les deux à égalité", "l'eau", "pH > pKa : base prédominante.") for pk, p in [(4.8, 6), (9.2, 7), (3.8, 2.5), (6.4, 8)]]
    + [(f"Ka = 10^(−{k}). pKa =", n(k), n(-k), n(14 - k), n(10 ** -k, 8), "pKa = −log Ka.") for k in [4.8, 9.2, 3.75]]
    + [(f"Acide faible : pKa = {pk}, [A⁻]/[AH] = {r}. pH =", n(round(pk + math.log10(r), 2)), n(round(pk - math.log10(r), 2)), n(pk), n(round(pk * r, 2)), "pH = pKa + log([A⁻]/[AH]).") for pk, r in [(4.8, 10), (4.8, 0.1), (9.2, 1), (3.8, 100)]]
    + [(f"Acide faible à C = {c} mol/L, pKa = {pk}. pH ≈ ½(pKa − log C) =", n(round(0.5 * (pk - math.log10(c)), 2)), n(round(-math.log10(c), 2)), n(round(0.5 * (pk + math.log10(c)), 2)), n(pk), "Formule approchée pour un acide faible peu dissocié.") for c, pk in [(0.1, 4.8), (0.01, 4.8), (0.1, 3.8)]]
    + [(f"Une solution d'acide faible à {sci(c)} mol/L a un pH de {p}. Taux d'avancement α :", n(round(10 ** -p / c, 3), 3), n(round(c / 10 ** -p, 1)), "1", n(round(10 ** -p, 5), 5), "α = [H₃O⁺]/C.") for c, p in [(0.1, 2.9), (0.01, 3.4), (0.05, 3)]]
)
M["C8. Dosages et solutions tampons"] = calc(
    [(f"Dosage de {Va} mL d'acide éthanoïque par la soude à {Cb} mol/L : équivalence à {Ve} mL. Concentration de l'acide :", u(Cb * Ve / Va, "mol/L", 4), u(Cb * Va / Ve, "mol/L", 4), u(Cb * Ve, "mol/L", 4), u(Cb, "mol/L", 4), "CaVa = CbVe.") for Va, Cb, Ve in [(10, 0.1, 12), (20, 0.05, 16), (25, 0.02, 20)]]
    + [(f"Dosage d'un acide faible : équivalence à Ve = {Ve} mL. Le pH vaut le pKa pour V_b =", u(Ve / 2, "mL"), u(Ve, "mL"), u(2 * Ve, "mL"), u(Ve / 4, "mL"), "À la demi-équivalence, pH = pKa.") for Ve in [12, 20, 15.4, 9]]
    + [(f"Solution tampon : {a} mol d'acide éthanoïque (pKa = 4,8) et {b} mol d'éthanoate. pH =", n(round(4.8 + math.log10(b / a), 2)), n(round(4.8 - math.log10(b / a), 2)), "4,8", n(round(4.8 * b / a, 2)), "pH = pKa + log(n_base/n_acide).") for a, b in [(0.1, 0.2), (0.2, 0.1), (0.05, 0.5)]]
    + [(f"Dosage : à l'équivalence on a versé {Ve} mL de soude à {Cb} mol/L. Quantité d'acide dosée :", sci(Cb * Ve / 1000) + " mol", sci(Cb * Ve) + " mol", sci(Cb / Ve) + " mol", sci(Cb * Ve / 1000 / 2) + " mol", "n = Cb × Ve.") for Ve, Cb in [(12, 0.1), (18.5, 0.02), (25, 0.05)]]
    + [(f"Pour un tampon de pH = {p} à partir du couple de pKa = {pk}, le rapport n(base)/n(acide) vaut :", n(round(10 ** (p - pk), 2)), n(round(10 ** (pk - p), 2)), "1", n(round(p - pk, 2)), "log(n_b/n_a) = pH − pKa.") for p, pk in [(5.8, 4.8), (9.2, 9.2), (4.3, 4.8)]]
)
QCM_TLE_X3_PC = {"tle-pc": M}
