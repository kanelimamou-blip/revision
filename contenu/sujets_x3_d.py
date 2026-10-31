# Sujets types d'entraînement ×3 : Terminale L (maths) et Terminale G (maths, économie, techniques comptables).
from sujets_tle2 import P, noter, A

L, G = ["Tle L"], ["Tle G"]
def _l(n, parts): return A(f"bac-type-l-maths-{n}", "Mathématiques", L, "L1a, L1b, L2, L'", "2 h", parts)
def _g(n, parts): return A(f"bac-type-g-maths-{n}", "Mathématiques", G, "G", "3 h", parts)
def _e(n, parts): return A(f"bac-type-g-eco-{n}", "Économie", G, "G", "3 h", parts)
def _c(n, parts): return A(f"bac-type-g-compta-{n}", "Techniques comptables", G, "G", "4 h", parts)

ANNALES_X = [
  _l(4, ["Exercice : suite arithmétique et salaire", "Problème : fonction du second degré"]),
  _l(5, ["Exercice : probabilités avec un dé", "Problème : fonction eˣ − x"]),
  _l(6, ["Exercice : placement à intérêts composés", "Problème : fonction logarithme"]),
  _l(7, ["Exercice : statistiques à une variable", "Problème : fonction homographique"]),
  _l(8, ["Exercice : dénombrement", "Problème : fonction x eˣ"]),
  _l(9, ["Exercice : croissance d'une population", "Exercice : système d'équations"]),
  _g(4, ["Exercice : intérêts simples et escompte", "Problème : bénéfice et seuils de rentabilité"]),
  _g(5, ["Exercice : intérêts composés et annuités", "Exercice : loi binomiale"]),
  _g(6, ["Exercice : ajustement affine publicité-ventes", "Exercice : évolution des prix"]),
  _g(7, ["Exercice : emprunt indivis", "Problème : coût marginal et coût moyen"]),
  _g(8, ["Exercice : probabilités et indépendance", "Problème : fonction de demande et élasticité"]),
  _g(9, ["Exercice : indices et taux d'évolution", "Exercice : suite géométrique du chiffre d'affaires"]),
  _e(4, ["Connaissances", "Exercice : croissance et développement", "Analyse : IDH et pauvreté"]),
  _e(5, ["Connaissances", "Exercice : indice des prix et inflation", "Analyse : vie chère"]),
  _e(6, ["Connaissances", "Exercice : production et valeur ajoutée", "Analyse : PME sénégalaises"]),
  _e(7, ["Connaissances", "Exercice : répartition des revenus", "Analyse : inégalités"]),
  _e(8, ["Connaissances", "Exercice : balance des paiements", "Analyse : transferts des émigrés"]),
  _e(9, ["Connaissances", "Exercice : population active et emploi", "Analyse : secteur informel"]),
  _c(4, ["Dossier 1 : facture et TVA", "Dossier 2 : amortissement linéaire"]),
  _c(5, ["Dossier 1 : rapprochement bancaire", "Dossier 2 : dépréciation des créances"]),
  _c(6, ["Dossier 1 : fiche de stock au CMUP", "Dossier 2 : marge commerciale"]),
  _c(7, ["Dossier 1 : escompte d'un effet de commerce", "Dossier 2 : équilibre financier du bilan"]),
  _c(8, ["Dossier 1 : enregistrements au journal", "Dossier 2 : coût de revient et résultat"]),
  _c(9, ["Dossier 1 : seuil de rentabilité", "Dossier 2 : affectation du résultat"]),
]

