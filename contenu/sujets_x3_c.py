# Sujets types d'entraînement ×3 : Terminale S, mathématiques, physique-chimie, SVT.
from sujets_tle2 import P, noter, A, S

SER = "S1, S2, S3, S4, S5"
def _m(n, parts): return A(f"bac-type-s-maths-{n}", "Mathématiques", S, SER, "4 h", parts)
def _p(n, parts): return A(f"bac-type-s-pc-{n}", "Physique-Chimie", S, SER, "4 h", parts)
def _v(n, parts): return A(f"bac-type-s-svt-{n}", "SVT", S, SER, "4 h", parts)

ANNALES_X = [
  _m(4, ["Exercice : équation dans ℂ", "Problème : fonction x ln x − x et intégrale"]),
  _m(5, ["Exercice : tirage simultané et variable aléatoire", "Problème : fonction (x + 1)e^(−x)"]),
  _m(6, ["Exercice : suite arithmético-géométrique", "Exercice : équations différentielles"]),
  _m(7, ["Exercice : plan et tétraèdre dans l'espace", "Problème : fonction ln x / x"]),
  _m(8, ["Exercice : complexes et transformations", "Exercice : statistiques à deux variables"]),
  _m(9, ["Exercice : probabilités conditionnelles", "Problème : fonction e^x − x − 1"]),
  _p(4, ["Chimie : dosage d'un acide faible", "Physique : radioactivité et datation"]),
  _p(5, ["Chimie : estérification", "Physique : mouvement d'un projectile"]),
  _p(6, ["Chimie : cinétique chimique", "Physique : satellites et lois de Kepler"]),
  _p(7, ["Chimie : pH des acides et bases forts", "Physique : dipôles RC, RL et circuit LC"]),
  _p(8, ["Chimie : acides α-aminés", "Physique : interférences et effet photoélectrique"]),
  _p(9, ["Chimie : solutions tampons", "Physique : particule dans un champ magnétique, pendule élastique"]),
  _v(4, ["Maîtrise des connaissances : contraction musculaire", "Compétences : monohybridisme"]),
  _v(5, ["Maîtrise des connaissances : régulation de la pression artérielle", "Compétences : dihybridisme"]),
  _v(6, ["Maîtrise des connaissances : le VIH et le sida", "Compétences : hérédité liée au sexe"]),
  _v(7, ["Maîtrise des connaissances : régulation hormonale chez la femme", "Compétences : exploitation de dosages hormonaux"]),
  _v(8, ["Maîtrise des connaissances : méiose et brassage génétique", "Compétences : réflexe myotatique"]),
  _v(9, ["Maîtrise des connaissances : fécondation et contraception", "Compétences : groupes sanguins ABO"]),
]

