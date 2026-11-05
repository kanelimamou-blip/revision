# Première S : devoirs types en plus (2 par trimestre et par matière), rédigés pour l'appli sur le programme officiel, non officiels.
from sujets_dev_common import D, pack, TRIM
L = "1ère S"
def d(s, name, n, exos): t = (n + 1) // 2; return D(f"dev-1ere-{s}-{n}", L, name, n, exos, duration="3 h", label=f"{TRIM[t]} · devoir {2 - n % 2}")

ANNALES_X, GUIDED_X = pack([
  # ================= Mathématiques
  d("maths", "Mathématiques", 1, [
    ("Second degré", "On considère f(x) = 2x² − 4x − 6.", [
      ("Discriminant Δ :", "64", "16", "−32", "40", "Δ = 16 − 4 × 2 × (−6) = 16 + 48."),
      ("Racines :", "−1 et 3", "1 et −3", "−2 et 6", "2 et 3", "x = (4 ± 8) / 4."),
      ("Forme factorisée :", "2(x + 1)(x − 3)", "(x + 1)(x − 3)", "2(x − 1)(x + 3)", "2(x + 3)(x − 1)", "a(x − x₁)(x − x₂)."),
      ("f(x) < 0 pour x ∈", "]−1 ; 3[", "]−∞ ; −1[ ∪ ]3 ; +∞[", "]1 ; 3[", "]−3 ; 1[", "Signe de −a entre les racines (a > 0).")]),
    ("Forme canonique", "On reprend f(x) = 2x² − 4x − 6.", [
      ("Forme canonique :", "2(x − 1)² − 8", "2(x + 1)² − 8", "2(x − 1)² + 8", "(x − 1)² − 8", "α = −b/2a = 1 ; f(1) = −8."),
      ("Sommet de la parabole :", "S(1 ; −8)", "S(−1 ; 8)", "S(1 ; 8)", "S(2 ; −6)", "(α ; β)."),
      ("Minimum de f :", "−8", "−6", "1", "0", "a > 0 : minimum en α."),
      ("Axe de symétrie :", "x = 1", "y = 1", "x = −8", "y = −8", "Droite verticale passant par S.")]),
    ("Équation paramétrée", "On cherche m pour que x² + mx + 4 = 0 ait une racine double.", [
      ("Condition :", "Δ = 0", "Δ > 0", "Δ < 0", "a = 0", "Racine double."),
      ("Δ en fonction de m :", "m² − 16", "m² + 16", "m − 16", "16 − 4m", "b² − 4ac."),
      ("Valeurs de m :", "4 et −4", "16", "2 et −2", "0", "m² = 16."),
      ("Pour m = 4, la racine double est", "−2", "2", "4", "−4", "−b / 2a.")])]),
  d("maths", "Mathématiques", 2, [
    ("Dérivation", "f(x) = x³ − 3x² + 2 sur ℝ.", [
      ("f'(x) =", "3x² − 6x", "3x² − 6x + 2", "x² − 6x", "3x − 6", "Dérivée de xⁿ : n xⁿ⁻¹."),
      ("f'(x) = 0 pour x =", "0 et 2", "0 et 3", "1 et 2", "−2 et 0", "3x(x − 2) = 0."),
      ("f est décroissante sur", "[0 ; 2]", "]−∞ ; 0]", "[2 ; +∞[", "ℝ", "f' < 0 entre les racines."),
      ("Maximum local :", "f(0) = 2", "f(2) = −2", "f(0) = 0", "f(3) = 2", "Changement de signe de f' de + à −.")]),
    ("Tangente", "On reprend f(x) = x³ − 3x² + 2.", [
      ("f(1) =", "0", "2", "−1", "1", "1 − 3 + 2."),
      ("f'(1) =", "−3", "3", "0", "−6", "3 − 6."),
      ("Équation de la tangente en 1 :", "y = −3x + 3", "y = −3x", "y = 3x − 3", "y = −3x − 3", "y = f'(1)(x − 1) + f(1)."),
      ("La tangente est horizontale en", "x = 0 et x = 2", "x = 1", "x = 3", "aucun point", "f'(x) = 0.")]),
    ("Dérivées usuelles", "Calculer les dérivées.", [
      ("(√x)' =", "1/(2√x)", "2√x", "1/√x", "√x/2", "Pour x > 0."),
      ("(1/x)' =", "−1/x²", "1/x²", "ln x", "−1/x", "Pour x ≠ 0."),
      ("(uv)' =", "u'v + uv'", "u'v'", "u'v − uv'", "(u'v − uv')/v²", "Produit."),
      ("((2x + 1)/(x − 1))' =", "−3/(x − 1)²", "3/(x − 1)²", "2/(x − 1)²", "−1/(x − 1)²", "(2(x − 1) − (2x + 1)) / (x − 1)².")])]),
  d("maths", "Mathématiques", 3, [
    ("Suites arithmétiques", "Une association de Kaolack plante 50 arbres la 1re année puis 20 de plus chaque année : u₁ = 50.", [
      ("Nature de la suite :", "arithmétique de raison 20", "géométrique de raison 20", "arithmétique de raison 50", "ni l'une ni l'autre", "On ajoute 20."),
      ("uₙ =", "50 + 20(n − 1)", "50 × 20ⁿ", "20 + 50n", "50 + 20n", "u₁ + (n − 1) r."),
      ("u₁₀ =", "230", "250", "200", "210", "50 + 180."),
      ("Total planté en 10 ans :", "1 400", "2 300", "1 150", "1 200", "10 × (50 + 230) / 2.")]),
    ("Suites géométriques", "Une population de 10 000 habitants augmente de 3 % par an : v₀ = 10 000.", [
      ("Raison :", "1,03", "0,03", "3", "1,3", "Coefficient multiplicateur."),
      ("vₙ =", "10 000 × 1,03ⁿ", "10 000 + 3n", "10 000 × 0,03ⁿ", "10 000 × 1,3ⁿ", "v₀ qⁿ."),
      ("v₂ ≈", "10 609", "10 600", "10 300", "10 900", "10 000 × 1,0609."),
      ("La suite est", "croissante", "décroissante", "constante", "alternée", "q > 1 et v₀ > 0.")]),
    ("Limites", "Calculer les limites.", [
      ("lim (x → +∞) (3x² − x + 1)/(x² + 2) =", "3", "+∞", "0", "1/2", "Rapport des termes de plus haut degré."),
      ("lim (x → 0⁺) 1/x =", "+∞", "−∞", "0", "1", "Inverse d'un nombre petit positif."),
      ("lim (x → +∞) (2x + 1)/(x² + 1) =", "0", "2", "+∞", "1", "Degré du dénominateur plus grand."),
      ("La droite y = 3 pour la 1re fonction est", "une asymptote horizontale", "une asymptote verticale", "une tangente", "un axe de symétrie", "Limite finie en +∞.")])]),
  d("maths", "Mathématiques", 4, [
    ("Produit scalaire", "Dans un repère orthonormé, u→(3 ; −1) et v→(2 ; 6).", [
      ("u→ · v→ =", "0", "12", "−6", "6", "3 × 2 + (−1) × 6."),
      ("Les vecteurs sont", "orthogonaux", "colinéaires", "égaux", "opposés", "Produit scalaire nul."),
      ("‖u→‖ =", "√10", "10", "2", "4", "√(9 + 1)."),
      ("Formule : u→ · v→ =", "‖u→‖ ‖v→‖ cos(u→, v→)", "‖u→‖ + ‖v→‖", "‖u→‖ ‖v→‖ sin(u→, v→)", "u→ × v→", "Définition géométrique.")]),
    ("Applications", "Dans un triangle ABC : AB = 5, AC = 7 et l'angle A = 60°.", [
      ("AB→ · AC→ =", "17,5", "35", "0", "12", "5 × 7 × 1/2."),
      ("Théorème d'Al-Kashi : BC² =", "AB² + AC² − 2 AB·AC cos A", "AB² + AC²", "AB² − AC²", "(AB + AC)²", "Généralise Pythagore."),
      ("BC² =", "39", "74", "49", "109", "25 + 49 − 35."),
      ("BC ≈", "6,24", "8,6", "7", "10,4", "√39.")]),
    ("Trigonométrie", "Résoudre et calculer.", [
      ("cos(π/3) =", "1/2", "√3/2", "√2/2", "0", "Valeur remarquable."),
      ("sin(5π/6) =", "1/2", "−1/2", "√3/2", "−√3/2", "sin(π − π/6) = sin(π/6)."),
      ("cos(2a) =", "cos² a − sin² a", "2 cos a", "2 sin a cos a", "1 + cos a", "Formule de duplication."),
      ("Solutions de cos x = 1/2 dans [0 ; 2π[ :", "π/3 et 5π/3", "π/6 et 5π/6", "π/3 et 2π/3", "π/3 seulement", "Symétrie par rapport à l'axe des abscisses.")])]),
  d("maths", "Mathématiques", 5, [
    ("Probabilités", "Une urne contient 5 boules rouges et 3 vertes. On tire une boule au hasard.", [
      ("P(rouge) =", "5/8", "3/8", "5/3", "1/2", "Cas favorables / cas possibles."),
      ("On tire 2 boules simultanément : nombre de tirages possibles", "28", "56", "64", "16", "C(8, 2) = 28."),
      ("P(2 boules rouges) =", "10/28 = 5/14", "25/64", "5/8", "3/28", "C(5, 2) / C(8, 2)."),
      ("P(au moins une verte) =", "9/14", "5/14", "3/8", "1/2", "1 − 5/14.")]),
    ("Dénombrement", "Un code d'accès a 4 chiffres (0 à 9).", [
      ("Nombre de codes possibles :", "10 000", "5 040", "40", "9 999", "10⁴."),
      ("Codes à 4 chiffres tous différents :", "5 040", "10 000", "210", "24", "10 × 9 × 8 × 7 (arrangements)."),
      ("Façons de choisir 3 délégués parmi 10 élèves :", "120", "720", "30", "1 000", "C(10, 3)."),
      ("5! =", "120", "25", "60", "720", "5 × 4 × 3 × 2 × 1.")]),
    ("Statistiques", "Série : 4 ; 6 ; 6 ; 8 ; 10 ; 14.", [
      ("Moyenne :", "8", "7", "6", "9", "48 / 6."),
      ("Variance :", "32/3 ≈ 10,7", "8", "3,4", "64", "Moyenne des carrés des écarts : (16 + 4 + 4 + 0 + 4 + 36)/6 = 64/6."),
      ("Écart type ≈", "3,27", "10,7", "8", "1,8", "√10,67."),
      ("Médiane :", "7", "6", "8", "10", "(6 + 8) / 2.")])]),
  d("maths", "Mathématiques", 6, [
    ("Barycentre", "G est le barycentre de (A ; 2) et (B ; 1), avec A(0 ; 0) et B(6 ; 3).", [
      ("Coordonnées de G :", "(2 ; 1)", "(4 ; 2)", "(3 ; 1,5)", "(6 ; 3)", "((2 × 0 + 1 × 6)/3 ; (0 + 3)/3)."),
      ("G est situé", "sur [AB], plus près de A", "sur [AB], plus près de B", "au milieu de [AB]", "hors de la droite (AB)", "Poids plus fort en A."),
      ("Relation vectorielle :", "2GA→ + GB→ = 0→", "GA→ + 2GB→ = 0→", "GA→ = GB→", "2GA→ = GB→ + AB→", "Définition."),
      ("Barycentre de (A ; 1) et (B ; 1) :", "le milieu de [AB]", "A", "B", "il n'existe pas", "Poids égaux.")]),
    ("Angles orientés et rotations", "On travaille dans le plan orienté.", [
      ("Mesure principale de 7π/3 :", "π/3", "7π/3", "−π/3", "2π/3", "7π/3 − 2π."),
      ("Image de A(1 ; 0) par la rotation de centre O et d'angle π/2 :", "(0 ; 1)", "(0 ; −1)", "(−1 ; 0)", "(1 ; 1)", "Quart de tour direct."),
      ("Une rotation conserve", "les distances et les angles orientés", "seulement les distances", "seulement l'alignement", "rien", "Déplacement."),
      ("(u→, v→) + (v→, w→) =", "(u→, w→) modulo 2π", "(w→, u→)", "0", "π", "Relation de Chasles.")]),
    ("Étude de fonction rationnelle", "g(x) = (x² + 3)/(x − 1) sur ]1 ; +∞[.", [
      ("g'(x) =", "(x² − 2x − 3)/(x − 1)²", "(x² + 2x + 3)/(x − 1)²", "2x/(x − 1)", "(x² − 3)/(x − 1)²", "(2x(x − 1) − (x² + 3))/(x − 1)²."),
      ("g'(x) = 0 sur ]1 ; +∞[ pour x =", "3", "−1", "1", "2", "x² − 2x − 3 = (x − 3)(x + 1)."),
      ("Minimum de g sur ]1 ; +∞[ :", "g(3) = 6", "g(3) = 3", "g(2) = 7", "g(1) = 4", "(9 + 3)/2."),
      ("lim (x → 1⁺) g(x) =", "+∞", "−∞", "4", "0", "4 / 0⁺.")])]),
  # ================= Physique-Chimie
  d("pc", "Physique-Chimie", 1, [
    ("Travail d'une force", "Un charretier tire une charrette avec une force de 300 N faisant un angle de 30° avec le déplacement de 50 m.", [
      ("W = F × AB × cos α ≈", "12 990 J", "15 000 J", "7 500 J", "0 J", "300 × 50 × 0,866."),
      ("Le travail du poids sur route horizontale :", "nul", "positif", "négatif", "infini", "Poids perpendiculaire au déplacement."),
      ("Un travail résistant est", "négatif", "positif", "nul", "toujours égal au poids", "Force opposée au mouvement."),
      ("Unité du travail :", "joule", "watt", "newton", "pascal", "J = N × m.")]),
    ("Puissance", "Une pompe solaire élève 1 200 kg d'eau de 15 m en 2 min (g = 10 N/kg).", [
      ("Travail du poids de l'eau (montée) :", "−180 000 J", "180 000 J", "18 000 J", "−18 000 J", "W = −m g h."),
      ("Travail fourni par la pompe :", "180 000 J", "18 000 J", "360 000 J", "1 800 J", "Il compense le poids."),
      ("Puissance moyenne :", "1 500 W", "90 000 W", "3 000 W", "150 W", "180 000 / 120."),
      ("1 kWh =", "3,6 × 10⁶ J", "1 000 J", "3 600 J", "3,6 × 10³ J", "1 000 W × 3 600 s.")]),
    ("Énergie cinétique", "Une moto de 150 kg (avec le pilote) roule à 72 km/h.", [
      ("Vitesse en m/s :", "20 m/s", "72 m/s", "7,2 m/s", "36 m/s", "72 / 3,6."),
      ("Énergie cinétique :", "30 000 J", "60 000 J", "3 000 J", "10 800 J", "½ × 150 × 20²."),
      ("Si la vitesse double, Ec est multipliée par", "4", "2", "8", "1/2", "Ec proportionnelle à v²."),
      ("Théorème de l'énergie cinétique : ΔEc =", "somme des travaux des forces", "m g h", "P × t", "F × v", "Énoncé.")])]),
  d("pc", "Physique-Chimie", 2, [
    ("Mouvement de rotation", "Une roue de rayon 0,3 m tourne à 120 tours par minute.", [
      ("Fréquence de rotation :", "2 tr/s", "120 tr/s", "0,5 tr/s", "20 tr/s", "120 / 60."),
      ("Vitesse angulaire :", "4π rad/s", "2π rad/s", "120 rad/s", "π rad/s", "ω = 2π N."),
      ("Vitesse d'un point de la périphérie :", "≈ 3,77 m/s", "≈ 1,2 m/s", "≈ 36 m/s", "≈ 0,6 m/s", "v = R ω = 0,3 × 12,57."),
      ("Moment d'une force de 20 N appliquée tangentiellement à 0,3 m :", "6 N·m", "60 N·m", "0,6 N·m", "66 N·m", "M = F × d.")]),
    ("Champ électrique", "Deux plaques parallèles distantes de 5 cm sont soumises à une tension de 1 000 V.", [
      ("Intensité du champ :", "20 000 V/m", "200 V/m", "50 V/m", "5 000 V/m", "E = U / d = 1 000 / 0,05."),
      ("Le champ est dirigé", "de la plaque + vers la plaque −", "de − vers +", "parallèlement aux plaques", "il n'a pas de direction", "Vers les potentiels décroissants."),
      ("Force sur un électron (e = 1,6 × 10⁻¹⁹ C) :", "3,2 × 10⁻¹⁵ N", "1,6 × 10⁻¹⁹ N", "2 × 10⁴ N", "3,2 × 10⁻¹⁹ N", "F = e E."),
      ("Cette force est dirigée", "vers la plaque +", "vers la plaque −", "parallèlement aux plaques", "vers le bas toujours", "Charge négative : sens opposé au champ.")]),
    ("Loi de Coulomb", "Deux charges q = 2 µC et q' = 3 µC sont à 30 cm (k = 9 × 10⁹ SI).", [
      ("F = k |q q'| / d² =", "0,6 N", "6 N", "0,06 N", "60 N", "9 × 10⁹ × 6 × 10⁻¹² / 0,09."),
      ("Les deux charges", "se repoussent", "s'attirent", "n'interagissent pas", "s'annulent", "Même signe."),
      ("Si la distance double, la force est", "divisée par 4", "divisée par 2", "multipliée par 2", "inchangée", "1/d²."),
      ("Unité de la charge électrique :", "coulomb", "volt", "ampère", "farad", "C.")])]),
  d("pc", "Physique-Chimie", 3, [
    ("Générateurs et effet Joule", "Une pile a une f.é.m. E = 9 V et une résistance interne r = 1 Ω. Elle débite dans un résistor R = 8 Ω.", [
      ("Intensité du courant :", "1 A", "9 A", "1,125 A", "0,9 A", "I = E / (R + r)."),
      ("Tension aux bornes de la pile :", "8 V", "9 V", "1 V", "10 V", "U = E − r I."),
      ("Puissance dissipée par effet Joule dans R :", "8 W", "9 W", "1 W", "64 W", "P = R I²."),
      ("Rendement de la pile :", "≈ 89 %", "100 %", "11 %", "50 %", "U / E = 8/9.")]),
    ("Récepteurs", "Un moteur (E' = 6 V, r' = 2 Ω) est traversé par I = 0,5 A.", [
      ("Tension aux bornes du moteur :", "7 V", "6 V", "5 V", "1 V", "U = E' + r' I."),
      ("Puissance utile :", "3 W", "3,5 W", "0,5 W", "12 W", "E' I."),
      ("Puissance perdue par effet Joule :", "0,5 W", "3 W", "1 W", "2 W", "r' I²."),
      ("Rendement du moteur :", "≈ 86 %", "50 %", "100 %", "14 %", "3 / 3,5.")]),
    ("Condensateurs", "Un condensateur de capacité C = 100 µF est chargé sous 12 V.", [
      ("Charge Q :", "1,2 × 10⁻³ C", "1 200 C", "8,3 × 10⁻⁶ C", "0,12 C", "Q = C U."),
      ("Énergie stockée :", "7,2 × 10⁻³ J", "1,44 J", "0,6 J", "7,2 J", "½ C U²."),
      ("Deux condensateurs identiques en parallèle : capacité totale", "200 µF", "50 µF", "100 µF", "10 000 µF", "Les capacités s'ajoutent."),
      ("En série : capacité totale", "50 µF", "200 µF", "100 µF", "25 µF", "1/C = 1/C₁ + 1/C₂.")])]),
  d("pc", "Physique-Chimie", 4, [
    ("Hydrocarbures", "On étudie le butane C₄H₁₀, gaz des bouteilles domestiques.", [
      ("Famille :", "alcanes", "alcènes", "alcynes", "alcools", "CₙH₂ₙ₊₂."),
      ("Masse molaire (C = 12 ; H = 1) :", "58 g/mol", "56 g/mol", "48 g/mol", "60 g/mol", "4 × 12 + 10."),
      ("Équation de combustion complète : 2 C₄H₁₀ + … O₂ → 8 CO₂ + 10 H₂O", "13", "9", "26", "6,5", "16 + 10 = 26 atomes O, donc 13 O₂."),
      ("Isomère du butane :", "le méthylpropane", "le propane", "le butène", "l'éthane", "Même formule brute, chaîne ramifiée.")]),
    ("Alcènes et polymères", "L'éthylène C₂H₄ sert à fabriquer le polyéthylène des sachets.", [
      ("L'éthylène est un", "alcène", "alcane", "alcool", "acide", "Double liaison C=C."),
      ("Réaction de formation du polyéthylène :", "polymérisation", "combustion", "estérification", "oxydation ménagée", "Addition de nombreux monomères."),
      ("Addition de H₂ sur l'éthylène donne", "l'éthane", "l'éthanol", "le méthane", "l'éthyne", "Hydrogénation."),
      ("Problème environnemental des sachets :", "ils se dégradent très lentement", "ils sont trop chers", "ils sont toxiques à toucher", "ils fondent au soleil", "Pollution durable.")]),
    ("Alcools et acides", "On étudie l'éthanol C₂H₅OH.", [
      ("Groupe caractéristique des alcools :", "−OH (hydroxyle)", "−COOH", "−CHO", "−NH₂", "Définition."),
      ("Oxydation ménagée de l'éthanol (en excès d'oxydant) donne", "l'acide éthanoïque", "le méthanol", "l'éthane", "le propanol", "Alcool primaire → aldéhyde → acide."),
      ("Alcool + acide carboxylique donne", "un ester et de l'eau", "un alcane", "un sel", "du dioxygène", "Estérification."),
      ("L'éthanol est un alcool", "primaire", "secondaire", "tertiaire", "aromatique", "Carbone fonctionnel lié à 1 seul carbone.")])]),
  d("pc", "Physique-Chimie", 5, [
    ("Oxydoréduction", "On plonge une lame de zinc dans une solution de sulfate de cuivre.", [
      ("Dépôt observé sur le zinc :", "du cuivre", "du zinc", "du fer", "du soufre", "Les ions Cu²⁺ sont réduits."),
      ("Le zinc est", "oxydé", "réduit", "inchangé", "dissous sans réaction", "Zn → Zn²⁺ + 2e⁻."),
      ("Équation bilan :", "Zn + Cu²⁺ → Zn²⁺ + Cu", "Cu + Zn²⁺ → Cu²⁺ + Zn", "Zn + Cu → ZnCu", "Zn²⁺ + Cu²⁺ → Zn + Cu", "Transfert d'électrons."),
      ("La couleur bleue de la solution", "s'atténue", "s'intensifie", "devient rouge", "ne change pas", "Les ions Cu²⁺ disparaissent.")]),
    ("Piles", "Pile Daniell : Zn | Zn²⁺ || Cu²⁺ | Cu.", [
      ("Pôle négatif :", "le zinc", "le cuivre", "le pont salin", "la solution", "Siège de l'oxydation."),
      ("Les électrons circulent dans le circuit extérieur", "du zinc vers le cuivre", "du cuivre vers le zinc", "dans le pont salin", "dans les deux sens", "Du pôle − vers le pôle +."),
      ("Rôle du pont salin :", "assurer la neutralité électrique et fermer le circuit", "produire des électrons", "servir de pôle +", "arrêter la réaction", "Migration des ions."),
      ("Quand la pile est usée,", "un des réactifs est épuisé", "le pont salin est plein de cuivre", "les électrons s'arrêtent seuls", "la tension augmente", "Fin de la réaction.")]),
    ("Dosage d'oxydoréduction", "On dose 20 mL de Fe²⁺ par du permanganate (MnO₄⁻ + 5 Fe²⁺ + 8 H⁺ → Mn²⁺ + 5 Fe³⁺ + 4 H₂O) à 0,02 mol/L ; équivalence pour 10 mL.", [
      ("Quantité de MnO₄⁻ versée :", "2 × 10⁻⁴ mol", "2 × 10⁻² mol", "0,2 mol", "10⁻⁴ mol", "0,02 × 0,010."),
      ("Quantité de Fe²⁺ :", "10⁻³ mol", "2 × 10⁻⁴ mol", "4 × 10⁻⁵ mol", "5 × 10⁻³ mol", "5 × 2 × 10⁻⁴."),
      ("Concentration de Fe²⁺ :", "0,05 mol/L", "0,01 mol/L", "0,5 mol/L", "0,02 mol/L", "10⁻³ / 0,020."),
      ("L'équivalence se repère par", "la persistance de la couleur violette", "un précipité blanc", "un dégagement gazeux", "la décoloration de l'eau", "MnO₄⁻ n'est plus réduit.")])]),
  d("pc", "Physique-Chimie", 6, [
    ("Calorimétrie", "On mélange 200 g d'eau à 20 °C et 100 g d'eau à 80 °C (c = 4 185 J/(kg·°C), calorimètre négligé).", [
      ("Température d'équilibre :", "40 °C", "50 °C", "60 °C", "30 °C", "(200 × 20 + 100 × 80) / 300."),
      ("Chaleur reçue par l'eau froide :", "≈ 16 740 J", "≈ 25 110 J", "≈ 8 370 J", "≈ 41 850 J", "0,2 × 4 185 × 20."),
      ("Chaleur cédée par l'eau chaude :", "≈ −16 740 J", "≈ 16 740 J", "≈ −25 110 J", "0 J", "0,1 × 4 185 × (40 − 80)."),
      ("Principe utilisé :", "la somme des chaleurs échangées est nulle", "la chaleur se crée", "la température s'additionne", "la masse se conserve seule", "Système isolé.")]),
    ("Changement d'état", "On fait fondre 50 g de glace à 0 °C (Lf = 330 kJ/kg).", [
      ("Chaleur nécessaire :", "16 500 J", "330 J", "6 600 J", "165 000 J", "Q = m Lf = 0,05 × 330 000."),
      ("Pendant la fusion, la température", "reste constante", "augmente", "diminue", "varie au hasard", "Palier de changement d'état."),
      ("La solidification", "libère de la chaleur", "absorbe de la chaleur", "n'échange rien", "est impossible", "Inverse de la fusion."),
      ("Unité de la capacité thermique massique :", "J/(kg·°C)", "J/kg", "W/°C", "°C/J", "Définition.")]),
    ("Amplificateur opérationnel", "Montage inverseur idéal avec R₁ = 10 kΩ et R₂ = 50 kΩ.", [
      ("Gain en tension :", "−5", "5", "−0,2", "6", "−R₂ / R₁."),
      ("Avec Ue = 0,4 V : Us =", "−2 V", "2 V", "0,4 V", "−0,08 V", "−5 × 0,4."),
      ("En fonctionnement linéaire idéal, ε =", "0", "Ue", "Us", "15 V", "V⁺ = V⁻."),
      ("Les courants d'entrée de l'AO idéal sont", "nuls", "infinis", "égaux à Us/R₂", "égaux à 1 A", "Impédance d'entrée infinie.")])]),
  # ================= SVT
  d("svt", "SVT", 1, [
    ("Tectonique des plaques", "On étudie la carte des séismes et des volcans du monde.", [
      ("Les séismes se concentrent", "aux limites des plaques", "au centre des plaques", "uniquement en Afrique", "au hasard", "Zones actives."),
      ("Au niveau d'une dorsale, les plaques", "s'écartent", "se rapprochent", "coulissent seulement", "restent immobiles", "Accrétion."),
      ("Une zone de subduction est une zone où", "une plaque plonge sous une autre", "deux plaques s'écartent", "il n'y a pas de séisme", "se forme une dorsale", "Convergence."),
      ("Moteur du mouvement des plaques :", "la convection dans le manteau", "le vent", "les marées seulement", "la rotation de la Lune", "Chaleur interne.")]),
    ("Structure du globe", "On étudie la propagation des ondes sismiques.", [
      ("Couche la plus externe :", "la croûte", "le manteau", "le noyau", "la graine", "Ordre."),
      ("La lithosphère comprend", "la croûte et le manteau supérieur rigide", "le noyau seul", "l'asthénosphère seule", "l'atmosphère", "Plaques lithosphériques."),
      ("Le noyau externe est", "liquide", "solide", "gazeux", "en roche granitique", "Les ondes S ne le traversent pas."),
      ("Discontinuité croûte-manteau :", "Moho", "Gutenberg", "Lehmann", "Richter", "Mohorovičić.")]),
    ("Géologie du Sénégal", "On observe la carte géologique du Sénégal.", [
      ("La plus grande partie du Sénégal est", "un bassin sédimentaire", "une chaîne de montagnes", "un volcan actif", "un socle granitique uniquement", "Bassin sénégalo-mauritanien."),
      ("Roches anciennes du socle :", "au sud-est (Kédougou)", "à Dakar", "à Saint-Louis", "à Louga", "Socle birimien."),
      ("Volcanisme ancien visible :", "presqu'île du Cap-Vert (Mamelles)", "Kédougou", "Tambacounda", "Matam", "Volcanisme du Cap-Vert."),
      ("Les phosphates de Taïba sont des roches", "sédimentaires", "magmatiques", "métamorphiques", "volcaniques", "Origine marine.")])]),
  d("svt", "SVT", 2, [
    ("Le réflexe", "On frappe le tendon sous la rotule : la jambe se lève (réflexe rotulien).", [
      ("Ce réflexe est", "inné et involontaire", "appris", "volontaire", "conditionnel", "Réflexe myotatique."),
      ("Centre nerveux du réflexe :", "la moelle épinière", "le cerveau", "le cœur", "le muscle", "Arc réflexe."),
      ("Ordre de l'arc réflexe :", "récepteur, nerf sensitif, centre, nerf moteur, effecteur", "effecteur, centre, récepteur", "cerveau, muscle, peau", "nerf moteur, récepteur, centre", "Trajet du message."),
      ("Effecteur :", "le muscle de la cuisse", "le tendon", "la moelle", "la peau", "Il se contracte.")]),
    ("Le message nerveux", "On enregistre l'activité d'une fibre nerveuse.", [
      ("Potentiel de repos d'un neurone :", "environ −70 mV", "0 mV", "+70 mV", "+30 V", "Intérieur négatif."),
      ("Le message nerveux est codé en", "fréquence de potentiels d'action", "amplitude variable", "couleur", "température", "Amplitude constante."),
      ("Zone de contact entre deux neurones :", "la synapse", "l'axone", "le noyau", "la gaine", "Transmission chimique."),
      ("Substance libérée dans la synapse :", "un neurotransmetteur", "une enzyme digestive", "de l'hémoglobine", "du glucose", "Ex. acétylcholine.")]),
    ("Le cerveau", "On étudie le rôle du cerveau.", [
      ("Les mouvements volontaires sont commandés par", "le cortex moteur", "la moelle seule", "le cervelet seulement", "le cœur", "Aire motrice."),
      ("Hémisphère gauche commande", "le côté droit du corps", "le côté gauche", "les deux côtés", "aucun côté", "Croisement des voies."),
      ("Drogues et alcool", "perturbent la transmission synaptique", "renforcent la mémoire", "n'ont aucun effet", "guérissent les neurones", "Hygiène du système nerveux."),
      ("Le cervelet intervient dans", "l'équilibre et la coordination", "la digestion", "la vision seule", "la respiration seule", "Rôle.")])]),
  d("svt", "SVT", 3, [
    ("Le muscle", "On observe un muscle squelettique.", [
      ("Unité de contraction :", "le sarcomère", "le noyau", "la mitochondrie", "le tendon", "Myofibrille."),
      ("Protéines contractiles :", "actine et myosine", "hémoglobine et insuline", "amylase et lipase", "kératine", "Glissement des filaments."),
      ("Lors de la contraction, le sarcomère", "raccourcit", "s'allonge", "disparaît", "se divise", "Filaments qui glissent."),
      ("Ion nécessaire à la contraction :", "Ca²⁺", "Na⁺ seulement", "Cl⁻", "Fe²⁺", "Libéré par le réticulum.")]),
    ("L'énergie musculaire", "Un coureur fait un 100 m puis un marathon.", [
      ("Molécule énergétique directement utilisée :", "l'ATP", "le glucose", "l'amidon", "l'ADN", "Hydrolyse de l'ATP."),
      ("Voie principale lors d'un effort long :", "la respiration (aérobie)", "la fermentation lactique seule", "la phosphocréatine seule", "aucune", "Rendement élevé."),
      ("Lors d'un effort bref et intense, produit qui s'accumule :", "l'acide lactique (lactate)", "l'éthanol", "le dioxygène", "l'amidon", "Fermentation lactique."),
      ("Lors d'un effort, la fréquence cardiaque", "augmente", "diminue", "reste nulle", "ne change jamais", "Apport de dioxygène.")]),
    ("Expérience", "On mesure la consommation de dioxygène d'un élève au repos (0,3 L/min) et pendant l'effort (2,1 L/min).", [
      ("Consommation multipliée par", "7", "3", "2,1", "0,7", "2,1 / 0,3."),
      ("Ce dioxygène sert à", "produire de l'ATP par respiration", "fabriquer du glucose", "former des muscles nouveaux", "rien", "Respiration cellulaire."),
      ("Le dioxygène est transporté par", "l'hémoglobine des globules rouges", "les plaquettes", "le plasma seulement", "les globules blancs", "Transport sanguin."),
      ("Un entraînement régulier", "améliore la capacité aérobie", "réduit le cœur", "supprime la respiration", "n'a aucun effet", "Adaptation.")])]),
  d("svt", "SVT", 4, [
    ("Le sang et le milieu intérieur", "On analyse le sang d'un élève.", [
      ("Le milieu intérieur comprend", "le sang, la lymphe et le liquide interstitiel", "seulement le sang", "l'air des poumons", "le contenu de l'estomac", "Liquides qui baignent les cellules."),
      ("Cellules qui défendent l'organisme :", "les globules blancs", "les globules rouges", "les plaquettes", "les neurones", "Immunité."),
      ("Rôle des plaquettes :", "la coagulation", "le transport du dioxygène", "la digestion", "la production d'anticorps", "Arrêt des saignements."),
      ("Un manque d'hémoglobine provoque", "une anémie", "un diabète", "une hypertension", "une fracture", "Fatigue, pâleur.")]),
    ("La glycémie", "La glycémie normale à jeun est d'environ 1 g/L.", [
      ("Hormone hypoglycémiante :", "l'insuline", "le glucagon", "l'adrénaline", "la thyroxine", "Fait baisser la glycémie."),
      ("Organe qui produit l'insuline :", "le pancréas", "le foie", "le rein", "l'estomac", "Îlots de Langerhans."),
      ("Après un repas, le foie stocke le glucose sous forme de", "glycogène", "amidon", "protéines", "lipides seulement", "Mise en réserve."),
      ("Glycémie à jeun de 1,4 g/L à plusieurs reprises :", "signe de diabète", "normale", "hypoglycémie", "anémie", "Hyperglycémie chronique.")]),
    ("Le rein", "On compare la composition du plasma et de l'urine.", [
      ("Unité fonctionnelle du rein :", "le néphron", "le neurone", "l'alvéole", "le sarcomère", "Filtration."),
      ("Normalement absent de l'urine :", "le glucose", "l'urée", "l'eau", "les sels minéraux", "Réabsorbé totalement."),
      ("L'urée est", "un déchet azoté", "un sucre", "une hormone", "une enzyme", "Issu des protéines."),
      ("Le rein participe à", "l'équilibre en eau et en sels du milieu intérieur", "la digestion", "la contraction musculaire", "la vision", "Homéostasie.")])]),
  d("svt", "SVT", 5, [
    ("Roches magmatiques", "On compare le granite et le basalte.", [
      ("Le granite a une structure", "grenue (gros cristaux)", "microlitique", "vitreuse", "litée", "Refroidissement lent en profondeur."),
      ("Le basalte est une roche", "volcanique", "plutonique", "sédimentaire", "métamorphique", "Refroidissement rapide en surface."),
      ("Minéraux du granite :", "quartz, feldspath, mica", "calcite seule", "argile", "sel", "Composition."),
      ("Le basalte de Dakar provient", "du volcanisme du Cap-Vert", "du socle de Kédougou", "de la mer actuelle", "d'une météorite", "Géologie locale.")]),
    ("Métamorphisme", "On étudie la transformation des roches.", [
      ("Le métamorphisme se produit sous l'effet de", "la température et la pression", "la pluie", "le vent", "les êtres vivants", "Transformation à l'état solide."),
      ("Une argile devient par métamorphisme", "un schiste puis un gneiss", "un basalte", "un calcaire", "du sable", "Série métamorphique."),
      ("Le calcaire métamorphisé donne", "le marbre", "le granite", "le grès", "le charbon", "Recristallisation."),
      ("Le métamorphisme se fait", "sans fusion de la roche", "en fondant totalement la roche", "à l'air libre", "seulement au fond de la mer", "Sinon c'est du magmatisme.")]),
    ("Cycle des roches", "On construit le cycle des roches.", [
      ("Une roche sédimentaire se forme par", "dépôt et compaction de sédiments", "refroidissement de magma", "fusion", "métamorphisme", "Diagenèse."),
      ("L'érosion transforme les roches en", "sédiments", "magma", "marbre", "cristaux de quartz purs", "Altération."),
      ("La fusion d'une roche donne", "un magma", "un sédiment", "un fossile", "une argile", "Anatexie."),
      ("Les fossiles se trouvent surtout dans les roches", "sédimentaires", "magmatiques", "métamorphiques de haut degré", "volcaniques", "Conservation.")])]),
  d("svt", "SVT", 6, [
    ("Synthèse : communication nerveuse et hormonale", "On compare deux modes de communication.", [
      ("Le message nerveux est", "rapide et localisé", "lent et diffus", "transporté par le sang", "toujours chimique dans l'axone", "Neurones."),
      ("Le message hormonal est transporté par", "le sang", "les nerfs", "les muscles", "la lymphe seulement", "Hormones."),
      ("Exemple d'hormone :", "l'insuline", "l'acétylcholine", "l'amylase", "l'hémoglobine", "Pancréas."),
      ("Une cellule cible possède", "des récepteurs spécifiques", "des chloroplastes", "une paroi", "un flagelle obligatoire", "Reconnaissance de l'hormone.")]),
    ("Synthèse : géologie", "Révision de géologie.", [
      ("Les plaques se déplacent de quelques", "centimètres par an", "kilomètres par jour", "mètres par heure", "millimètres par siècle", "Vitesse."),
      ("Chaîne de montagnes née d'une collision :", "l'Himalaya", "la dorsale atlantique", "le rift est-africain", "le Sahara", "Inde contre Asie."),
      ("Le rift est-africain est une zone", "d'écartement", "de collision", "de subduction", "inactive", "L'Afrique se fracture."),
      ("Roche formée en profondeur par refroidissement lent :", "le granite", "le basalte", "le calcaire", "le grès", "Plutonique.")]),
    ("Synthèse : santé", "Conseils de santé.", [
      ("Pour éviter le diabète de type 2 :", "alimentation équilibrée et activité physique", "manger très sucré", "dormir moins", "ne plus boire d'eau", "Prévention."),
      ("Boire assez d'eau aide", "le rein à éliminer les déchets", "le cerveau à grossir", "le sang à coaguler", "rien", "Hydratation."),
      ("Échauffement avant l'effort :", "prépare muscles et articulations", "inutile", "dangereux", "réduit la respiration", "Prévention des blessures."),
      ("Le dopage", "est dangereux et interdit", "améliore la santé", "est recommandé", "n'a aucun effet", "Éthique sportive.")])]),
])
