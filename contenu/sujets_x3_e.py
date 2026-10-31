# Devoirs types d'entraînement pour la Première (compositions sur 20, corrigées pas à pas).
from sujets_tle2 import P, noter

T1 = ["1ère S", "1ère L", "1ère G"]
def D(id_, subject, levels, series, duration, parts):
    return {"id": id_, "exam": "Devoir", "year": "type " + id_.rsplit("-", 1)[1], "series": series, "subject": subject, "levels": levels, "duration": duration, "modele": True, "parts": parts}

ANNALES_X = [
  D("devoir-1ere-fr-1", "Français", T1, "L, S et G", "3 h", ["Commentaire : un poème romantique"]),
  D("devoir-1ere-fr-2", "Français", T1, "L, S et G", "3 h", ["Dissertation : le rôle de l'écrivain"]),
  D("devoir-1ere-anglais-1", "Anglais", T1, "L, S et G", "2 h", ["Reading : school life", "Language in use", "Writing"]),
  D("devoir-1ere-anglais-2", "Anglais", T1, "L, S et G", "2 h", ["Reading : the city", "Language in use", "Writing"]),
  D("devoir-1ere-s-maths-1", "Mathématiques", ["1ère S"], "S1, S2, S3, S4, S5", "3 h", ["Exercice : second degré", "Problème : dérivée et variations"]),
  D("devoir-1ere-s-maths-2", "Mathématiques", ["1ère S"], "S1, S2, S3, S4, S5", "3 h", ["Exercice : suites", "Exercice : barycentre et trigonométrie"]),
  D("devoir-1ere-s-maths-3", "Mathématiques", ["1ère S"], "S1, S2, S3, S4, S5", "3 h", ["Exercice : dénombrement", "Problème : fonction rationnelle"]),
  D("devoir-1ere-s-pc-1", "Physique-Chimie", ["1ère S"], "S1, S2, S3, S4, S5", "3 h", ["Chimie : alcanes et combustion", "Physique : travail et énergie cinétique"]),
  D("devoir-1ere-s-pc-2", "Physique-Chimie", ["1ère S"], "S1, S2, S3, S4, S5", "3 h", ["Chimie : oxydoréduction", "Physique : condensateurs"]),
  D("devoir-1ere-s-pc-3", "Physique-Chimie", ["1ère S"], "S1, S2, S3, S4, S5", "3 h", ["Chimie : dosage d'oxydoréduction", "Physique : calorimétrie"]),
  D("devoir-1ere-s-svt-1", "SVT", ["1ère S"], "S1, S2, S3, S4, S5", "3 h", ["Connaissances : nutrition des plantes", "Compétences : photosynthèse"]),
  D("devoir-1ere-s-svt-2", "SVT", ["1ère S"], "S1, S2, S3, S4, S5", "3 h", ["Connaissances : géologie du Sénégal", "Compétences : respiration cellulaire"]),
  D("devoir-1ere-l-maths-1", "Mathématiques", ["1ère L"], "L1a, L1b, L2, L'", "2 h", ["Exercice : pourcentages", "Exercice : fonction affine et second degré"]),
  D("devoir-1ere-g-maths-1", "Mathématiques", ["1ère G"], "G", "3 h", ["Exercice : intérêts simples", "Exercice : statistiques"]),
]

