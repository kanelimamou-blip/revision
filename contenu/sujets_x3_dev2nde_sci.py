# Seconde S : devoirs types (2 par trimestre et par matière), rédigés pour l'appli sur le programme officiel, non officiels.
from sujets_dev_common import D, pack, TRIM
L = "2nde S"
def d(s, name, n, exos): t = (n + 1) // 2; return D(f"dev-2nde-{s}-{n}", L, name, n, exos, label=f"{TRIM[t]} · devoir {2 - n % 2}")

ANNALES_X, GUIDED_X = pack([
  # ================= Mathématiques
  d("maths", "Mathématiques", 1, [
    ("Calcul dans ℝ", "On donne A = √50 − 3√8 + √18 et B = (2 − √3)(2 + √3).", [
      ("√50 =", "5√2", "25√2", "2√5", "10√5", "√50 = √(25 × 2) = 5√2."),
      ("A =", "2√2", "4√2", "14√2", "−2√2", "5√2 − 6√2 + 3√2 = 2√2."),
      ("B =", "1", "4 − √3", "7", "−1", "(a − b)(a + b) = a² − b² = 4 − 3."),
      ("1/(2 − √3) =", "2 + √3", "2 − √3", "1/2 − √3", "(2 + √3)/7", "On multiplie par la quantité conjuguée : (2 + √3)/1.")]),
    ("Valeur absolue et intervalles", "On s'intéresse aux réels x tels que |x − 3| ≤ 2.", [
      ("|x − 3| est", "la distance entre x et 3", "la distance entre x et −3", "toujours égal à x − 3", "toujours négatif", "Définition géométrique."),
      ("|x − 3| ≤ 2 équivaut à x ∈", "[1 ; 5]", "[−5 ; −1]", "]1 ; 5[", "[−2 ; 2]", "3 − 2 ≤ x ≤ 3 + 2."),
      ("[1 ; 5] ∩ [4 ; 8] =", "[4 ; 5]", "[1 ; 8]", "[5 ; 8]", "∅", "Partie commune."),
      ("|−7| + |2 − 5| =", "10", "4", "−10", "−4", "7 + 3.")]),
    ("Équations", "Résoudre dans ℝ.", [
      ("Solution de 3x − 7 = 2x + 5 :", "x = 12", "x = −12", "x = 2", "x = −2", "3x − 2x = 5 + 7."),
      ("Solutions de (x − 2)(2x + 6) = 0 :", "2 et −3", "−2 et 3", "2 et 6", "2 et −6", "Produit nul : x = 2 ou x = −3."),
      ("Solutions de x² = 49 :", "7 et −7", "7", "49", "√7 et −√7", "x = ±√49."),
      ("L'équation x² = −4 a", "aucune solution réelle", "deux solutions", "une solution", "une infinité de solutions", "Un carré n'est jamais négatif.")])]),
  d("maths", "Mathématiques", 2, [
    ("Inéquations", "Résoudre dans ℝ.", [
      ("−2x + 6 > 0 équivaut à", "x < 3", "x > 3", "x < −3", "x > −3", "On divise par −2 : le sens change."),
      ("Ensemble des solutions de 3x − 1 ≤ 5 :", "]−∞ ; 2]", "[2 ; +∞[", "]−∞ ; 2[", "]−∞ ; 4/3]", "3x ≤ 6."),
      ("Signe de (x − 1)(x + 2) pour x = 0 :", "négatif", "positif", "nul", "on ne peut pas savoir", "(−1) × 2 = −2."),
      ("(x − 1)(x + 2) < 0 pour x ∈", "]−2 ; 1[", "]−∞ ; −2[", "]1 ; +∞[", "]−1 ; 2[", "Tableau de signes : négatif entre les racines.")]),
    ("Fonctions affines", "f est la fonction affine telle que f(0) = −1 et f(2) = 5.", [
      ("Coefficient directeur de f :", "3", "2", "−3", "6", "(5 − (−1)) / (2 − 0) = 3."),
      ("Expression de f(x) :", "3x − 1", "3x + 1", "2x − 1", "−x + 3", "f(x) = ax + b avec b = f(0)."),
      ("f(x) = 0 pour x =", "1/3", "−1/3", "3", "1", "3x − 1 = 0."),
      ("Sens de variation de f :", "croissante sur ℝ", "décroissante sur ℝ", "constante", "croissante puis décroissante", "a = 3 > 0.")]),
    ("Fonctions de référence", "On étudie la fonction carré et la fonction inverse.", [
      ("La fonction carré est décroissante sur", "]−∞ ; 0]", "[0 ; +∞[", "ℝ", "]0 ; +∞[", "Sa courbe est une parabole de sommet O."),
      ("Si 2 < x < 3, alors x² est compris entre", "4 et 9", "2 et 3", "4 et 6", "−9 et −4", "La fonction carré est croissante sur [0 ; +∞[."),
      ("Ensemble de définition de x ↦ 1/x :", "ℝ*", "ℝ", "[0 ; +∞[", "]0 ; +∞[ seulement", "On ne divise pas par 0."),
      ("Si 2 ≤ x ≤ 4, alors 1/x est compris entre", "1/4 et 1/2", "2 et 4", "1/2 et 1/4 avec 1/2 ≤ 1/x", "−4 et −2", "La fonction inverse est décroissante sur ]0 ; +∞[ : 1/4 ≤ 1/x ≤ 1/2.")])]),
  d("maths", "Mathématiques", 3, [
    ("Vecteurs et repérage", "Dans un repère, A(1 ; 2), B(5 ; 4) et C(3 ; 7).", [
      ("Coordonnées de AB→ :", "(4 ; 2)", "(6 ; 6)", "(−4 ; −2)", "(4 ; 6)", "(5 − 1 ; 4 − 2)."),
      ("Milieu I de [AB] :", "(3 ; 3)", "(6 ; 6)", "(2 ; 1)", "(4 ; 2)", "((1 + 5)/2 ; (2 + 4)/2)."),
      ("Longueur AB :", "2√5", "√20/2", "20", "6", "√(4² + 2²) = √20 = 2√5."),
      ("D tel que ABCD soit un parallélogramme :", "(−1 ; 5)", "(7 ; 9)", "(3 ; 3)", "(−1 ; −5)", "AB→ = DC→ : D = C − AB→ = (3 − 4 ; 7 − 2).")]),
    ("Droites", "On considère la droite (d) : y = 2x − 3 et le point E(4 ; 5).", [
      ("E appartient-il à (d) ?", "oui", "non", "seulement si x = 0", "on ne peut pas savoir", "2 × 4 − 3 = 5."),
      ("Coefficient directeur de (d) :", "2", "−3", "3", "1/2", "y = mx + p."),
      ("Droite parallèle à (d) passant par O :", "y = 2x", "y = −2x", "y = x/2", "y = 2x − 3", "Même coefficient directeur."),
      ("Point d'intersection de (d) avec l'axe des abscisses :", "(1,5 ; 0)", "(0 ; −3)", "(3 ; 0)", "(−1,5 ; 0)", "2x − 3 = 0.")]),
    ("Trigonométrie", "Le triangle ABC est rectangle en A, avec AB = 6 cm et l'angle B = 30°.", [
      ("cos 30° =", "√3/2", "1/2", "√2/2", "√3", "Valeur remarquable."),
      ("BC = AB / cos B =", "4√3 cm", "3√3 cm", "12 cm", "6√3 cm", "6 / (√3/2) = 12/√3 = 4√3."),
      ("AC = AB × tan B =", "2√3 cm", "6√3 cm", "3 cm", "√3 cm", "6 × (√3/3)."),
      ("Pour tout angle x : cos² x + sin² x =", "1", "0", "2", "tan x", "Relation fondamentale.")])]),
  d("maths", "Mathématiques", 4, [
    ("Pourcentages", "Le prix d'un sac de riz de 25 kg passe de 12 500 F à 13 750 F.", [
      ("Augmentation en francs :", "1 250 F", "1 375 F", "125 F", "12 500 F", "13 750 − 12 500."),
      ("Taux d'augmentation :", "10 %", "12,5 %", "9 %", "1,25 %", "1 250 / 12 500."),
      ("Coefficient multiplicateur :", "1,1", "0,9", "1,01", "10", "1 + 10/100."),
      ("Après une baisse de 10 % du nouveau prix :", "12 375 F", "12 500 F", "12 250 F", "13 625 F", "13 750 × 0,9 : on ne revient pas au prix de départ.")]),
    ("Statistiques", "Notes d'un groupe : 8 ; 10 ; 10 ; 12 ; 13 ; 14 ; 15.", [
      ("Moyenne :", "≈ 11,7", "12", "10", "13", "82 / 7 ≈ 11,71."),
      ("Médiane :", "12", "10", "11,7", "13", "Valeur du milieu (4e sur 7)."),
      ("Étendue :", "7", "15", "8", "6", "15 − 8."),
      ("Mode :", "10", "12", "15", "8", "Valeur la plus fréquente.")]),
    ("Polynômes", "On donne P(x) = x² − 5x + 6.", [
      ("P(2) =", "0", "4", "−4", "20", "4 − 10 + 6."),
      ("Factorisation de P(x) :", "(x − 2)(x − 3)", "(x + 2)(x + 3)", "(x − 1)(x − 6)", "(x − 2)(x + 3)", "Racines 2 et 3."),
      ("Degré de P :", "2", "1", "3", "6", "Le terme de plus haut degré est x²."),
      ("Valeur interdite de F(x) = P(x)/(x − 1) :", "1", "2", "3", "0", "Le dénominateur s'annule pour x = 1.")])]),
  d("maths", "Mathématiques", 5, [
    ("Transformations du plan", "Dans un repère, A(2 ; 1).", [
      ("Image de A par la symétrie de centre O :", "(−2 ; −1)", "(2 ; −1)", "(−2 ; 1)", "(1 ; 2)", "On change les deux signes."),
      ("Image de A par la translation de vecteur u→(3 ; −4) :", "(5 ; −3)", "(−1 ; 5)", "(6 ; −4)", "(5 ; 5)", "(2 + 3 ; 1 − 4)."),
      ("Image de A par l'homothétie de centre O et de rapport 3 :", "(6 ; 3)", "(5 ; 4)", "(2/3 ; 1/3)", "(−6 ; −3)", "On multiplie par 3."),
      ("Une translation conserve", "les longueurs et les angles", "seulement les angles", "seulement l'alignement", "rien", "C'est une isométrie.")]),
    ("Cercles", "Le cercle (C) a pour centre Ω(1 ; −2) et passe par A(4 ; 2).", [
      ("Rayon de (C) :", "5", "25", "7", "√7", "√(3² + 4²) = 5."),
      ("Une équation de (C) :", "(x − 1)² + (y + 2)² = 25", "(x + 1)² + (y − 2)² = 25", "(x − 1)² + (y + 2)² = 5", "x² + y² = 25", "(x − a)² + (y − b)² = r²."),
      ("Le point B(1 ; 3) est", "sur le cercle", "à l'intérieur", "à l'extérieur", "le centre", "ΩB = |3 − (−2)| = 5."),
      ("La tangente en A est", "perpendiculaire à (ΩA)", "parallèle à (ΩA)", "confondue avec (ΩA)", "parallèle à l'axe des abscisses", "Propriété de la tangente.")]),
    ("Équations de droites", "On donne A(−1 ; 2) et B(3 ; 10).", [
      ("Coefficient directeur de (AB) :", "2", "8", "1/2", "−2", "(10 − 2) / (3 + 1)."),
      ("Équation réduite de (AB) :", "y = 2x + 4", "y = 2x + 2", "y = 8x + 10", "y = x/2 + 4", "y = 2x + p avec 2 = −2 + p."),
      ("Droite perpendiculaire à (AB) : coefficient directeur", "−1/2", "2", "−2", "1/2", "m × m' = −1 dans un repère orthonormé."),
      ("Le point C(0 ; 4) est", "sur (AB)", "au-dessus de (AB)", "au-dessous de (AB)", "le milieu de [AB]", "2 × 0 + 4 = 4.")])]),
  d("maths", "Mathématiques", 6, [
    ("Géométrie dans l'espace", "Un cube ABCDEFGH a des arêtes de 4 cm.", [
      ("Volume du cube :", "64 cm³", "16 cm³", "48 cm³", "96 cm³", "4³."),
      ("Longueur d'une diagonale de face :", "4√2 cm", "4√3 cm", "8 cm", "16 cm", "Pythagore dans un carré."),
      ("Longueur de la grande diagonale [AG] :", "4√3 cm", "4√2 cm", "12 cm", "8 cm", "√(4² + 4² + 4²)."),
      ("Les droites (AB) et (GH) sont", "parallèles", "sécantes", "non coplanaires", "perpendiculaires", "(GH) est parallèle à (EF), elle-même parallèle à (AB).")]),
    ("Volumes", "Un château d'eau a une cuve cylindrique de rayon 3 m et de hauteur 5 m (π ≈ 3,14).", [
      ("Volume de la cuve :", "≈ 141,3 m³", "≈ 47,1 m³", "≈ 94,2 m³", "≈ 15 m³", "π × 3² × 5."),
      ("En litres :", "≈ 141 300 L", "≈ 14 130 L", "≈ 1 413 L", "≈ 1 413 000 L", "1 m³ = 1 000 L."),
      ("Un cône de même base et même hauteur a un volume", "3 fois plus petit", "2 fois plus petit", "égal", "3 fois plus grand", "V = (1/3) B h."),
      ("Si on double le rayon, le volume est multiplié par", "4", "2", "8", "6", "Le rayon est au carré.")]),
    ("Fonctions et problème", "Un vendeur de jus gagne B(x) = −x² + 40x − 300 francs (en centaines) pour x bouteilles.", [
      ("B(10) =", "0", "100", "−100", "300", "−100 + 400 − 300."),
      ("Forme canonique : B(x) =", "−(x − 20)² + 100", "−(x + 20)² + 100", "(x − 20)² − 100", "−(x − 20)² − 300", "−(x² − 40x + 400) + 400 − 300."),
      ("Bénéfice maximal pour x =", "20", "10", "40", "30", "Sommet de la parabole."),
      ("Bénéfice maximal :", "100", "300", "400", "20", "B(20) = 100.")])]),
  # ================= Sciences physiques
  d("pc", "Physique-Chimie", 1, [
    ("Structure de l'atome", "L'atome d'aluminium est noté ²⁷₁₃Al.", [
      ("Nombre de protons :", "13", "27", "14", "40", "Z = 13."),
      ("Nombre de neutrons :", "14", "13", "27", "40", "A − Z = 27 − 13."),
      ("Répartition électronique :", "K² L⁸ M³", "K² L⁸ M⁸", "K² L¹¹", "K³ L⁸ M²", "13 électrons : 2 + 8 + 3."),
      ("Ion formé le plus probablement :", "Al³⁺", "Al³⁻", "Al⁺", "Al²⁻", "Il perd ses 3 électrons de valence.")]),
    ("Classification périodique", "On considère le sodium (Z = 11) et le chlore (Z = 17).", [
      ("Le sodium est dans la colonne", "1 (métaux alcalins)", "17 (halogènes)", "18 (gaz nobles)", "2", "Un électron de valence."),
      ("Le chlore est dans la", "3e période", "2e période", "1re période", "4e période", "Trois couches : K² L⁸ M⁷."),
      ("Ion chlorure :", "Cl⁻", "Cl⁺", "Cl²⁻", "Cl⁷⁺", "Il gagne un électron (règle de l'octet)."),
      ("Formule du chlorure de sodium :", "NaCl", "Na₂Cl", "NaCl₂", "Na₂Cl₂", "Électriquement neutre : Na⁺ et Cl⁻.")]),
    ("Liaisons", "On étudie la molécule d'eau H₂O (O : Z = 8 ; H : Z = 1).", [
      ("Nombre de liaisons covalentes formées par O :", "2", "1", "4", "6", "Il lui manque 2 électrons pour l'octet."),
      ("Nombre de doublets non liants sur O :", "2", "0", "1", "4", "6 électrons de valence − 2 engagés = 4 = 2 doublets."),
      ("Une liaison covalente est", "une mise en commun de deux électrons", "un transfert d'électrons", "une attraction entre ions", "une liaison entre noyaux", "Doublet liant."),
      ("Formule de Lewis de l'eau : la molécule est", "coudée", "linéaire", "plane triangulaire", "pyramidale", "Les doublets non liants repoussent les liaisons.")])]),
  d("pc", "Physique-Chimie", 2, [
    ("La mole", "M(C) = 12 g/mol ; M(H) = 1 g/mol ; M(O) = 16 g/mol ; NA = 6,02 × 10²³ mol⁻¹.", [
      ("Masse molaire du glucose C₆H₁₂O₆ :", "180 g/mol", "29 g/mol", "96 g/mol", "168 g/mol", "6 × 12 + 12 × 1 + 6 × 16."),
      ("Quantité de matière dans 36 g de glucose :", "0,2 mol", "5 mol", "0,5 mol", "2 mol", "n = m/M = 36/180."),
      ("Nombre de molécules :", "1,2 × 10²³", "6,02 × 10²³", "3 × 10²³", "1,2 × 10²²", "0,2 × 6,02 × 10²³."),
      ("Masse molaire de l'eau H₂O :", "18 g/mol", "17 g/mol", "10 g/mol", "34 g/mol", "2 × 1 + 16.")]),
    ("Concentration", "On dissout 5,85 g de NaCl (M = 58,5 g/mol) dans de l'eau pour obtenir 500 mL de solution.", [
      ("Quantité de NaCl :", "0,1 mol", "1 mol", "0,01 mol", "10 mol", "5,85 / 58,5."),
      ("Concentration molaire :", "0,2 mol/L", "0,05 mol/L", "0,1 mol/L", "2 mol/L", "C = n / V = 0,1 / 0,5."),
      ("Concentration massique :", "11,7 g/L", "5,85 g/L", "2,9 g/L", "117 g/L", "5,85 / 0,5."),
      ("On dilue 10 fois : nouvelle concentration molaire", "0,02 mol/L", "2 mol/L", "0,2 mol/L", "0,002 mol/L", "C / 10.")]),
    ("Gaz", "Dans les conditions de l'expérience, le volume molaire vaut 24 L/mol.", [
      ("Volume de 0,5 mol de dioxygène :", "12 L", "48 L", "24 L", "0,5 L", "V = n × Vm."),
      ("Quantité dans 72 L de gaz :", "3 mol", "0,33 mol", "72 mol", "1,5 mol", "72 / 24."),
      ("Le volume molaire dépend", "de la température et de la pression", "de la nature du gaz", "de la masse du gaz", "de la couleur du gaz", "Il est le même pour tous les gaz."),
      ("Masse de 12 L de CO₂ (M = 44 g/mol) :", "22 g", "44 g", "11 g", "528 g", "n = 0,5 mol ; m = 0,5 × 44.")])]),
  d("pc", "Physique-Chimie", 3, [
    ("Équation de réaction", "Le méthane brûle dans le dioxygène : CH₄ + … O₂ → CO₂ + … H₂O.", [
      ("Coefficient devant O₂ :", "2", "1", "3", "4", "Conservation des atomes d'oxygène : 2 + 2 = 4 O."),
      ("Coefficient devant H₂O :", "2", "1", "4", "3", "4 atomes H."),
      ("Lors d'une réaction chimique, il y a conservation", "des éléments et de la masse", "des molécules", "du volume", "de la couleur", "Loi de Lavoisier."),
      ("Avec 0,3 mol de CH₄ (O₂ en excès), on obtient de CO₂ :", "0,3 mol", "0,6 mol", "0,15 mol", "0,9 mol", "Rapport 1 pour 1.")]),
    ("Réactif limitant", "On fait réagir 0,4 mol de fer avec 0,3 mol de soufre : Fe + S → FeS.", [
      ("Réactif limitant :", "le soufre", "le fer", "aucun", "les deux", "Il y a moins de soufre et le rapport est 1 pour 1."),
      ("Quantité de FeS formée :", "0,3 mol", "0,4 mol", "0,7 mol", "0,1 mol", "Limitée par le soufre."),
      ("Fer restant :", "0,1 mol", "0 mol", "0,3 mol", "0,4 mol", "0,4 − 0,3."),
      ("Masse de FeS formée (M = 88 g/mol) :", "26,4 g", "35,2 g", "88 g", "8,8 g", "0,3 × 88.")]),
    ("Tests d'identification", "On réalise des tests au laboratoire.", [
      ("L'eau de chaux se trouble en présence de", "dioxyde de carbone", "dioxygène", "dihydrogène", "eau", "Test du CO₂."),
      ("Le sulfate de cuivre anhydre bleuit en présence d'", "eau", "air sec", "sel", "huile", "Test de l'eau."),
      ("Une bûchette incandescente se rallume dans le", "dioxygène", "dioxyde de carbone", "diazote", "dihydrogène", "Test du dioxygène."),
      ("Les ions chlorure donnent avec le nitrate d'argent un précipité", "blanc qui noircit à la lumière", "bleu", "rouille", "vert", "Précipité de AgCl.")])]),
  d("pc", "Physique-Chimie", 4, [
    ("Mouvement", "Un bus part de Thiès à 7 h 15 et arrive à Dakar (70 km) à 8 h 25.", [
      ("Durée du trajet :", "1 h 10 min", "1 h 25 min", "70 min et 15 s", "50 min", "8 h 25 − 7 h 15."),
      ("Vitesse moyenne :", "60 km/h", "70 km/h", "50 km/h", "84 km/h", "70 km / (7/6) h."),
      ("En m/s :", "≈ 16,7 m/s", "≈ 60 m/s", "≈ 216 m/s", "≈ 6 m/s", "60 / 3,6."),
      ("Le mouvement du bus par rapport au chauffeur :", "le bus est immobile", "rectiligne uniforme", "circulaire", "accéléré", "Le mouvement dépend du référentiel.")]),
    ("Principe d'inertie", "Un palet glisse sur une table à coussin d'air horizontale.", [
      ("Forces exercées sur le palet :", "poids et réaction de la table", "poids seulement", "aucune", "réaction seulement", "Frottements négligés."),
      ("Ces forces se compensent, donc le mouvement est", "rectiligne uniforme", "accéléré", "circulaire", "ralenti", "Principe d'inertie."),
      ("Le référentiel utilisé est", "terrestre", "héliocentrique", "géocentrique", "lunaire", "Lié à la table."),
      ("Un passager est projeté vers l'avant quand le bus freine car", "son corps tend à garder sa vitesse", "une force le pousse", "le bus accélère", "il saute", "Inertie.")]),
    ("Poids et gravitation", "g = 9,8 N/kg sur la Terre et 1,6 N/kg sur la Lune.", [
      ("Poids d'un élève de 50 kg sur la Terre :", "490 N", "50 N", "4,9 N", "80 N", "P = m g."),
      ("Sa masse sur la Lune :", "50 kg", "8 kg", "80 kg", "306 kg", "La masse ne change pas."),
      ("Son poids sur la Lune :", "80 N", "490 N", "50 N", "8 N", "50 × 1,6."),
      ("La force de gravitation entre deux corps", "diminue quand la distance augmente", "augmente avec la distance", "ne dépend pas des masses", "est toujours nulle", "F = G m m' / d².")])]),
  d("pc", "Physique-Chimie", 5, [
    ("Intensité du courant", "Un circuit en dérivation comporte deux lampes. I = 0,8 A dans la branche principale et I₁ = 0,3 A dans la lampe L₁.", [
      ("Intensité dans L₂ :", "0,5 A", "1,1 A", "0,3 A", "0,8 A", "Loi des nœuds : 0,8 − 0,3."),
      ("L'ampèremètre se branche", "en série", "en dérivation", "aux bornes du générateur seulement", "n'importe comment", "Le courant doit le traverser."),
      ("0,3 A en mA :", "300 mA", "30 mA", "3 000 mA", "3 mA", "× 1 000."),
      ("Sens conventionnel du courant :", "de la borne + vers la borne − à l'extérieur du générateur", "de − vers +", "dans les deux sens", "il n'a pas de sens", "Convention.")]),
    ("Tension", "Un générateur de 12 V alimente deux résistors en série. U₁ = 4,5 V.", [
      ("Tension U₂ :", "7,5 V", "16,5 V", "4,5 V", "12 V", "Loi des mailles : 12 − 4,5."),
      ("Le voltmètre se branche", "en dérivation", "en série", "à la place d'une lampe", "n'importe comment", "Aux bornes du dipôle."),
      ("Avec R₁ = 15 Ω, l'intensité est", "0,3 A", "3,33 A", "67,5 A", "0,8 A", "Loi d'Ohm : I = 4,5 / 15."),
      ("Valeur de R₂ :", "25 Ω", "15 Ω", "2,25 Ω", "40 Ω", "R₂ = 7,5 / 0,3.")]),
    ("Puissance et énergie", "Un fer à repasser porte les indications 220 V – 1 100 W.", [
      ("Intensité qui le traverse :", "5 A", "0,2 A", "242 A", "50 A", "I = P / U."),
      ("Énergie consommée en 2 h :", "2,2 kWh", "1,1 kWh", "550 Wh", "22 kWh", "1,1 kW × 2 h."),
      ("Coût à 100 F le kWh :", "220 F", "110 F", "2 200 F", "22 F", "2,2 × 100."),
      ("Un fusible sert à", "protéger le circuit contre les surintensités", "augmenter la tension", "stocker l'énergie", "mesurer l'intensité", "Il fond si l'intensité est trop forte.")])]),
  d("pc", "Physique-Chimie", 6, [
    ("Réflexion", "Un rayon lumineux arrive sur un miroir plan avec un angle d'incidence de 35°.", [
      ("Angle de réflexion :", "35°", "55°", "70°", "145°", "i = r."),
      ("Angle entre le rayon réfléchi et le miroir :", "55°", "35°", "90°", "70°", "90 − 35."),
      ("Les angles se mesurent par rapport à", "la normale", "la surface du miroir", "l'horizontale", "le rayon réfléchi", "Convention."),
      ("L'image d'un objet dans un miroir plan est", "symétrique de l'objet par rapport au miroir", "plus petite", "renversée haut-bas", "réelle", "Image virtuelle symétrique.")]),
    ("Réfraction", "Un rayon passe de l'air (n₁ = 1) dans l'eau (n₂ = 1,33) avec i₁ = 30°.", [
      ("Loi de Descartes :", "n₁ sin i₁ = n₂ sin i₂", "n₁ i₁ = n₂ i₂", "sin i₁ = sin i₂", "n₁ cos i₁ = n₂ cos i₂", "Deuxième loi de la réfraction."),
      ("sin i₂ ≈", "0,376", "0,5", "0,665", "1,33", "0,5 / 1,33."),
      ("i₂ ≈", "22°", "30°", "42°", "48°", "Arcsin 0,376."),
      ("En entrant dans l'eau, le rayon", "se rapproche de la normale", "s'éloigne de la normale", "n'est pas dévié", "est totalement réfléchi", "Milieu plus réfringent.")]),
    ("Dispersion de la lumière", "On envoie de la lumière blanche sur un prisme.", [
      ("On observe", "un spectre de couleurs", "une seule couleur", "rien", "une ombre", "Décomposition de la lumière blanche."),
      ("La lumière blanche est", "polychromatique", "monochromatique", "invisible", "toujours rouge", "Mélange de radiations."),
      ("La radiation la plus déviée :", "le violet", "le rouge", "le jaune", "le vert", "L'indice dépend de la longueur d'onde."),
      ("Phénomène naturel de dispersion :", "l'arc-en-ciel", "l'éclipse", "l'écho", "la marée", "Gouttes d'eau = prismes.")])]),
  # ================= SVT
  d("svt", "SVT", 1, [
    ("La cellule", "On observe au microscope des cellules d'épiderme d'oignon et des cellules de la joue.", [
      ("Organite présent dans les deux cellules :", "le noyau", "la paroi", "le chloroplaste", "la grande vacuole", "Cellule animale et végétale."),
      ("Propre à la cellule végétale :", "la paroi cellulosique", "la membrane plasmique", "le cytoplasme", "les mitochondries", "Rigidité de la cellule végétale."),
      ("Rôle de la mitochondrie :", "respiration cellulaire", "photosynthèse", "contenir l'ADN principal", "protéger la cellule", "Production d'énergie (ATP)."),
      ("Grossissement avec un oculaire ×10 et un objectif ×40 :", "×400", "×50", "×4", "×4 000", "On multiplie les deux.")]),
    ("Membrane et échanges", "On place des cellules végétales dans de l'eau très salée.", [
      ("L'eau sort de la cellule par", "osmose", "phagocytose", "photosynthèse", "mitose", "Vers le milieu le plus concentré."),
      ("La cellule devient", "plasmolysée", "turgescente", "plus grosse", "morte immédiatement", "La vacuole perd de l'eau."),
      ("Dans l'eau distillée, la cellule devient", "turgescente", "plasmolysée", "desséchée", "colorée", "L'eau entre."),
      ("La membrane plasmique est", "semi-perméable", "imperméable", "totalement perméable", "rigide", "Elle laisse passer certaines substances.")]),
    ("Les êtres unicellulaires", "La paramécie et le plasmodium sont des êtres unicellulaires.", [
      ("Un être unicellulaire est formé", "d'une seule cellule", "de deux cellules", "de tissus", "d'organes", "Définition."),
      ("Le plasmodium provoque", "le paludisme", "la tuberculose", "le sida", "la rougeole", "Parasite transmis par l'anophèle."),
      ("Les bactéries sont des cellules", "sans noyau véritable", "avec noyau", "végétales", "animales", "Procaryotes."),
      ("Instrument pour observer une bactérie :", "microscope", "loupe à main", "jumelles", "œil nu", "Taille de l'ordre du micromètre.")])]),
  d("svt", "SVT", 2, [
    ("ADN et génome", "Le noyau contient l'ADN, support de l'information génétique.", [
      ("ADN signifie", "acide désoxyribonucléique", "acide diribonucléique", "azote dinucléique", "acide de noyau", "Définition."),
      ("Bases azotées de l'ADN :", "A, T, C, G", "A, U, C, G", "A, B, C, D", "T, U, C, G", "Thymine dans l'ADN."),
      ("Complémentarité :", "A avec T et C avec G", "A avec C et T avec G", "A avec G et C avec T", "A avec U", "Règle d'appariement."),
      ("Brin complémentaire de ATG-CCA :", "TAC-GGT", "ATG-CCA", "UAC-GGU", "GCA-TTG", "On applique la complémentarité.")]),
    ("Mitose", "Une cellule de 46 chromosomes se divise par mitose.", [
      ("Chaque cellule fille a", "46 chromosomes", "23 chromosomes", "92 chromosomes", "12 chromosomes", "La mitose conserve le nombre de chromosomes."),
      ("Phase où les chromosomes s'alignent sur l'équateur :", "métaphase", "prophase", "anaphase", "télophase", "Plaque équatoriale."),
      ("Phase où les chromatides se séparent :", "anaphase", "métaphase", "prophase", "interphase", "Migration vers les pôles."),
      ("La réplication de l'ADN a lieu pendant", "l'interphase", "la métaphase", "l'anaphase", "la télophase", "Avant la division.")]),
    ("Caryotype", "On observe le caryotype d'une personne.", [
      ("Nombre de paires de chromosomes chez l'être humain :", "23", "46", "22", "44", "46 chromosomes = 23 paires."),
      ("Chromosomes sexuels d'un homme :", "XY", "XX", "YY", "X seul", "Définition."),
      ("Un caryotype à 47 chromosomes avec trois chromosomes 21 indique", "une trisomie 21", "un caryotype normal", "une monosomie", "un homme", "Anomalie du nombre."),
      ("Les gènes sont portés par", "les chromosomes", "les mitochondries seulement", "la membrane", "les ribosomes", "Segments d'ADN.")])]),
  d("svt", "SVT", 3, [
    ("Enzymes", "On met de l'amidon avec de la salive à 37 °C, puis à 0 °C et à 90 °C.", [
      ("L'enzyme de la salive transforme l'amidon en", "maltose", "glucose et protéines", "graisses", "eau", "Amylase salivaire."),
      ("Test qui montre la disparition de l'amidon :", "l'eau iodée ne bleuit plus", "la liqueur de Fehling reste bleue", "l'eau de chaux se trouble", "rien", "L'iode colore l'amidon en bleu-noir."),
      ("À 0 °C l'enzyme est", "inactive mais pas détruite", "détruite", "plus active", "transformée en amidon", "Réactivée en réchauffant."),
      ("À 90 °C l'enzyme est", "dénaturée", "plus active", "inactive mais réutilisable", "transformée en sucre", "La chaleur détruit la protéine.")]),
    ("Respiration et fermentation", "On compare des levures dans un milieu avec dioxygène et sans dioxygène.", [
      ("Avec dioxygène, les levures font", "la respiration", "la fermentation", "la photosynthèse", "la mitose seulement", "Oxydation complète du glucose."),
      ("Sans dioxygène, elles produisent", "de l'éthanol et du CO₂", "de l'eau et du CO₂", "du glucose", "du dioxygène", "Fermentation alcoolique."),
      ("Réaction qui libère le plus d'énergie :", "la respiration", "la fermentation", "les deux autant", "aucune", "Environ 18 fois plus d'ATP."),
      ("Application de la fermentation :", "la fabrication du pain", "la cuisson du riz", "le séchage du poisson", "la congélation", "La pâte lève grâce au CO₂.")]),
    ("Photosynthèse", "On place une plante verte à la lumière, puis à l'obscurité.", [
      ("La photosynthèse a lieu dans", "les chloroplastes", "les mitochondries", "le noyau", "les racines", "Pigment chlorophyllien."),
      ("Elle consomme", "du CO₂ et de l'eau", "du dioxygène et du glucose", "de l'amidon", "de l'azote seulement", "Matières minérales."),
      ("Elle produit", "du glucose et du dioxygène", "du CO₂", "de l'éthanol", "de l'eau seulement", "Matière organique."),
      ("Condition indispensable :", "la lumière", "l'obscurité", "le froid", "l'absence d'eau", "Énergie lumineuse.")])]),
  d("svt", "SVT", 4, [
    ("Écosystème", "Dans une savane du Niokolo-Koba : herbe → gazelle → lion ; les champignons décomposent les cadavres.", [
      ("Producteur :", "l'herbe", "la gazelle", "le lion", "le champignon", "Il fabrique sa matière organique."),
      ("Consommateur secondaire :", "le lion", "la gazelle", "l'herbe", "le champignon", "Il mange un herbivore."),
      ("Rôle des décomposeurs :", "recycler la matière en sels minéraux", "produire de l'oxygène", "chasser", "polliniser", "Ils ferment le cycle."),
      ("Si les lions disparaissent, les gazelles risquent de", "devenir trop nombreuses", "disparaître aussitôt", "devenir carnivores", "ne pas changer", "Plus de prédateur.")]),
    ("Biodiversité", "Le Sénégal protège plusieurs parcs et réserves.", [
      ("La biodiversité est", "la diversité des êtres vivants", "le nombre d'habitants", "la quantité de pluie", "la surface des forêts seulement", "Définition."),
      ("Parc national ornithologique célèbre :", "Djoudj", "Niokolo-Koba seulement", "Bandia", "Hann", "Oiseaux migrateurs (classé UNESCO)."),
      ("Menace pour la biodiversité :", "la destruction des habitats", "le reboisement", "les aires protégées", "la jachère", "Défrichement, feux, braconnage."),
      ("Mesure de protection :", "créer des aires protégées", "couper les mangroves", "chasser davantage", "brûler la brousse", "Conservation.")]),
    ("Relations entre êtres vivants", "On observe différentes relations dans la nature.", [
      ("Le lichen associe une algue et un champignon qui profitent tous les deux : c'est", "une symbiose", "un parasitisme", "une prédation", "une compétition", "Bénéfice réciproque."),
      ("La tique sur une vache est", "un parasite", "un prédateur", "un symbiote", "un producteur", "Il vit aux dépens de l'hôte."),
      ("Deux arbres qui cherchent la même lumière sont en", "compétition", "symbiose", "parasitisme", "prédation", "Ressource commune."),
      ("Le lion qui chasse le phacochère est un", "prédateur", "parasite", "décomposeur", "producteur", "Il tue sa proie.")])]),
  d("svt", "SVT", 5, [
    ("Formation des sols", "On observe un profil de sol dans une région boisée.", [
      ("Horizon le plus riche en matière organique :", "l'horizon A (humifère)", "la roche mère", "l'horizon C", "l'horizon B profond", "Litière décomposée."),
      ("La roche mère est située", "en profondeur", "en surface", "au milieu de l'humus", "dans l'air", "Elle s'altère lentement."),
      ("L'humus provient de", "la décomposition des débris végétaux et animaux", "la roche mère seulement", "la pluie", "le sable des dunes", "Action des décomposeurs."),
      ("Le sol se forme", "très lentement (des milliers d'années)", "en quelques jours", "en un an", "jamais", "Ressource non renouvelable à l'échelle humaine.")]),
    ("Érosion des sols", "Dans le bassin arachidier, les sols nus s'appauvrissent.", [
      ("L'érosion éolienne est causée par", "le vent", "la pluie", "les vers de terre", "le soleil seul", "Transport des particules."),
      ("L'érosion hydrique est causée par", "le ruissellement de l'eau", "le vent", "les arbres", "la jachère", "Pluies fortes sur sol nu."),
      ("Technique de lutte :", "brise-vent et haies", "déboisement", "feux de brousse", "surpâturage", "Freiner le vent."),
      ("Le surpâturage", "favorise l'érosion", "protège le sol", "enrichit le sol", "n'a aucun effet", "Il dénude le sol.")]),
    ("Propriétés du sol", "On compare un sol sableux (dior) et un sol argileux (deck).", [
      ("Sol qui retient le mieux l'eau :", "argileux", "sableux", "les deux autant", "aucun", "Particules fines."),
      ("Sol qui laisse passer l'eau rapidement :", "sableux", "argileux", "les deux autant", "aucun", "Gros grains, grande perméabilité."),
      ("La porosité d'un sol est", "le volume des vides entre les particules", "sa couleur", "sa masse", "sa température", "Air et eau."),
      ("Pour enrichir un sol pauvre, on peut", "apporter du fumier ou du compost", "le laisser brûler", "enlever l'humus", "le tasser", "Matière organique.")]),
    ]),
  d("svt", "SVT", 6, [
    ("Synthèse : métabolisme", "Une graine de mil germe à l'obscurité puis la plantule est mise à la lumière.", [
      ("Pendant la germination, la graine utilise", "ses réserves", "la photosynthèse", "le CO₂ de l'air", "la lumière", "Réserves d'amidon."),
      ("Gaz rejeté par la graine qui germe :", "CO₂", "O₂", "N₂", "H₂", "Respiration."),
      ("À la lumière, la plantule", "fait aussi la photosynthèse", "arrête de respirer", "perd ses chloroplastes", "meurt", "Elle respire toujours."),
      ("Enzymes qui transforment l'amidon des réserves :", "amylases", "lipases", "protéases", "ligases", "Hydrolyse de l'amidon.")]),
    ("Synthèse : cellule et ADN", "Un élève prépare une fiche de révision.", [
      ("Le support de l'information génétique :", "l'ADN", "la membrane", "le glucose", "la vacuole", "Molécule de l'hérédité."),
      ("La mitose permet", "la croissance et le renouvellement des cellules", "la formation des gamètes", "la digestion", "la photosynthèse", "Cellules identiques."),
      ("Organite qui fabrique les protéines :", "le ribosome", "la vacuole", "la paroi", "le chloroplaste", "Traduction."),
      ("Une cellule sans noyau véritable est dite", "procaryote", "eucaryote", "diploïde", "végétale", "Bactéries.")]),
    ("Synthèse : environnement", "Un village de Casamance veut protéger sa mangrove.", [
      ("La mangrove sert de", "nurserie pour les poissons et les huîtres", "désert", "zone de culture d'arachide", "carrière de sable", "Riche biodiversité."),
      ("Menace principale :", "la coupe du bois et la salinisation", "la pluie", "les oiseaux", "le reboisement", "Activités humaines et sécheresse."),
      ("Action utile :", "reboiser les palétuviers", "brûler la mangrove", "assécher le marigot", "construire sur la mangrove", "Restauration."),
      ("Cette action protège aussi", "les côtes contre l'érosion", "les feux de brousse", "le trafic routier", "les mines", "Les racines fixent le sol.")])]),
])
