from sujets_dev_common import D, pack, TRIM
L = "6e"
def d(s, name, n, exos): return D(f"dev-6e-{s}-{n}", L, name, n, exos, label=TRIM[n])

ANNALES_X, GUIDED_X = pack([
  # ---------------- Mathématiques
  d("maths", "Mathématiques", 1, [
    ("Nombres décimaux", "On donne les nombres 12,07 ; 12,7 ; 12,075 et 1,27.", [
      ("Le plus grand nombre :", "12,7", "12,075", "12,07", "1,27", "12,700 > 12,075 > 12,070."),
      ("12,07 + 1,27 =", "13,34", "13,97", "24,77", "12,34", "On aligne les virgules."),
      ("12,7 × 100 =", "1 270", "127", "12,700", "0,127", "Virgule de 2 rangs vers la droite."),
      ("Arrondi de 12,075 au centième :", "12,08", "12,07", "12,1", "12", "Le chiffre des millièmes est 5 : on arrondit au-dessus.")]),
    ("Divisibilité", "Le directeur veut ranger 126 élèves en rangées égales.", [
      ("126 est divisible par 2 car", "il se termine par 6", "1 + 2 + 6 = 9", "il se termine par 5", "il est impair", "Chiffre des unités pair."),
      ("126 est divisible par 9 car", "1 + 2 + 6 = 9", "il est pair", "il se termine par 6", "126 > 9", "Somme des chiffres divisible par 9."),
      ("Rangées de 9 élèves : nombre de rangées", "14", "12", "16", "13", "126 ÷ 9."),
      ("126 est-il divisible par 5 ?", "non", "oui", "seulement par 10", "on ne sait pas", "Il ne se termine ni par 0 ni par 5.")]),
    ("Division euclidienne", "Une coopérative a 250 mangues à mettre dans des cageots de 12.", [
      ("Nombre de cageots pleins :", "20", "21", "25", "12", "12 × 20 = 240."),
      ("Mangues restantes :", "10", "2", "0", "12", "250 − 240."),
      ("Égalité de la division :", "250 = 12 × 20 + 10", "250 = 12 × 21 − 2", "250 = 20 × 10 + 12", "250 = 12 + 20 × 10", "a = b × q + r avec r < b."),
      ("Cageots nécessaires pour tout ranger :", "21", "20", "22", "10", "Il faut un cageot de plus pour les 10 restantes.")])]),
  d("maths", "Mathématiques", 2, [
    ("Fractions", "Dans une classe de 45 élèves, 2/5 viennent à pied et 1/3 viennent en car.", [
      ("Élèves à pied :", "18", "15", "9", "20", "45 ÷ 5 × 2."),
      ("Élèves en car :", "15", "18", "3", "30", "45 ÷ 3."),
      ("Autres élèves :", "12", "15", "27", "30", "45 − 18 − 15."),
      ("Fraction des autres élèves :", "4/15", "1/3", "12/30", "3/4", "12/45 = 4/15.")]),
    ("Proportionnalité", "Un tailleur utilise 3 m de tissu pour 2 boubous.", [
      ("Tissu pour 4 boubous :", "6 m", "5 m", "8 m", "12 m", "Deux fois plus."),
      ("Tissu pour 1 boubou :", "1,5 m", "1 m", "2 m", "3 m", "3 ÷ 2."),
      ("Tissu pour 10 boubous :", "15 m", "30 m", "13 m", "20 m", "1,5 × 10."),
      ("Boubous avec 12 m :", "8", "6", "4", "10", "12 ÷ 1,5.")]),
    ("Mesures", "Un marathon local part à 7 h 50 et le premier arrive à 10 h 25.", [
      ("Durée de course du premier :", "2 h 35 min", "3 h 35 min", "2 h 25 min", "3 h 25 min", "7 h 50 → 9 h 50 = 2 h, puis 35 min."),
      ("42 km en m :", "42 000 m", "4 200 m", "420 m", "420 000 m", "× 1 000."),
      ("Une bouteille de 1,5 L en cL :", "150 cL", "15 cL", "1 500 cL", "0,15 cL", "× 100."),
      ("Le dernier arrive 1 h 50 min après le premier, à :", "12 h 15", "12 h 75", "11 h 15", "12 h 05", "10 h 25 + 1 h 50 = 11 h 75 = 12 h 15.")])]),
  d("maths", "Mathématiques", 3, [
    ("Angles et triangles", "Dans le triangle MNP, l'angle M mesure 90° et l'angle N mesure 35°.", [
      ("Le triangle MNP est", "rectangle en M", "équilatéral", "isocèle en N", "obtus", "Angle droit en M."),
      ("Angle P :", "55°", "65°", "35°", "90°", "180 − 90 − 35."),
      ("Un angle de 35° est", "aigu", "obtus", "droit", "plat", "Moins de 90°."),
      ("Instrument pour vérifier l'angle droit :", "équerre", "compas", "rapporteur seul", "règle graduée seule", "Angle droit.")]),
    ("Périmètres et aires", "Un terrain de basket rectangulaire mesure 28 m sur 15 m.", [
      ("Périmètre :", "86 m", "43 m", "420 m", "56 m", "2 × (28 + 15)."),
      ("Aire :", "420 m²", "86 m²", "43 m²", "210 m²", "28 × 15."),
      ("Un carré de 20 m de côté a une aire de", "400 m²", "80 m²", "40 m²", "200 m²", "20 × 20."),
      ("Le terrain de basket est-il plus grand que ce carré ?", "oui, de 20 m²", "non", "égal", "oui, de 200 m²", "420 − 400.")]),
    ("Le cercle", "Une roue de vélo a un diamètre de 60 cm (π ≈ 3,14).", [
      ("Rayon :", "30 cm", "60 cm", "120 cm", "15 cm", "Diamètre ÷ 2."),
      ("Périmètre de la roue :", "188,4 cm", "94,2 cm", "2 826 cm", "60 cm", "π × 60."),
      ("Distance parcourue en 10 tours :", "1 884 cm", "188,4 cm", "600 cm", "18 840 cm", "188,4 × 10."),
      ("1 884 cm en m :", "18,84 m", "188,4 m", "1,884 m", "0,1884 m", "÷ 100.")])]),
  # ---------------- Français
  d("francais", "Français", 1, [
    ("Classes de mots", "« Ce matin, la jeune vendeuse installe ses beaux paniers au marché. »", [
      ("Nature de « vendeuse » :", "nom commun", "adjectif", "verbe", "déterminant", "Désigne une personne."),
      ("Nature de « ses » :", "déterminant possessif", "pronom", "adjectif qualificatif", "nom", "Devant paniers."),
      ("Nature de « beaux » :", "adjectif qualificatif", "nom", "adverbe", "déterminant", "Qualifie paniers."),
      ("Nature de « installe » :", "verbe", "nom", "adjectif", "préposition", "Action conjuguée.")]),
    ("Fonctions", "« Mon grand-père raconte une histoire aux enfants. »", [
      ("Sujet :", "mon grand-père", "une histoire", "aux enfants", "raconte", "Qui raconte ?"),
      ("COD :", "une histoire", "aux enfants", "mon grand-père", "il n'y en a pas", "Raconte quoi ?"),
      ("« aux enfants » répond à la question", "à qui ?", "quoi ?", "où ?", "quand ?", "Destinataire."),
      ("Si le sujet devient « mes grands-parents », le verbe devient", "racontent", "raconte", "racontes", "racontons", "Pluriel.")]),
    ("Conjugaison au présent", "Conjugue au présent de l'indicatif.", [
      ("Nous (manger) du thiéboudiène.", "mangeons", "mangons", "mangeont", "mangez", "On garde le e."),
      ("Tu (finir) ton devoir.", "finis", "finit", "finissez", "finie", "2e groupe."),
      ("Ils (faire) du sport.", "font", "faisent", "fons", "faient", "Irrégulier."),
      ("Vous (dire) la vérité.", "dites", "disez", "dises", "disons", "Irrégulier.")])]),
  d("francais", "Français", 2, [
    ("Imparfait et futur", "Mets le verbe au temps demandé.", [
      ("Imparfait : Autrefois, nous (aller) au puits.", "allions", "allons", "irons", "allâmes", "-ions."),
      ("Futur : Demain, il (venir).", "viendra", "venira", "vient", "venait", "Radical viendr-."),
      ("Imparfait : Vous (être) fatigués.", "étiez", "êtes", "serez", "étaient", "Être."),
      ("Futur : Je (avoir) douze ans.", "aurai", "aurais", "avais", "ai", "Futur, pas conditionnel.")]),
    ("Orthographe", "Choisis la bonne orthographe.", [
      ("Des (journal) :", "journaux", "journals", "journeaux", "journales", "-al → -aux."),
      ("Des (genou) :", "genoux", "genous", "genouxs", "genoues", "Exception."),
      ("Une robe (neuf) :", "neuve", "neufe", "neuf", "neuves", "-f → -ve."),
      ("Les enfants (jouer) dehors.", "jouent", "joue", "jouez", "jouons", "Sujet pluriel.")]),
    ("Vocabulaire", "Travaille sur le mot « courageux ».", [
      ("Synonyme :", "brave", "peureux", "lent", "triste", "Sens proche."),
      ("Contraire :", "peureux", "brave", "fort", "hardi", "Sens opposé."),
      ("Nom de la même famille :", "courage", "cour", "courir", "couronne", "Radical courag-."),
      ("Dans le dictionnaire, « courage » vient", "avant « courageux »", "après « courageux »", "au même endroit", "à la lettre D", "Ordre alphabétique.")])]),
  d("francais", "Français", 3, [
    ("Le conte", "« Il était une fois un roi qui avait trois fils. Le plus jeune, malin, partit chercher l'eau magique. Après bien des épreuves, il revint et devint roi. »", [
      ("Formule d'ouverture :", "Il était une fois", "Après bien des épreuves", "il revint", "devint roi", "Début du conte."),
      ("Héros :", "le plus jeune fils", "le roi", "les deux aînés", "l'eau", "Personnage principal."),
      ("Objet de la quête :", "l'eau magique", "un trésor d'or", "une princesse", "un cheval", "Ce qu'il cherche."),
      ("Situation finale :", "il devient roi", "il meurt", "il se perd", "il reste pauvre", "Fin heureuse.")]),
    ("Types de phrases", "Identifie et transforme.", [
      ("« Range ta chambre. » :", "injonctive", "interrogative", "déclarative", "exclamative", "Ordre."),
      ("« Que la mer est belle ! » :", "exclamative", "interrogative", "injonctive", "négative", "Émotion."),
      ("Forme interrogative de « Tu viens. » :", "Viens-tu ?", "Tu viens.", "Viens !", "Ne viens pas.", "Inversion."),
      ("Forme négative de « Il pleut toujours. » :", "Il ne pleut jamais.", "Il ne pleut toujours.", "Il pleut pas.", "Il ne pleut pas toujours jamais.", "toujours → jamais.")]),
    ("Expression écrite", "Sujet : « Raconte une fête de Tabaski dans ta famille. »", [
      ("Type de texte demandé :", "récit", "argumentation", "poème", "dialogue de théâtre", "Raconte."),
      ("Temps principal du récit au passé :", "imparfait et passé simple (ou passé composé)", "futur", "impératif", "conditionnel", "Récit."),
      ("Bon ordre du récit :", "préparatifs, prière, repas, visites", "visites, repas, prière, préparatifs", "repas, préparatifs, prière", "au hasard", "Chronologie."),
      ("Avant de rendre la copie :", "relire et corriger", "compter les mots", "rien", "recopier le sujet", "Relecture.")])]),
  # ---------------- SVT
  d("svt", "SVT", 1, [
    ("Le vivant", "On observe un baobab, un caillou, une poule et une moisissure sur du pain.", [
      ("Éléments vivants :", "baobab, poule, moisissure", "caillou et poule", "caillou seul", "baobab seulement", "Ils naissent, se nourrissent, se reproduisent."),
      ("La moisissure est", "un champignon", "un animal", "une roche", "une plante verte", "Règne des champignons."),
      ("Caractère commun aux êtres vivants :", "ils respirent", "ils volent", "ils sont verts", "ils ont des pattes", "Respiration."),
      ("Le caillou est non vivant car il", "ne se nourrit pas et ne se reproduit pas", "est dur", "est gris", "est petit", "Critères.")]),
    ("Nutrition des plantes", "On arrose une plante A avec de l'eau pure et une plante B avec de l'eau contenant des sels minéraux.", [
      ("Plante qui pousse le mieux :", "B", "A", "les deux pareil", "aucune", "Les sels minéraux nourrissent."),
      ("La plante absorbe l'eau par", "les poils absorbants des racines", "les fleurs", "les fruits", "l'écorce", "Absorption."),
      ("La sève brute monte", "des racines vers les feuilles", "des feuilles vers les racines", "du sol vers le ciel", "nulle part", "Trajet."),
      ("Engrais naturel :", "fumier", "plastique", "sable", "ciment", "Matière organique.")]),
    ("Germination", "Une graine de haricot est mise à germer sur du coton humide.", [
      ("Première partie qui apparaît :", "racine", "fleur", "fruit", "feuille adulte", "Radicule."),
      ("Les cotylédons contiennent", "des réserves", "de l'eau de pluie", "du sable", "des graines", "Nourriture."),
      ("Le coton doit rester humide car il faut", "de l'eau", "du froid", "de l'obscurité totale", "du sel", "Condition."),
      ("Après plusieurs jours, la plantule", "verdit à la lumière", "devient blanche à la lumière", "disparaît", "devient une graine", "Chlorophylle.")])]),
  d("svt", "SVT", 2, [
    ("Régimes alimentaires", "On compare la vache, le chien et la poule.", [
      ("Régime de la vache :", "herbivore", "carnivore", "omnivore", "insectivore", "Herbe."),
      ("Régime de la poule :", "omnivore (graines, insectes)", "carnivore strict", "herbivore strict", "aucun", "Varié."),
      ("La vache n'a pas de", "canines développées", "molaires", "incisives inférieures", "dents", "Herbivore."),
      ("Chaîne alimentaire correcte :", "herbe → vache → homme", "homme → vache → herbe", "vache → herbe → homme", "herbe → homme → vache", "Qui mange qui.")]),
    ("Classification", "Classe : chèvre, tortue, crabe, pigeon, carpe.", [
      ("Animal à plumes :", "pigeon", "tortue", "carpe", "crabe", "Oiseau."),
      ("Animal à carapace et 10 pattes :", "crabe", "tortue", "pigeon", "chèvre", "Crustacé."),
      ("Reptile :", "tortue", "carpe", "chèvre", "pigeon", "Écailles, carapace."),
      ("Mammifère :", "chèvre", "carpe", "crabe", "pigeon", "Poils, allaite.")]),
    ("Métamorphoses", "Le moustique pond ses œufs dans l'eau stagnante.", [
      ("Ordre du développement :", "œuf, larve, nymphe, adulte", "adulte, larve, œuf", "nymphe, œuf, adulte", "larve, œuf, adulte", "Métamorphose complète."),
      ("La larve vit", "dans l'eau", "dans le sable sec", "dans l'air", "dans le sang", "Eau stagnante."),
      ("Moyen de lutte :", "vider les eaux stagnantes", "laisser les flaques", "élever plus de moustiques", "couper les arbres", "Prévention."),
      ("Maladie transmise par l'anophèle :", "paludisme", "rhume", "rougeole", "carie", "Santé.")])]),
  d("svt", "SVT", 3, [
    ("Le squelette", "On observe un squelette humain.", [
      ("Os qui protège le cerveau :", "crâne", "fémur", "tibia", "radius", "Boîte crânienne."),
      ("Os qui protègent cœur et poumons :", "côtes", "vertèbres seules", "phalanges", "rotule", "Cage thoracique."),
      ("Os le plus long :", "fémur", "crâne", "côte", "clavicule", "Cuisse."),
      ("Jonction entre deux os :", "articulation", "muscle", "tendon seul", "veine", "Mouvement.")]),
    ("Respiration et circulation", "Après une course, Awa compte 120 battements par minute contre 75 au repos.", [
      ("Augmentation du rythme :", "45 battements", "195", "75", "120", "120 − 75."),
      ("Organe qui bat :", "cœur", "poumon", "estomac", "foie", "Pompe."),
      ("Gaz apporté aux muscles :", "oxygène", "dioxyde de carbone", "azote", "fumée", "Respiration."),
      ("Le sang circule dans", "les vaisseaux sanguins", "les os", "l'estomac", "les nerfs", "Artères et veines.")]),
    ("Le sol", "On met de la terre de jardin dans un bocal d'eau, on agite et on laisse reposer.", [
      ("En bas du bocal se dépose", "les cailloux et le sable", "l'humus", "l'air", "rien", "Plus lourds."),
      ("En surface flotte", "l'humus (débris végétaux)", "les cailloux", "l'argile lourde", "le sable", "Léger."),
      ("Rôle des vers de terre :", "aérer et enrichir le sol", "polluer", "assécher", "aucun", "Décomposeurs."),
      ("Pratique qui appauvrit le sol :", "feux de brousse", "jachère", "compost", "reboisement", "Destruction.")])]),
  # ---------------- Histoire
  d("histoire", "Histoire", 1, [
    ("Les sources", "Un élève présente : un récit de griot, une hache en pierre, un manuscrit en arabe.", [
      ("Source orale :", "récit de griot", "hache", "manuscrit", "aucune", "Parole."),
      ("Source matérielle :", "hache en pierre", "récit", "manuscrit", "chanson", "Objet."),
      ("Source écrite :", "manuscrit", "hache", "récit de griot", "poterie", "Texte."),
      ("Un siècle dure", "100 ans", "10 ans", "1 000 ans", "50 ans", "Repère.")]),
    ("Repères chronologiques", "On place des dates sur une frise : 1960, 1444, 2000, 1895.", [
      ("Date la plus ancienne :", "1444", "1895", "1960", "2000", "Plus petit nombre."),
      ("1895 appartient au", "XIXe siècle", "XVIIIe siècle", "XXe siècle", "XVe siècle", "1801-1900."),
      ("1960 appartient au", "XXe siècle", "XIXe siècle", "XXIe siècle", "XVIe siècle", "1901-2000."),
      ("Écart entre 1960 et 2000 :", "40 ans", "60 ans", "20 ans", "400 ans", "2000 − 1960.")]),
    ("La préhistoire", "Les premiers hommes vivaient de chasse et de cueillette.", [
      ("Mode de vie au Paléolithique :", "nomade", "sédentaire en ville", "industriel", "agricole", "Déplacements."),
      ("Grande découverte :", "le feu", "l'électricité", "l'écriture d'abord", "le fer d'abord", "Paléolithique."),
      ("Au Néolithique, l'homme", "cultive et élève", "invente l'avion", "écrit des livres", "vit en ville moderne", "Révolution néolithique."),
      ("Fin de la préhistoire :", "invention de l'écriture", "invention du feu", "découverte de l'Amérique", "indépendance", "Repère.")])]),
  d("histoire", "Histoire", 2, [
    ("L'Égypte ancienne", "« L'Égypte est un don du Nil » (Hérodote).", [
      ("Sens de la phrase :", "sans le Nil, pas d'agriculture", "le Nil est un cadeau d'un roi", "l'Égypte est petite", "le Nil est salé", "Crue et limon."),
      ("Souverain égyptien :", "pharaon", "damel", "empereur romain", "sultan", "Titre."),
      ("Monument funéraire :", "pyramide", "mosquée", "château fort", "tata", "Tombeau."),
      ("Écriture :", "hiéroglyphes", "alphabet latin", "tifinagh", "ajami", "Sacrée.")]),
    ("La société égyptienne", "La société égyptienne était organisée en groupes.", [
      ("Au sommet :", "le pharaon", "les paysans", "les esclaves", "les scribes", "Pyramide sociale."),
      ("Ceux qui savent écrire :", "les scribes", "les paysans", "les soldats", "les pêcheurs", "Administration."),
      ("La majorité de la population :", "paysans", "prêtres", "pharaons", "scribes", "Agriculture."),
      ("Les Égyptiens croyaient en", "plusieurs dieux", "un seul dieu", "aucun dieu", "les ancêtres seulement", "Polythéisme.")]),
    ("Cheikh Anta Diop", "Cheikh Anta Diop a étudié les liens entre l'Égypte ancienne et l'Afrique noire.", [
      ("Nationalité :", "sénégalaise", "égyptienne", "française", "malienne", "Né à Thieytou."),
      ("Université qui porte son nom :", "Université de Dakar (UCAD)", "Université de Saint-Louis", "Sorbonne", "Université de Thiès", "UCAD."),
      ("Domaine :", "histoire et sciences", "football", "musique", "commerce", "Savant."),
      ("Idée principale :", "l'Égypte ancienne est africaine", "l'Égypte est européenne", "l'Afrique n'a pas d'histoire", "le Nil est en Asie", "Thèse.")])]),
  d("histoire", "Histoire", 3, [
    ("Les mégalithes", "Les cercles de pierres de Sine Ngayène et Wanar sont classés au patrimoine mondial.", [
      ("Mégalithe signifie", "grande pierre", "petite maison", "vieux village", "fleuve sacré", "Méga + lithos."),
      ("Fonction principale :", "monuments funéraires", "marchés", "terrains de lutte", "écoles", "Tombes."),
      ("Organisation qui les classe :", "UNESCO", "ONU-Femmes", "FIFA", "CEDEAO", "Patrimoine."),
      ("Zone :", "Sénégambie (centre du Sénégal et Gambie)", "Casamance seule", "Cap-Vert", "Fouta", "Localisation.")]),
    ("Les amas coquilliers", "Dans le delta du Saloum, d'anciens habitants ont laissé d'immenses tas de coquillages.", [
      ("Ces amas sont formés de", "restes de repas (coquillages)", "pierres taillées", "os de baleine", "briques", "Origine."),
      ("Ils montrent que les habitants", "pêchaient et ramassaient des coquillages", "fabriquaient des voitures", "cultivaient le blé", "vivaient dans le désert", "Mode de vie."),
      ("Certains amas contiennent aussi", "des tombes (tumulus)", "des avions", "des pièces d'euro", "du pétrole", "Sépultures."),
      ("Le delta du Saloum est classé", "patrimoine mondial de l'UNESCO", "parc d'attractions", "zone industrielle", "désert", "2011.")]),
    ("Protéger le patrimoine", "Des visiteurs gravent leur nom sur les pierres de Sine Ngayène.", [
      ("Ce geste", "abîme le patrimoine", "protège les pierres", "est conseillé", "n'a aucun effet", "Dégradation."),
      ("Bonne attitude :", "regarder sans toucher ni graver", "emporter une pierre", "peindre les pierres", "construire dessus", "Respect."),
      ("Le patrimoine appartient", "à tous, y compris aux générations futures", "à un seul village", "aux touristes", "à personne", "Bien commun."),
      ("Musée à Dakar sur les civilisations noires :", "Musée des civilisations noires", "Louvre", "Musée du Caire", "British Museum", "Ouvert en 2018.")])]),
  # ---------------- Géographie
  d("geo", "Géographie", 1, [
    ("Le système solaire", "Le Soleil est une étoile autour de laquelle tournent 8 planètes.", [
      ("Le Soleil est", "une étoile", "une planète", "un satellite", "une comète", "Il produit sa lumière."),
      ("Planète la plus proche du Soleil :", "Mercure", "Terre", "Mars", "Neptune", "Ordre."),
      ("Planète où nous vivons :", "Terre", "Vénus", "Jupiter", "Saturne", "3e planète."),
      ("Plus grande planète :", "Jupiter", "Terre", "Mercure", "Mars", "Géante gazeuse.")]),
    ("Les mouvements de la Terre", "La Terre tourne sur elle-même en 24 h et autour du Soleil en 365 jours 1/4.", [
      ("Le jour et la nuit sont dus à", "la rotation", "la révolution", "la Lune", "les nuages", "Sur elle-même."),
      ("L'année bissextile compte", "366 jours", "365 jours", "364 jours", "360 jours", "Le quart de jour en plus."),
      ("Le Soleil se lève à", "l'est", "l'ouest", "le nord", "le sud", "Rotation d'ouest en est."),
      ("Quand il fait jour à Dakar, il fait nuit", "de l'autre côté de la Terre", "partout", "nulle part", "seulement en Afrique", "Hémisphère éclairé.")]),
    ("Les coordonnées", "Saint-Louis : environ 16° Nord et 16° Ouest.", [
      ("Latitude de Saint-Louis :", "16° Nord", "16° Ouest", "0°", "90° Nord", "Par rapport à l'équateur."),
      ("Longitude de Saint-Louis :", "16° Ouest", "16° Nord", "0°", "180°", "Par rapport à Greenwich."),
      ("Les parallèles sont", "des cercles parallèles à l'équateur", "des demi-cercles d'un pôle à l'autre", "des fleuves", "des routes", "Définition."),
      ("Les méridiens relient", "le pôle Nord au pôle Sud", "deux villes", "l'équateur aux tropiques", "les océans", "Définition.")])]),
  d("geo", "Géographie", 2, [
    ("L'échelle", "Sur une carte au 1/500 000, Kaolack et Fatick sont à 9 cm l'une de l'autre.", [
      ("1 cm représente", "5 km", "500 m", "50 km", "500 km", "500 000 cm = 5 km."),
      ("Distance réelle :", "45 km", "4,5 km", "450 km", "9 km", "9 × 5."),
      ("Plus l'échelle est grande, plus la carte est", "détaillée", "floue", "colorée", "petite", "Lecture."),
      ("Échelle graphique :", "un segment gradué", "une fraction", "une couleur", "un titre", "Type.")]),
    ("La légende", "Une carte du Sénégal montre des points rouges, des traits bleus et des zones vertes.", [
      ("Les traits bleus représentent souvent", "les cours d'eau", "les routes", "les frontières", "les villes", "Convention."),
      ("Les points rouges peuvent représenter", "les villes", "les lacs", "les forêts", "le désert", "Lecture."),
      ("Les zones vertes peuvent représenter", "la végétation", "la mer", "les villes", "les routes", "Couleur."),
      ("Sans légende, on", "ne peut pas comprendre les symboles", "comprend tout", "voit mieux", "connaît la date", "Utilité.")]),
    ("Continents et océans", "On travaille sur le planisphère.", [
      ("Nombre de continents (souvent retenu) :", "6 (dont l'Antarctique)", "3", "10", "2", "Afrique, Amérique, Antarctique, Asie, Europe, Océanie."),
      ("Océan entre l'Afrique et l'Amérique :", "Atlantique", "Pacifique", "Indien", "Arctique", "Ouest de l'Afrique."),
      ("Océan à l'est de l'Afrique :", "Indien", "Atlantique", "Pacifique", "Arctique", "Madagascar."),
      ("Mer au nord de l'Afrique :", "Méditerranée", "mer Rouge seule", "mer Noire", "mer du Nord", "Maghreb.")])]),
  d("geo", "Géographie", 3, [
    ("Situation du Sénégal", "Le Sénégal est en Afrique de l'Ouest, au bord de l'Atlantique.", [
      ("Capitale :", "Dakar", "Saint-Louis", "Thiès", "Touba", "Cap-Vert."),
      ("Pays au sud :", "Guinée et Guinée-Bissau", "Mauritanie", "Mali seul", "Maroc", "Frontières."),
      ("Pays à l'est :", "Mali", "Mauritanie", "Guinée-Bissau", "Cap-Vert", "Frontière."),
      ("Point le plus à l'ouest de l'Afrique :", "pointe des Almadies", "Gorée", "Saint-Louis", "Ziguinchor", "Presqu'île du Cap-Vert.")]),
    ("Le climat", "Graphique : à Dakar, il pleut de juillet à octobre, environ 450 mm par an.", [
      ("Saison des pluies :", "hivernage", "saison sèche", "harmattan", "printemps", "Juillet-octobre."),
      ("Mois sans pluie :", "janvier", "août", "septembre", "juillet", "Saison sèche."),
      ("Vent chaud et sec :", "harmattan", "alizé maritime", "mousson", "brise", "Sahara."),
      ("Vent qui apporte la pluie :", "mousson", "harmattan", "alizé continental", "sirocco", "Atlantique sud.")]),
    ("Les fleuves", "Le Sénégal est traversé par plusieurs fleuves.", [
      ("Fleuve au nord, frontière avec la Mauritanie :", "Sénégal", "Gambie", "Casamance", "Saloum", "Saint-Louis."),
      ("Fleuve qui traverse la Gambie :", "Gambie", "Sénégal", "Casamance", "Niger", "Nom."),
      ("Fleuve du sud :", "Casamance", "Sénégal", "Saloum", "Ferlo", "Ziguinchor."),
      ("Les fleuves servent à", "irriguer, pêcher, transporter", "rien", "produire du sable seulement", "faire du ski", "Usages.")])]),
  # ---------------- Anglais
  d("anglais", "Anglais", 1, [
    ("Reading", "« Hi! I'm Samba. I'm twelve. I've got a sister. Her name is Ndeye. She's nine. »", [
      ("How old is Samba?", "twelve", "nine", "two", "twenty", "Texte."),
      ("Ndeye is Samba's", "sister", "brother", "mother", "cousin", "Famille."),
      ("« I've got » =", "I have got", "I am got", "I give", "I go", "Contraction."),
      ("« She's nine » =", "She is nine", "She has nine", "She was nine", "She goes nine", "Contraction.")]),
    ("Grammar : to be", "Complete with am, is or are.", [
      ("I … a pupil.", "am", "is", "are", "be", "I am."),
      ("They … in class.", "are", "is", "am", "be", "Pluriel."),
      ("Fatou … happy.", "is", "are", "am", "be", "3e personne."),
      ("We … friends.", "are", "is", "am", "be", "Pluriel.")]),
    ("Vocabulary : numbers", "Write the numbers.", [
      ("13 :", "thirteen", "thirty", "three", "thirteenth", "Teen."),
      ("40 :", "forty", "fourty", "fourteen", "four", "Orthographe."),
      ("21 :", "twenty-one", "twelve-one", "one-twenty", "twenty-first", "Dizaine-unité."),
      ("100 :", "a hundred", "a thousand", "ten", "a million", "Centaine.")])]),
  d("anglais", "Anglais", 2, [
    ("Time", "What time is it?", [
      ("8:15 :", "a quarter past eight", "a quarter to eight", "half past eight", "eight to fifteen", "past = après."),
      ("6:30 :", "half past six", "half to six", "six half", "a quarter past six", "Et demie."),
      ("9:45 :", "a quarter to ten", "a quarter past nine", "half past nine", "nine to forty-five", "to = moins."),
      ("12:00 at night :", "midnight", "midday", "noon", "morning", "Minuit.")]),
    ("Days and months", "Answer the questions.", [
      ("First day of the school week :", "Monday", "Sunday", "Friday", "Saturday", "Lundi."),
      ("Month of Tabaski 2026 (approximately) :", "May", "December", "January", "October", "Fin mai 2026."),
      ("Last month of the year :", "December", "November", "January", "October", "Décembre."),
      ("Day before Friday :", "Thursday", "Saturday", "Wednesday", "Sunday", "Jeudi.")]),
    ("Colours and objects", "« My pencil case is green. In it, there are two red pens and a black pencil. »", [
      ("Colour of the pencil case :", "green", "red", "black", "blue", "Texte."),
      ("How many pens?", "two", "one", "three", "four", "Texte."),
      ("« pencil » :", "crayon", "stylo", "gomme", "règle", "Vocabulaire."),
      ("« trousse » :", "pencil case", "schoolbag", "pen", "book", "Vocabulaire.")])]),
  d("anglais", "Anglais", 3, [
    ("Plurals", "Write the plural.", [
      ("a woman → two …", "women", "womans", "womens", "woman", "Irrégulier."),
      ("a baby → two …", "babies", "babys", "babyes", "baby", "y → ies."),
      ("a foot → two …", "feet", "foots", "feets", "foot", "Irrégulier."),
      ("a bus → two …", "buses", "buss", "busies", "bus", "-es.")]),
    ("Opposites", "Find the opposite.", [
      ("old ≠", "young (ou new)", "tall", "big", "fast", "Contraire."),
      ("happy ≠", "sad", "kind", "nice", "funny", "Contraire."),
      ("open ≠", "closed", "big", "empty", "full", "Contraire."),
      ("long ≠", "short", "tall", "small", "thin", "Contraire.")]),
    ("Dialogue", "A : « Good afternoon! What's your name? » B : « My name is Coumba. » A : « Nice to meet you! »", [
      ("« Good afternoon » se dit", "l'après-midi", "le matin", "la nuit", "à minuit", "Moment."),
      ("Réponse à « Nice to meet you » :", "Nice to meet you too.", "I'm twelve.", "Good night.", "Thank you, goodbye father.", "Politesse."),
      ("« What's your name? » =", "Comment t'appelles-tu ?", "Quel âge as-tu ?", "Où habites-tu ?", "Comment vas-tu ?", "Traduction."),
      ("« Pardon, excusez-moi » :", "Sorry / Excuse me", "Please", "Thank you", "Welcome", "Politesse.")])]),
])