GUIDED_X = {
  "devoir-1ere-fr-1": noter([
    P("1. Comprendre le poème", "Texte : « Le Lac » de Lamartine (extrait : « Ô temps, suspends ton vol ! … »).", [
      ("Mouvement littéraire :", "le romantisme", "la Négritude", "le classicisme", "le réalisme", "Lamartine, 1820."),
      ("Thème principal :", "la fuite du temps et le souvenir de l'amour", "la guerre", "la ville", "le travail", "Lyrisme."),
      ("Projet de lecture :", "Comment le poète exprime-t-il sa révolte contre le temps qui passe ?", "Combien de strophes ?", "Qui est l'éditeur ?", "Où est le lac ?", "Problématique."),
    ]),
    P("2. Analyser", "Procédés.", [
      ("« Ô temps, suspends ton vol ! » est :", "une apostrophe et une personnification", "une comparaison", "une litote", "une énumération", "On s'adresse au temps comme à une personne."),
      ("Le registre dominant :", "lyrique", "comique", "épique", "fantastique", "Expression des sentiments."),
      ("La nature dans le poème :", "est témoin et confidente du bonheur passé", "est indifférente", "est absente", "est hostile uniquement", "Le lac garde le souvenir."),
    ]),
    P("3. Rédiger", "Plan et conclusion.", [
      ("Plan adapté :", "I. La plainte face au temps / II. La nature, gardienne du souvenir", "I. Auteur / II. Œuvre", "I. Résumé / II. Opinion", "Un seul paragraphe", "Axes liés au projet."),
      ("Chaque argument contient :", "une idée, une citation et l'analyse de son effet", "une citation seule", "son avis personnel seul", "la biographie", "Méthode."),
      ("Ouverture possible :", "le thème du temps chez Ronsard (« Mignonne, allons voir si la rose »)", "la date de naissance de Lamartine", "le plan", "un résumé", "Ouverture."),
    ]),
  ]),
  "devoir-1ere-fr-2": noter([
    P("1. Comprendre le sujet", "Sujet : « L'écrivain doit-il seulement divertir son lecteur ? »", [
      ("« Seulement » invite à :", "montrer d'autres fonctions de la littérature", "approuver sans nuance", "parler de sport", "résumer un livre", "Restriction à discuter."),
      ("Les fonctions de la littérature :", "plaire, instruire, émouvoir, dénoncer", "uniquement vendre", "remplacer l'école", "décorer", "Placere et docere."),
      ("Type de plan :", "dialectique", "chronologique", "descriptif", "aucun", "Thèse, antithèse, synthèse."),
    ]),
    P("2. Arguments et exemples", "Œuvres étudiées.", [
      ("L'écrivain divertit, par exemple :", "les fables de La Fontaine qui amusent", "un manuel de chimie", "un dictionnaire", "un code de la route", "Plaisir de lecture."),
      ("L'écrivain dénonce, par exemple :", "Victor Hugo contre la misère dans Les Misérables", "un roman sans message", "une recette de cuisine", "un annuaire", "Engagement."),
      ("Un écrivain africain engagé :", "Mongo Beti (Ville cruelle)", "Molière", "Ronsard", "Racine", "Critique de la colonisation."),
    ]),
    P("3. Rédiger", "Conclusion.", [
      ("Partie 3 possible :", "le divertissement est un moyen efficace de faire passer un message", "il faut interdire le divertissement", "l'écrivain doit se taire", "seul le style compte", "Plaire pour instruire."),
      ("La conclusion :", "répond clairement et ouvre sur une autre question", "répète l'introduction", "ajoute une partie", "reste vide", "Bilan et ouverture."),
      ("Les transitions :", "relient les parties et annoncent la suite", "sont inutiles", "contiennent la conclusion", "répètent le sujet", "Cohérence."),
    ]),
  ]),
  "devoir-1ere-anglais-1": noter([
    P("1. Reading", "Text: « Fatou wakes up at six. She walks to school with her friends. Her favourite subject is biology because she wants to become a doctor. »", [
      ("What time does Fatou wake up?", "at six", "at seven", "at noon", "at nine", "Detail."),
      ("How does she go to school?", "She walks with her friends.", "By car", "By plane", "She stays home.", "Detail."),
      ("Why does she like biology?", "She wants to become a doctor.", "It is easy.", "Her friend teaches it.", "She hates maths.", "Reason."),
    ]),
    P("2. Language in use", "Grammar.", [
      ("Fatou ___ to school every day.", "walks", "walk", "is walk", "walking", "Simple present, 3rd person -s."),
      ("She ___ a doctor in the future.", "will become", "becomes yesterday", "became tomorrow", "is became", "Future."),
      ("« Favourite » means:", "the one you like most", "the one you hate", "the cheapest", "the oldest", "Vocabulary."),
    ]),
    P("3. Writing", "Describe your school day (about 100 words).", [
      ("A good opening sentence:", "I get up at six o'clock every morning.", "Yesterday tomorrow school.", "School me go.", "I am school.", "Correct sentence."),
      ("A linking word for order:", "Then", "Although", "However", "Because of", "Sequence."),
      ("A good ending:", "After dinner, I revise my lessons and go to bed.", "The end school.", "Bye.", "I don't know.", "Conclusion."),
    ]),
  ]),
  "devoir-1ere-anglais-2": noter([
    P("1. Reading", "Text: « Dakar is growing fast. There are more cars, more buildings and more jobs, but also traffic jams and pollution. »", [
      ("The text is about:", "life in a growing city", "a village festival", "a football match", "a school exam", "Main idea."),
      ("An advantage of the city:", "more jobs", "less traffic", "no pollution", "fewer buildings", "Detail."),
      ("A problem of the city:", "traffic jams and pollution", "too many trees", "no cars", "no people", "Detail."),
    ]),
    P("2. Language in use", "Grammar.", [
      ("Dakar is ___ than Thiès.", "bigger", "more big", "biggest", "big", "Comparative."),
      ("There ___ many cars in the streets.", "are", "is", "be", "am", "Plural."),
      ("The opposite of « clean » is:", "dirty", "new", "large", "quiet", "Antonym."),
    ]),
    P("3. Writing", "City or village: where would you prefer to live? (about 100 words)", [
      ("To give your opinion:", "I would rather live in…", "I rather to live…", "Me prefer…", "I am prefer…", "Expression."),
      ("To compare:", "The village is quieter than the city.", "The village is more quiet that the city.", "Village quiet city.", "The village quietest city.", "Comparative."),
      ("To conclude:", "In conclusion,", "Once upon a time,", "Firstly,", "By the way,", "Conclusion."),
    ]),
  ]),
  "devoir-1ere-s-maths-1": noter([
    P("Exercice : second degré", "f(x) = 2x² − 3x − 2.", [
      ("Discriminant :", "25", "7", "−7", "9", "9 + 16."),
      ("Racines :", "2 et −1/2", "−2 et 1/2", "1 et −2", "3 et −1", "(3 ± 5)/4."),
      ("Forme factorisée :", "2(x − 2)(x + 1/2)", "(x − 2)(x + 1/2)", "2(x + 2)(x − 1/2)", "(2x − 2)(x + 1)", "a(x − x₁)(x − x₂)."),
      ("f(x) ≤ 0 pour :", "x ∈ [−1/2 ; 2]", "x ≤ −1/2", "x ≥ 2", "jamais", "Entre les racines (a > 0)."),
    ]),
    P("Problème : g(x) = x³ − 3x + 1", "Variations sur ℝ.", [
      ("g'(x) :", "3x² − 3", "3x² − 3x", "x² − 3", "3x − 3", "Dérivée."),
      ("g' s'annule en :", "−1 et 1", "0 et 3", "1 seulement", "−3 et 3", "x² = 1."),
      ("Maximum local :", "g(−1) = 3", "g(1) = −1", "g(0) = 1", "g(−1) = −1", "−1 + 3 + 1."),
      ("Minimum local :", "g(1) = −1", "g(−1) = 3", "g(1) = 1", "g(0) = 1", "1 − 3 + 1."),
      ("Tangente en x = 0 :", "y = −3x + 1", "y = 3x + 1", "y = 1", "y = −3x", "g(0) = 1, g'(0) = −3."),
    ]),
  ]),
  "devoir-1ere-s-maths-2": noter([
    P("Exercice : suites", "u₀ = 3 et u(n+1) = u(n) + 4 ; v(n) = 2 × 3ⁿ.", [
      ("(uₙ) est :", "arithmétique de raison 4", "géométrique de raison 4", "constante", "géométrique de raison 3", "On ajoute 4."),
      ("u₁₀ :", "43", "40", "47", "34", "3 + 10 × 4."),
      ("u₀ + u₁ + … + u₁₀ :", "253", "230", "473", "264", "11 × (3 + 43)/2."),
      ("v₃ :", "54", "18", "162", "27", "2 × 27."),
    ]),
    P("Exercice : barycentre et trigonométrie", "Barycentre de points pondérés ; angles remarquables.", [
      ("G barycentre de (A, 2) et (B, 1) vérifie AG = :", "1/3 AB", "2/3 AB", "1/2 AB", "2 AB", "AG = b/(a + b) × AB."),
      ("cos(π/3) :", "1/2", "√3/2", "√2/2", "0", "Valeur remarquable."),
      ("sin(5π/6) :", "1/2", "−1/2", "√3/2", "−√3/2", "sin(π − π/6) = sin(π/6)."),
      ("Solutions de cos x = 0 dans [0 ; 2π[ :", "π/2 et 3π/2", "0 et π", "π/4 et 3π/4", "π seulement", "Cercle trigonométrique."),
    ]),
  ]),
  "devoir-1ere-s-maths-3": noter([
    P("Exercice : dénombrement", "Une classe de 30 élèves.", [
      ("Choisir un délégué et un suppléant :", "870", "435", "60", "900", "30 × 29 (ordre compte)."),
      ("Choisir 2 représentants sans ordre :", "435", "870", "60", "30", "C(30, 2)."),
      ("Nombre de façons de ranger 5 livres sur une étagère :", "120", "25", "5", "60", "5!."),
    ]),
    P("Problème : f(x) = (x + 3)/(x − 1)", "Sur ℝ \\ {1}.", [
      ("Valeur interdite :", "1", "−3", "0", "3", "Dénominateur nul."),
      ("f'(x) :", "−4/(x − 1)²", "4/(x − 1)²", "1/(x − 1)²", "−2/(x − 1)²", "(x − 1 − x − 3)/(x − 1)²."),
      ("f est :", "décroissante sur chaque intervalle", "croissante partout", "constante", "croissante puis décroissante", "f' < 0."),
      ("Asymptotes :", "x = 1 et y = 1", "x = −3 et y = 1", "x = 1 et y = 3", "x = 0 et y = 0", "Rapport des coefficients."),
      ("f(x) = 0 pour :", "x = −3", "x = 1", "x = 3", "jamais", "x + 3 = 0."),
    ]),
  ]),
  "devoir-1ere-s-pc-1": noter([
    P("Chimie : alcanes", "Combustion complète du propane C₃H₈. M(C) = 12 ; M(H) = 1 g/mol.", [
      ("Formule générale des alcanes :", "CₙH₂ₙ₊₂", "CₙH₂ₙ", "CₙH₂ₙ₋₂", "CₙHₙ", "Hydrocarbures saturés."),
      ("Équation équilibrée :", "C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O", "C₃H₈ + 3 O₂ → 3 CO₂ + 4 H₂O", "C₃H₈ + O₂ → CO₂ + H₂O", "C₃H₈ + 5 O₂ → 3 CO + 4 H₂O", "Conservation des atomes."),
      ("Masse molaire du propane :", "44 g/mol", "36 g/mol", "42 g/mol", "48 g/mol", "3 × 12 + 8."),
      ("Quantité de CO₂ formée par 2 mol de propane :", "6 mol", "3 mol", "2 mol", "10 mol", "Coefficient 3."),
    ]),
    P("Physique : travail et énergie cinétique", "Un solide de 2 kg passe de 0 à 4 m/s.", [
      ("Énergie cinétique finale :", "16 J", "8 J", "32 J", "4 J", "½ × 2 × 16."),
      ("Théorème de l'énergie cinétique :", "ΔEc = somme des travaux des forces", "Ec = m g h", "ΔEc = 0 toujours", "Ec = F × v", "Énoncé."),
      ("Travail total des forces :", "16 J", "0 J", "8 J", "32 J", "ΔEc = 16 − 0."),
      ("Travail du poids pour une chute de 5 m (g = 10) d'un objet de 2 kg :", "100 J", "10 J", "50 J", "−100 J", "W = m g h."),
      ("Puissance d'une force qui fournit 600 J en 2 min :", "5 W", "300 W", "1 200 W", "50 W", "600/120."),
    ]),
  ]),
  "devoir-1ere-s-pc-2": noter([
    P("Chimie : oxydoréduction", "Une lame de zinc plonge dans une solution de sulfate de cuivre II.", [
      ("Un oxydant est une espèce qui :", "capte des électrons", "cède des électrons", "cède des protons", "capte des protons", "Définition."),
      ("Observation :", "un dépôt rouge de cuivre se forme sur le zinc", "rien ne se passe", "le zinc grossit", "la solution devient plus bleue", "Cu²⁺ réduit."),
      ("Équation bilan :", "Zn + Cu²⁺ → Zn²⁺ + Cu", "Cu + Zn²⁺ → Cu²⁺ + Zn", "Zn + Cu → ZnCu", "Zn²⁺ + Cu²⁺ → ZnCu", "Le zinc est plus réducteur."),
      ("Le zinc est :", "oxydé", "réduit", "inchangé", "un oxydant", "Il perd des électrons."),
    ]),
    P("Physique : condensateurs", "Condensateurs de 2 µF et 4 µF.", [
      ("Capacité équivalente en parallèle :", "6 µF", "4/3 µF", "8 µF", "2 µF", "Somme."),
      ("Capacité équivalente en série :", "4/3 µF", "6 µF", "8 µF", "2 µF", "1/C = 1/2 + 1/4."),
      ("Charge du 4 µF sous 10 V :", "40 µC", "4 µC", "0,4 µC", "2,5 µC", "q = C U."),
      ("Énergie stockée par le 4 µF sous 10 V :", "200 µJ", "40 µJ", "400 µJ", "20 µJ", "½ × 4 × 10⁻⁶ × 100."),
    ]),
  ]),
  "devoir-1ere-s-pc-3": noter([
    P("Chimie : dosage", "On dose 10 mL de Fe²⁺ par MnO₄⁻ à 0,02 mol/L ; équivalence à 8 mL. Équation : MnO₄⁻ + 5 Fe²⁺ + 8 H⁺ → Mn²⁺ + 5 Fe³⁺ + 4 H₂O.", [
      ("À l'équivalence :", "n(Fe²⁺) = 5 × n(MnO₄⁻)", "n(Fe²⁺) = n(MnO₄⁻)", "n(MnO₄⁻) = 5 × n(Fe²⁺)", "n(Fe²⁺) = 8 × n(MnO₄⁻)", "Coefficients stœchiométriques."),
      ("n(MnO₄⁻) versé :", "1,6 × 10⁻⁴ mol", "1,6 × 10⁻² mol", "8 × 10⁻⁴ mol", "2 × 10⁻⁴ mol", "0,02 × 0,008."),
      ("Concentration en Fe²⁺ :", "0,08 mol/L", "0,016 mol/L", "0,04 mol/L", "0,8 mol/L", "5 × 1,6 × 10⁻⁴ / 0,010."),
      ("On repère l'équivalence par :", "la persistance de la teinte violette", "un dégagement gazeux", "un précipité blanc", "rien", "MnO₄⁻ en excès."),
    ]),
    P("Physique : calorimétrie", "Eau : c = 4 180 J/(kg·°C).", [
      ("Chaleur pour chauffer 1 kg d'eau de 20 à 70 °C :", "209 000 J", "4 180 J", "83 600 J", "292 600 J", "1 × 4 180 × 50."),
      ("On mélange 1 kg d'eau à 20 °C et 1 kg à 60 °C (sans pertes). Température finale :", "40 °C", "80 °C", "30 °C", "50 °C", "Masses égales : moyenne."),
      ("Dans un calorimètre isolé :", "la somme des chaleurs échangées est nulle", "la chaleur se crée", "la température ne change jamais", "l'énergie disparaît", "Principe."),
      ("Unité de la capacité thermique d'un calorimètre :", "J/°C", "J/kg", "°C/J", "W", "C = Q/Δθ."),
    ]),
  ]),
  "devoir-1ere-s-svt-1": noter([
    P("Connaissances : nutrition des plantes", "Absorption de l'eau et des sels minéraux.", [
      ("L'eau est absorbée surtout par :", "les poils absorbants des racines", "les feuilles", "les fleurs", "les fruits", "Zone pilifère."),
      ("La sève brute circule dans :", "le xylème (vaisseaux du bois)", "le phloème", "les stomates", "le pollen", "Des racines aux feuilles."),
      ("La transpiration a lieu par :", "les stomates", "les racines", "les graines", "l'écorce seule", "Évaporation foliaire."),
    ]),
    P("Compétences : photosynthèse", "Expérience : une plante éclairée dans une enceinte riche en CO₂ ; on mesure le dioxygène.", [
      ("La photosynthèse produit :", "du glucose et du dioxygène", "du CO₂ et de l'eau seulement", "de l'azote", "de l'alcool", "6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂."),
      ("Organite de la photosynthèse :", "le chloroplaste", "la mitochondrie", "le noyau", "le ribosome", "Chlorophylle."),
      ("À l'obscurité, la production de dioxygène :", "s'arrête", "double", "reste identique", "devient infinie", "Besoin de lumière."),
      ("Le test de l'eau iodée sur une feuille éclairée révèle :", "de l'amidon", "des protéines", "des lipides", "du glucose directement", "Coloration bleu-noir."),
      ("Un facteur limitant de la photosynthèse :", "la concentration en CO₂", "la couleur du pot", "le bruit", "la forme de la feuille seule", "Facteurs : lumière, CO₂, température."),
    ]),
  ]),
  "devoir-1ere-s-svt-2": noter([
    P("Connaissances : géologie du Sénégal", "Les roches et les ressources du sous-sol.", [
      ("Le bassin sédimentaire sénégalo-mauritanien est formé surtout de :", "roches sédimentaires", "roches volcaniques uniquement", "glace", "roches métamorphiques uniquement", "Grande partie du pays."),
      ("Ressource minière exploitée à Taïba :", "les phosphates", "le diamant", "le charbon", "le cuivre", "Industries chimiques."),
      ("Le socle ancien du Sénégal oriental contient :", "de l'or (Sabodala)", "du pétrole uniquement", "du sel", "des coquillages", "Roches anciennes."),
    ]),
    P("Compétences : respiration cellulaire", "Expérience : des levures dans une solution de glucose, avec ou sans dioxygène.", [
      ("Bilan de la respiration :", "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + énergie", "6 CO₂ + 6 H₂O → C₆H₁₂O₆", "glucose → alcool seulement", "O₂ → CO₂ sans glucose", "Oxydation complète."),
      ("Organite de la respiration :", "la mitochondrie", "le chloroplaste", "la vacuole", "la paroi", "Centrale énergétique."),
      ("Sans dioxygène, les levures font :", "la fermentation alcoolique", "la photosynthèse", "la respiration", "rien", "Glucose → éthanol + CO₂."),
      ("Quelle voie produit le plus d'ATP ?", "la respiration", "la fermentation", "les deux autant", "aucune", "36 à 38 ATP contre 2."),
      ("Le CO₂ dégagé se met en évidence par :", "l'eau de chaux qui se trouble", "l'eau iodée", "la liqueur de Fehling", "le papier pH seulement", "Test classique."),
    ]),
  ]),
  "devoir-1ere-l-maths-1": noter([
    P("Exercice : pourcentages", "Un pagne coûte 8 000 F.", [
      ("Après une hausse de 15 %, il coûte :", "9 200 F", "8 150 F", "9 500 F", "6 800 F", "8 000 × 1,15."),
      ("Après une remise de 25 % sur 8 000 F :", "6 000 F", "7 750 F", "2 000 F", "6 500 F", "8 000 × 0,75."),
      ("Une hausse de 10 % suivie d'une baisse de 10 % donne :", "une baisse de 1 %", "aucun changement", "une hausse de 1 %", "une baisse de 10 %", "1,1 × 0,9 = 0,99."),
    ]),
    P("Exercice : fonctions", "f(x) = 2x − 3 et g(x) = x² − 4.", [
      ("f(5) :", "7", "10", "13", "2", "10 − 3."),
      ("Solution de f(x) = 0 :", "x = 3/2", "x = −3/2", "x = 3", "x = 2/3", "2x = 3."),
      ("Solutions de g(x) = 0 :", "x = 2 et x = −2", "x = 4", "x = 2 seulement", "x = 16", "x² = 4."),
      ("La courbe de f est :", "une droite de coefficient directeur 2", "une parabole", "un cercle", "une droite horizontale", "Fonction affine."),
    ]),
  ]),
  "devoir-1ere-g-maths-1": noter([
    P("Exercice : intérêts simples", "I = C × t × n / 1 200 (n en mois).", [
      ("Intérêt de 300 000 F à 8 % pendant 6 mois :", "12 000 F", "24 000 F", "144 000 F", "1 200 F", "300 000 × 8 × 6 / 1 200."),
      ("Valeur acquise :", "312 000 F", "324 000 F", "300 000 F", "288 000 F", "C + I."),
      ("Durée pour qu'un capital de 100 000 F à 6 % rapporte 3 000 F :", "6 mois", "3 mois", "1 an", "5 mois", "3 000 = 100 000 × 6 × n / 1 200."),
    ]),
    P("Exercice : statistiques", "Salaires journaliers de 10 ouvriers : 3 000 (4 ouvriers), 4 000 (5), 6 000 (1).", [
      ("Moyenne :", "3 800 F", "4 000 F", "4 333 F", "3 500 F", "(12 000 + 20 000 + 6 000)/10."),
      ("Mode :", "4 000 F", "3 000 F", "6 000 F", "5 000 F", "Effectif 5."),
      ("Médiane :", "4 000 F", "3 000 F", "3 500 F", "6 000 F", "5e et 6e valeurs = 4 000."),
      ("Étendue :", "3 000 F", "6 000 F", "1 000 F", "2 000 F", "6 000 − 3 000."),
    ]),
  ]),
}
