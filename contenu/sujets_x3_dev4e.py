from sujets_dev_common import D, pack, TRIM
L = "4e"
def d(s, name, n, exos): return D(f"dev-4e-{s}-{n}", L, name, n, exos, label=TRIM[n])

ANNALES_X, GUIDED_X = pack([
  d("maths", "Mathématiques", 1, [
    ("Puissances", "Calcule.", [
      ("3⁴ =", "81", "12", "64", "27", "3 × 3 × 3 × 3."),
      ("2³ × 2² =", "2⁵", "2⁶", "4⁵", "2¹", "Exposants additionnés."),
      ("(10²)³ =", "10⁶", "10⁵", "10⁸", "1 000²", "Exposants multipliés."),
      ("Écriture scientifique de 45 000 :", "4,5 × 10⁴", "45 × 10³", "4,5 × 10³", "0,45 × 10⁵", "Un chiffre non nul avant la virgule.")]),
    ("Calcul littéral", "On donne A = 2(3x − 1) − (x + 4).", [
      ("2(3x − 1) =", "6x − 2", "6x − 1", "5x − 2", "6x + 2", "Distributivité."),
      ("A réduit :", "5x − 6", "5x + 2", "7x − 6", "5x − 2", "6x − 2 − x − 4."),
      ("A pour x = 2 :", "4", "8", "−4", "16", "10 − 6."),
      ("Factoriser 4x − 12 :", "4(x − 3)", "4(x − 12)", "x(4 − 12)", "2(x − 12)", "Facteur commun 4.")]),
    ("Équation : le partage", "Trois frères se partagent 25 000 F. L'aîné reçoit 4 000 F de plus que chacun des deux autres, qui reçoivent la même somme x.", [
      ("Part de l'aîné :", "x + 4 000", "4 000x", "x − 4 000", "25 000 − x", "4 000 de plus."),
      ("Équation :", "3x + 4 000 = 25 000", "x + 4 000 = 25 000", "2x = 25 000", "3x = 25 000", "x + x + (x + 4 000)."),
      ("x =", "7 000 F", "8 333 F", "4 000 F", "21 000 F", "3x = 21 000."),
      ("Part de l'aîné :", "11 000 F", "7 000 F", "4 000 F", "14 000 F", "7 000 + 4 000.")])]),
  d("maths", "Mathématiques", 2, [
    ("Fractions", "Calcule et simplifie.", [
      ("5/6 − 1/4 =", "7/12", "4/2", "1/3", "4/12", "10/12 − 3/12."),
      ("(3/4) × (8/9) =", "2/3", "24/36 non simplifiable", "11/13", "3/2", "24/36 = 2/3."),
      ("(2/5) ÷ (4/15) =", "3/2", "8/75", "2/3", "6/5", "2/5 × 15/4 = 30/20."),
      ("Inverse de −3 :", "−1/3", "3", "1/3", "−3", "Produit égal à 1.")]),
    ("Théorème de Pythagore", "Un poteau électrique de 8 m est maintenu par un câble fixé au sommet et au sol à 6 m du pied.", [
      ("Le triangle est rectangle au", "pied du poteau", "sommet", "point d'ancrage", "nulle part", "Poteau vertical."),
      ("Longueur² du câble :", "100", "28", "14", "64", "8² + 6² = 64 + 36."),
      ("Longueur du câble :", "10 m", "14 m", "100 m", "7 m", "√100."),
      ("cos de l'angle au sol :", "0,6", "0,8", "0,75", "1,33", "Adjacent 6 / hypoténuse 10.")]),
    ("Droite des milieux", "Dans le triangle KLM, KL = 12 cm, LM = 9 cm, KM = 8 cm. A est le milieu de [KL] et B le milieu de [KM].", [
      ("(AB) est parallèle à", "(LM)", "(KL)", "(KM)", "aucune", "Théorème des milieux."),
      ("AB =", "4,5 cm", "9 cm", "6 cm", "4 cm", "LM ÷ 2."),
      ("KA =", "6 cm", "12 cm", "4 cm", "4,5 cm", "Milieu de [KL]."),
      ("Périmètre de KAB :", "14,5 cm", "29 cm", "18 cm", "10 cm", "6 + 4 + 4,5.")])]),
  d("maths", "Mathématiques", 3, [
    ("Vitesse", "Une pirogue fait 36 km en 1 h 30 min.", [
      ("1 h 30 min =", "1,5 h", "1,3 h", "1,03 h", "90 h", "30 min = 0,5 h."),
      ("Vitesse moyenne :", "24 km/h", "36 km/h", "54 km/h", "12 km/h", "36 ÷ 1,5."),
      ("Distance en 2 h 15 min :", "54 km", "48 km", "60 km", "36 km", "24 × 2,25."),
      ("Durée pour 60 km :", "2 h 30 min", "2 h", "3 h", "2 h 15 min", "60 ÷ 24 = 2,5 h.")]),
    ("Statistiques", "Notes d'un élève : 12 (coef 3), 8 (coef 2), 15 (coef 1).", [
      ("Somme des coefficients :", "6", "3", "35", "5", "3 + 2 + 1."),
      ("Total des points :", "67", "35", "60", "72", "36 + 16 + 15."),
      ("Moyenne pondérée (au centième) :", "11,17", "11,67", "12", "10,5", "67 ÷ 6."),
      ("Moyenne simple des trois notes :", "11,67", "11,17", "12", "35", "35 ÷ 3.")]),
    ("Cercle circonscrit", "RST est rectangle en R avec RS = 5 cm et RT = 12 cm.", [
      ("ST =", "13 cm", "17 cm", "7 cm", "169 cm", "√(25 + 144)."),
      ("Centre du cercle circonscrit :", "milieu de [ST]", "R", "milieu de [RS]", "milieu de [RT]", "Hypoténuse."),
      ("Rayon :", "6,5 cm", "13 cm", "6 cm", "8,5 cm", "13 ÷ 2."),
      ("Aire du triangle :", "30 cm²", "60 cm²", "65 cm²", "32,5 cm²", "5 × 12 ÷ 2.")])]),
  d("francais", "Français", 1, [
    ("Voix passive", "« Les élèves ont planté des arbres. »", [
      ("Voix passive :", "Des arbres ont été plantés par les élèves.", "Des arbres sont plantés par les élèves.", "Les élèves ont été plantés.", "Des arbres plantaient les élèves.", "Même temps."),
      ("Complément d'agent :", "par les élèves", "des arbres", "ont été", "plantés", "par + agent."),
      ("Accord de « plantés » :", "masculin pluriel (arbres)", "féminin", "singulier", "aucun accord", "Avec le sujet."),
      ("Phrase impossible au passif :", "Il dort.", "Le chat mange la souris.", "On lit le livre.", "Awa écrit la lettre.", "Pas de COD.")]),
    ("Discours rapporté", "Le maître dit : « Je corrigerai vos copies demain. »", [
      ("Au discours indirect (verbe au présent) :", "Le maître dit qu'il corrigera nos copies demain.", "Le maître dit qu'il corrigerait vos copies demain.", "Le maître dit je corrigerai.", "Le maître dit qu'il corrige hier.", "Présent : temps gardé, pronoms changés."),
      ("Avec « a dit » :", "Le maître a dit qu'il corrigerait nos copies le lendemain.", "Le maître a dit qu'il corrigera vos copies demain.", "Le maître a dit : il corrigera.", "Le maître a dit qu'il corrige.", "Futur → conditionnel."),
      ("Ponctuation du discours direct :", "deux points et guillemets", "point-virgule", "parenthèses", "aucune", "Signes."),
      ("Verbe introducteur :", "dit", "corrigerai", "copies", "demain", "Verbe de parole.")]),
    ("Subordonnées", "« Comme il pleuvait, nous sommes restés à la maison où nous avons lu. »", [
      ("« Comme il pleuvait » exprime", "la cause", "le but", "le temps", "la conséquence", "Comme = parce que."),
      ("« où nous avons lu » est une subordonnée", "relative", "complétive", "circonstancielle de but", "indépendante", "Antécédent maison."),
      ("Proposition principale :", "nous sommes restés à la maison", "comme il pleuvait", "où nous avons lu", "il pleuvait", "Ne dépend de rien."),
      ("Subordonnée de but :", "pour que tu réussisses", "parce que tu réussis", "quand tu réussis", "qui réussit", "Pour que.")])]),
  d("francais", "Français", 2, [
    ("Conditionnel et subjonctif", "Conjugue.", [
      ("Si tu venais, nous (être) contents.", "serions", "serons", "soyons", "étions", "Conditionnel."),
      ("Il faut que nous (aller) au marché.", "allions", "allons", "irions", "irons", "Subjonctif."),
      ("Je voudrais qu'elle (savoir) la vérité.", "sache", "sait", "saura", "saurait", "Subjonctif."),
      ("Vous (pouvoir) m'aider ? (politesse)", "Pourriez-vous", "Pouvez-vous seulement au futur", "Pourrez-vous", "Puissiez-vous", "Conditionnel.")]),
    ("Accord du participe passé", "Accorde.", [
      ("Les chansons que j'ai (entendre)…", "entendues", "entendu", "entendus", "entendue", "COD avant."),
      ("Elles sont (partir) tôt.", "parties", "parti", "partis", "partie", "Être."),
      ("Nous avons (manger) des mangues.", "mangé", "mangées", "mangés", "mangeons", "COD après."),
      ("La lettre ? Je l'ai (lire).", "lue", "lu", "lus", "lues", "l' = la lettre.")]),
    ("Figures de style", "Identifie.", [
      ("« Ses yeux brillent comme des étoiles. »", "comparaison", "métaphore", "hyperbole", "litote", "comme."),
      ("« La ville dort. »", "personnification", "comparaison", "antithèse", "litote", "Qualité humaine."),
      ("« Ce n'est pas mauvais. » (pour « c'est bon »)", "litote", "hyperbole", "métaphore", "oxymore", "Dire moins."),
      ("« Je meurs de faim. »", "hyperbole", "litote", "comparaison", "euphémisme", "Exagération.")])]),
  d("francais", "Français", 3, [
    ("L'autobiographie", "« Je suis né à Kouroussa, en Guinée. Mon père était forgeron. » (d'après L'Enfant noir)", [
      ("Le narrateur est", "l'auteur lui-même", "un témoin extérieur", "un animal", "un personnage inventé sans lien", "Pacte autobiographique."),
      ("Pronom dominant :", "je", "il", "nous", "vous", "Première personne."),
      ("Métier du père :", "forgeron", "pêcheur", "griot", "tailleur", "Texte."),
      ("Auteur de L'Enfant noir :", "Camara Laye", "Mariama Bâ", "Cheikh Hamidou Kane", "Ousmane Sembène", "1953.")]),
    ("Le roman africain", "Œuvres étudiées en classe.", [
      ("Une si longue lettre :", "Mariama Bâ", "Camara Laye", "Birago Diop", "Aminata Sow Fall", "1979."),
      ("Les Bouts de bois de Dieu :", "Ousmane Sembène", "Senghor", "Mongo Beti", "Hampâté Bâ", "Grève du rail."),
      ("L'Aventure ambiguë :", "Cheikh Hamidou Kane", "Mariama Bâ", "Ousmane Sembène", "Camara Laye", "1961."),
      ("La Grève des bàttu :", "Aminata Sow Fall", "Mariama Bâ", "Ken Bugul", "Fatou Diome", "1979.")]),
    ("Le théâtre et l'argumentation", "Un personnage dit : « L'école est la clé de l'avenir, car elle donne un métier et ouvre l'esprit. »", [
      ("Thèse défendue :", "l'école est la clé de l'avenir", "l'école est inutile", "il faut travailler aux champs", "rien", "Prise de position."),
      ("Connecteur qui introduit l'argument :", "car", "et", "l'", "avenir", "Cause."),
      ("Premier argument :", "elle donne un métier", "elle est fermée", "elle est loin", "elle coûte cher", "Texte."),
      ("Une réplique est", "ce que dit un personnage", "une indication de mise en scène", "un décor", "un acte entier", "Théâtre.")])]),
  d("svt", "SVT", 1, [
    ("Appareils reproducteurs", "On étudie les organes reproducteurs humains.", [
      ("Les testicules produisent", "les spermatozoïdes", "les ovules", "le lait", "l'urine", "Gonades mâles."),
      ("Les ovaires produisent", "les ovules", "les spermatozoïdes", "le sang", "la salive", "Gonades femelles."),
      ("Organe où se développe l'embryon :", "utérus", "ovaire", "trompe", "vessie", "Nidation."),
      ("La puberté est marquée chez la fille par", "les premières règles", "la mue de la voix", "la barbe", "la calvitie", "Signe.")]),
    ("Fécondation et grossesse", "La fécondation a lieu le 15e jour d'un cycle.", [
      ("Fécondation :", "union d'un ovule et d'un spermatozoïde", "division d'une cellule", "naissance", "règles", "Définition."),
      ("Cellule obtenue :", "cellule-œuf", "ovule", "spermatozoïde", "neurone", "Zygote."),
      ("Durée de la grossesse :", "environ 9 mois", "28 jours", "1 an", "3 mois", "Gestation."),
      ("Échanges mère-enfant par", "le placenta", "l'ovaire", "les poumons du fœtus", "l'estomac", "Placenta.")]),
    ("Les IST", "Une campagne parle de prévention.", [
      ("Le VIH attaque", "les défenses immunitaires", "les os", "les dents", "les cheveux", "Lymphocytes."),
      ("Transmission possible du VIH :", "sang contaminé", "poignée de main", "moustique", "partage d'un repas", "Voies."),
      ("Protection lors des rapports :", "préservatif", "pilule", "antibiotique", "vaccin contre la rougeole", "Barrière."),
      ("Seul moyen de connaître son statut :", "test de dépistage", "regarder son poids", "prendre sa température", "deviner", "Dépistage.")])]),
  d("svt", "SVT", 2, [
    ("Volcans", "Le mont Cameroun est un volcan actif.", [
      ("Matière sortant du cratère :", "lave", "eau de mer", "sable", "glace", "Éruption."),
      ("Réservoir de magma en profondeur :", "chambre magmatique", "cratère", "cône", "épicentre", "Structure."),
      ("Éruption très explosive :", "type gris (explosif)", "type rouge (effusif)", "aucune", "type bleu", "Lave visqueuse."),
      ("Les îles du Cap-Vert (pays voisin) sont d'origine", "volcanique", "glaciaire", "sédimentaire", "artificielle", "Origine.")]),
    ("Séismes", "Un séisme de magnitude 6 frappe une région.", [
      ("Échelle de la magnitude :", "Richter", "Celsius", "Beaufort", "Mercalli seule", "Énergie."),
      ("Lieu en profondeur où naît le séisme :", "foyer", "épicentre", "cratère", "faille en surface seulement", "Origine."),
      ("Ondes du séisme enregistrées par un", "sismographe", "baromètre", "anémomètre", "pluviomètre", "Mesure."),
      ("Bon réflexe pendant un séisme :", "s'abriter sous une table solide", "prendre l'ascenseur", "rester près des vitres", "courir dans l'escalier", "Sécurité.")]),
    ("Roches et érosion", "La falaise de Popenguine recule.", [
      ("Agent principal du recul :", "vagues", "lumière", "électricité", "fossiles", "Érosion marine."),
      ("Roche formée de dépôts :", "sédimentaire", "volcanique", "métamorphique", "magmatique", "Couches."),
      ("Les sédiments se déposent souvent", "en couches horizontales", "en boules", "verticalement", "au hasard", "Stratification."),
      ("Un fossile permet de", "dater et reconstituer un milieu ancien", "faire du feu", "fabriquer du ciment", "rien", "Utilité.")])]),
  d("svt", "SVT", 3, [
    ("L'hérédité", "Awa a le groupe sanguin O comme sa mère.", [
      ("Le groupe sanguin est un caractère", "héréditaire", "acquis", "appris", "lié à l'alimentation", "Transmis."),
      ("Les gènes sont portés par", "les chromosomes", "les os", "les globules blancs uniquement", "la peau", "Support."),
      ("Chromosomes d'une cellule humaine :", "46 (23 paires)", "23", "92", "12", "Caryotype."),
      ("Cellule reproductrice : chromosomes", "23", "46", "92", "0", "Gamète.")]),
    ("Caractères acquis", "Moussa parle wolof, anglais et sait nager.", [
      ("Parler anglais est", "acquis", "héréditaire", "génétique", "inné", "Appris."),
      ("Couleur des yeux :", "héréditaire", "acquise", "apprise", "liée au sport", "Gènes."),
      ("Un muscle développé par le sport est", "acquis", "héréditaire", "génétique", "transmis aux enfants", "Entraînement."),
      ("Un caractère acquis", "ne se transmet pas par les gènes", "se transmet toujours", "est dans l'ADN", "est un chromosome", "Distinction.")]),
    ("Sexe de l'enfant", "Un couple attend un enfant.", [
      ("Chromosomes sexuels du père :", "XY", "XX", "YY", "X", "Homme."),
      ("La mère transmet toujours un chromosome", "X", "Y", "XY", "aucun", "XX."),
      ("Le sexe de l'enfant dépend du chromosome", "apporté par le spermatozoïde", "apporté par l'ovule", "de la nourriture", "du hasard du climat", "X ou Y."),
      ("Probabilité d'avoir une fille :", "1 chance sur 2", "1 sur 4", "toujours", "jamais", "50 %.")])]),
  d("pc", "Sciences physiques", 1, [
    ("Masse et volume", "Une pierre de 260 g est plongée dans une éprouvette : le niveau passe de 120 mL à 220 mL.", [
      ("Volume de la pierre :", "100 cm³", "220 cm³", "340 cm³", "120 cm³", "220 − 120."),
      ("Masse volumique :", "2,6 g/cm³", "0,38 g/cm³", "26 g/cm³", "260 g/cm³", "260 ÷ 100."),
      ("En kg/m³ :", "2 600 kg/m³", "2,6 kg/m³", "260 kg/m³", "26 000 kg/m³", "× 1 000."),
      ("La pierre dans l'eau :", "coule", "flotte", "se dissout", "disparaît", "Plus dense.")]),
    ("Mélanges", "On mélange du sable, du sel et de l'eau.", [
      ("Le mélange est", "hétérogène", "homogène", "un corps pur", "un gaz", "On voit le sable."),
      ("Pour retirer le sable :", "filtration", "évaporation", "distillation seule", "aimantation", "Solide insoluble."),
      ("Le filtrat contient", "eau et sel dissous", "sable", "rien", "seulement du sel solide", "Solution."),
      ("Pour récupérer le sel :", "évaporer l'eau", "filtrer encore", "congeler", "ajouter du sable", "Évaporation.")]),
    ("Changements d'état", "On met de l'eau au congélateur.", [
      ("Passage liquide → solide :", "solidification", "fusion", "vaporisation", "condensation", "Nom."),
      ("Température de solidification de l'eau pure :", "0 °C", "100 °C", "−10 °C", "4 °C", "Palier."),
      ("Le volume de l'eau en gelant", "augmente", "diminue", "ne change pas", "disparaît", "Bouteille qui éclate."),
      ("La masse en gelant", "reste la même", "augmente", "diminue", "double", "Conservation.")])]),
  d("pc", "Sciences physiques", 2, [
    ("Le circuit en série", "Une pile alimente deux lampes L1 et L2 en série.", [
      ("Si L1 est dévissée :", "L2 s'éteint", "L2 brille plus", "L2 brille pareil", "la pile explose", "Boucle ouverte."),
      ("L'intensité dans L1 et L2 est", "la même", "plus forte dans L1", "plus forte dans L2", "nulle", "Série."),
      ("Appareil branché en série pour mesurer I :", "ampèremètre", "voltmètre", "ohmmètre", "thermomètre", "Branchement."),
      ("Unité d'intensité :", "ampère (A)", "volt (V)", "watt (W)", "ohm (Ω)", "Unité.")]),
    ("Le circuit en dérivation", "Deux lampes sont branchées en dérivation sur une pile de 4,5 V.", [
      ("Si une lampe grille, l'autre", "reste allumée", "s'éteint", "explose", "clignote", "Boucles indépendantes."),
      ("Tension aux bornes de chaque lampe :", "4,5 V", "2,25 V", "9 V", "0 V", "Dérivation."),
      ("Installation d'une maison :", "en dérivation", "en série", "sans fil", "en court-circuit", "Indépendance."),
      ("Court-circuit :", "les bornes de la pile reliées par un fil seul", "deux lampes en série", "un interrupteur ouvert", "une lampe grillée", "Danger.")]),
    ("La lumière", "Un élève observe une éclipse de Soleil.", [
      ("Pendant une éclipse de Soleil, la Lune est", "entre le Soleil et la Terre", "derrière la Terre", "derrière le Soleil", "absente", "Alignement."),
      ("Il ne faut jamais regarder le Soleil", "à l'œil nu", "avec des lunettes spéciales", "par projection", "sur un écran", "Danger."),
      ("Objet opaque :", "carton", "verre", "eau claire", "air", "Ne laisse pas passer la lumière."),
      ("Vitesse de la lumière :", "300 000 km/s", "340 m/s", "1 000 km/h", "30 km/s", "Vide.")])]),
  d("pc", "Sciences physiques", 3, [
    ("Les dangers de l'électricité", "Le courant du secteur (220 V) est dangereux.", [
      ("Tension du secteur au Sénégal :", "220 V", "4,5 V", "12 V", "1 000 V", "Prise."),
      ("Ne jamais toucher une prise", "avec les mains mouillées", "avec un gant isolant", "débranchée", "éteinte", "Électrocution."),
      ("Appareil qui protège l'installation :", "disjoncteur", "lampe", "moteur", "résistance", "Coupure."),
      ("Un bon isolant :", "plastique", "cuivre", "fer", "eau salée", "Ne conduit pas.")]),
    ("Conducteurs et isolants", "On teste des objets dans un circuit avec une lampe.", [
      ("La lampe brille avec", "une clé en fer", "une gomme", "un crayon en bois", "une règle en plastique", "Métal conducteur."),
      ("Le corps humain est", "conducteur", "isolant", "parfait isolant", "aimant", "Danger."),
      ("Matériau des fils électriques :", "cuivre", "verre", "papier", "caoutchouc seul", "Conducteur."),
      ("Gaine des fils :", "plastique isolant", "fer", "or", "eau", "Protection.")]),
    ("Tension et intensité", "On mesure U = 6 V aux bornes d'une lampe parcourue par I = 0,3 A.", [
      ("Voltmètre branché", "en dérivation", "en série", "nulle part", "à la place de la lampe", "Branchement."),
      ("Unité de tension :", "volt", "ampère", "watt", "ohm", "U."),
      ("0,3 A en mA :", "300 mA", "30 mA", "3 mA", "3 000 mA", "× 1 000."),
      ("Puissance P = U × I :", "1,8 W", "6,3 W", "20 W", "0,05 W", "6 × 0,3.")])]),
  d("histoire", "Histoire", 1, [
    ("Les grandes découvertes", "Au XVe siècle, les Portugais longent les côtes africaines.", [
      ("Arrivée des Portugais au Cap-Vert (presqu'île) :", "1444", "1492", "1659", "1885", "Dinis Dias."),
      ("Christophe Colomb :", "atteint l'Amérique en 1492", "fait le tour de l'Afrique", "découvre l'Inde", "fonde Saint-Louis", "Repère."),
      ("Navire des explorateurs :", "caravelle", "pirogue", "paquebot", "sous-marin", "Bateau."),
      ("Motif principal des voyages :", "épices et or", "tourisme", "football", "pétrole", "Commerce.")]),
    ("La Renaissance", "Aux XVe-XVIe siècles, l'Europe redécouvre l'Antiquité.", [
      ("Invention de Gutenberg :", "imprimerie", "boussole", "télescope", "électricité", "Vers 1450."),
      ("Peintre de La Joconde :", "Léonard de Vinci", "Picasso", "Michel-Ange", "Van Gogh", "Renaissance."),
      ("Les humanistes placent au centre", "l'homme et le savoir", "la guerre", "l'argent seul", "la magie", "Humanisme."),
      ("Pays berceau de la Renaissance :", "Italie", "Russie", "Sénégal", "Chine", "Florence.")]),
    ("Les comptoirs", "Les Européens installent des comptoirs sur la côte.", [
      ("Fondation de Saint-Louis :", "1659", "1444", "1848", "1902", "Français."),
      ("Île comptoir face à Dakar :", "Gorée", "Carabane", "Ngor", "Madeleines", "Comptoir."),
      ("Un comptoir est", "un établissement de commerce", "une école", "une mosquée", "un champ", "Définition."),
      ("Produit acheté par les Européens au XVIIe siècle :", "gomme arabique", "pétrole", "cacao", "smartphones", "Commerce.")])]),
  d("histoire", "Histoire", 2, [
    ("La traite négrière", "Des millions d'Africains sont déportés vers l'Amérique.", [
      ("Nom du trajet Afrique → Amérique :", "« passage du milieu »", "route de la soie", "transsaharien", "route des épices", "Traversée."),
      ("Destination des captifs :", "plantations d'Amérique", "usines d'Europe", "mines d'Asie", "Sahara", "Travail forcé."),
      ("Conséquence pour l'Afrique :", "perte de population et de forces vives", "enrichissement général", "croissance démographique", "aucune", "Saignée."),
      ("Abolition dans les colonies françaises :", "1848", "1815", "1960", "1794 seulement", "Schœlcher.")]),
    ("La Révolution française", "Les révolutionnaires proclament des droits nouveaux.", [
      ("Abolition des privilèges :", "nuit du 4 août 1789", "14 juillet 1789", "1792", "1848", "Fin de l'Ancien Régime."),
      ("Devise de la République française :", "Liberté, Égalité, Fraternité", "Un Peuple, Un But, Une Foi", "Travail, Famille, Patrie", "Paix et unité", "Devise."),
      ("Roi exécuté en 1793 :", "Louis XVI", "Louis XIV", "Napoléon", "Charlemagne", "Révolution."),
      ("Les cahiers de doléances de Saint-Louis (1789) montrent", "que les colonies suivaient les événements", "que rien n'était connu", "que Saint-Louis était anglaise", "qu'il n'y avait pas de commerce", "Document.")]),
    ("La révolution industrielle", "Au XIXe siècle, les usines se multiplient.", [
      ("Énergie de la machine à vapeur :", "charbon", "pétrole", "soleil", "vent", "Combustion."),
      ("Nouveau moyen de transport :", "chemin de fer", "avion", "voiture électrique", "fusée", "Rail."),
      ("Conditions des ouvriers :", "longues journées, salaires bas", "4 h par jour", "vacances longues", "aucun travail", "Misère ouvrière."),
      ("Besoin créé :", "matières premières des colonies", "moins de commerce", "fermeture des ports", "fin des usines", "Impérialisme.")])]),
  d("histoire", "Histoire", 3, [
    ("La pénétration coloniale", "Après 1850, la France conquiert l'intérieur du Sénégal.", [
      ("Gouverneur à partir de 1854 :", "Faidherbe", "Blaise Diagne", "Lamine Guèye", "Roume", "Conquête."),
      ("Arme de la conquête :", "les tirailleurs et les canons", "les livres", "les pirogues de pêche", "les lettres", "Militaire."),
      ("Chemin de fer Dakar – Saint-Louis :", "1885", "1960", "1923", "1848", "Arachide."),
      ("Les habitants des Quatre communes avaient", "des droits de citoyens français", "aucun droit", "le statut d'indigène", "un roi", "Statut.")]),
    ("Les résistances armées", "Plusieurs souverains combattent les Français.", [
      ("Lat Dior meurt à", "Dékheulé (1886)", "Kirina", "Tondibi", "Thiaroye", "Bataille."),
      ("El Hadj Omar Tall s'oppose aux Français à", "Médine (1857)", "Gorée", "Dakar", "Ziguinchor", "Siège."),
      ("Maba Diakhou Bâ résiste dans", "le Rip (Saloum)", "le Fouta Djalon", "le Cap-Vert", "le Walo", "Région."),
      ("Alboury Ndiaye était roi du", "Djolof", "Cayor", "Sine", "Baol", "Bourba.")]),
    ("Les résistances pacifiques", "Certains résistent sans armes.", [
      ("Cheikh Ahmadou Bamba est exilé au", "Gabon", "Maroc", "Mali", "Cap-Vert", "1895."),
      ("Confrérie fondée par Cheikh Ahmadou Bamba :", "mouridiyya", "tidjaniyya", "qadiriyya", "layène", "Touba."),
      ("Aline Sitoé Diatta s'oppose", "aux réquisitions de riz en Casamance", "au chemin de fer", "aux Portugais en 1444", "à l'indépendance", "Seconde Guerre mondiale."),
      ("Aline Sitoé meurt en exil à", "Tombouctou", "Gorée", "Paris", "Dakar", "1944.")])]),
  d("geo", "Géographie", 1, [
    ("La population mondiale", "La population mondiale dépasse 8 milliards.", [
      ("Continent le plus peuplé :", "Asie", "Afrique", "Europe", "Amérique", "Plus de 4,5 milliards."),
      ("Zone peu peuplée :", "Sahara", "Asie du Sud", "Europe de l'Ouest", "Nigeria du Sud", "Désert."),
      ("Densité = population ÷", "superficie", "naissances", "âge", "PIB", "Formule."),
      ("Forte croissance :", "Afrique subsaharienne", "Japon", "Europe de l'Est", "Russie", "Natalité élevée.")]),
    ("Natalité et mortalité", "Pays A : natalité 35 ‰, mortalité 8 ‰.", [
      ("Accroissement naturel :", "27 ‰", "43 ‰", "4,3 %", "8 ‰", "35 − 8."),
      ("En pourcentage :", "2,7 %", "27 %", "0,27 %", "4,3 %", "27 ‰ = 2,7 %."),
      ("Ce pays est probablement", "en développement", "très vieillissant", "sans enfants", "en baisse de population", "Natalité forte."),
      ("Mortalité infantile :", "décès d'enfants de moins d'1 an", "décès de personnes âgées", "naissances", "migrations", "Définition.")]),
    ("Les migrations", "Des Sénégalais partent vers l'Europe, l'Amérique et d'autres pays d'Afrique.", [
      ("Diaspora :", "ensemble des émigrés d'un pays", "un pays", "une ville", "un fleuve", "Définition."),
      ("Argent envoyé au pays :", "transferts", "impôts", "amendes", "dettes", "Remises."),
      ("Migration la plus fréquente pour les Africains :", "vers d'autres pays africains", "vers l'Antarctique", "vers la Lune", "vers l'Océanie seulement", "Migrations intra-africaines."),
      ("Exode rural :", "campagne → ville", "ville → campagne", "pays → pays", "mer → terre", "Interne.")])]),
  d("geo", "Géographie", 2, [
    ("Le développement", "Pays X : IDH 0,52 ; pays Y : IDH 0,94.", [
      ("Pays le plus développé :", "Y", "X", "égalité", "aucun", "Proche de 1."),
      ("Composantes de l'IDH :", "santé, éducation, revenu", "superficie, climat, relief", "armée, police, routes", "football, musique, cinéma", "Indicateur."),
      ("Le Sénégal a un IDH", "faible à moyen", "le plus élevé du monde", "égal à 1", "négatif", "Environ 0,5."),
      ("Inégalité Nord-Sud :", "écart de richesse entre pays riches et pauvres", "écart de température", "différence de langue", "aucune", "Définition.")]),
    ("Pauvreté et solutions", "On cherche à réduire la pauvreté.", [
      ("Solution par l'éducation :", "scolariser tous les enfants", "fermer les écoles", "réduire les enseignants", "rien", "Capital humain."),
      ("Solution par la santé :", "vaccination et centres de santé", "supprimer les hôpitaux", "interdire les médicaments", "rien", "Santé."),
      ("Les ODD sont fixés par", "l'ONU", "la FIFA", "une seule entreprise", "le maire", "Objectifs de développement durable."),
      ("Échéance des ODD :", "2030", "2000", "2100", "1960", "Agenda 2030.")]),
    ("Les grandes puissances", "On compare les États-Unis, la Chine et l'Union européenne.", [
      ("Puissance asiatique :", "Chine", "Brésil", "Canada", "Mexique", "Asie."),
      ("Monnaie des États-Unis :", "dollar", "euro", "yuan", "franc CFA", "Monnaie."),
      ("Siège des institutions européennes :", "Bruxelles", "Dakar", "New York", "Pékin", "Belgique."),
      ("Atout de la Chine :", "population et industrie", "désert vide", "absence d'usines", "pas de commerce", "Atelier du monde.")])]),
  d("geo", "Géographie", 3, [
    ("Les zones climatiques", "La Terre est divisée en zones selon la latitude.", [
      ("Zone chaude :", "entre les tropiques", "aux pôles", "en Europe du Nord", "en Sibérie", "Intertropicale."),
      ("Zone froide :", "autour des pôles", "à l'équateur", "au Sahel", "en Casamance", "Polaire."),
      ("Zone tempérée :", "entre tropiques et cercles polaires", "à l'équateur seul", "aux pôles", "dans le Sahara", "Moyennes latitudes."),
      ("Le Sénégal est dans la zone", "chaude", "froide", "tempérée", "polaire", "≈ 12°-16° N.")]),
    ("Milieux et activités", "On relie milieux et activités humaines.", [
      ("Activité du désert :", "élevage nomade", "riziculture inondée", "pêche en mer", "culture du cacao", "Adaptation."),
      ("Activité en forêt équatoriale :", "exploitation du bois", "élevage de rennes", "ski", "culture du blé d'hiver", "Ressource."),
      ("Activité des régions polaires :", "pêche et chasse (Inuits)", "culture de l'arachide", "riz", "coton", "Adaptation."),
      ("En climat tempéré, on cultive", "blé et vigne", "cacao", "manioc seulement", "palmier à huile", "Agriculture.")]),
    ("Protéger les milieux", "La mangrove du Saloum recule.", [
      ("Rôle de la mangrove :", "abri pour poissons et protection des côtes", "aucun", "polluer", "produire du pétrole", "Écosystème."),
      ("Cause du recul :", "coupe du bois et salinisation", "trop de pluie", "neige", "volcans", "Menaces."),
      ("Action locale :", "replanter des palétuviers", "brûler la mangrove", "construire des routes dedans", "y jeter les ordures", "Reboisement."),
      ("Arbre de la mangrove :", "palétuvier", "baobab", "sapin", "rônier", "Racines échasses.")])]),
  d("anglais", "Anglais", 1, [
    ("Present perfect", "« I have lived in Kaolack since 2018. I have visited Saint-Louis twice. »", [
      ("Since when has he lived in Kaolack?", "since 2018", "for 2018", "in 2018 only", "never", "since."),
      ("How many times has he visited Saint-Louis?", "twice", "once", "never", "three times", "twice = deux fois."),
      ("I have … (eat) thieboudienne.", "eaten", "ate", "eat", "eated", "Participe."),
      ("She has worked here … five years.", "for", "since", "ago", "during", "Durée.")]),
    ("Past simple vs past continuous", "Choose.", [
      ("While I … (walk), I saw a snake.", "was walking", "walked", "am walking", "walk", "Action en cours."),
      ("When the teacher arrived, we … (sing).", "were singing", "sang", "are singing", "sing", "Fond du récit."),
      ("She … (break) her arm last week.", "broke", "breaked", "was breaking", "has broken", "Last week."),
      ("They … (not / play) when it rained.", "weren't playing", "didn't playing", "wasn't playing", "don't play", "Pluriel.")]),
    ("Reading", "« Last Saturday, Bineta was reading when the lights went out. She lit a candle and finished her book. »", [
      ("What was Bineta doing?", "She was reading.", "She was cooking.", "She was sleeping.", "She was dancing.", "Texte."),
      ("What happened?", "The lights went out.", "It rained.", "The book fell.", "Her friend came.", "Texte."),
      ("« lit » is the past of", "light", "lie", "let", "leave", "Irrégulier."),
      ("Did she finish her book?", "Yes, she did.", "No, she didn't.", "Yes, she was.", "No, she wasn't.", "Texte.")])]),
  d("anglais", "Anglais", 2, [
    ("Conditional type 1", "Complete.", [
      ("If it … (rain), we will stay home.", "rains", "will rain", "rained", "raining", "If + présent."),
      ("If you study, you … (succeed).", "will succeed", "succeed", "succeeded", "would succeeded", "will."),
      ("She will be angry if you … late.", "are", "will be", "were", "be", "Présent après if."),
      ("If he doesn't hurry, he … (miss) the bus.", "will miss", "misses", "missed", "would missed", "Type 1.")]),
    ("Must / mustn't", "School rules.", [
      ("You … smoke in class. (interdit)", "mustn't", "must", "have to", "can", "Interdiction."),
      ("You … wear a uniform. (obligatoire)", "must", "mustn't", "can't", "don't have to", "Obligation."),
      ("You … bring food, it's not necessary.", "don't have to", "mustn't", "must", "have", "Pas obligatoire."),
      ("Pupils … be on time.", "must", "musts", "must to", "musting", "Pas de -s, pas de to.")]),
    ("Superlatives", "Senegal facts.", [
      ("Dakar is … city in Senegal.", "the biggest", "the bigger", "biggest", "the most big", "Superlatif."),
      ("The Senegal River is … river in the country.", "the longest", "the longer", "longest than", "the most long", "Superlatif."),
      ("This is … day of my life!", "the best", "the better", "the goodest", "best", "Irrégulier."),
      ("It was … film I've ever seen.", "the worst", "the baddest", "the worse", "worst than", "Irrégulier.")])]),
  d("anglais", "Anglais", 3, [
    ("Relative pronouns", "Choose who, which or where.", [
      ("The man … sells fish is my uncle.", "who", "which", "where", "what", "Personne."),
      ("The bag … I bought is blue.", "which", "who", "where", "whom", "Chose."),
      ("This is the school … I study.", "where", "who", "which", "whose", "Lieu."),
      ("The girl … father is a doctor.", "whose", "who", "which", "where", "Possession.")]),
    ("Question tags", "Complete.", [
      ("You are tired, … ?", "aren't you", "are you", "don't you", "isn't you", "Tag négatif."),
      ("He can swim, … ?", "can't he", "can he", "doesn't he", "isn't he", "Modal."),
      ("They didn't come, … ?", "did they", "didn't they", "do they", "were they", "Tag positif."),
      ("She likes rice, … ?", "doesn't she", "does she", "isn't she", "don't she", "Présent.")]),
    ("Passive voice", "Change to the passive.", [
      ("They grow rice in Casamance. →", "Rice is grown in Casamance.", "Rice grows in Casamance by them.", "Rice was grow in Casamance.", "Rice is growing Casamance.", "be + participe."),
      ("Participe de « build » :", "built", "builded", "build", "building", "Irrégulier."),
      ("The bridge … built in 1897.", "was", "is", "were", "has", "Passé."),
      ("English … spoken in Gambia.", "is", "are", "was being always", "has", "Présent passif.")])]),
  d("espagnol", "Espagnol (LV2)", 1, [
    ("Presentarse", "« Hola, me llamo Pape. Soy de Thiès. Tengo catorce años. »", [
      ("¿Cómo se llama?", "Pape", "Thiès", "catorce", "Hola", "Texte."),
      ("¿De dónde es?", "de Thiès", "de Dakar", "de Madrid", "de Pape", "Origine."),
      ("¿Cuántos años tiene?", "14", "4", "40", "13", "catorce."),
      ("« Soy » vient de", "ser", "estar", "tener", "ir", "Être.")]),
    ("Los números", "Écris en chiffres.", [
      ("diecisiete :", "17", "7", "70", "16", "Nombre."),
      ("treinta y dos :", "32", "23", "302", "13", "Nombre."),
      ("cincuenta :", "50", "15", "5", "500", "Nombre."),
      ("cien :", "100", "1 000", "10", "110", "Nombre.")]),
    ("La hora", "¿Qué hora es?", [
      ("Son las tres y cuarto :", "3 h 15", "3 h 45", "3 h 30", "4 h 15", "y cuarto."),
      ("Es la una y media :", "1 h 30", "1 h 15", "12 h 30", "2 h 30", "y media."),
      ("Son las ocho menos cuarto :", "7 h 45", "8 h 15", "8 h 45", "7 h 15", "menos = moins."),
      ("Jour après « lunes » :", "martes", "jueves", "domingo", "viernes", "Semaine.")])]),
  d("espagnol", "Espagnol (LV2)", 2, [
    ("La familia", "« Mi familia es grande. Tengo tres hermanas y un hermano. Mis abuelos viven en el pueblo. »", [
      ("« hermanas » :", "sœurs", "frères", "cousines", "tantes", "Famille."),
      ("« abuelos » :", "grands-parents", "oncles", "parents", "enfants", "Famille."),
      ("« pueblo » :", "village", "peuple seulement", "ville", "pays", "Contexte."),
      ("« Mis » :", "mes", "ma", "mon", "tes", "Possessif pluriel.")]),
    ("Tener y los posesivos", "Complète.", [
      ("Yo … dos perros.", "tengo", "tiene", "tienes", "tenemos", "Tener."),
      ("Nosotros … una casa.", "tenemos", "tienen", "tengo", "tenéis", "Tener."),
      ("… casa (à nous) :", "Nuestra", "Nuestro", "Mi", "Su", "Féminin."),
      ("… libro (à toi) :", "Tu", "Su", "Mi", "Vuestro", "Possessif.")]),
    ("La casa", "« En mi casa hay una cocina, un salón y tres dormitorios. »", [
      ("« cocina » :", "cuisine", "salon", "chambre", "jardin", "Pièce."),
      ("« dormitorios » :", "chambres", "toilettes", "salons", "cours", "Pièce."),
      ("« hay » :", "il y a", "il est", "il a", "il va", "Haber."),
      ("Nombre de chambres :", "3", "1", "2", "4", "tres.")])]),
  d("espagnol", "Espagnol (LV2)", 3, [
    ("El presente regular", "Conjugue.", [
      ("Ella (cantar) bien.", "canta", "canto", "cantan", "cantas", "-a."),
      ("Nosotros (aprender) español.", "aprendemos", "aprendimos", "aprenden", "aprendamos", "-emos."),
      ("Ellos (escribir) cartas.", "escriben", "escribian", "escribimos", "escribe", "-en."),
      ("Tú (vivir) en Dakar.", "vives", "vivas", "vivo", "viven", "-es.")]),
    ("Mi día", "« Por la mañana, desayuno a las siete. Luego, voy al colegio en autobús. »", [
      ("« desayuno » :", "je prends le petit-déjeuner", "je dîne", "je dors", "je déjeune à midi", "Desayunar."),
      ("« voy » vient de", "ir", "ver", "venir", "volver", "Irrégulier."),
      ("Moyen de transport :", "autobús", "coche", "tren", "bicicleta", "Texte."),
      ("« Por la mañana » :", "le matin", "le soir", "la nuit", "à midi", "Moment.")]),
    ("Saludos y cortesía", "Choisis.", [
      ("« Merci beaucoup » :", "Muchas gracias", "De nada", "Por favor", "Perdón", "Politesse."),
      ("« De rien » :", "De nada", "Gracias", "Hola", "Adiós", "Politesse."),
      ("« Bonsoir » :", "Buenas noches (ou buenas tardes)", "Buenos días", "Hasta luego", "Gracias", "Salutation."),
      ("« À bientôt » :", "Hasta pronto", "Buenos días", "Por favor", "Lo siento", "Au revoir.")])]),
])
