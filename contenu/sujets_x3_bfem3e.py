from sujets_dev_common import D, pack
L = "3e"
def b(s, name, n, exos, coef=None): return D(f"bfem-type-{s}-{n}", L, name, n, exos, exam="BFEM", coef=coef)

ANNALES_X, GUIDED_X = pack([
  # ---------------- Mathématiques (types 2 à 4)
  b("maths", "Mathématiques", 2, [
    ("Activités numériques : radicaux et identités", "On donne A = (√3 − 2)² et B = √75 − 2√27 + √12.", [
      ("A développé :", "7 − 4√3", "1", "7 + 4√3", "−1 − 4√3", "3 − 4√3 + 4."),
      ("B =", "√3", "3√3", "−√3", "5√3", "5√3 − 6√3 + 2√3."),
      ("A × (7 + 4√3) =", "1", "49", "97", "−1", "49 − 48."),
      ("Encadrement : sachant 1,73 < √3 < 1,74, on a", "0,04 < A < 0,08 environ", "A > 1", "A < 0", "A = 0", "7 − 4√3 ≈ 0,07.")]),
    ("Activités numériques : système et application affine", "Un club vend des tickets à 1 000 F (adultes) et 500 F (enfants). On vend 120 tickets pour 85 000 F.", [
      ("Système :", "x + y = 120 et 1 000x + 500y = 85 000", "x + y = 85 000 et x + 2y = 120", "x − y = 120 et 2x + y = 170", "1 000x = 85 000 et y = 120", "Traduction."),
      ("Équation simplifiée (÷ 500) :", "2x + y = 170", "x + y = 170", "2x + y = 120", "x + 2y = 170", "Division."),
      ("Nombre d'adultes :", "50", "70", "60", "85", "(2x + y) − (x + y) = 50."),
      ("Nombre d'enfants :", "70", "50", "60", "35", "120 − 50.")]),
    ("Activités géométriques : Thalès et trigonométrie", "Dans le triangle ABC rectangle en A, AB = 9 cm et AC = 12 cm. M est sur [AB] avec AM = 3 cm ; la parallèle à (BC) passant par M coupe [AC] en N.", [
      ("BC =", "15 cm", "21 cm", "√63 cm", "225 cm", "Pythagore : 81 + 144 = 225."),
      ("AN =", "4 cm", "3 cm", "6 cm", "9 cm", "AN/AC = AM/AB = 1/3."),
      ("MN =", "5 cm", "4 cm", "7,5 cm", "3 cm", "MN/BC = 1/3."),
      ("tan ABC =", "4/3", "3/4", "3/5", "4/5", "AC/AB = 12/9.")])], coef=4),
  b("maths", "Mathématiques", 3, [
    ("Activités numériques : factorisation et équation", "F = (3x + 1)² − (x − 2)².", [
      ("Identité utilisée :", "a² − b² = (a − b)(a + b)", "(a + b)²", "(a − b)²", "a² + b²", "Différence de deux carrés."),
      ("F factorisé :", "(2x + 3)(4x − 1)", "(2x − 1)(4x + 3)", "(4x + 3)(2x + 1)", "(3x + 1)(x − 2)", "(3x + 1 − x + 2)(3x + 1 + x − 2)."),
      ("Solutions de F = 0 :", "−3/2 et 1/4", "3/2 et −1/4", "−3 et 1", "2/3 et 4", "Produit nul."),
      ("F pour x = 0 :", "−3", "3", "1", "5", "1 − 4.")]),
    ("Activités numériques : PGCD et statistiques", "Un fleuriste a 210 roses et 154 tulipes pour faire des bouquets identiques.", [
      ("PGCD(210 ; 154) :", "14", "7", "42", "2", "210 = 154 + 56 ; 154 = 2 × 56 + 42 ; 56 = 42 + 14 ; 42 = 3 × 14."),
      ("Nombre maximal de bouquets :", "14", "7", "21", "11", "PGCD."),
      ("Roses par bouquet :", "15", "11", "14", "21", "210 ÷ 14."),
      ("Tulipes par bouquet :", "11", "15", "14", "7", "154 ÷ 14.")]),
    ("Activités géométriques : repérage", "Dans un repère orthonormé, A(−1 ; 2), B(3 ; 4) et C(5 ; 0).", [
      ("Coordonnées du vecteur AB :", "(4 ; 2)", "(2 ; 6)", "(−4 ; −2)", "(4 ; 6)", "(3 − (−1) ; 4 − 2)."),
      ("Distance AB :", "2√5", "√20/2", "6", "√52", "√(16 + 4)."),
      ("Coefficient directeur de (AB) :", "1/2", "2", "−1/2", "3", "2/4."),
      ("Le triangle ABC est rectangle en B car", "AB² + BC² = AC²", "AB = BC", "AC est le plus court", "les points sont alignés", "AB² = 20, BC² = 4 + 16 = 20, AC² = 36 + 4 = 40.")])], coef=4),
  b("maths", "Mathématiques", 4, [
    ("Activités numériques : inéquations", "Un opérateur propose : forfait A à 3 000 F + 50 F/min ; forfait B à 100 F/min sans abonnement.", [
      ("Coût A pour x minutes :", "3 000 + 50x", "50 + 3 000x", "100x", "3 050x", "Fixe + variable."),
      ("Coût B :", "100x", "3 000 + 100x", "50x", "100 + x", "Sans abonnement."),
      ("A est moins cher si", "x > 60", "x < 60", "x > 30", "x = 0", "3 000 + 50x < 100x ⟺ 3 000 < 50x."),
      ("Pour 80 minutes, le moins cher est", "A (7 000 F contre 8 000 F)", "B", "égalité", "aucun", "3 000 + 4 000 et 8 000.")]),
    ("Activités numériques : application affine", "f est l'application affine telle que f(2) = 1 et f(5) = 7.", [
      ("Coefficient a :", "2", "3", "6", "1/2", "(7 − 1)/(5 − 2)."),
      ("f(x) =", "2x − 3", "2x + 1", "3x − 5", "x − 1", "1 = 2 × 2 + b, b = −3."),
      ("Antécédent de 9 :", "6", "15", "3", "4,5", "2x − 3 = 9."),
      ("f(0) =", "−3", "0", "3", "2", "b.")]),
    ("Activités géométriques : espace et angles inscrits", "Un cône de révolution a un rayon de 6 cm et une génératrice de 10 cm. Par ailleurs, sur un cercle de centre O, l'angle au centre AOB mesure 140°.", [
      ("Hauteur du cône :", "8 cm", "4 cm", "√136 cm", "16 cm", "Pythagore : 100 − 36 = 64."),
      ("Volume du cône (en π cm³) :", "96π", "288π", "48π", "120π", "π × 36 × 8 ÷ 3."),
      ("Angle inscrit AMB interceptant le petit arc AB :", "70°", "140°", "110°", "40°", "Moitié de l'angle au centre."),
      ("Réduction de coefficient 1/2 : volume du petit cône", "12π", "48π", "24π", "96π", "96π × 1/8.")])], coef=4),
  # ---------------- Physique-Chimie (types 2 à 4)
  b("pc", "Physique-Chimie", 2, [
    ("Chimie : acides et bases", "On dispose d'une solution d'acide chlorhydrique de pH 2 et d'une solution d'hydroxyde de sodium de pH 12.", [
      ("La solution de pH 2 est", "acide", "basique", "neutre", "un corps pur", "pH < 7."),
      ("En ajoutant de l'eau à l'acide, le pH", "augmente vers 7", "diminue", "devient 0", "ne change pas", "Dilution."),
      ("Mélanger acide et base donne une réaction de", "neutralisation", "combustion", "fusion", "électrolyse", "Nom."),
      ("Ions responsables de l'acidité :", "H⁺ (H₃O⁺)", "OH⁻", "Na⁺", "Cl⁻ seul", "Acide.")]),
    ("Chimie : la mole", "On brûle 24 g de carbone : C + O₂ → CO₂ (C = 12 ; O = 16 g/mol).", [
      ("Quantité de carbone :", "2 mol", "24 mol", "0,5 mol", "12 mol", "24 ÷ 12."),
      ("Masse molaire de CO₂ :", "44 g/mol", "28 g/mol", "32 g/mol", "12 g/mol", "12 + 32."),
      ("Quantité de CO₂ formée :", "2 mol", "1 mol", "4 mol", "44 mol", "1 C donne 1 CO₂."),
      ("Masse de CO₂ :", "88 g", "44 g", "24 g", "56 g", "2 × 44.")]),
    ("Physique : électricité", "Un conducteur ohmique R = 100 Ω est branché sous 12 V.", [
      ("Intensité :", "0,12 A", "1 200 A", "8,3 A", "12 A", "I = U/R."),
      ("Puissance :", "1,44 W", "1 200 W", "0,12 W", "12 W", "P = U × I."),
      ("Énergie en 1 h :", "5 184 J", "1,44 J", "86,4 J", "3 600 J", "1,44 × 3 600."),
      ("Avec deux résistances de 100 Ω en série, I =", "0,06 A", "0,24 A", "0,12 A", "6 A", "12 ÷ 200.")])], coef=2),
  b("pc", "Physique-Chimie", 3, [
    ("Chimie : métaux", "On plonge un clou en fer dans de l'acide chlorhydrique dilué.", [
      ("On observe", "un dégagement gazeux", "rien", "une flamme", "un dépôt d'or", "Réaction."),
      ("Gaz dégagé :", "dihydrogène", "dioxygène", "CO₂", "chlore", "Détonation à la flamme."),
      ("Test du gaz :", "petite détonation à l'approche d'une flamme", "trouble l'eau de chaux", "rallume une bûchette", "odeur de rose", "Test."),
      ("Ion formé en solution :", "Fe²⁺", "Fe³⁺ seulement", "Cl⁺", "O²⁻", "Ions fer II.")]),
    ("Physique : poids et masse", "Un sac de riz de 50 kg (g = 10 N/kg).", [
      ("Poids :", "500 N", "50 N", "5 N", "5 000 N", "P = mg."),
      ("Point d'application :", "centre de gravité", "le sol", "la main", "le sommet du sac", "Caractéristique."),
      ("Sur la Lune (g = 1,6 N/kg), poids :", "80 N", "500 N", "50 N", "16 N", "50 × 1,6."),
      ("Instrument de mesure de la masse :", "balance", "dynamomètre", "ampèremètre", "chronomètre", "kg.")]),
    ("Physique : lentilles", "Une lentille convergente a une vergence de +10 δ. Un objet est placé à 30 cm devant elle.", [
      ("Distance focale :", "10 cm", "1 cm", "100 cm", "30 cm", "f = 1/C = 0,1 m."),
      ("L'objet est placé", "au-delà du double de la focale", "au foyer", "entre la lentille et le foyer", "sur la lentille", "30 > 20 cm."),
      ("L'image est", "réelle et renversée", "virtuelle et droite", "inexistante", "à l'infini", "Objet au-delà du foyer."),
      ("Lentille divergente :", "bords plus épais que le centre", "centre épais", "plate", "ronde comme une bille", "Forme.")])], coef=2),
  b("pc", "Physique-Chimie", 4, [
    ("Chimie : combustions", "On brûle du butane C₄H₁₀ dans une gazinière.", [
      ("Produits d'une combustion complète :", "CO₂ et H₂O", "CO et C", "H₂ et O₂", "N₂", "Combustion complète."),
      ("Équation équilibrée :", "2 C₄H₁₀ + 13 O₂ → 8 CO₂ + 10 H₂O", "C₄H₁₀ + O₂ → CO₂ + H₂O", "C₄H₁₀ + 13 O₂ → 4 CO₂ + 5 H₂O", "2 C₄H₁₀ + 8 O₂ → 8 CO₂ + 10 H₂O", "Conservation des atomes."),
      ("Flamme jaune qui noircit les casseroles :", "combustion incomplète", "combustion complète", "fusion", "dissolution", "Carbone (suie)."),
      ("Gaz mortel d'une combustion incomplète :", "CO", "CO₂", "O₂", "H₂O", "Monoxyde de carbone.")]),
    ("Physique : masse volumique", "Un bloc de bois de 2 dm³ a une masse de 1,4 kg.", [
      ("Masse volumique :", "0,7 kg/dm³", "2,8 kg/dm³", "1,4 kg/dm³", "0,35 kg/dm³", "1,4 ÷ 2."),
      ("En g/cm³ :", "0,7 g/cm³", "700 g/cm³", "7 g/cm³", "0,07 g/cm³", "Mêmes valeurs."),
      ("Le bois dans l'eau :", "flotte", "coule", "se dissout", "fond", "Moins dense que l'eau."),
      ("Densité par rapport à l'eau :", "0,7", "700", "1,4", "7", "Sans unité.")]),
    ("Physique : énergie électrique", "Une lampe de 60 W et un téléviseur de 100 W fonctionnent 5 h par jour pendant 30 jours.", [
      ("Puissance totale :", "160 W", "40 W", "6 000 W", "100 W", "60 + 100."),
      ("Énergie par jour :", "0,8 kWh", "8 kWh", "800 kWh", "0,16 kWh", "0,16 kW × 5 h."),
      ("Énergie en 30 jours :", "24 kWh", "2,4 kWh", "240 kWh", "4,8 kWh", "0,8 × 30."),
      ("Coût à 110 F le kWh :", "2 640 F", "264 F", "26 400 F", "2 400 F", "24 × 110.")])], coef=2),
  # ---------------- SVT (types 2 à 4)
  b("svt", "SVT", 2, [
    ("Maîtrise des connaissances : digestion", "Questions sur la nutrition.", [
      ("Organe où commence la digestion des protéines :", "estomac", "bouche", "gros intestin", "œsophage", "Pepsine."),
      ("Les nutriments passent dans le sang au niveau des", "villosités intestinales", "dents", "alvéoles pulmonaires", "reins", "Absorption."),
      ("Le glucose est transporté par", "le plasma sanguin", "les globules rouges seulement", "la lymphe uniquement", "les nerfs", "Transport."),
      ("Organe qui stocke le glycogène :", "foie", "rein", "cœur", "poumon", "Réserve.")]),
    ("Exploitation de documents : courbe de glycémie", "Après un repas à 12 h, la glycémie d'Awa passe de 0,9 g/L à 1,4 g/L à 13 h, puis revient à 1 g/L à 15 h.", [
      ("Glycémie normale à jeun (environ) :", "1 g/L", "3 g/L", "0,1 g/L", "10 g/L", "Valeur de référence."),
      ("La hausse à 13 h est due", "à l'absorption du glucose du repas", "au sport", "au sommeil", "à la respiration", "Repas."),
      ("Hormone qui fait baisser la glycémie :", "insuline", "adrénaline", "testostérone", "glucagon", "Pancréas."),
      ("Maladie si la glycémie reste élevée :", "diabète", "paludisme", "anémie", "goitre", "Hyperglycémie.")]),
    ("Exploitation de documents : excrétion", "Comparaison de l'urine et du plasma : l'urine contient de l'urée en grande quantité mais pas de glucose.", [
      ("Organe qui produit l'urine :", "rein", "vessie", "foie", "intestin", "Filtration."),
      ("Déchet azoté principal :", "urée", "glucose", "oxygène", "lipides", "Excrétion."),
      ("Absence de glucose dans l'urine :", "il est réabsorbé", "il n'existe pas dans le sang", "il est brûlé dans la vessie", "il est transformé en urée", "Réabsorption."),
      ("Glucose dans l'urine :", "signe possible de diabète", "normal", "signe de bonne santé", "signe de paludisme", "Glycosurie.")])], coef=2),
  b("svt", "SVT", 3, [
    ("Maîtrise des connaissances : système nerveux", "Questions sur la commande nerveuse.", [
      ("Cellule nerveuse :", "neurone", "globule rouge", "hépatocyte", "spermatozoïde", "Unité."),
      ("Centre des mouvements volontaires :", "cerveau", "moelle épinière", "estomac", "cœur", "Cortex moteur."),
      ("Message nerveux :", "électrique (influx)", "chimique sanguin seulement", "sonore", "lumineux", "Nature."),
      ("Substance qui ralentit les réflexes :", "alcool", "eau", "vitamine C", "lait", "Hygiène.")]),
    ("Exploitation de documents : le réflexe rotulien", "Un coup sur le tendon sous la rotule provoque l'extension de la jambe.", [
      ("Récepteur :", "fuseau neuromusculaire du muscle de la cuisse", "la peau du pied", "l'œil", "le cerveau", "Étirement."),
      ("Centre nerveux :", "moelle épinière", "cerveau", "cervelet", "cœur", "Réflexe médullaire."),
      ("Ordre de l'arc réflexe :", "récepteur, nerf sensitif, moelle, nerf moteur, muscle", "muscle, moelle, récepteur", "cerveau, muscle, nerf", "nerf moteur, récepteur, moelle", "Trajet."),
      ("Si le nerf moteur est coupé :", "pas de réflexe", "réflexe plus fort", "rien ne change", "douleur seulement", "Effecteur non commandé.")]),
    ("Exploitation de documents : vaccination", "Courbe : après une 1re injection de vaccin, peu d'anticorps ; après un rappel, beaucoup d'anticorps, très vite.", [
      ("Les anticorps sont produits par", "les lymphocytes B", "les globules rouges", "les plaquettes", "les neurones", "Immunité."),
      ("Réponse plus forte au rappel grâce à", "la mémoire immunitaire", "la fatigue", "la digestion", "un hasard", "Cellules mémoire."),
      ("Le vaccin contient", "un microbe atténué ou une partie de microbe", "un antibiotique", "du sang", "une vitamine", "Composition."),
      ("Différence avec le sérum :", "le sérum apporte des anticorps tout faits", "le sérum dure toute la vie", "aucune", "le sérum est un vaccin", "Immunité passive.")])], coef=2),
  b("svt", "SVT", 4, [
    ("Maîtrise des connaissances : reproduction", "Questions sur la reproduction humaine.", [
      ("Hormone féminine sécrétée par l'ovaire :", "œstrogène", "testostérone", "insuline", "adrénaline", "Hormone."),
      ("La fécondation a lieu dans", "la trompe", "l'utérus", "le vagin", "l'ovaire", "Lieu."),
      ("Méthode contraceptive hormonale :", "pilule", "préservatif", "abstinence", "calendrier", "Hormones."),
      ("Seul moyen qui protège aussi des IST :", "préservatif", "pilule", "stérilet", "calendrier", "Barrière.")]),
    ("Exploitation de documents : cycle ovarien", "Graphique de température d'une femme : 36,6 °C du jour 1 au jour 14, puis 37 °C jusqu'au jour 28.", [
      ("La montée de température indique", "l'ovulation (vers le 14e jour)", "les règles", "la grossesse certaine", "une maladie", "Repère."),
      ("Phase avant l'ovulation :", "phase folliculaire", "phase lutéale", "grossesse", "ménopause", "Nom."),
      ("Si la température reste haute après 28 jours :", "grossesse possible", "règles certaines", "ovulation à nouveau", "rien", "Corps jaune maintenu."),
      ("Durée du cycle :", "28 jours", "14 jours", "7 jours", "9 mois", "Graphique.")]),
    ("Exploitation de documents : tectonique", "Carte : les séismes et volcans se répartissent en bandes étroites ; l'âge du fond océanique augmente en s'éloignant de la dorsale.", [
      ("Les bandes de séismes marquent", "les limites des plaques", "les déserts", "les capitales", "les fleuves", "Plaques."),
      ("Au niveau de la dorsale, les plaques", "s'écartent", "se rapprochent", "ne bougent pas", "fondent toutes", "Divergence."),
      ("Les roches les plus jeunes sont", "près de la dorsale", "près des côtes", "partout le même âge", "au centre des continents", "Formation du plancher."),
      ("Zone où une plaque plonge sous une autre :", "subduction", "dorsale", "rift", "plateau", "Convergence.")])], coef=2),
  # ---------------- Français (types 1 à 3)
  b("francais", "Français", 1, [
    ("Compréhension du texte", "« Chaque matin, la vieille Coumba se rendait au marché de Kaolack. Elle vendait des légumes qu'elle cultivait elle-même. Malgré la fatigue, elle souriait à tous ses clients. »", [
      ("Personnage principal :", "Coumba", "un client", "le marché", "Kaolack", "Texte."),
      ("Activité de Coumba :", "vendre des légumes", "pêcher", "coudre", "enseigner", "Texte."),
      ("Qualité de Coumba :", "courage et gentillesse", "paresse", "méchanceté", "avarice", "Elle sourit malgré la fatigue."),
      ("« Malgré » exprime", "l'opposition", "la cause", "le but", "le temps", "Concession.")]),
    ("Grammaire et conjugaison", "Phrase : « Elle vendait des légumes qu'elle cultivait elle-même. »", [
      ("Temps de « vendait » :", "imparfait", "passé simple", "présent", "conditionnel", "-ait."),
      ("« qu'elle cultivait » est une subordonnée", "relative", "complétive", "circonstancielle", "indépendante", "Antécédent légumes."),
      ("Au passé simple : « Elle (vendre) »", "vendit", "vendait", "vendut", "vendra", "3e groupe."),
      ("Fonction de « des légumes » :", "COD de vendait", "sujet", "COI", "attribut", "Vendait quoi ?")]),
    ("Expression écrite : le récit", "Sujet : « Racontez une journée au marché avec un parent. »", [
      ("Type de texte :", "narratif", "argumentatif", "explicatif", "poétique", "Raconter."),
      ("Plan adapté :", "situation initiale, événements, fin", "thèse, arguments, conclusion", "question, réponse", "titre seul", "Récit."),
      ("Temps du récit au passé :", "passé simple et imparfait", "futur", "subjonctif", "impératif", "Récit."),
      ("Pour enrichir la description :", "utiliser les cinq sens (couleurs, bruits, odeurs)", "répéter « et puis »", "écrire en abrégé", "copier le sujet", "Qualité.")])]),
  b("francais", "Français", 2, [
    ("Compréhension du texte", "« Le téléphone portable est devenu indispensable. Pourtant, chez beaucoup d'élèves, il vole le temps des devoirs et du sommeil. »", [
      ("Thème :", "le téléphone portable chez les élèves", "le sport", "la pêche", "la cuisine", "Texte."),
      ("Connecteur d'opposition :", "pourtant", "chez", "devenu", "et", "Opposition."),
      ("Inconvénient cité :", "il vole le temps des devoirs", "il est cher", "il est lourd", "il fait du bruit", "Texte."),
      ("Figure dans « il vole le temps » :", "personnification", "comparaison", "litote", "antithèse", "Objet qui agit comme un humain.")]),
    ("Vocabulaire et grammaire", "Travail sur le texte.", [
      ("Synonyme de « indispensable » :", "nécessaire", "inutile", "rare", "cher", "Sens."),
      ("Antonyme de « indispensable » :", "superflu", "essentiel", "vital", "obligatoire", "Contraire."),
      ("Préfixe de « indispensable » :", "in-", "dis-", "-able", "pens", "Négation."),
      ("Voix passive de « Le téléphone vole le temps » :", "Le temps est volé par le téléphone.", "Le téléphone est volé par le temps.", "Le temps vole le téléphone.", "Le temps a volé le téléphone.", "COD devient sujet.")]),
    ("Expression écrite : argumenter", "Sujet : « Faut-il interdire le téléphone portable aux élèves ? Donnez votre avis. »", [
      ("Type de texte :", "argumentatif", "narratif", "descriptif", "poétique", "Avis."),
      ("Bon argument pour l'interdiction :", "il distrait des études", "il est joli", "il a des couleurs", "il sonne", "Argument."),
      ("Bon argument contre l'interdiction :", "il permet de rechercher des informations et de joindre les parents", "il est noir", "il est petit", "il a une batterie", "Argument."),
      ("Conclusion réussie :", "réponse claire à la question et ouverture", "un nouvel argument", "une recette", "rien", "Méthode.")])]),
  b("francais", "Français", 3, [
    ("Compréhension d'un poème", "« Femme nue, femme noire / Vêtue de ta couleur qui est vie, de ta forme qui est beauté ! » (Senghor)", [
      ("Auteur :", "Léopold Sédar Senghor", "Aimé Césaire", "Birago Diop", "David Diop", "Chants d'ombre."),
      ("Mouvement littéraire :", "la Négritude", "le romantisme", "le réalisme", "le surréalisme seul", "Senghor, Césaire, Damas."),
      ("Figure dans « Femme nue, femme noire » :", "anaphore", "litote", "comparaison", "oxymore", "Répétition en tête."),
      ("Sentiment exprimé :", "admiration", "colère", "peur", "ennui", "Éloge.")]),
    ("Langue", "« Vêtue de ta couleur qui est vie »", [
      ("Nature de « vêtue » :", "participe passé", "nom", "adverbe", "verbe conjugué", "Forme verbale adjectivée."),
      ("Accord de « vêtue » :", "avec « femme »", "avec « couleur »", "avec « vie »", "aucun", "Féminin singulier."),
      ("« qui est vie » :", "subordonnée relative", "complétive", "principale", "circonstancielle", "Pronom relatif."),
      ("Ponctuation finale du vers 2 :", "point d'exclamation", "point d'interrogation", "virgule", "points de suspension", "Émotion.")]),
    ("Expression écrite : commentaire", "Consigne : « Montrez en un paragraphe que le poète célèbre la femme africaine. »", [
      ("Première étape :", "formuler l'idée directrice", "copier tout le poème", "raconter sa vie", "faire une liste de mots", "Méthode."),
      ("Chaque idée doit être", "illustrée par une citation et expliquée", "répétée trois fois", "sans exemple", "écrite au futur", "Méthode."),
      ("Une citation se met", "entre guillemets", "en majuscules", "entre parenthèses seulement", "sans signe", "Présentation."),
      ("Un bon paragraphe se termine par", "une phrase de bilan", "une question sans réponse", "un nouvel exemple", "une date", "Clôture.")])]),
  # ---------------- Histoire-Géographie (types 1 à 3)
  b("hg", "Histoire-Géographie", 1, [
    ("Histoire : les guerres mondiales", "Questions de cours.", [
      ("Déclenchement de la Seconde Guerre mondiale :", "1939, invasion de la Pologne", "1914, Sarajevo", "1929, krach", "1945, Hiroshima", "Repère."),
      ("Massacre de Thiaroye :", "1er décembre 1944", "11 novembre 1918", "4 avril 1960", "8 mai 1945", "Tirailleurs."),
      ("Organisation créée en 1919 :", "SDN", "ONU", "OUA", "OTAN", "Paix."),
      ("Krach boursier de New York :", "1929", "1933", "1918", "1945", "Crise.")]),
    ("Histoire : la décolonisation", "Questions de cours.", [
      ("Conférence de Brazzaville :", "1944", "1958", "1960", "1946", "De Gaulle."),
      ("Loi-cadre Defferre :", "1956", "1946", "1960", "1944", "Autonomie interne."),
      ("Indépendance du Sénégal, après l'éclatement de la Fédération du Mali :", "20 août 1960", "4 avril 1958", "1er janvier 1960", "1962", "Date."),
      ("Premier président du Sénégal :", "Senghor", "Mamadou Dia", "Lamine Guèye", "Abdou Diouf", "1960.")]),
    ("Géographie : le Sénégal", "Questions de cours.", [
      ("Superficie du Sénégal (environ) :", "197 000 km²", "1 000 000 km²", "19 700 km²", "50 000 km²", "Pays."),
      ("Nombre de régions administratives :", "14", "10", "8", "20", "Découpage."),
      ("Principal port :", "Dakar", "Ziguinchor", "Kaolack", "Saint-Louis", "Port autonome."),
      ("Grande culture d'exportation traditionnelle :", "arachide", "cacao", "café", "thé", "Bassin arachidier.")])]),
  b("hg", "Histoire-Géographie", 2, [
    ("Histoire : le XIXe siècle", "Questions de cours.", [
      ("Conférence de Berlin :", "1884-1885", "1919", "1945", "1960", "Partage de l'Afrique."),
      ("Création de l'AOF :", "1895", "1885", "1960", "1944", "Fédération."),
      ("Lat Dior combat contre", "le chemin de fer Dakar – Saint-Louis", "les Portugais", "les Marocains", "l'indépendance", "Cayor."),
      ("Abolition de l'esclavage dans les colonies françaises :", "1848", "1789", "1885", "1905", "Schœlcher.")]),
    ("Histoire : le monde après 1945", "Questions de cours.", [
      ("Symbole de la guerre froide en Allemagne :", "mur de Berlin", "tour Eiffel", "arc de triomphe", "Big Ben", "1961-1989."),
      ("Chute du mur de Berlin :", "1989", "1961", "1945", "2001", "Fin de la guerre froide."),
      ("Déclaration universelle des droits de l'homme :", "1948", "1789", "1945", "1960", "ONU."),
      ("Création de l'OUA :", "1963", "1945", "1960", "2002", "Addis-Abeba.")]),
    ("Géographie : population et environnement", "Questions de cours.", [
      ("Région la plus peuplée du Sénégal :", "Dakar", "Kédougou", "Matam", "Sédhiou", "Capitale."),
      ("Ville sainte du mouridisme :", "Touba", "Tivaouane", "Ndiassane", "Médina Baye", "Grand Magal."),
      ("Menace sur la Langue de Barbarie :", "érosion côtière", "volcans", "neige", "séismes", "Saint-Louis."),
      ("Projet de reboisement sahélien :", "Grande Muraille verte", "Plan Marshall", "OMVS", "Canal de Suez", "Sahel.")])]),
  b("hg", "Histoire-Géographie", 3, [
    ("Histoire : étude d'un document", "Extrait : « Nous préférons la pauvreté dans la liberté à la richesse dans l'esclavage. » (Sékou Touré, 1958)", [
      ("Nature du document :", "discours", "carte", "photographie", "tableau statistique", "Parole publique."),
      ("Contexte :", "référendum de 1958", "Seconde Guerre mondiale", "conquête coloniale", "guerre froide en Europe", "Communauté française."),
      ("Choix de la Guinée :", "« non » et indépendance immédiate", "« oui » à la Communauté", "rattachement au Sénégal", "aucun vote", "Résultat."),
      ("Idée principale :", "la liberté compte plus que l'aide matérielle", "la richesse avant tout", "rester colonie", "la guerre", "Thèse.")]),
    ("Histoire : le Sénégal indépendant", "Questions de cours.", [
      ("Crise de décembre 1962 :", "opposition entre Senghor et Mamadou Dia", "guerre avec le Mali", "coup d'État militaire réussi", "élection de Wade", "Bicéphalisme."),
      ("Première alternance politique :", "2000", "1981", "2012", "1960", "Abdoulaye Wade."),
      ("Président de 2012 à 2024 :", "Macky Sall", "Abdou Diouf", "Abdoulaye Wade", "Bassirou Diomaye Faye", "Mandats."),
      ("Organe qui vote les lois :", "Assemblée nationale", "Conseil constitutionnel", "Présidence seule", "Cour suprême", "Législatif.")]),
    ("Géographie : l'économie du Sénégal", "Questions de cours.", [
      ("Gisement de pétrole exploité depuis 2024 :", "Sangomar", "Kayar", "Bakel", "Podor", "Offshore."),
      ("Barrage anti-sel :", "Diama", "Manantali", "Anambé", "Assouan", "Fleuve Sénégal."),
      ("Secteur qui emploie le plus de personnes :", "primaire (agriculture, pêche)", "industrie lourde", "nucléaire", "spatial", "Emploi."),
      ("Zone industrielle principale :", "Dakar – Rufisque – Thiès", "Kédougou", "Matam", "Kolda", "Concentration.")])]),
  # ---------------- Anglais (types 1 à 3)
  b("anglais", "Anglais", 1, [
    ("Reading comprehension", "« Fatou lives in Ziguinchor. Every Saturday, she helps her mother at the market. Last week, she sold all the mangoes before noon. She is saving money to buy a bicycle. »", [
      ("Where does Fatou live?", "in Ziguinchor", "in Dakar", "at the market", "in a bicycle shop", "Texte."),
      ("When does she help her mother?", "every Saturday", "every day", "on Sundays", "never", "Texte."),
      ("What did she sell last week?", "mangoes", "bicycles", "fish", "bread", "Texte."),
      ("Why is she saving money?", "to buy a bicycle", "to travel", "to buy mangoes", "to pay school fees", "Texte.")]),
    ("Grammar", "Choose the correct answer.", [
      ("She … (sell) all the mangoes last week.", "sold", "sells", "has sold", "selled", "Last week."),
      ("She is saving money … buy a bike.", "to", "for", "at", "of", "But."),
      ("If she saves enough, she … buy it.", "will", "would", "has", "is", "Type 1."),
      ("Her mother is … than her.", "older", "more old", "oldest", "the older", "Comparatif.")]),
    ("Writing", "Write a short paragraph about your weekend.", [
      ("Good opening sentence :", "Last weekend, I visited my grandparents.", "Weekend last I visit.", "I am visiting weekend last.", "Grandparents my weekend.", "Phrase correcte."),
      ("Linking word to add an idea :", "moreover", "however", "although", "because", "Addition."),
      ("Linking word for the end :", "finally", "firstly", "but", "if", "Conclusion."),
      ("Tense for a past weekend :", "past simple", "present simple", "future", "present perfect continuous", "Moment fini.")])]),
  b("anglais", "Anglais", 2, [
    ("Reading comprehension", "« Plastic waste is a serious problem in Dakar. It blocks drains and causes floods during the rainy season. Many young people now organise clean-up days in their neighbourhoods. »", [
      ("Main problem :", "plastic waste", "traffic", "noise", "unemployment", "Texte."),
      ("Consequence mentioned :", "floods", "earthquakes", "fires", "droughts", "Texte."),
      ("When do floods happen?", "during the rainy season", "in the dry season", "every night", "never", "Texte."),
      ("What do young people organise?", "clean-up days", "concerts", "football matches", "elections", "Texte.")]),
    ("Grammar", "Choose.", [
      ("Plastic … (block) drains.", "blocks", "block", "blocking", "is block", "Sujet singulier."),
      ("Drains … by plastic. (passif)", "are blocked", "blocks", "is blocking", "blocked are", "Passif."),
      ("People … throw plastic in the street. (interdit)", "mustn't", "must", "can", "should to", "Interdiction."),
      ("We should … the environment.", "protect", "to protect", "protecting", "protects", "Base verbale.")]),
    ("Vocabulary", "Find the meaning.", [
      ("« waste » :", "déchets", "eau", "vent", "argent", "Contexte."),
      ("« floods » :", "inondations", "incendies", "sécheresses", "tempêtes de sable", "Contexte."),
      ("« neighbourhood » :", "quartier", "voisin seulement", "ville entière", "pays", "Contexte."),
      ("« to recycle » :", "recycler", "jeter", "brûler", "acheter", "Vocabulaire.")])]),
  b("anglais", "Anglais", 3, [
    ("Reading comprehension", "« When I was ten, I wanted to be a pilot. Now I am fifteen and I have changed my mind: I would like to become a doctor because I want to help sick people in my village. »", [
      ("What did the narrator want to be at ten?", "a pilot", "a doctor", "a teacher", "a farmer", "Texte."),
      ("How old is the narrator now?", "fifteen", "ten", "fifty", "five", "Texte."),
      ("Why does he want to be a doctor?", "to help sick people", "to earn money", "to travel", "to fly", "Texte."),
      ("« I have changed my mind » :", "j'ai changé d'avis", "j'ai perdu la tête", "j'ai changé d'école", "j'ai grandi", "Expression.")]),
    ("Grammar", "Choose.", [
      ("I … (want) to be a pilot when I was ten.", "wanted", "want", "have wanted", "am wanting", "Passé."),
      ("I would like … a doctor.", "to become", "become", "becoming", "became", "would like to."),
      ("A doctor is a person … treats sick people.", "who", "which", "where", "whose", "Relatif."),
      ("If I were a doctor, I … open a clinic.", "would", "will", "am", "did", "Type 2.")]),
    ("Writing : a letter", "Write a letter to a friend about your future job.", [
      ("Opening :", "Dear Moussa,", "Dear Sir or Madam,", "To whom it may concern,", "Yours faithfully,", "Lettre amicale."),
      ("Ending :", "Best wishes,", "Yours faithfully,", "Dear friend,", "Hello,", "Formule."),
      ("Tense to talk about your plans :", "be going to / will", "past simple", "past perfect", "past continuous", "Futur."),
      ("A good letter has", "an opening, a body and an ending", "only one sentence", "no paragraph", "only questions", "Structure.")])]),
  # ---------------- Espagnol (types 1 à 3)
  b("espagnol", "Espagnol (LV2)", 1, [
    ("Comprensión", "« Me llamo Aïssatou. Vivo en Saint-Louis con mis padres. Me gusta mucho leer y nadar. El verano pasado fui a Dakar. »", [
      ("¿Dónde vive Aïssatou?", "en Saint-Louis", "en Dakar", "en Madrid", "en Thiès", "Texte."),
      ("¿Qué le gusta?", "leer y nadar", "cocinar", "bailar", "dormir", "Texte."),
      ("« fui » :", "je suis allée", "je vais", "j'irai", "j'allais", "Indefinido de ir."),
      ("« con mis padres » :", "avec mes parents", "avec mes frères", "sans mes parents", "chez mes amis", "Traduction.")]),
    ("Gramática", "Elige.", [
      ("Saint-Louis … en el norte.", "está", "es", "son", "estoy", "Lieu."),
      ("A ella le … los libros.", "gustan", "gusta", "gusto", "gustas", "Pluriel."),
      ("Ayer (ir, nosotros) a la playa.", "fuimos", "vamos", "íbamos", "iremos", "Indefinido."),
      ("Mañana (tener, yo) un examen.", "tendré", "teneré", "tengo", "tuve", "Futur irrégulier.")]),
    ("Expresión escrita", "Escribe cinco líneas sobre tus vacaciones.", [
      ("Bon début :", "El verano pasado, fui a casa de mis abuelos.", "Verano pasado yo ir abuelos.", "Yo soy vacaciones.", "Las vacaciones están Dakar.", "Phrase correcte."),
      ("Marqueur du passé :", "el año pasado", "mañana", "siempre", "ahora", "Indefinido."),
      ("Connecteur « ensuite » :", "luego / después", "pero", "porque", "aunque", "Enchaînement."),
      ("Connecteur « mais » :", "pero", "y", "también", "luego", "Opposition.")])]),
  b("espagnol", "Espagnol (LV2)", 2, [
    ("Comprensión", "« Mi hermano está enfermo. Le duele la garganta y tiene fiebre. Mi madre lo lleva al médico. »", [
      ("¿Quién está enfermo?", "el hermano", "la madre", "el médico", "el narrador", "Texte."),
      ("¿Qué le duele?", "la garganta", "la cabeza", "el pie", "los ojos", "Texte."),
      ("« tiene fiebre » :", "il a de la fièvre", "il a faim", "il a froid", "il a peur", "Expression."),
      ("¿Adónde lo lleva la madre?", "al médico", "al colegio", "al mercado", "a la playa", "Texte.")]),
    ("Gramática", "Elige.", [
      ("Mi hermano … enfermo (état).", "está", "es", "son", "estoy", "Estar."),
      ("Me … las piernas.", "duelen", "duele", "dolor", "duelo", "Pluriel."),
      ("Mi madre (llevar, indefinido) a mi hermano al médico.", "llevó", "lleva", "llevaba", "llevará", "Passé."),
      ("Cuando (ser, yo) mayor, seré médico.", "sea", "seré", "soy", "fui", "Subjonctif après cuando.")]),
    ("Vocabulario", "Encuentra la palabra.", [
      ("« estómago » :", "ventre / estomac", "tête", "dos", "bras", "Corps."),
      ("« la espalda » :", "le dos", "l'épaule seulement", "la jambe", "la bouche", "Corps."),
      ("« el hospital » :", "l'hôpital", "l'hôtel", "l'école", "la pharmacie", "Lieu."),
      ("« la farmacia » :", "la pharmacie", "la ferme", "la famille", "le marché", "Lieu.")])]),
  b("espagnol", "Espagnol (LV2)", 3, [
    ("Comprensión", "« El próximo año, voy a estudiar en el liceo. Quiero ser ingeniero. Trabajaré mucho para conseguirlo. »", [
      ("¿Dónde va a estudiar?", "en el liceo", "en la universidad", "en Madrid", "en casa", "Texte."),
      ("¿Qué quiere ser?", "ingeniero", "médico", "profesor", "futbolista", "Texte."),
      ("« Trabajaré » :", "je travaillerai", "j'ai travaillé", "je travaille", "je travaillais", "Futur."),
      ("« voy a estudiar » :", "futur proche", "passé", "présent de habitude", "subjonctif", "ir a + infinitif.")]),
    ("Gramática", "Elige.", [
      ("Futur de « poder », yo :", "podré", "poderé", "pude", "puedo", "Irrégulier."),
      ("Futur de « hacer », nosotros :", "haremos", "haceremos", "hicimos", "hacemos", "Irrégulier."),
      ("Futur de « salir », ellos :", "saldrán", "salirán", "salieron", "salen", "Irrégulier."),
      ("« Je vais réviser » :", "Voy a repasar", "Voy repasar", "Iré a repasar ayer", "Repasaba", "ir a.")]),
    ("Expresión escrita", "Escribe tus proyectos para el futuro.", [
      ("Phrase correcte :", "En el futuro, seré profesora.", "En el futuro, soy fui profesora.", "Futuro yo ser profesora.", "Profesora seré futuro el.", "Futur."),
      ("« parce que » :", "porque", "pero", "por favor", "para", "Cause."),
      ("« je voudrais » :", "me gustaría (quisiera)", "me gusta", "quiero ayer", "quería mañana", "Souhait."),
      ("Fin de texte :", "Por eso estudio mucho.", "Hola.", "Adiós ayer.", "Gracias por favor.", "Conclusion.")])]),
])
