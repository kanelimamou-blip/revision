# Sujets refaits dans l'appli sur le modèle des épreuves officielles du BFEM et du BAC (même structure, même barème,
# mêmes notions), avec des données nouvelles et un corrigé étape par étape. Les références des épreuves officielles
# sont gardées dans catalogue.py et annales.py. Chaque étape : (question, [4 choix, le bon en premier ou à l'indice donné], indice, explication, points).

MODELE_ANNALES = [
  {"id": "bfem-type-maths-1", "exam": "BFEM", "year": "type 1", "series": "", "subject": "Mathématiques", "levels": ["3e"], "duration": "2 h", "coef": 4, "modele": True,
   "parts": ["Activités numériques (10 pts) : racines carrées, factorisation, équation produit, système de deux équations",
             "Activités géométriques (10 pts) : Pythagore, Thalès, cosinus, repérage, pyramide"]},
  {"id": "bfem-type-pc-1", "exam": "BFEM", "year": "type 1", "series": "", "subject": "Physique-Chimie", "levels": ["3e"], "duration": "2 h", "coef": 2, "modele": True,
   "parts": ["Chimie (8 pts) : solution basique, neutralisation, action d'un acide sur le fer",
             "Physique (12 pts) : lentille convergente, résistances en série, travail et puissance"]},
  {"id": "bfem-type-svt-1", "exam": "BFEM", "year": "type 1", "series": "", "subject": "SVT", "levels": ["3e"], "duration": "2 h", "coef": 2, "modele": True,
   "parts": ["Maîtrise des connaissances (8 pts) : immunité, groupes sanguins, système nerveux",
             "Compétences méthodologiques (12 pts) : exploitation d'une courbe d'anticorps, vision, roches"]},
  {"id": "bac-type-s2-maths-1", "exam": "BAC", "year": "type 1", "series": "S2, S4, S5", "subject": "Mathématiques", "levels": ["Tle S2", "Tle S4", "Tle S5"], "duration": "4 h", "coef": 5, "modele": True,
   "parts": ["Exercice 1 (3 pts) : limites usuelles et primitives",
             "Exercice 2 (4 pts) : polynôme complexe de degré 3, triangle, barycentre et lieu de points",
             "Exercice 3 (4 pts) : suite récurrente et suite géométrique associée",
             "Problème (9 pts) : équation différentielle, étude de fonction, asymptote, aire"]},
]

