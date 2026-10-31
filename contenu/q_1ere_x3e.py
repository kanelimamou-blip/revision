# QCM de première, volume ×3 (lot E : compléments pour atteindre le triple en maths S et en PC).
from q_tle_plus import _q

QCM_1X_E = {
  "1ere-maths": {
    "Barycentre": _q([
      ("G barycentre de (A, 1) et (B, 1) est :", "le milieu de [AB]", "le point A", "le point B", "hors du segment [AB]", "Poids égaux : milieu."),
      ("G barycentre de (A, 3) et (B, 1) vérifie AG = :", "1/4 AB", "3/4 AB", "1/3 AB", "3 AB", "AG = b/(a + b) AB = 1/4 AB."),
    ]),
    "Angles orientés et rotations": _q([
      ("La mesure principale de 9π/4 est :", "π/4", "9π/4", "−π/4", "π/2", "9π/4 − 2π = π/4."),
      ("La rotation de centre O d'angle −π/2 envoie (0 ; 1) sur :", "(1 ; 0)", "(−1 ; 0)", "(0 ; −1)", "(1 ; 1)", "(x ; y) → (y ; −x)."),
    ]),
    "Dénombrement": _q([
      ("Nombre d'anagrammes du mot « AMI » :", "6", "3", "9", "27", "3! = 6."),
      ("Nombre de poignées de main entre 6 personnes (chacune serre la main de toutes les autres une fois) :", "15", "30", "36", "12", "C(6, 2) = 15."),
    ]),
    "Statistiques": _q([
      ("Série 2, 2, 3, 9 : la médiane vaut :", "2,5", "4", "3", "2", "(2 + 3)/2."),
    ]),
  },
  "1ere-pc": {
    "Calorimétrie": _q([
      ("Un calorimètre de capacité 100 J/°C passe de 20 °C à 30 °C. Il reçoit :", "1 000 J", "100 J", "3 000 J", "10 J", "Q = C Δθ = 100 × 10."),
      ("La fusion de 0,5 kg de glace à 0 °C (L_f = 334 kJ/kg) demande :", "167 kJ", "334 kJ", "668 kJ", "33,4 kJ", "Q = m L_f."),
    ]),
    "Condensateurs": _q([
      ("Trois condensateurs de 3 µF en parallèle équivalent à :", "9 µF", "1 µF", "3 µF", "27 µF", "Somme des capacités."),
      ("Un condensateur porte 6 µC sous 3 V. Sa capacité vaut :", "2 µF", "18 µF", "0,5 µF", "9 µF", "C = q/U."),
    ]),
    "Amplificateur opérationnel": _q([
      ("Un montage inverseur avec R₁ = 10 kΩ et R₂ = 50 kΩ a un gain de :", "−5", "5", "6", "−6", "−R₂/R₁."),
      ("Un montage non inverseur avec R₁ = 10 kΩ et R₂ = 20 kΩ a un gain de :", "3", "2", "−2", "0,5", "1 + R₂/R₁."),
    ]),
  },
}