GUIDED_X = {
  "bac-type-s-maths-4": noter([
    P("Exercice : équation dans ℂ", "On considère l'équation (E) : z² − 2z + 5 = 0.", [
      ("Le discriminant de (E) vaut :", "−16", "16", "−20", "24", "Δ = 4 − 20 = −16."),
      ("Les solutions de (E) dans ℂ :", "1 + 2i et 1 − 2i", "2 + i et 2 − i", "−1 ± 2i", "1 ± 4i", "z = (2 ± 4i)/2."),
      ("Le module de 1 + 2i vaut :", "√5", "5", "3", "√3", "√(1 + 4)."),
      ("Les points images A(1 + 2i) et B(1 − 2i) sont :", "symétriques par rapport à l'axe des réels", "confondus", "symétriques par rapport à O", "sur l'axe des imaginaires", "Conjugués."),
    ]),
    P("Problème : f(x) = x ln x − x sur ]0 ; +∞[", "Étude de f et calcul d'aire.", [
      ("f'(x) vaut :", "ln x", "ln x − 1", "1/x", "x ln x", "(x ln x)' = ln x + 1, puis − 1."),
      ("f admet un minimum en x = 1, égal à :", "−1", "0", "1", "e", "f(1) = 0 − 1."),
      ("La limite de f en 0⁺ vaut :", "0", "−∞", "+∞", "−1", "x ln x → 0."),
      ("f(x) = 0 pour x > 0 a pour solution :", "x = e", "x = 1", "x = 0", "x = e²", "x(ln x − 1) = 0."),
      ("∫₁ᵉ ln x dx vaut :", "1", "e", "e − 1", "0", "[x ln x − x]₁ᵉ = 0 − (−1)."),
    ]),
  ]),
  "bac-type-s-maths-5": noter([
    P("Exercice : tirage simultané", "Une urne contient 3 boules rouges et 2 blanches. On tire simultanément 2 boules. X = nombre de boules rouges.", [
      ("Nombre de tirages possibles :", "10", "20", "25", "6", "C(5, 2) = 10."),
      ("P(2 rouges) :", "3/10", "1/10", "6/10", "9/25", "C(3, 2)/10."),
      ("P(X = 1) :", "3/5", "3/10", "1/5", "2/5", "3 × 2 / 10."),
      ("E(X) :", "6/5", "1", "3/2", "3/5", "0 × 1/10 + 1 × 6/10 + 2 × 3/10."),
      ("On répète 3 fois l'épreuve avec remise. P(obtenir exactement une fois 2 rouges) :", "0,441", "0,3", "0,147", "0,9", "3 × 0,3 × 0,7²."),
    ]),
    P("Problème : g(x) = (x + 1)e^(−x)", "Étude sur ℝ et intégrale.", [
      ("g'(x) vaut :", "−x e^(−x)", "e^(−x)", "(x + 2)e^(−x)", "−(x + 1)e^(−x)", "e^(−x) − (x + 1)e^(−x)."),
      ("g admet un maximum en 0 égal à :", "1", "0", "e", "2", "g(0) = 1."),
      ("Limite de g en +∞ :", "0", "+∞", "1", "−∞", "Croissances comparées."),
      ("Une primitive de g est :", "−(x + 2)e^(−x)", "(x + 2)e^(−x)", "−(x + 1)e^(−x)", "x e^(−x)", "On vérifie en dérivant."),
      ("∫₀¹ g(x) dx vaut :", "2 − 3/e", "3/e − 2", "1 − 1/e", "2/e", "−3e^(−1) + 2."),
    ]),
  ]),
  "bac-type-s-maths-6": noter([
    P("Exercice : suite", "u₀ = 2 et u(n+1) = ½ u(n) + 3. On pose v(n) = u(n) − 6.", [
      ("u₁ vaut :", "4", "5", "7", "3", "½ × 2 + 3."),
      ("La limite éventuelle ℓ vérifie ℓ = ½ ℓ + 3, donc ℓ =", "6", "3", "2", "12", "½ ℓ = 3."),
      ("(v(n)) est géométrique de raison :", "½", "2", "3", "−½", "v(n+1) = ½ u(n) + 3 − 6 = ½ v(n)."),
      ("Expression de u(n) :", "6 − 4 (½)ⁿ", "2 (½)ⁿ", "6 + 4 (½)ⁿ", "2 + 3n", "v₀ = −4."),
      ("lim u(n) :", "6", "0", "+∞", "2", "(½)ⁿ → 0."),
    ]),
    P("Exercice : équations différentielles", "Résoudre et trouver des solutions particulières.", [
      ("Solutions de y' − 2y = 0 :", "y = C e^(2x)", "y = C e^(−2x)", "y = 2x + C", "y = C cos 2x", "y' = ay → C e^(ax)."),
      ("Solutions de y'' + 4y = 0 :", "y = A cos 2x + B sin 2x", "y = A e^(2x) + B e^(−2x)", "y = A cos 4x + B sin 4x", "y = (Ax + B)e^(2x)", "ω² = 4."),
      ("Avec y(0) = 1 et y'(0) = 2 :", "y = cos 2x + sin 2x", "y = cos 2x + 2 sin 2x", "y = 2 cos 2x + sin 2x", "y = cos 2x", "A = 1 ; 2B = 2."),
      ("Cette solution s'écrit aussi :", "√2 cos(2x − π/4)", "2 cos(2x + π/4)", "√2 sin 2x", "cos(2x − π/2)", "Amplitude √(1 + 1)."),
    ]),
  ]),
  "bac-type-s-maths-7": noter([
    P("Exercice : espace", "Repère orthonormé. A(1 ; 0 ; 0), B(0 ; 2 ; 0), C(0 ; 0 ; 3).", [
      ("Une équation du plan (ABC) :", "6x + 3y + 2z − 6 = 0", "x + y + z − 1 = 0", "x + 2y + 3z − 6 = 0", "6x + 3y + 2z = 0", "x/1 + y/2 + z/3 = 1, multiplié par 6."),
      ("Un vecteur normal à (ABC) a pour norme (pour (6 ; 3 ; 2)) :", "7", "11", "√11", "49", "√(36 + 9 + 4)."),
      ("Distance de O au plan (ABC) :", "6/7", "1", "7/6", "6", "|−6|/7."),
      ("Volume du tétraèdre OABC :", "1", "6", "2", "3", "(1 × 2 × 3)/6."),
      ("Aire du triangle ABC :", "7/2", "3", "7", "6/7", "V = (1/3) × aire × d, donc aire = 3/(6/7)."),
    ]),
    P("Problème : h(x) = (ln x)/x sur ]0 ; +∞[", "Étude et intégrale.", [
      ("h'(x) vaut :", "(1 − ln x)/x²", "(ln x − 1)/x²", "1/x²", "−ln x/x²", "Dérivée d'un quotient."),
      ("h admet un maximum en :", "x = e, égal à 1/e", "x = 1, égal à 0", "x = e, égal à e", "x = 0", "h'(e) = 0."),
      ("Limite de h en +∞ :", "0", "+∞", "1", "−∞", "Croissances comparées."),
      ("∫₁ᵉ (ln x)/x dx vaut :", "½", "1", "e", "1/e", "[(ln x)²/2]₁ᵉ."),
    ]),
  ]),
  "bac-type-s-maths-8": noter([
    P("Exercice : complexes et transformations", "Soit a = 1 + i.", [
      ("Module et argument de a :", "√2 et π/4", "2 et π/4", "√2 et π/2", "1 et π/4", "Forme trigonométrique."),
      ("a⁴ vaut :", "−4", "4", "4i", "−4i", "a² = 2i, puis (2i)² = −4."),
      ("La rotation de centre O d'angle π/2 envoie a sur :", "−1 + i", "1 − i", "−1 − i", "i", "z' = iz."),
      ("L'application z' = (1 + i) z est :", "une similitude de rapport √2 et d'angle π/4", "une translation", "une rotation d'angle π/2", "une homothétie de rapport 2", "z' = az, a non réel."),
    ]),
    P("Exercice : statistiques à deux variables", "x : 1, 2, 3, 4, 5 et y : 3, 5, 6, 8, 8.", [
      ("Moyennes x̄ et ȳ :", "3 et 6", "3 et 5", "2,5 et 6", "3 et 6,5", "15/5 et 30/5."),
      ("Covariance cov(x, y) :", "2,6", "13", "2", "3", "(6 + 1 + 0 + 2 + 4)/5."),
      ("Variance de x :", "2", "10", "2,5", "4", "(4 + 1 + 0 + 1 + 4)/5."),
      ("Droite de régression de y en x :", "y = 1,3x + 2,1", "y = 2x", "y = 1,3x + 6", "y = 0,77x + 3,7", "a = 2,6/2 ; b = 6 − 3a."),
      ("Estimation de y pour x = 7 :", "11,2", "9,1", "12", "10,4", "1,3 × 7 + 2,1."),
    ]),
  ]),
  "bac-type-s-maths-9": noter([
    P("Exercice : probabilités conditionnelles", "Une usine : la machine A produit 60 % des pièces (2 % défectueuses), la machine B 40 % (5 % défectueuses).", [
      ("P(A ∩ D) :", "0,012", "0,02", "0,6", "0,032", "0,6 × 0,02."),
      ("P(D) :", "0,032", "0,07", "0,035", "0,012", "0,012 + 0,4 × 0,05."),
      ("P_D(A), probabilité qu'une pièce défectueuse vienne de A :", "0,375", "0,6", "0,02", "0,625", "0,012/0,032."),
      ("On prélève 10 pièces (tirages indépendants). L'espérance du nombre de pièces défectueuses :", "0,32", "3,2", "0,032", "1", "n p = 10 × 0,032."),
    ]),
    P("Problème : f(x) = eˣ − x − 1", "Étude sur ℝ.", [
      ("f'(x) :", "eˣ − 1", "eˣ − x", "eˣ", "eˣ + 1", "Dérivée terme à terme."),
      ("f admet un minimum en 0, égal à :", "0", "1", "−1", "e", "f(0) = 1 − 0 − 1."),
      ("On en déduit, pour tout réel x :", "eˣ ≥ x + 1", "eˣ ≤ x + 1", "eˣ ≥ x²", "eˣ = x + 1", "f(x) ≥ 0."),
      ("Limite de f en −∞ :", "+∞", "0", "−∞", "1", "−x → +∞."),
      ("∫₀¹ f(x) dx :", "e − 5/2", "e − 2", "e − 3/2", "5/2 − e", "[eˣ − x²/2 − x]₀¹ = e − 3/2 − 1."),
    ]),
  ]),
  "bac-type-s-pc-4": noter([
    P("Chimie : dosage", "On dose 20 mL d'acide éthanoïque par la soude à 0,1 mol/L. L'équivalence est obtenue pour 10 mL. pKa = 4,8.", [
      ("Relation à l'équivalence :", "Ca × Va = Cb × Vb,E", "Ca = Cb", "Va = Vb", "Ca × Vb = Cb × Va", "Quantités égales."),
      ("Concentration de l'acide :", "0,05 mol/L", "0,1 mol/L", "0,2 mol/L", "0,02 mol/L", "0,1 × 10 / 20."),
      ("pH à la demi-équivalence :", "4,8", "7", "2,4", "9,6", "pH = pKa."),
      ("Le pH à l'équivalence est :", "supérieur à 7", "égal à 7", "inférieur à 7", "égal à 0", "Ion éthanoate basique."),
      ("Indicateur coloré adapté :", "la phénolphtaléine (zone 8,2 - 10)", "l'hélianthine (3,1 - 4,4)", "le BBT seulement à pH 2", "aucun", "Zone de virage contenant pH(E)."),
    ]),
    P("Physique : radioactivité", "Le carbone 14 a une demi-vie T = 5 730 ans ; il est émetteur β⁻.", [
      ("Une émission β⁻ :", "augmente Z de 1 sans changer A", "diminue A de 4", "diminue Z de 1", "ne change rien", "n → p + e⁻."),
      ("Le carbone 14 (Z = 6) donne :", "de l'azote 14 (Z = 7)", "du bore 14", "du carbone 12", "de l'oxygène 16", "Z + 1."),
      ("Constante radioactive λ :", "ln 2 / T", "T / ln 2", "2T", "1/T", "Loi de décroissance."),
      ("Après 11 460 ans, il reste :", "un quart des noyaux", "la moitié", "un huitième", "rien", "Deux demi-vies."),
    ]),
  ]),
  "bac-type-s-pc-5": noter([
    P("Chimie : estérification", "On chauffe un mélange équimolaire d'acide éthanoïque et d'éthanol avec quelques gouttes d'acide sulfurique.", [
      ("Produits obtenus :", "éthanoate d'éthyle et eau", "éthanal et eau", "éthylène et dioxygène", "acide méthanoïque", "Acide + alcool → ester + eau."),
      ("Caractéristiques de la réaction :", "lente, limitée, athermique", "rapide et totale", "explosive", "totale et exothermique", "Équilibre."),
      ("Rôle de l'acide sulfurique :", "catalyseur", "réactif principal", "solvant", "produit", "Accélère sans modifier l'équilibre."),
      ("Rendement avec un alcool primaire en mélange équimolaire :", "environ 67 %", "100 %", "10 %", "33 %", "Valeur classique."),
      ("Pour augmenter le rendement on peut :", "utiliser un réactif en excès ou éliminer l'eau", "refroidir", "ajouter de l'eau", "diluer", "Déplacement d'équilibre."),
    ]),
    P("Physique : projectile", "Une balle est lancée depuis le sol avec v₀ = 10 m/s sous un angle de 45°. g = 10 m/s², frottements négligés.", [
      ("La trajectoire est :", "une parabole", "une droite", "un cercle", "une hélice", "Mouvement dans le champ de pesanteur."),
      ("La composante horizontale de la vitesse :", "reste constante", "augmente", "s'annule au sommet", "change de signe", "Aucune force horizontale."),
      ("Hauteur maximale :", "2,5 m", "5 m", "10 m", "1,25 m", "v₀² sin²α / 2g = 100 × 0,5 / 20."),
      ("Portée horizontale :", "10 m", "5 m", "20 m", "7,07 m", "v₀² sin 2α / g."),
    ]),
  ]),
  "bac-type-s-pc-6": noter([
    P("Chimie : cinétique", "On suit la décomposition de l'eau oxygénée en présence d'ions fer III.", [
      ("La vitesse volumique de formation d'un produit P :", "v = d[P]/dt", "v = [P] × t", "v = t/[P]", "v = constante", "Définition."),
      ("Les ions fer III jouent le rôle :", "de catalyseur", "de réactif", "de produit", "de solvant", "Non consommés."),
      ("Le temps de demi-réaction est :", "la durée pour atteindre la moitié de l'avancement final", "la moitié de la durée totale", "toujours 1 minute", "la durée pour tout consommer", "t½."),
      ("Un facteur qui augmente la vitesse :", "l'élévation de la température", "la dilution", "le refroidissement", "l'agitation nulle", "Facteur cinétique."),
    ]),
    P("Physique : satellites", "Un satellite de masse m décrit une orbite circulaire de rayon r autour de la Terre de masse M.", [
      ("Dans le référentiel géocentrique, le mouvement est :", "circulaire uniforme", "rectiligne", "accéléré tangentiellement", "parabolique", "Force centrale."),
      ("Vitesse du satellite :", "v = √(GM/r)", "v = GM/r", "v = √(r/GM)", "v = GMr", "Deuxième loi de Newton."),
      ("Période :", "T = 2πr/v", "T = v/r", "T = 2πv/r", "T = r/2π", "Un tour à vitesse v."),
      ("La troisième loi de Kepler dit que :", "T²/r³ est constant pour tous les satellites de la Terre", "T/r est constant", "T × r est constant", "T est le même pour tous", "Kepler."),
      ("Un satellite géostationnaire a une période de :", "24 h environ (jour sidéral)", "1 h", "12 h", "365 jours", "Il tourne avec la Terre."),
    ]),
  ]),
  "bac-type-s-pc-7": noter([
    P("Chimie : acides et bases forts", "À 25 °C : solution d'acide chlorhydrique à 0,01 mol/L et soude à 0,01 mol/L.", [
      ("pH de l'acide chlorhydrique :", "2", "1", "12", "7", "pH = −log 0,01."),
      ("pH de la soude :", "12", "2", "10", "14", "pH = 14 + log 0,01."),
      ("On dilue 10 fois l'acide : nouveau pH :", "3", "1", "2", "20", "pH augmente d'une unité."),
    ]),
    P("Physique : dipôles", "R = 1 kΩ, C = 10 µF, E = 10 V.", [
      ("Constante de temps du dipôle RC :", "10 ms", "1 ms", "100 ms", "10 s", "τ = RC = 10³ × 10⁻⁵."),
      ("À t = τ, lors de la charge, uC vaut :", "environ 6,3 V", "10 V", "5 V", "3,7 V", "63 % de E."),
      ("Énergie stockée quand uC = 10 V :", "0,5 mJ", "5 mJ", "50 mJ", "0,05 mJ", "½ C U² = ½ × 10⁻⁵ × 100."),
      ("Constante de temps d'un dipôle RL :", "τ = L/R", "τ = RL", "τ = R/L", "τ = √(LC)", "Bobine."),
      ("Période propre d'un circuit LC :", "T₀ = 2π√(LC)", "T₀ = 2πLC", "T₀ = √(L/C)", "T₀ = 1/(LC)", "Oscillations libres."),
    ]),
  ]),
  "bac-type-s-pc-8": noter([
    P("Chimie : acides α-aminés", "Étude de la glycine H₂N−CH₂−COOH et de l'alanine H₂N−CH(CH₃)−COOH.", [
      ("Les deux groupes fonctionnels d'un acide α-aminé :", "amine et acide carboxylique", "alcool et aldéhyde", "ester et amide", "cétone et alcool", "Définition."),
      ("Lequel est chiral ?", "l'alanine", "la glycine", "les deux", "aucun", "La glycine n'a pas de carbone asymétrique."),
      ("En solution aqueuse, l'acide α-aminé existe surtout sous forme :", "d'amphion (zwitterion)", "de cation uniquement", "de molécule neutre", "d'anion uniquement", "H₃N⁺−…−COO⁻."),
      ("La liaison formée entre deux acides α-aminés :", "liaison peptidique (amide)", "liaison ester", "liaison hydrogène seulement", "liaison ionique", "Dipeptide."),
    ]),
    P("Physique : lumière", "Fentes de Young : λ = 600 nm, a = 1 mm, D = 2 m. Constante de Planck h = 6,63 × 10⁻³⁴ J·s ; c = 3 × 10⁸ m/s.", [
      ("Interfrange i = λD/a :", "1,2 mm", "0,3 mm", "12 mm", "0,6 mm", "600 × 10⁻⁹ × 2 / 10⁻³."),
      ("Les interférences prouvent :", "le caractère ondulatoire de la lumière", "le caractère corpusculaire", "que la lumière est un son", "rien", "Superposition d'ondes."),
      ("Énergie d'un photon de 600 nm :", "environ 3,3 × 10⁻¹⁹ J", "3,3 × 10⁻¹⁰ J", "6 × 10⁻⁷ J", "2 J", "E = hc/λ."),
      ("L'effet photoélectrique a lieu si :", "l'énergie du photon dépasse le travail d'extraction", "la lumière est très intense quelle que soit sa fréquence", "le métal est froid", "jamais", "Seuil en fréquence."),
      ("L'effet photoélectrique prouve :", "le caractère corpusculaire de la lumière", "le caractère ondulatoire", "la diffraction", "la réfraction", "Einstein, photons."),
    ]),
  ]),
  "bac-type-s-pc-9": noter([
    P("Chimie : solutions tampons", "Mélange d'acide éthanoïque et d'éthanoate de sodium en quantités égales. pKa = 4,8.", [
      ("pH du mélange :", "4,8", "7", "2,4", "9,6", "[A⁻] = [AH] donc pH = pKa."),
      ("Propriété d'une solution tampon :", "son pH varie peu par ajout modéré d'acide, de base ou par dilution", "son pH est toujours 7", "elle est très concentrée en sel", "elle conduit mal", "Définition."),
      ("Un tampon naturel important :", "le sang (pH ≈ 7,4)", "l'eau de mer pure", "le jus de citron", "l'eau distillée", "Couple CO₂/HCO₃⁻."),
    ]),
    P("Physique : champ magnétique et oscillateur", "Une particule de charge q, masse m, entre avec la vitesse v perpendiculairement à un champ magnétique uniforme B.", [
      ("La force magnétique s'écrit :", "F = q v ∧ B", "F = q E", "F = m g", "F = q B / v", "Force de Lorentz."),
      ("Le travail de cette force est :", "nul", "positif", "négatif", "égal à qvB", "Force perpendiculaire à la vitesse."),
      ("Le mouvement est :", "circulaire uniforme de rayon R = mv/(|q|B)", "rectiligne accéléré", "parabolique", "elliptique", "Accélération normale constante."),
      ("Pendule élastique m = 0,1 kg, k = 10 N/m : période propre :", "environ 0,63 s", "6,3 s", "0,1 s", "1 s", "T₀ = 2π√(m/k) = 2π × 0,1."),
      ("Si m est multipliée par 4, la période :", "double", "est multipliée par 4", "est divisée par 2", "ne change pas", "√4 = 2."),
    ]),
  ]),
  "bac-type-s-svt-4": noter([
    P("Maîtrise des connaissances : contraction musculaire", "Exposé sur le muscle strié squelettique.", [
      ("L'unité contractile du muscle strié :", "le sarcomère", "le neurone", "la synapse", "le noyau", "Entre deux stries Z."),
      ("Lors de la contraction, les filaments d'actine :", "glissent entre les filaments de myosine", "se raccourcissent", "disparaissent", "s'allongent", "Théorie du glissement."),
      ("L'ion qui déclenche la contraction en se libérant du réticulum :", "le calcium", "le sodium", "le chlore", "le fer", "Ca²⁺ libéré."),
      ("La source d'énergie immédiate de la contraction :", "l'ATP", "le glucose directement", "l'oxygène", "l'eau", "Hydrolyse de l'ATP."),
    ]),
    P("Compétences : monohybridisme", "On croise deux lignées pures de pois : graines lisses × graines ridées. F1 : 100 % lisses.", [
      ("L'allèle dominant est :", "lisse", "ridé", "aucun", "les deux (codominance)", "Seul le phénotype lisse apparaît en F1."),
      ("Génotype des F1 :", "L//r", "L//L", "r//r", "L", "Hétérozygotes."),
      ("Proportions attendues en F2 (F1 × F1) :", "3/4 lisses, 1/4 ridées", "1/2 – 1/2", "100 % lisses", "9/16 – 7/16", "Ségrégation."),
      ("Croisement F1 × parent ridé (test-cross) :", "1/2 lisses, 1/2 ridées", "3/4 lisses", "100 % ridées", "1/4 lisses", "Révèle les gamètes du F1."),
      ("Ce résultat illustre :", "la première loi de Mendel (pureté des gamètes)", "le crossing-over", "l'hérédité liée au sexe", "la mutation", "Loi de disjonction."),
    ]),
  ]),
  "bac-type-s-svt-5": noter([
    P("Maîtrise des connaissances : pression artérielle", "Régulation nerveuse de la pression artérielle.", [
      ("Les récepteurs sensibles à la pression artérielle :", "les barorécepteurs du sinus carotidien et de la crosse aortique", "les cônes de la rétine", "les papilles gustatives", "les cellules β du pancréas", "Mécanorécepteurs."),
      ("Une hausse de pression entraîne :", "une stimulation du parasympathique et un ralentissement du cœur", "une accélération du cœur", "une vasoconstriction", "rien", "Système cardio-modérateur."),
      ("Le nerf parasympathique libère au niveau du cœur :", "de l'acétylcholine", "de l'adrénaline", "de l'insuline", "du glucagon", "Neurotransmetteur."),
      ("Le centre nerveux de cette régulation :", "le bulbe rachidien", "le cortex visuel", "la moelle osseuse", "le cervelet", "Centres bulbaires."),
    ]),
    P("Compétences : dihybridisme", "Drosophiles : corps gris ailes longues (lignée pure) × corps noir ailes vestigiales (lignée pure). F1 : 100 % gris longues. Croisement test : 4 phénotypes à 25 % chacun.", [
      ("Allèles dominants :", "gris et ailes longues", "noir et vestigiales", "gris et vestigiales", "aucun", "Phénotype F1."),
      ("4 phénotypes équiprobables au test-cross indiquent :", "des gènes indépendants", "des gènes liés sans crossing-over", "un seul gène", "une hérédité liée au sexe", "Brassage interchromosomique."),
      ("Si les gènes étaient liés, on observerait :", "deux phénotypes parentaux majoritaires", "4 phénotypes à 25 %", "un seul phénotype", "aucun descendant", "Recombinés minoritaires."),
      ("Proportions en F2 pour deux gènes indépendants :", "9/16, 3/16, 3/16, 1/16", "3/4, 1/4", "1/4 chacun", "1/2, 1/2", "Dihybridisme mendélien."),
      ("Les phénotypes recombinés résultent :", "d'un brassage lors de la méiose", "d'une mutation", "de la mitose", "de l'environnement", "Méiose."),
    ]),
  ]),
  "bac-type-s-svt-6": noter([
    P("Maîtrise des connaissances : VIH et sida", "Exposé sur l'infection par le VIH.", [
      ("La cible principale du VIH :", "les lymphocytes T4 (CD4)", "les globules rouges", "les neurones", "les plaquettes", "Récepteur CD4."),
      ("Le VIH est un rétrovirus car :", "il transcrit son ARN en ADN grâce à la transcriptase inverse", "il n'a pas de génome", "il est une bactérie", "il se divise par mitose", "Rétrotranscription."),
      ("Au stade sida, l'organisme :", "est vulnérable aux maladies opportunistes", "est immunisé contre tout", "élimine le virus", "n'a plus de virus", "Effondrement des T4."),
      ("Un moyen de prévention :", "l'usage du préservatif et le dépistage", "les antibiotiques", "un vaccin obligatoire disponible", "éviter de serrer la main", "Transmission sexuelle et sanguine."),
    ]),
    P("Compétences : hérédité liée au sexe", "L'hémophilie est due à un allèle récessif h porté par le chromosome X. Un couple : père sain, mère saine, fils hémophile.", [
      ("Génotype de la mère :", "Xᴴ Xʰ (conductrice)", "Xᴴ Xᴴ", "Xʰ Xʰ", "Xᴴ Y", "Le fils reçoit son X de sa mère."),
      ("Génotype du père :", "Xᴴ Y", "Xʰ Y", "Xᴴ Xʰ", "Y Y", "Père sain."),
      ("Probabilité qu'un autre fils soit hémophile :", "1/2", "1/4", "0", "1", "Moitié des X maternels portent h."),
      ("Probabilité qu'une fille soit hémophile :", "0", "1/2", "1/4", "1", "Elle reçoit Xᴴ du père."),
      ("Pourquoi les hommes sont-ils plus souvent atteints ?", "un seul X : l'allèle récessif s'exprime toujours", "ils ont deux X", "le Y porte la maladie", "par hasard", "Hémizygotie."),
    ]),
  ]),
  "bac-type-s-svt-7": noter([
    P("Maîtrise des connaissances : régulation hormonale chez la femme", "Exposé sur le cycle sexuel.", [
      ("Les hormones hypophysaires agissant sur l'ovaire :", "FSH et LH", "insuline et glucagon", "adrénaline et cortisol", "testostérone seule", "Gonadostimulines."),
      ("Le pic de LH déclenche :", "l'ovulation", "les règles", "la puberté", "la ménopause", "Vers le 14e jour."),
      ("Après l'ovulation, le corps jaune sécrète :", "de la progestérone et des œstrogènes", "de la FSH", "de l'insuline", "de la GnRH", "Phase lutéale."),
      ("L'hormone hypothalamique qui contrôle l'hypophyse :", "la GnRH", "la LH", "la prolactine", "la thyroxine", "Neurohormone."),
    ]),
    P("Compétences : exploiter des dosages", "Document : courbes des taux d'œstradiol et de LH au cours d'un cycle de 28 jours.", [
      ("Juste avant le pic de LH, le taux d'œstradiol :", "est élevé (pic)", "est nul", "baisse fortement", "reste constant", "Rétrocontrôle positif."),
      ("En phase lutéale, les fortes concentrations d'hormones ovariennes exercent :", "un rétrocontrôle négatif sur l'hypothalamus et l'hypophyse", "un rétrocontrôle positif", "aucun effet", "une stimulation de la LH", "Freinage."),
      ("La chute de la progestérone en fin de cycle provoque :", "les règles (menstruation)", "l'ovulation", "la fécondation", "la nidation", "Desquamation de l'endomètre."),
      ("En cas de grossesse, le corps jaune est maintenu par :", "l'hormone hCG de l'embryon", "la FSH", "la chute de LH", "l'adrénaline", "Base des tests de grossesse."),
      ("La pilule contraceptive agit surtout par :", "rétrocontrôle négatif qui bloque l'ovulation", "destruction des ovules", "augmentation de la FSH", "stimulation de la LH", "Hormones de synthèse."),
    ]),
  ]),
  "bac-type-s-svt-8": noter([
    P("Maîtrise des connaissances : méiose", "Exposé sur la méiose et le brassage génétique.", [
      ("La méiose produit à partir d'une cellule diploïde :", "4 cellules haploïdes", "2 cellules diploïdes", "4 cellules diploïdes", "1 cellule", "Deux divisions successives."),
      ("Le brassage intrachromosomique a lieu :", "en prophase I par crossing-over", "en anaphase II", "pendant la fécondation", "en interphase", "Échanges entre chromatides."),
      ("Le brassage interchromosomique a lieu :", "en anaphase I par migration aléatoire des homologues", "en prophase II", "en télophase II", "pendant la mitose", "Disjonction indépendante."),
      ("Chez l'homme (2n = 46), nombre de combinaisons par le seul brassage interchromosomique :", "2²³", "23", "46", "2⁴⁶", "Environ 8 millions."),
    ]),
    P("Compétences : réflexe myotatique", "Document : un choc sur le tendon rotulien provoque l'extension de la jambe.", [
      ("Le récepteur du réflexe myotatique :", "le fuseau neuromusculaire du muscle étiré", "la peau", "l'œil", "l'oreille", "Récepteur à l'étirement."),
      ("Le centre nerveux de ce réflexe :", "la moelle épinière", "le cerveau", "le cervelet", "le bulbe", "Réflexe médullaire."),
      ("Ce réflexe est monosynaptique car :", "une seule synapse relie le neurone sensitif au motoneurone du muscle", "il n'y a pas de synapse", "il passe par le cerveau", "il met en jeu 10 neurones", "Arc réflexe court."),
      ("Le muscle antagoniste (fléchisseur) est :", "inhibé par un interneurone", "contracté en même temps", "stimulé directement", "sans lien", "Innervation réciproque."),
      ("La synapse neuromusculaire utilise comme neurotransmetteur :", "l'acétylcholine", "la dopamine", "le GABA", "l'insuline", "Plaque motrice."),
    ]),
  ]),
  "bac-type-s-svt-9": noter([
    P("Maîtrise des connaissances : fécondation et contraception", "Exposé sur la fécondation chez l'espèce humaine.", [
      ("La fécondation a lieu normalement :", "dans le tiers supérieur de la trompe", "dans l'utérus", "dans l'ovaire", "dans le vagin", "Rencontre des gamètes."),
      ("La réaction acrosomiale permet :", "au spermatozoïde de traverser la zone pellucide", "à l'ovule de se diviser", "la nidation", "la menstruation", "Enzymes de l'acrosome."),
      ("La nidation a lieu environ :", "7 jours après la fécondation", "le jour même", "1 mois après", "à l'accouchement", "Implantation du blastocyste."),
      ("Une méthode contraceptive mécanique :", "le préservatif", "la pilule", "l'implant hormonal", "la pilule du lendemain", "Barrière physique."),
    ]),
    P("Compétences : groupes sanguins ABO", "Les allèles A et B sont codominants, O est récessif. Un père de groupe A et une mère de groupe B ont un enfant de groupe O.", [
      ("Génotype de l'enfant :", "O//O", "A//O", "A//B", "B//O", "O récessif."),
      ("Génotype du père :", "A//O", "A//A", "A//B", "O//O", "Il a transmis O."),
      ("Génotype de la mère :", "B//O", "B//B", "A//B", "O//O", "Elle a transmis O."),
      ("Probabilité d'un enfant de groupe AB :", "1/4", "1/2", "0", "3/4", "1/2 × 1/2."),
      ("Les allèles A et B sont dits codominants car :", "chez A//B les deux s'expriment", "l'un masque l'autre", "aucun ne s'exprime", "ils sont sur le Y", "Groupe AB."),
    ]),
  ]),
}