MODELE_GUIDED = {
  "bfem-type-maths-1": [
    {"title": "Exercice 1 : racines carrées (3 pts)", "context": "On donne a = √50 − 3√8 + √18 et b = (2 − √2)².", "steps": [
      ("a s'écrit sous la forme k√2 avec k =", ["2", "−4", "14", "8"], 0, "√50 = 5√2, 3√8 = 6√2, √18 = 3√2 : a = (5 − 6 + 3)√2 = 2√2.", 1),
      ("Développer b :", ["6 − 4√2", "4 − 2", "2 − 4√2", "6"], 0, "(2 − √2)² = 4 − 4√2 + 2 = 6 − 4√2.", 1),
      ("Rendre rationnel le dénominateur de 1/(2 − √2) :", ["(2 + √2)/2", "(2 − √2)/2", "2 + √2", "1/2"], 0, "On multiplie par le conjugué : (2 + √2)/((2 − √2)(2 + √2)) = (2 + √2)/(4 − 2) = (2 + √2)/2.", 1),
    ]},
    {"title": "Exercice 2 : factorisation et équation (3 pts)", "context": "E = (2x − 1)² − 9.", "steps": [
      ("Factoriser E :", ["(2x − 4)(2x + 2)", "(2x − 10)(2x + 8)", "(2x − 1)(2x − 9)", "4x² − 10"], 0, "a² − b² = (a − b)(a + b) avec a = 2x − 1 et b = 3.", 1),
      ("E s'écrit aussi :", ["4(x − 2)(x + 1)", "2(x − 2)(x + 1)", "4(x + 2)(x − 1)", "(x − 2)(x + 1)"], 0, "2x − 4 = 2(x − 2) et 2x + 2 = 2(x + 1).", 1),
      ("Les solutions de E = 0 sont :", ["2 et −1", "−2 et 1", "1/2 et 3", "4 et −2"], 0, "Produit nul : x − 2 = 0 ou x + 1 = 0.", 1),
    ]},
    {"title": "Exercice 3 : système (4 pts)", "context": "Pour une sortie, 25 élèves paient en tout 17 500 F. Les élèves de 4e paient 500 F, ceux de 3e paient 1 000 F. On note x le nombre d'élèves de 4e et y celui de 3e.", "steps": [
      ("Le système qui traduit l'énoncé est :", ["x + y = 25 et 500x + 1 000y = 17 500", "x + y = 17 500 et 500x + 1 000y = 25", "x − y = 25 et x + 2y = 35", "500x + y = 25 et x + 1 000y = 17 500"], 0, "Nombre total d'élèves et montant total.", 1.5),
      ("En divisant la 2e équation par 500, on obtient :", ["x + 2y = 35", "x + 2y = 3,5", "2x + y = 35", "x + y = 35"], 0, "500x/500 = x, 1 000y/500 = 2y, 17 500/500 = 35.", 1),
      ("La solution est :", ["x = 15 et y = 10", "x = 10 et y = 15", "x = 20 et y = 5", "x = 5 et y = 20"], 0, "Par soustraction : y = 35 − 25 = 10, puis x = 25 − 10 = 15.", 1.5),
    ]},
    {"title": "Exercice 4 : triangle, Thalès et cosinus (5 pts)", "context": "ABC est un triangle tel que AB = 6 cm, AC = 8 cm et BC = 10 cm. M est le point de [AB] tel que AM = 3 cm ; la parallèle à (BC) passant par M coupe [AC] en N.", "steps": [
      ("Le triangle ABC est :", ["rectangle en A", "rectangle en B", "isocèle", "équilatéral"], 0, "AB² + AC² = 36 + 64 = 100 = BC² : réciproque de Pythagore, l'angle droit est en A (opposé au plus grand côté).", 1.5),
      ("AN vaut :", ["4 cm", "3 cm", "5 cm", "6 cm"], 0, "Thalès : AN/AC = AM/AB = 3/6, donc AN = 8/2 = 4 cm.", 1.5),
      ("MN vaut :", ["5 cm", "4 cm", "10 cm", "2,5 cm"], 0, "MN/BC = 1/2, donc MN = 5 cm.", 1),
      ("cos ABC vaut :", ["0,6", "0,8", "0,75", "1,2"], 0, "Dans le triangle rectangle en A : cos B = AB/BC = 6/10.", 1),
    ]},
    {"title": "Exercice 5 : repérage et pyramide (5 pts)", "context": "Dans un repère orthonormé, A(1 ; 2) et B(3 ; 6). SABCD est une pyramide régulière à base carrée de côté 6 cm et de hauteur 4 cm.", "steps": [
      ("La distance AB vaut :", ["2√5", "√20/2", "4", "√52"], 0, "AB = √((3 − 1)² + (6 − 2)²) = √(4 + 16) = √20 = 2√5.", 1),
      ("Le milieu de [AB] a pour coordonnées :", ["(2 ; 4)", "(4 ; 8)", "(1 ; 2)", "(2 ; 3)"], 0, "On fait la moyenne des abscisses et des ordonnées.", 1),
      ("Une équation de la droite (AB) est :", ["y = 2x", "y = 2x + 2", "y = x + 1", "y = 4x − 2"], 0, "Coefficient directeur (6 − 2)/(3 − 1) = 2 ; y = 2x + p avec 2 = 2 × 1 + p, donc p = 0.", 1.5),
      ("Le volume de la pyramide vaut :", ["48 cm³", "144 cm³", "24 cm³", "96 cm³"], 0, "V = (aire de la base × hauteur)/3 = 36 × 4 / 3 = 48 cm³.", 1.5),
    ]},
  ],
  "bfem-type-pc-1": [
    {"title": "Exercice 1 : solution d'hydroxyde de sodium (4 pts)", "context": "On dissout 4 g d'hydroxyde de sodium NaOH (M = 40 g/mol) dans de l'eau pour obtenir 200 mL de solution. On dose 20 mL de cette solution par de l'acide chlorhydrique à 0,25 mol/L.", "steps": [
      ("La quantité de NaOH dissoute est :", ["0,1 mol", "10 mol", "0,01 mol", "160 mol"], 0, "n = m/M = 4/40 = 0,1 mol.", 1),
      ("La concentration molaire de la solution est :", ["0,5 mol/L", "0,02 mol/L", "20 mol/L", "0,05 mol/L"], 0, "C = n/V = 0,1/0,2 = 0,5 mol/L.", 1),
      ("Le pH de cette solution est :", ["supérieur à 7", "égal à 7", "inférieur à 7", "égal à 0"], 0, "L'hydroxyde de sodium donne une solution basique.", 0.5),
      ("Le volume d'acide versé à l'équivalence est :", ["40 mL", "20 mL", "10 mL", "80 mL"], 0, "À l'équivalence n(acide) = n(base) = 0,5 × 0,020 = 0,01 mol, donc Va = 0,01/0,25 = 0,040 L.", 1.5),
    ]},
    {"title": "Exercice 2 : action de l'acide chlorhydrique sur le fer (4 pts)", "context": "On fait réagir 5,6 g de fer (M = 56 g/mol) avec de l'acide chlorhydrique en excès. Volume molaire : 22,4 L/mol.", "steps": [
      ("L'équation-bilan est :", ["Fe + 2H⁺ → Fe²⁺ + H₂", "Fe + H⁺ → Fe⁺ + H", "2Fe + 6H⁺ → 2Fe³⁺ + 3H₂O", "Fe + Cl⁻ → FeCl"], 0, "Le fer est oxydé en ions Fe²⁺ et il se dégage du dihydrogène.", 1.5),
      ("La quantité de fer est :", ["0,1 mol", "1 mol", "10 mol", "0,56 mol"], 0, "5,6/56.", 1),
      ("Le volume de dihydrogène dégagé est :", ["2,24 L", "22,4 L", "1,12 L", "4,48 L"], 0, "1 mol de Fe donne 1 mol de H₂ : 0,1 × 22,4 = 2,24 L.", 1),
      ("On identifie le dihydrogène par :", ["une détonation à l'approche d'une flamme", "le trouble de l'eau de chaux", "la coloration bleue du sulfate de cuivre", "le rallumage d'une bûchette"], 0, "Le dihydrogène brûle avec une petite détonation.", 0.5),
    ]},
    {"title": "Exercice 3 : lentille convergente (4 pts)", "context": "Une lentille convergente a une distance focale f = 20 cm. Un objet AB de 2 cm est placé perpendiculairement à l'axe, à 30 cm devant la lentille.", "steps": [
      ("La vergence de la lentille est :", ["5 δ", "0,05 δ", "20 δ", "−5 δ"], 0, "C = 1/f = 1/0,20 m = 5 dioptries.", 1),
      ("L'image se forme :", ["à 60 cm derrière la lentille", "à 12 cm derrière la lentille", "à 60 cm devant la lentille", "à l'infini"], 0, "1/OA′ = 1/f + 1/OA = 1/20 − 1/30 = 1/60, donc OA′ = 60 cm.", 1.5),
      ("L'image est :", ["réelle, renversée, 2 fois plus grande", "virtuelle, droite, plus petite", "réelle, droite, de même taille", "virtuelle, renversée"], 0, "Grandissement γ = OA′/OA = 60/(−30) = −2 : renversée et 2 fois plus grande, donc A′B′ = 4 cm.", 1.5),
    ]},
    {"title": "Exercice 4 : électricité et puissance (8 pts)", "context": "Deux conducteurs ohmiques R₁ = 10 Ω et R₂ = 20 Ω sont montés en série sous une tension de 6 V. Par ailleurs, un moteur de grue soulève une charge de 200 kg de 10 m en 40 s (g = 10 N/kg).", "steps": [
      ("La résistance équivalente est :", ["30 Ω", "6,7 Ω", "200 Ω", "10 Ω"], 0, "En série, les résistances s'ajoutent.", 1.5),
      ("L'intensité du courant est :", ["0,2 A", "5 A", "180 A", "0,3 A"], 0, "I = U/R = 6/30.", 1.5),
      ("La tension aux bornes de R₁ est :", ["2 V", "4 V", "6 V", "0,5 V"], 0, "U₁ = R₁ I = 10 × 0,2.", 1),
      ("La puissance électrique reçue par l'ensemble est :", ["1,2 W", "30 W", "0,2 W", "6 W"], 0, "P = U I = 6 × 0,2.", 1),
      ("Le travail du poids lors de la montée est :", ["−20 000 J", "20 000 J", "2 000 J", "−2 000 J"], 0, "W = −m g h = −200 × 10 × 10 : il est résistant car la charge monte.", 1.5),
      ("La puissance mécanique minimale du moteur est :", ["500 W", "800 000 W", "50 W", "5 000 W"], 0, "P = W/t = 20 000/40.", 1.5),
    ]},
  ],
  "bfem-type-svt-1": [
    {"title": "I. Maîtrise des connaissances (8 pts)", "context": "Réponds aux questions de cours sur l'immunité, le sang et le système nerveux.", "steps": [
      ("Les anticorps sont produits par :", ["les lymphocytes B (plasmocytes)", "les globules rouges", "les plaquettes", "les neurones"], 0, "Les lymphocytes B se transforment en plasmocytes qui sécrètent les anticorps.", 1.5),
      ("La phagocytose est réalisée par :", ["des globules blancs (macrophages)", "des globules rouges", "les anticorps", "les plaquettes"], 0, "Les phagocytes englobent et digèrent les microbes.", 1.5),
      ("Une personne du groupe A possède :", ["l'antigène A et des anticorps anti-B", "l'antigène B et des anticorps anti-A", "les antigènes A et B", "aucun antigène"], 0, "Les anticorps du plasma sont dirigés contre l'antigène absent.", 1.5),
      ("Le donneur universel est du groupe :", ["O", "AB", "A", "B"], 0, "Ses hématies ne portent ni A ni B.", 1),
      ("Le centre nerveux d'un réflexe médullaire est :", ["la moelle épinière", "le cerveau", "le cervelet", "le nerf"], 0, "Le réflexe ne passe pas par le cerveau.", 1.5),
      ("Le trajet du message dans un arc réflexe est :", ["récepteur → nerf sensitif → moelle → nerf moteur → muscle", "muscle → moelle → récepteur", "cerveau → récepteur → muscle", "nerf moteur → récepteur → moelle"], 0, "Il part du récepteur et aboutit à l'effecteur.", 1),
    ]},
    {"title": "II. Compétences méthodologiques (12 pts)", "context": "Document : on injecte deux fois le même vaccin à un enfant, au jour 0 puis au jour 60. Le taux d'anticorps reste faible et monte lentement après la 1re injection (maximum vers le 15e jour) ; après la 2e injection, il monte en 3 jours à une valeur 10 fois plus élevée et reste haut longtemps.", "steps": [
      ("Après la 1re injection, la réponse est :", ["lente et faible", "rapide et forte", "nulle", "immédiate"], 0, "C'est la réponse primaire.", 2),
      ("Après la 2e injection, la réponse est :", ["plus rapide, plus forte et plus durable", "identique à la première", "plus faible", "absente"], 0, "C'est la réponse secondaire.", 2),
      ("Cette différence s'explique par :", ["la mémoire immunitaire", "la fatigue de l'organisme", "la destruction des lymphocytes", "un autre microbe"], 0, "Des lymphocytes mémoire reconnaissent l'antigène et réagissent vite.", 2),
      ("Le rappel de vaccin sert donc à :", ["renforcer et prolonger la protection", "soigner une maladie déclarée", "diminuer le taux d'anticorps", "remplacer les globules rouges"], 0, "Chaque rappel relance une réponse secondaire.", 2),
      ("Chez un myope, l'image d'un objet lointain se forme :", ["en avant de la rétine", "sur la rétine", "en arrière de la rétine", "sur le cristallin"], 0, "L'œil myope est trop convergent.", 2),
      ("Une roche à grands cristaux visibles à l'œil nu (granite) est une roche :", ["plutonique à structure grenue", "volcanique à structure microlitique", "sédimentaire", "métamorphique"], 0, "Refroidissement lent du magma en profondeur.", 2),
    ]},
  ],
  "bac-type-s2-maths-1": [
    {"title": "Exercice 1 : limites et primitives (3 pts)", "context": "Pour chaque question, choisis la bonne réponse.", "steps": [
      ("lim (eˣ − 1)/x quand x → 0 :", ["1", "0", "+∞", "e"], 0, "C'est le nombre dérivé de exp en 0.", 0.5),
      ("lim (ln x)/x quand x → +∞ :", ["0", "1", "+∞", "−∞"], 0, "Croissances comparées : x l'emporte sur ln x.", 0.5),
      ("lim x ln x quand x → 0⁺ :", ["0", "−∞", "1", "+∞"], 0, "Limite usuelle.", 0.5),
      ("Une primitive de 2x/(x² + 1) sur ℝ :", ["ln(x² + 1)", "1/(x² + 1)", "2 ln x", "x²/(x² + 1)"], 0, "Forme u′/u avec u = x² + 1 > 0.", 0.5),
      ("Une primitive de x e^(x²) :", ["½ e^(x²)", "e^(x²)", "2x e^(x²)", "x² e^(x²)/2"], 0, "Forme ½ u′ eᵘ avec u = x².", 0.5),
      ("Une primitive de cos x sin² x :", ["sin³x / 3", "cos³x / 3", "−sin³x / 3", "sin² x / 2"], 0, "Forme u′u² avec u = sin x.", 0.5),
    ]},
    {"title": "Exercice 2 : nombres complexes et barycentre (4 pts)", "context": "P(z) = z³ − (4 + i)z² + (5 + 4i)z − 5i. A, B, C ont pour affixes i, 2 + i et 2 − i.", "steps": [
      ("P(i) vaut :", ["0", "i", "−5i", "4"], 0, "i³ = −i ; −(4 + i)(−1) = 4 + i ; (5 + 4i)i = 5i − 4 ; total : −i + 4 + i + 5i − 4 − 5i = 0.", 0.5),
      ("P(z) = (z − i)Q(z) avec Q(z) =", ["z² − 4z + 5", "z² + 4z + 5", "z² − 4z − 5", "z² − 5"], 0, "En développant (z − i)(z² − 4z + 5), on retrouve P(z).", 0.75),
      ("Les solutions de P(z) = 0 sont :", ["i, 2 + i et 2 − i", "i, −2 + i, −2 − i", "−i, 2, 5", "i seulement"], 0, "Δ = 16 − 20 = −4 = (2i)², d'où z = (4 ± 2i)/2 = 2 ± i.", 0.75),
      ("Le triangle ABC est :", ["rectangle isocèle en B", "équilatéral", "rectangle en A", "isocèle en A"], 0, "AB = |2| = 2, BC = |−2i| = 2, AC = |2 − 2i| = 2√2 et AC² = AB² + BC².", 0.75),
      ("G barycentre de (A ; 1), (B ; −1), (C ; 1) a pour affixe :", ["−i", "i", "4 − i", "2"], 0, "z_G = (z_A − z_B + z_C)/1 = i − 2 − i + 2 − i = −i. ABCG est alors un carré.", 0.75),
      ("L'ensemble des M tels que ‖MA⃗ − MB⃗ + MC⃗‖ = 2 est :", ["le cercle de centre G et de rayon 2", "la droite (AC)", "le point G", "le cercle de centre B de rayon 2"], 0, "MA⃗ − MB⃗ + MC⃗ = (1 − 1 + 1) MG⃗ = MG⃗, donc GM = 2.", 0.5),
    ]},
    {"title": "Exercice 3 : suite récurrente (4 pts)", "context": "u₀ = 2 et uₙ₊₁ = ½ uₙ + 3. On pose vₙ = uₙ − 6.", "steps": [
      ("u₁ vaut :", ["4", "7", "5", "1"], 0, "½ × 2 + 3.", 0.5),
      ("(vₙ) est géométrique de raison :", ["½", "3", "2", "−6"], 0, "vₙ₊₁ = ½ uₙ + 3 − 6 = ½ (uₙ − 6) = ½ vₙ.", 1),
      ("v₀ vaut :", ["−4", "4", "2", "−6"], 0, "2 − 6.", 0.5),
      ("Pour tout n, uₙ =", ["6 − 4(½)ⁿ", "6 + 4(½)ⁿ", "2(½)ⁿ", "6 − (½)ⁿ"], 0, "vₙ = −4(½)ⁿ, puis uₙ = vₙ + 6.", 1),
      ("La suite (uₙ) :", ["est croissante et converge vers 6", "est décroissante et converge vers 0", "diverge", "converge vers 2"], 0, "−4(½)ⁿ augmente vers 0 : uₙ croît vers 6.", 1),
    ]},
    {"title": "Problème : équation différentielle et étude de fonction (9 pts)", "context": "(E) : y′ − y = −x. On note f la solution de (E) telle que f(0) = 0, et C sa courbe.", "steps": [
      ("Une solution particulière affine de (E) est :", ["x + 1", "x", "−x", "x − 1"], 0, "Si y = x + 1, y′ − y = 1 − x − 1 = −x.", 1),
      ("Les solutions de (E) sont :", ["Ceˣ + x + 1", "Ce⁻ˣ + x + 1", "Ceˣ − x", "Cx + 1"], 0, "Solution générale de y′ = y, plus la solution particulière.", 1),
      ("f(x) =", ["x + 1 − eˣ", "x + 1 + eˣ", "eˣ − x − 1", "x − eˣ"], 0, "f(0) = C + 1 = 0, donc C = −1.", 1),
      ("f′(x) =", ["1 − eˣ", "1 + eˣ", "−eˣ", "eˣ − 1"], 0, "Dérivée de x + 1 − eˣ.", 1),
      ("Les variations de f :", ["croissante sur ]−∞ ; 0], décroissante sur [0 ; +∞[", "décroissante puis croissante", "toujours croissante", "toujours décroissante"], 0, "1 − eˣ > 0 pour x < 0 et < 0 pour x > 0 ; maximum f(0) = 0, donc f(x) ≤ 0.", 1),
      ("lim f en +∞ :", ["−∞", "+∞", "0", "1"], 0, "f(x) = x(1 + 1/x − eˣ/x) et eˣ/x → +∞.", 1),
      ("En −∞, C admet l'asymptote oblique :", ["y = x + 1", "y = x", "y = −x", "y = 1"], 0, "f(x) − (x + 1) = −eˣ tend vers 0 en −∞.", 1),
      ("C est située, par rapport à cette asymptote :", ["en dessous", "au-dessus", "elle la coupe en 0", "on ne peut pas savoir"], 0, "f(x) − (x + 1) = −eˣ < 0.", 0.5),
      ("L'aire entre C, l'asymptote et les droites x = −1 et x = 0 vaut (en unités d'aire) :", ["1 − 1/e", "1/e", "e − 1", "1"], 0, "∫ de −1 à 0 de eˣ dx = e⁰ − e⁻¹ = 1 − 1/e.", 1.5),
    ]},
  ],
}