GUIDED_X = {
  "bac-type-l-maths-4": noter([
    P("Exercice : suite arithmétique", "Un employé gagne 500 000 F la première année (u₀) ; son salaire annuel augmente de 50 000 F par an.", [
      ("(uₙ) est une suite :", "arithmétique de raison 50 000", "géométrique de raison 50 000", "constante", "géométrique de raison 1,1", "On ajoute la même somme."),
      ("u₁₀ vaut :", "1 000 000 F", "550 000 F", "5 000 000 F", "1 050 000 F", "500 000 + 10 × 50 000."),
      ("Total perçu de u₀ à u₁₀ (11 années) :", "8 250 000 F", "8 000 000 F", "11 000 000 F", "5 500 000 F", "11 × (500 000 + 1 000 000)/2."),
    ]),
    P("Problème : f(x) = x² − 4x + 3", "Étude sur ℝ.", [
      ("f'(x) :", "2x − 4", "2x + 4", "x − 4", "2x² − 4", "Dérivée d'un polynôme."),
      ("f admet un minimum en x = 2 égal à :", "−1", "3", "0", "1", "4 − 8 + 3."),
      ("Les solutions de f(x) = 0 :", "1 et 3", "−1 et −3", "2 et 4", "0 et 4", "(x − 1)(x − 3)."),
      ("f(x) < 0 pour :", "x ∈ ]1 ; 3[", "x < 1", "x > 3", "jamais", "Entre les racines (a > 0)."),
      ("Équation de la tangente en x = 0 :", "y = −4x + 3", "y = 4x + 3", "y = −4x", "y = 3", "f(0) = 3, f'(0) = −4."),
    ]),
  ]),
  "bac-type-l-maths-5": noter([
    P("Exercice : dé équilibré", "On lance un dé cubique équilibré numéroté de 1 à 6.", [
      ("P(obtenir un nombre pair) :", "1/2", "1/3", "1/6", "2/3", "3 cas sur 6."),
      ("P(obtenir au moins 5) :", "1/3", "1/6", "1/2", "5/6", "5 ou 6."),
      ("On lance deux fois. P(deux 6) :", "1/36", "1/6", "1/12", "2/6", "1/6 × 1/6."),
      ("P(au moins un 6 en deux lancers) :", "11/36", "1/3", "1/36", "25/36", "1 − (5/6)²."),
    ]),
    P("Problème : f(x) = eˣ − x", "Étude sur ℝ.", [
      ("f'(x) :", "eˣ − 1", "eˣ", "eˣ − x", "1 − eˣ", "Dérivée."),
      ("f est croissante sur :", "[0 ; +∞[", "]−∞ ; 0]", "ℝ", "aucun intervalle", "eˣ ≥ 1 pour x ≥ 0."),
      ("Minimum de f :", "1, atteint en 0", "0, atteint en 1", "e, atteint en 1", "−1", "f(0) = 1."),
      ("f(1) vaut :", "e − 1 ≈ 1,72", "e", "1", "0", "Calcul."),
    ]),
  ]),
  "bac-type-l-maths-6": noter([
    P("Exercice : intérêts composés", "On place 100 000 F à 5 % par an, intérêts composés. Cₙ = capital après n années.", [
      ("C₁ :", "105 000 F", "150 000 F", "100 500 F", "110 000 F", "100 000 × 1,05."),
      ("C₂ :", "110 250 F", "110 000 F", "105 000 F", "115 000 F", "105 000 × 1,05."),
      ("Expression de Cₙ :", "100 000 × 1,05ⁿ", "100 000 + 5n", "100 000 × 5ⁿ", "105 000n", "Suite géométrique."),
      ("Le capital double dès que n ≥ ln 2 / ln 1,05 ≈ 14,2, soit au bout de :", "15 ans", "14 ans", "20 ans", "10 ans", "Premier entier qui convient."),
    ]),
    P("Problème : g(x) = 2 ln x sur [1 ; e]", "Étude rapide.", [
      ("g'(x) :", "2/x", "2 ln x", "1/(2x)", "2x", "(ln x)' = 1/x."),
      ("Sens de variation de g :", "croissante", "décroissante", "constante", "alternée", "2/x > 0."),
      ("g(1) et g(e) :", "0 et 2", "1 et e", "0 et e", "2 et 0", "ln 1 = 0, ln e = 1."),
      ("Solution de g(x) = 1 :", "x = √e", "x = e", "x = 1/2", "x = e²", "ln x = 1/2."),
    ]),
  ]),
  "bac-type-l-maths-7": noter([
    P("Exercice : statistiques", "Notes d'une classe : 8 (2 élèves), 10 (3), 12 (5), 14 (3), 16 (2).", [
      ("Effectif total :", "15", "5", "60", "12", "2 + 3 + 5 + 3 + 2."),
      ("Moyenne :", "12", "11", "13", "10", "180/15."),
      ("Mode :", "12", "16", "8", "5", "Effectif le plus grand."),
      ("Médiane :", "12", "10", "14", "11", "8e valeur sur 15."),
    ]),
    P("Problème : f(x) = (2x + 1)/(x − 1)", "Définie sur ℝ \\ {1}.", [
      ("Asymptote verticale :", "x = 1", "x = 2", "y = 1", "x = −1/2", "Le dénominateur s'annule."),
      ("Asymptote horizontale :", "y = 2", "y = 1", "y = 0", "y = −1", "Quotient des coefficients de x."),
      ("f'(x) :", "−3/(x − 1)²", "3/(x − 1)²", "2/(x − 1)", "−1/(x − 1)²", "(2(x − 1) − (2x + 1))/(x − 1)²."),
      ("f s'annule en :", "x = −1/2", "x = 1", "x = 2", "x = 0", "2x + 1 = 0."),
    ]),
  ]),
  "bac-type-l-maths-8": noter([
    P("Exercice : dénombrement", "Codes et comités.", [
      ("Nombre de codes à 4 chiffres (0 à 9) :", "10 000", "5 040", "40", "9 999", "10⁴."),
      ("Codes à 4 chiffres tous différents :", "5 040", "10 000", "210", "24", "10 × 9 × 8 × 7."),
      ("Comités de 3 personnes parmi 10 :", "120", "720", "30", "1 000", "C(10, 3)."),
      ("Classements des 3 premiers parmi 10 coureurs :", "720", "120", "30", "6", "10 × 9 × 8 (ordre compte)."),
    ]),
    P("Problème : f(x) = x eˣ", "Étude sur ℝ.", [
      ("f'(x) :", "(x + 1)eˣ", "eˣ", "x eˣ", "(x − 1)eˣ", "Dérivée d'un produit."),
      ("f admet un minimum en :", "x = −1, égal à −1/e", "x = 0, égal à 0", "x = 1, égal à e", "x = −1, égal à e", "f'(−1) = 0."),
      ("Limite de f en −∞ :", "0", "−∞", "+∞", "1", "Croissances comparées."),
      ("f(x) = 0 a pour solution :", "x = 0", "x = 1", "x = −1", "aucune", "eˣ > 0."),
    ]),
  ]),
  "bac-type-l-maths-9": noter([
    P("Exercice : population", "Une ville compte 2 000 000 d'habitants en 2025 ; la population augmente de 3 % par an.", [
      ("Population en 2026 :", "2 060 000", "2 003 000", "2 300 000", "2 600 000", "× 1,03."),
      ("La suite des populations est :", "géométrique de raison 1,03", "arithmétique de raison 3", "géométrique de raison 0,03", "constante", "Coefficient multiplicateur."),
      ("Population en 2025 + n :", "2 000 000 × 1,03ⁿ", "2 000 000 + 3n", "2 000 000 × 3ⁿ", "2 060 000n", "uₙ = u₀ qⁿ."),
    ]),
    P("Exercice : système", "Un vendeur : 2 cahiers et 1 stylo coûtent 700 F ; un cahier coûte 200 F de plus qu'un stylo. (unités de 100 F : 2x + y = 7 et x − y = 2)", [
      ("En additionnant les deux équations :", "3x = 9", "x = 5", "3y = 9", "2x = 5", "y s'élimine."),
      ("x vaut :", "3", "2", "1", "4", "9/3."),
      ("y vaut :", "1", "3", "2", "0", "x − 2."),
      ("Prix d'un cahier et d'un stylo :", "300 F et 100 F", "200 F et 100 F", "100 F et 300 F", "350 F et 0 F", "Retour aux unités."),
    ]),
  ]),
  "bac-type-g-maths-4": noter([
    P("Exercice : intérêts simples et escompte", "Formules : I = C t n / 1 200 (n en mois) ; escompte E = V t j / 36 000 (j en jours).", [
      ("Intérêt de 200 000 F à 6 % pendant 9 mois :", "9 000 F", "12 000 F", "1 080 F", "90 000 F", "200 000 × 6 × 9 / 1 200."),
      ("Escompte d'un effet de 500 000 F, taux 12 %, 60 jours :", "10 000 F", "60 000 F", "1 000 F", "5 000 F", "500 000 × 12 × 60 / 36 000."),
      ("Valeur actuelle de cet effet :", "490 000 F", "510 000 F", "500 000 F", "440 000 F", "V − E."),
    ]),
    P("Problème : bénéfice", "B(x) = −x² + 40x − 300, en milliers de F, pour x centaines d'articles.", [
      ("B'(x) :", "−2x + 40", "−2x + 40x", "2x − 40", "−x + 40", "Dérivée."),
      ("Production qui maximise le bénéfice :", "x = 20", "x = 40", "x = 10", "x = 30", "B'(x) = 0."),
      ("Bénéfice maximal :", "100", "300", "400", "0", "−400 + 800 − 300."),
      ("Seuils de rentabilité (B = 0) :", "x = 10 et x = 30", "x = 20", "x = 0 et x = 40", "x = 15 et x = 25", "x² − 40x + 300 = (x − 10)(x − 30)."),
      ("L'entreprise est bénéficiaire pour :", "10 < x < 30", "x < 10", "x > 30", "toujours", "Entre les racines."),
    ]),
  ]),
  "bac-type-g-maths-5": noter([
    P("Exercice : intérêts composés et annuités", "Taux annuel i, capital C₀, n années.", [
      ("1 000 000 F à 8 % pendant 2 ans :", "1 166 400 F", "1 160 000 F", "1 080 000 F", "1 640 000 F", "1 000 000 × 1,08²."),
      ("Valeur actuelle de 1 166 400 F payables dans 2 ans à 8 % :", "1 000 000 F", "1 080 000 F", "1 166 400 F", "933 120 F", "Actualisation : × 1,08⁻²."),
      ("Valeur acquise de 3 annuités de 100 000 F à 10 % : formule a((1 + i)ⁿ − 1)/i :", "331 000 F", "300 000 F", "330 000 F", "133 100 F", "100 000 × 0,331/0,1."),
    ]),
    P("Exercice : loi binomiale", "Un client achète avec la probabilité 0,5 ; on observe 4 clients indépendants. X = nombre d'acheteurs.", [
      ("X suit une loi :", "binomiale B(4 ; 0,5)", "uniforme sur {0 ; 4}", "normale", "géométrique", "Répétition d'épreuves de Bernoulli."),
      ("P(X = 2) :", "0,375", "0,5", "0,25", "0,0625", "C(4, 2) × 0,5⁴ = 6/16."),
      ("P(X = 0) :", "0,0625", "0", "0,5", "0,25", "0,5⁴."),
      ("E(X) :", "2", "4", "1", "0,5", "n p."),
      ("P(X ≥ 1) :", "0,9375", "0,0625", "0,5", "1", "1 − P(X = 0)."),
    ]),
  ]),
  "bac-type-g-maths-6": noter([
    P("Exercice : publicité et ventes", "x (dépenses en millions) : 2, 4, 6, 8 ; y (ventes en millions) : 10, 14, 20, 24.", [
      ("x̄ et ȳ :", "5 et 17", "4 et 17", "5 et 16", "6 et 20", "20/4 et 68/4."),
      ("cov(x, y) :", "12", "48", "5", "17", "(21 + 3 + 3 + 21)/4."),
      ("V(x) :", "5", "20", "4", "2,5", "(9 + 1 + 1 + 9)/4."),
      ("Droite de y en x :", "y = 2,4x + 5", "y = 2x + 7", "y = 2,4x + 17", "y = 0,4x + 15", "a = 12/5 ; b = 17 − 2,4 × 5."),
      ("Ventes prévues pour x = 10 :", "29 millions", "24 millions", "34 millions", "17 millions", "2,4 × 10 + 5."),
    ]),
    P("Exercice : évolution des prix", "Un article coûte 10 000 F et son prix augmente de 4 % par an.", [
      ("Prix au bout d'un an :", "10 400 F", "10 040 F", "14 000 F", "10 004 F", "× 1,04."),
      ("Prix au bout de n années :", "10 000 × 1,04ⁿ", "10 000 + 400n", "10 000 × 4ⁿ", "10 400n", "Suite géométrique."),
      ("Deux hausses successives de 4 % équivalent à une hausse de :", "8,16 %", "8 %", "16 %", "4 %", "1,04² = 1,0816."),
    ]),
  ]),
  "bac-type-g-maths-7": noter([
    P("Exercice : emprunt indivis", "Emprunt de 1 000 000 F à 10 %, remboursé par 2 annuités constantes a = C i / (1 − (1 + i)⁻ⁿ).", [
      ("Annuité constante (arrondie) :", "576 190 F", "550 000 F", "500 000 F", "605 000 F", "100 000 / (1 − 1/1,21)."),
      ("Intérêt de la 1re année :", "100 000 F", "57 619 F", "10 000 F", "50 000 F", "1 000 000 × 0,1."),
      ("Premier amortissement :", "476 190 F", "576 190 F", "500 000 F", "100 000 F", "a − intérêt."),
      ("Capital restant dû après la 1re annuité :", "523 810 F", "476 190 F", "500 000 F", "423 810 F", "1 000 000 − 476 190."),
    ]),
    P("Problème : coûts", "C(x) = x² + 10x + 100 (coût total en milliers de F pour x unités).", [
      ("Coût marginal Cm(x) = C'(x) :", "2x + 10", "x + 10", "2x + 110", "x² + 10", "Dérivée."),
      ("Coût moyen CM(x) = C(x)/x :", "x + 10 + 100/x", "x + 10", "2x + 10", "x² + 10x", "Division par x."),
      ("Le coût moyen est minimal pour :", "x = 10", "x = 100", "x = 5", "x = 20", "CM'(x) = 1 − 100/x² = 0."),
      ("Coût moyen minimal :", "30", "20", "10", "210", "10 + 10 + 10."),
      ("Au minimum du coût moyen :", "coût marginal = coût moyen", "coût marginal = 0", "coût total = 0", "coût moyen = 0", "Cm(10) = 30."),
    ]),
  ]),
  "bac-type-g-maths-8": noter([
    P("Exercice : probabilités", "Dans une clientèle : P(A) = 0,4 (paie par mobile), P(B) = 0,5 (achète en gros), P(A ∩ B) = 0,2.", [
      ("P(A ∪ B) :", "0,7", "0,9", "0,2", "0,5", "0,4 + 0,5 − 0,2."),
      ("A et B sont-ils indépendants ?", "oui, car P(A) × P(B) = P(A ∩ B)", "non", "on ne peut pas savoir", "oui car P(A) < P(B)", "0,4 × 0,5 = 0,2."),
      ("P_B(A) :", "0,4", "0,2", "0,5", "0,8", "0,2/0,5."),
      ("P(ni A ni B) :", "0,3", "0,7", "0,1", "0,5", "1 − P(A ∪ B)."),
    ]),
    P("Problème : demande", "q(p) = 1 000 e^(−0,1 p), demande en fonction du prix p.", [
      ("q(0) :", "1 000", "0", "100", "e", "e⁰ = 1."),
      ("q(10) ≈", "368", "1 000", "100", "632", "1 000/e."),
      ("q est :", "décroissante", "croissante", "constante", "nulle", "q'(p) = −100 e^(−0,1 p) < 0."),
      ("Élasticité E(p) = p q'(p)/q(p) :", "−0,1 p", "0,1 p", "−p", "−0,1", "Le facteur e^(−0,1p) se simplifie."),
      ("Élasticité pour p = 10 :", "−1", "−10", "1", "0", "−0,1 × 10."),
    ]),
  ]),
  "bac-type-g-maths-9": noter([
    P("Exercice : indices et taux", "Le prix d'un sac de riz passe de 20 000 F à 25 000 F.", [
      ("Taux d'évolution :", "+25 %", "+20 %", "+5 %", "+50 %", "5 000/20 000."),
      ("Indice base 100 :", "125", "120", "25", "80", "25 000/20 000 × 100."),
      ("Deux hausses de 10 % puis 20 % équivalent à :", "+32 %", "+30 %", "+20 %", "+12 %", "1,1 × 1,2 = 1,32."),
      ("Une hausse de 21 % en 2 ans correspond à un taux annuel moyen de :", "10 %", "10,5 %", "21 %", "11 %", "√1,21 = 1,1."),
    ]),
    P("Exercice : chiffre d'affaires", "Une entreprise réalise 50 millions de F en 2025 ; prévision : +5 % par an.", [
      ("Chiffre d'affaires 2026 :", "52,5 millions", "55 millions", "50,5 millions", "57,5 millions", "50 × 1,05."),
      ("Somme des CA de 2025 à 2027 :", "157,625 millions", "150 millions", "157,5 millions", "165 millions", "50 + 52,5 + 55,125."),
      ("Le CA dépassera 60 millions la première année où 1,05ⁿ > 1,2, soit n =", "4 (en 2029)", "3", "2", "5", "1,05³ ≈ 1,158 ; 1,05⁴ ≈ 1,216."),
    ]),
  ]),
  "bac-type-g-eco-4": noter([
    P("Connaissances", "Croissance et développement.", [
      ("La croissance économique est :", "l'augmentation durable de la production (PIB réel)", "l'amélioration du bien-être", "la hausse des prix", "la baisse du chômage", "Notion quantitative."),
      ("Le développement est :", "une transformation qualitative des structures et du niveau de vie", "seulement la hausse du PIB", "la hausse des impôts", "l'exportation de pétrole", "Notion qualitative."),
      ("Le PIB mesure :", "la somme des valeurs ajoutées produites sur le territoire", "la richesse des seuls nationaux à l'étranger", "le patrimoine", "les impôts", "Définition."),
    ]),
    P("Exercice", "Le PIB réel passe de 16 000 à 16 800 milliards de F en un an ; la population de 18 à 18,45 millions.", [
      ("Taux de croissance du PIB :", "5 %", "8 %", "2,5 %", "50 %", "800/16 000."),
      ("Taux de croissance de la population :", "2,5 %", "5 %", "0,45 %", "4,5 %", "0,45/18."),
      ("Le PIB par habitant a augmenté d'environ :", "2,4 %", "5 %", "7,5 %", "0 %", "1,05/1,025 ≈ 1,024."),
    ]),
    P("Analyse", "Document : le Sénégal a un IDH faible malgré une croissance soutenue.", [
      ("Les trois dimensions de l'IDH :", "santé, éducation, niveau de vie", "PIB, exportations, impôts", "population, superficie, climat", "monnaie, banque, bourse", "PNUD."),
      ("Pourquoi croissance ne signifie pas toujours développement :", "les fruits de la croissance peuvent être mal répartis", "la croissance fait baisser le PIB", "la croissance est toujours négative", "le PIB n'existe pas", "Inégalités."),
      ("Une politique favorable au développement :", "investir dans l'éducation et la santé", "supprimer les écoles", "augmenter seulement les importations", "réduire la scolarisation", "Capital humain."),
    ]),
  ]),
  "bac-type-g-eco-5": noter([
    P("Connaissances", "L'inflation.", [
      ("L'inflation est :", "une hausse générale et durable des prix", "une baisse des prix", "une hausse d'un seul prix", "une hausse des salaires seulement", "Définition."),
      ("L'inflation par la demande vient :", "d'une demande supérieure à l'offre", "d'une hausse des coûts de production", "d'une baisse de la monnaie en circulation", "d'une récolte abondante", "Cause."),
      ("Au Sénégal, la stabilité des prix est un objectif de :", "la BCEAO", "l'ONU", "la FIFA", "la BAD seulement", "Banque centrale de l'UEMOA."),
    ]),
    P("Exercice", "Indice des prix : 100 en 2023, 104 en 2024, 110,24 en 2025.", [
      ("Taux d'inflation 2024 :", "4 %", "104 %", "10 %", "1,04 %", "Indice − 100."),
      ("Taux d'inflation 2025 :", "6 %", "6,24 %", "10,24 %", "5 %", "110,24/104 = 1,06."),
      ("Un salaire de 100 000 F en 2023 devenu 105 000 F en 2025 :", "a perdu du pouvoir d'achat", "a gagné du pouvoir d'achat", "est resté identique", "a doublé", "Hausse de 5 % < 10,24 %."),
    ]),
    P("Analyse", "Document : « la vie chère » au Sénégal (prix du riz, de l'huile, du loyer).", [
      ("Une conséquence de l'inflation :", "la baisse du pouvoir d'achat des ménages", "la hausse automatique de l'épargne", "la baisse des prix", "plus de pouvoir d'achat", "Effet sur les ménages."),
      ("Une mesure de l'État contre la vie chère :", "subventions et contrôle de certains prix", "supprimer les marchés", "augmenter toutes les taxes", "interdire les salaires", "Politique de prix."),
      ("Une cause importée de l'inflation :", "la hausse des prix mondiaux des produits importés", "la baisse du pétrole", "une bonne récolte locale", "la baisse des loyers", "Inflation importée."),
    ]),
  ]),
  "bac-type-g-eco-6": noter([
    P("Connaissances", "Production et entreprise.", [
      ("Les facteurs de production :", "le travail et le capital", "les impôts et les taxes", "les prix et les salaires", "la monnaie et le crédit", "Combinaison productive."),
      ("La valeur ajoutée :", "production − consommations intermédiaires", "chiffre d'affaires + achats", "salaires − impôts", "profit + TVA", "Richesse créée."),
      ("Une PME est :", "une petite ou moyenne entreprise", "une banque publique", "une administration", "une organisation internationale", "Taille."),
    ]),
    P("Exercice", "Une boulangerie vend pour 12 millions de F ; elle achète farine, énergie et emballages pour 7 millions ; salaires 3 millions.", [
      ("Valeur ajoutée :", "5 millions", "12 millions", "2 millions", "9 millions", "12 − 7."),
      ("Excédent brut d'exploitation (impôts négligés) :", "2 millions", "5 millions", "3 millions", "9 millions", "VA − salaires."),
      ("Taux de valeur ajoutée :", "environ 41,7 %", "58 %", "25 %", "100 %", "5/12."),
    ]),
    P("Analyse", "Document : les PME représentent l'essentiel des entreprises sénégalaises.", [
      ("Un rôle des PME :", "créer des emplois locaux", "émettre la monnaie", "voter les lois", "fixer le taux directeur", "Emploi."),
      ("Une difficulté des PME :", "l'accès difficile au crédit bancaire", "trop de crédits", "aucun concurrent", "trop de subventions", "Financement."),
      ("Une structure publique d'appui :", "l'ADEPME", "la FIFA", "l'OTAN", "l'OPEP", "Agence de développement des PME."),
    ]),
  ]),
  "bac-type-g-eco-7": noter([
    P("Connaissances", "La répartition des revenus.", [
      ("Les revenus primaires viennent :", "de la participation à la production (salaires, profits, intérêts)", "des allocations seulement", "des dons", "des impôts", "Répartition primaire."),
      ("La redistribution est assurée surtout par :", "l'État (impôts et prestations sociales)", "les marchés seuls", "les banques étrangères", "les clubs sportifs", "Répartition secondaire."),
      ("Un revenu de transfert :", "une pension de retraite", "un salaire", "un loyer perçu", "un profit", "Revenu sans contrepartie productive directe."),
    ]),
    P("Exercice", "Un ménage gagne 300 000 F de salaire par mois, paie 30 000 F d'impôts et reçoit 20 000 F d'allocations ; il dépense 240 000 F.", [
      ("Revenu disponible :", "290 000 F", "300 000 F", "270 000 F", "320 000 F", "300 000 − 30 000 + 20 000."),
      ("Épargne :", "50 000 F", "60 000 F", "30 000 F", "0 F", "290 000 − 240 000."),
      ("Propension moyenne à consommer :", "environ 0,83", "0,8", "1,2", "0,17", "240 000/290 000."),
    ]),
    P("Analyse", "Document : les 10 % les plus riches perçoivent une part importante du revenu national.", [
      ("Un indicateur des inégalités :", "l'indice (ou coefficient) de Gini", "le taux directeur", "le PIB", "l'IDH seul", "0 = égalité parfaite."),
      ("Un impôt progressif :", "taxe davantage les hauts revenus en proportion", "taxe tout le monde au même taux", "ne taxe que les pauvres", "est supprimé", "Réduit les inégalités."),
      ("Une politique de réduction des inégalités :", "bourses de sécurité familiale et couverture maladie universelle", "suppression de l'école publique", "baisse des aides sociales", "fermeture des hôpitaux", "Programmes sénégalais."),
    ]),
  ]),
  "bac-type-g-eco-8": noter([
    P("Connaissances", "La balance des paiements.", [
      ("La balance des paiements retrace :", "toutes les opérations entre résidents et non-résidents", "le budget de l'État", "les comptes d'une entreprise", "les dépenses d'un ménage", "Définition."),
      ("La balance commerciale enregistre :", "les exportations et importations de biens", "les salaires", "les impôts", "les dépôts bancaires", "Biens."),
      ("Taux de couverture :", "exportations / importations × 100", "importations / PIB", "PIB / population", "exportations − importations", "Formule."),
    ]),
    P("Exercice", "Exportations de biens : 3 000 milliards de F ; importations : 5 000 milliards.", [
      ("Solde commercial :", "−2 000 milliards (déficit)", "+2 000 milliards", "8 000 milliards", "0", "3 000 − 5 000."),
      ("Taux de couverture :", "60 %", "166 %", "40 %", "2 %", "3 000/5 000."),
      ("Les transferts des émigrés sont comptés dans :", "les revenus secondaires de la balance courante", "la balance commerciale", "le budget de l'État", "les exportations de biens", "Transferts courants."),
    ]),
    P("Analyse", "Document : les envois de fonds de la diaspora sénégalaise dépassent l'aide publique au développement.", [
      ("Un effet positif de ces transferts :", "ils soutiennent la consommation et l'investissement des familles", "ils créent un déficit", "ils détruisent l'épargne", "ils n'ont aucun effet", "Revenus des ménages."),
      ("Une limite :", "ils financent surtout la consommation et peu l'investissement productif", "ils sont trop faibles", "ils sont interdits", "ils réduisent la population", "Usage des fonds."),
      ("Pour réduire le déficit commercial :", "produire localement ce qu'on importe et diversifier les exportations", "importer davantage", "supprimer les exportations", "fermer les ports", "Substitution aux importations."),
    ]),
  ]),
  "bac-type-g-eco-9": noter([
    P("Connaissances", "Population et emploi.", [
      ("La population active comprend :", "les actifs occupés et les chômeurs", "toute la population", "les seuls salariés", "les élèves", "Définition (BIT)."),
      ("Un chômeur au sens du BIT :", "est sans emploi, disponible et recherche activement un emploi", "est un retraité", "est un élève", "travaille à mi-temps", "Trois conditions."),
      ("Le secteur informel :", "regroupe les activités non enregistrées par l'État", "désigne les grandes entreprises", "est la fonction publique", "est illégal par nature", "Petits métiers non déclarés."),
    ]),
    P("Exercice", "Une région compte 400 000 actifs dont 60 000 chômeurs.", [
      ("Taux de chômage :", "15 %", "60 %", "6 %", "40 %", "60 000/400 000."),
      ("Nombre d'actifs occupés :", "340 000", "460 000", "400 000", "60 000", "400 000 − 60 000."),
      ("Si 20 000 chômeurs trouvent un emploi, le taux devient :", "10 %", "5 %", "15 %", "20 %", "40 000/400 000."),
    ]),
    P("Analyse", "Document : le secteur informel occupe la majorité des travailleurs au Sénégal.", [
      ("Un avantage du secteur informel :", "il offre des revenus et des emplois rapidement", "il paie beaucoup d'impôts", "il garantit la sécurité sociale", "il est très réglementé", "Rôle d'amortisseur social."),
      ("Un inconvénient :", "pas de protection sociale et peu de recettes fiscales", "trop de cotisations", "des salaires très élevés", "aucune activité", "Précarité."),
      ("Une mesure pour formaliser l'informel :", "simplifier l'enregistrement et la fiscalité des petites entreprises", "interdire les marchés", "augmenter les sanctions seulement", "supprimer le crédit", "Incitation."),
    ]),
  ]),
  "bac-type-g-compta-4": noter([
    P("Dossier 1 : facture", "Montant brut 1 000 000 F ; remise 10 % ; escompte 2 % ; TVA 18 %.", [
      ("Net commercial :", "900 000 F", "980 000 F", "1 000 000 F", "882 000 F", "1 000 000 × 0,9."),
      ("Escompte :", "18 000 F", "20 000 F", "2 000 F", "180 000 F", "900 000 × 2 %."),
      ("Net financier (HT) :", "882 000 F", "900 000 F", "880 000 F", "918 000 F", "900 000 − 18 000."),
      ("TVA :", "158 760 F", "162 000 F", "180 000 F", "88 200 F", "882 000 × 18 %."),
      ("Net à payer TTC :", "1 040 760 F", "1 062 000 F", "1 180 000 F", "1 058 760 F", "882 000 + 158 760."),
    ]),
    P("Dossier 2 : amortissement linéaire", "Machine acquise le 1er avril N pour 6 000 000 F HT ; durée 5 ans ; clôture au 31 décembre.", [
      ("Taux d'amortissement :", "20 %", "5 %", "25 %", "40 %", "100/5."),
      ("Annuité complète :", "1 200 000 F", "1 500 000 F", "600 000 F", "6 000 000 F", "6 000 000 × 20 %."),
      ("Dotation de l'exercice N (9 mois) :", "900 000 F", "1 200 000 F", "300 000 F", "1 000 000 F", "1 200 000 × 9/12."),
      ("VNC au 31/12/N :", "5 100 000 F", "4 800 000 F", "6 000 000 F", "5 400 000 F", "6 000 000 − 900 000."),
      ("Écriture de la dotation :", "débit 681 Dotations aux amortissements, crédit 284 Amortissements du matériel", "débit 284, crédit 681", "débit 241, crédit 521", "débit 601, crédit 401", "SYSCOHADA."),
    ]),
  ]),
  "bac-type-g-compta-5": noter([
    P("Dossier 1 : rapprochement bancaire", "Au 31/12 : compte 521 de l'entreprise débiteur de 500 000 F ; relevé bancaire créditeur de 620 000 F. Écarts : chèque émis non encaissé 100 000 F ; virement client non enregistré par l'entreprise 30 000 F ; frais bancaires non enregistrés 10 000 F.", [
      ("Solde rectifié côté entreprise :", "520 000 F", "500 000 F", "540 000 F", "480 000 F", "500 000 + 30 000 − 10 000."),
      ("Solde rectifié côté banque :", "520 000 F", "620 000 F", "720 000 F", "590 000 F", "620 000 − 100 000."),
      ("Les deux soldes rectifiés doivent être :", "égaux", "opposés", "nuls", "différents", "Contrôle."),
      ("Le chèque non encaissé s'enregistre :", "seulement dans l'état de rapprochement, pas dans le journal de l'entreprise", "au journal de l'entreprise", "en charges", "en produits", "L'entreprise l'a déjà comptabilisé."),
    ]),
    P("Dossier 2 : dépréciation des créances", "Client douteux : créance de 1 180 000 F TTC (TVA 18 %) ; perte probable 40 %.", [
      ("Le client est d'abord viré :", "du compte 411 au compte 416 Clients douteux", "du 401 au 411", "du 521 au 411", "du 701 au 411", "Reclassement."),
      ("Créance HT :", "1 000 000 F", "1 180 000 F", "818 000 F", "980 000 F", "1 180 000 / 1,18."),
      ("Dépréciation à constater :", "400 000 F", "472 000 F", "180 000 F", "600 000 F", "40 % du HT."),
      ("Compte de charge utilisé :", "659 Charges provisionnées d'exploitation", "601 Achats", "661 Salaires", "701 Ventes", "Dotation aux dépréciations."),
      ("Compte de dépréciation crédité :", "491 Dépréciations des comptes clients", "411 Clients", "281 Amortissements", "521 Banque", "SYSCOHADA."),
    ]),
  ]),
  "bac-type-g-compta-6": noter([
    P("Dossier 1 : fiche de stock", "Stock initial : 100 unités à 1 000 F. Entrée : 300 unités à 1 200 F. Sortie : 250 unités. Méthode du CMUP après chaque entrée.", [
      ("Valeur totale après l'entrée :", "460 000 F", "400 000 F", "360 000 F", "480 000 F", "100 000 + 360 000."),
      ("CMUP :", "1 150 F", "1 100 F", "1 200 F", "1 000 F", "460 000/400."),
      ("Valeur de la sortie :", "287 500 F", "250 000 F", "300 000 F", "275 000 F", "250 × 1 150."),
      ("Stock final :", "150 unités pour 172 500 F", "150 unités pour 180 000 F", "250 unités", "400 unités", "460 000 − 287 500."),
    ]),
    P("Dossier 2 : marge commerciale", "Ventes de marchandises 5 000 000 F ; achats 3 000 000 F ; stock initial 400 000 F ; stock final 600 000 F.", [
      ("Variation de stock (SI − SF) :", "−200 000 F", "+200 000 F", "1 000 000 F", "0", "400 000 − 600 000."),
      ("Coût d'achat des marchandises vendues :", "2 800 000 F", "3 200 000 F", "3 000 000 F", "2 600 000 F", "3 000 000 − 200 000."),
      ("Marge commerciale :", "2 200 000 F", "2 000 000 F", "1 800 000 F", "5 000 000 F", "5 000 000 − 2 800 000."),
      ("Taux de marque (marge / ventes HT) :", "44 %", "78,6 %", "22 %", "56 %", "2 200 000/5 000 000."),
      ("Taux de marge (marge / coût d'achat) :", "environ 78,6 %", "44 %", "100 %", "22 %", "2 200 000/2 800 000."),
    ]),
  ]),
  "bac-type-g-compta-7": noter([
    P("Dossier 1 : escompte d'un effet", "Effet de 600 000 F à 90 jours remis à l'escompte ; taux 10 % ; commission 2 000 F (taxes négligées).", [
      ("Escompte :", "15 000 F", "60 000 F", "1 500 F", "6 000 F", "600 000 × 10 × 90 / 36 000."),
      ("Agios totaux :", "17 000 F", "15 000 F", "2 000 F", "13 000 F", "15 000 + 2 000."),
      ("Net crédité en banque :", "583 000 F", "585 000 F", "600 000 F", "617 000 F", "600 000 − 17 000."),
      ("L'effet escompté est sorti du compte :", "412 Clients, effets à recevoir", "601 Achats", "281 Amortissements", "101 Capital", "Effets de commerce."),
    ]),
    P("Dossier 2 : équilibre financier", "Bilan : capitaux permanents 8 000 000 F ; actif immobilisé 6 000 000 F ; besoin de financement de l'activité (BFR) 1 500 000 F.", [
      ("Fonds de roulement :", "2 000 000 F", "14 000 000 F", "1 500 000 F", "500 000 F", "8 000 000 − 6 000 000."),
      ("Trésorerie nette :", "500 000 F", "3 500 000 F", "−500 000 F", "2 000 000 F", "FR − BFR."),
      ("Interprétation :", "le FR finance le BFR et dégage une trésorerie positive", "l'entreprise est en faillite", "le BFR n'est pas financé", "la trésorerie est négative", "Équilibre."),
      ("Ratio de financement des immobilisations :", "environ 1,33", "0,75", "2", "1", "8/6 : supérieur à 1, bon signe."),
    ]),
  ]),
  "bac-type-g-compta-8": noter([
    P("Dossier 1 : journal", "Enregistrer des opérations selon le SYSCOHADA (TVA 18 %).", [
      ("Achat de marchandises à crédit 500 000 F HT :", "débit 601 et 4452, crédit 401", "débit 401, crédit 601", "débit 411, crédit 701", "débit 521, crédit 601", "Achat + TVA récupérable."),
      ("Montant de la TVA récupérable :", "90 000 F", "500 000 F", "18 000 F", "590 000 F", "500 000 × 18 %."),
      ("Vente de marchandises à crédit 800 000 F HT :", "débit 411, crédit 701 et 4431", "débit 701, crédit 411", "débit 601, crédit 411", "débit 521, crédit 401", "Vente + TVA facturée."),
      ("Règlement d'un fournisseur par chèque :", "débit 401, crédit 521", "débit 521, crédit 401", "débit 411, crédit 521", "débit 601, crédit 521", "Dette éteinte."),
    ]),
    P("Dossier 2 : coût de revient", "Un atelier fabrique 1 000 articles : matières 800 000 F ; main-d'œuvre 400 000 F ; charges indirectes de production 300 000 F ; frais de distribution 100 000 F. Prix de vente unitaire 2 000 F.", [
      ("Coût de production total :", "1 500 000 F", "1 200 000 F", "1 600 000 F", "800 000 F", "800 000 + 400 000 + 300 000."),
      ("Coût de revient total :", "1 600 000 F", "1 500 000 F", "2 000 000 F", "1 400 000 F", "+ distribution."),
      ("Coût de revient unitaire :", "1 600 F", "1 500 F", "2 000 F", "160 F", "1 600 000/1 000."),
      ("Résultat analytique total :", "400 000 F", "500 000 F", "2 000 000 F", "−400 000 F", "2 000 000 − 1 600 000."),
    ]),
  ]),
  "bac-type-g-compta-9": noter([
    P("Dossier 1 : seuil de rentabilité", "Chiffre d'affaires 10 000 000 F ; charges variables 6 000 000 F ; charges fixes 2 000 000 F.", [
      ("Marge sur coût variable :", "4 000 000 F", "8 000 000 F", "2 000 000 F", "6 000 000 F", "10 − 6 millions."),
      ("Taux de marge sur coût variable :", "40 %", "60 %", "20 %", "4 %", "4/10."),
      ("Seuil de rentabilité :", "5 000 000 F", "2 000 000 F", "4 000 000 F", "8 000 000 F", "2 000 000/0,4."),
      ("Résultat :", "2 000 000 F", "4 000 000 F", "−2 000 000 F", "0", "MCV − charges fixes."),
      ("Point mort (activité régulière sur 12 mois) :", "fin juin (6 mois)", "fin mars", "fin décembre", "fin septembre", "5/10 × 12."),
    ]),
    P("Dossier 2 : affectation du résultat", "Bénéfice net 2 000 000 F ; réserve légale 10 % du bénéfice ; dividendes 1 200 000 F ; le reste en report à nouveau.", [
      ("Réserve légale :", "200 000 F", "2 000 000 F", "120 000 F", "20 000 F", "10 % de 2 000 000."),
      ("Report à nouveau :", "600 000 F", "800 000 F", "1 000 000 F", "0", "2 000 000 − 200 000 − 1 200 000."),
      ("Le compte de résultat bénéficiaire (131) est :", "débité pour être soldé lors de l'affectation", "crédité", "conservé tel quel", "supprimé du bilan sans écriture", "Solde du 131."),
      ("Les dividendes à payer sont crédités au compte :", "465 Associés, dividendes à payer", "601 Achats", "411 Clients", "281 Amortissements", "Dette envers les associés."),
    ]),
  ]),
}
