from sujets_dev_common import D, pack, TRIM
L = "5e"
def d(s, name, n, exos): return D(f"dev-5e-{s}-{n}", L, name, n, exos, label=TRIM[n])

ANNALES_X, GUIDED_X = pack([
  d("maths", "Mathématiques", 1, [
    ("Nombres relatifs", "Calcule.", [
      ("(−7) + (+4) =", "−3", "3", "−11", "11", "Signes contraires : on soustrait, signe du plus éloigné de 0."),
      ("(−5) − (−9) =", "4", "−14", "−4", "14", "−5 + 9."),
      ("(−2) × (−6) =", "12", "−12", "−8", "8", "Deux signes moins : positif."),
      ("Ranger : −3 ; 2 ; −8 ; 0. Le plus petit :", "−8", "−3", "0", "2", "Plus loin de 0 du côté négatif.")]),
    ("Priorités et fractions", "Calcule en respectant les priorités.", [
      ("12 − 4 × 2 =", "4", "16", "8", "20", "Multiplication d'abord."),
      ("(12 − 4) × 2 =", "16", "4", "20", "8", "Parenthèses d'abord."),
      ("3/5 + 1/10 =", "7/10", "4/15", "4/10", "1/2", "6/10 + 1/10."),
      ("2/3 de 24 :", "16", "8", "12", "18", "24 ÷ 3 × 2.")]),
    ("Repère et températures", "Températures relevées à 6 h : lundi −2 °C, mardi +3 °C, mercredi −5 °C (montagne en Europe).", [
      ("Jour le plus froid :", "mercredi", "lundi", "mardi", "égalité", "−5 est le plus petit."),
      ("Écart entre mardi et mercredi :", "8 °C", "2 °C", "−8 °C", "3 °C", "3 − (−5)."),
      ("Moyenne des trois températures :", "−4/3 °C (environ −1,3 °C)", "0 °C", "−2 °C", "10/3 °C", "(−2 + 3 − 5) ÷ 3 = −4/3."),
      ("Si lundi la température monte de 6 °C :", "4 °C", "−8 °C", "8 °C", "−4 °C", "−2 + 6.")])]),
  d("maths", "Mathématiques", 2, [
    ("Pourcentages", "Un commerçant achète un sac de sucre 20 000 F et le revend avec 15 % de bénéfice.", [
      ("Bénéfice :", "3 000 F", "1 500 F", "15 000 F", "2 000 F", "20 000 × 15 ÷ 100."),
      ("Prix de vente :", "23 000 F", "21 500 F", "35 000 F", "17 000 F", "20 000 + 3 000."),
      ("Coefficient multiplicateur :", "1,15", "0,15", "15", "0,85", "1 + 15/100."),
      ("Remise de 10 % sur 23 000 F :", "20 700 F", "22 990 F", "2 300 F", "21 000 F", "23 000 × 0,9.")]),
    ("Angles", "Dans le triangle RST, R = 48° et S = 67°.", [
      ("Angle T :", "65°", "75°", "115°", "55°", "180 − 48 − 67."),
      ("Le triangle est", "acutangle", "rectangle", "obtusangle", "équilatéral", "Trois angles aigus."),
      ("Complémentaire de 48° :", "42°", "132°", "52°", "48°", "90 − 48."),
      ("Supplémentaire de 67° :", "113°", "23°", "123°", "293°", "180 − 67.")]),
    ("Parallélogramme", "EFGH est un parallélogramme de centre O avec EF = 7 cm, FG = 4 cm, EG = 9 cm.", [
      ("GH =", "7 cm", "4 cm", "9 cm", "3,5 cm", "Côtés opposés égaux."),
      ("EO =", "4,5 cm", "9 cm", "3,5 cm", "2 cm", "Diagonales se coupent en leur milieu."),
      ("Périmètre :", "22 cm", "28 cm", "11 cm", "20 cm", "2 × (7 + 4)."),
      ("Symétrique de E par rapport à O :", "G", "F", "H", "E", "O milieu de [EG].")])]),
  d("maths", "Mathématiques", 3, [
    ("Aires", "Un champ a la forme d'un trapèze de bases 40 m et 60 m et de hauteur 25 m.", [
      ("Formule de l'aire du trapèze :", "(B + b) × h ÷ 2", "B × b × h", "(B + b) × h", "B × h ÷ 2", "Formule."),
      ("Aire :", "1 250 m²", "2 500 m²", "60 000 m²", "1 000 m²", "(60 + 40) × 25 ÷ 2."),
      ("1 ha = 10 000 m² : aire en ha", "0,125 ha", "1,25 ha", "12,5 ha", "0,0125 ha", "1 250 ÷ 10 000."),
      ("Récolte de 2 kg par m² :", "2 500 kg", "1 250 kg", "625 kg", "5 000 kg", "1 250 × 2.")]),
    ("Volumes", "Une citerne cylindrique a un rayon de 1 m et une hauteur de 2 m (π ≈ 3,14).", [
      ("Aire de la base :", "3,14 m²", "6,28 m²", "1 m²", "12,56 m²", "π × 1²."),
      ("Volume :", "6,28 m³", "3,14 m³", "12,56 m³", "2 m³", "Base × hauteur."),
      ("En litres :", "6 280 L", "628 L", "62,8 L", "62 800 L", "× 1 000."),
      ("Bidons de 20 L pour la remplir :", "314", "628", "31,4", "3 140", "6 280 ÷ 20.")]),
    ("Statistiques", "Âges des 10 joueurs d'une équipe : 13, 14, 14, 13, 15, 14, 12, 14, 15, 13.", [
      ("Âge le plus fréquent :", "14", "13", "15", "12", "Quatre fois."),
      ("Effectif des joueurs de 13 ans :", "3", "4", "2", "1", "On compte."),
      ("Moyenne d'âge :", "13,7", "14", "13,5", "13", "137 ÷ 10."),
      ("Fréquence des 15 ans :", "20 %", "15 %", "2 %", "10 %", "2 ÷ 10.")])]),
  d("francais", "Français", 1, [
    ("Le passé composé", "Mets au passé composé.", [
      ("Nous (partir) tôt.", "sommes partis", "avons parti", "sommes parti", "avons partis", "Auxiliaire être."),
      ("Elle (prendre) le car.", "a pris", "est prise", "a prendu", "a prit", "Participe irrégulier."),
      ("Ils (voir) la mer.", "ont vu", "sont vus", "ont vus", "ont voyé", "Avoir."),
      ("Tu (venir) hier.", "es venu(e)", "as venu", "es venus", "a venu", "Être.")]),
    ("Le passé simple", "Mets au passé simple (3e personne).", [
      ("Il (marcher) longtemps.", "marcha", "marchait", "marchit", "a marché", "1er groupe : -a."),
      ("Ils (finir) le travail.", "finirent", "finissaient", "finèrent", "ont fini", "2e groupe."),
      ("Elle (faire) un vœu.", "fit", "faisa", "faisait", "fut", "Irrégulier."),
      ("Ils (être) heureux.", "furent", "étaient", "sont", "fûmes", "Irrégulier.")]),
    ("Homophones", "Choisis.", [
      ("… enfants jouent.", "Ces", "Ses", "C'est", "S'est", "Démonstratif (ceux-là)."),
      ("Il … blessé.", "s'est", "c'est", "ses", "ces", "Verbe pronominal."),
      ("Je ne sais pas … il viendra.", "s'il", "cil", "si l'", "ci il", "Si + il."),
      ("Elle … partie.", "est", "et", "ait", "es", "Être.")])]),
  d("francais", "Français", 2, [
    ("COD et COI", "« Le vieux pêcheur offre des poissons à ses voisins. »", [
      ("COD :", "des poissons", "à ses voisins", "le vieux pêcheur", "offre", "Offre quoi ?"),
      ("COI :", "à ses voisins", "des poissons", "le vieux pêcheur", "aucun", "Offre à qui ?"),
      ("Remplace le COD par un pronom :", "Le vieux pêcheur les offre à ses voisins.", "Le vieux pêcheur leur offre.", "Le vieux pêcheur lui offre.", "Le vieux pêcheur y offre.", "les."),
      ("Remplace le COI par un pronom :", "Le vieux pêcheur leur offre des poissons.", "Le vieux pêcheur les offre des poissons.", "Le vieux pêcheur lui offre des poissons.", "Le vieux pêcheur en offre des poissons.", "leur (pluriel).")]),
    ("Le groupe nominal", "« Une grande maison blanche aux volets bleus »", [
      ("Nom noyau :", "maison", "grande", "volets", "bleus", "Mot principal."),
      ("Épithète :", "grande (et blanche)", "volets", "aux", "une", "Adjectif collé au nom."),
      ("« aux volets bleus » :", "complément du nom", "COD", "sujet", "attribut", "Précise maison."),
      ("Déterminant :", "une", "grande", "aux", "blanche", "Avant le nom.")]),
    ("Formation des mots", "Observe : imprévisible, replanter, chanteuse, rapidement.", [
      ("Préfixe de « imprévisible » :", "im-", "pré-", "-ible", "vis", "Négation (et pré- ensuite)."),
      ("Sens de « re- » :", "de nouveau", "contraire", "avant", "petit", "Répétition."),
      ("Suffixe de « chanteuse » :", "-euse", "chant-", "-ante", "-eur", "Féminin du métier."),
      ("Classe de « rapidement » :", "adverbe", "adjectif", "nom", "verbe", "Suffixe -ment.")])]),
  d("francais", "Français", 3, [
    ("La fable", "« Le Corbeau et le Renard » : le renard flatte le corbeau pour obtenir son fromage.", [
      ("Auteur :", "La Fontaine", "Molière", "Senghor", "Hugo", "Fables."),
      ("Défaut du corbeau :", "la vanité", "la gourmandise", "la paresse", "la colère", "Il aime les compliments."),
      ("Arme du renard :", "la flatterie", "la force", "la course", "le mensonge sur l'heure", "Ruse."),
      ("Morale :", "Tout flatteur vit aux dépens de celui qui l'écoute.", "Rien ne sert de courir.", "La raison du plus fort est toujours la meilleure.", "Aide-toi, le ciel t'aidera.", "Fable.")]),
    ("Le dialogue", "— Où vas-tu ? demanda Moussa.\n— Au marché, répondit Awa.", [
      ("Signe qui marque le changement d'interlocuteur :", "le tiret", "la virgule", "le point-virgule", "les parenthèses", "Ponctuation."),
      ("« demanda Moussa » est", "une incise", "un sujet", "un COD", "une didascalie", "Indique qui parle."),
      ("Verbe de parole :", "répondit", "marché", "vas", "où", "Introduit la parole."),
      ("Au discours indirect : Moussa demanda à Awa", "où elle allait", "où vas-tu", "où tu vas ?", "où allait-elle ?", "Question indirecte.")]),
    ("Champ lexical", "« La brousse s'éveille : les oiseaux chantent, les singes crient et le lion rugit au loin. »", [
      ("Champ lexical dominant :", "les bruits des animaux", "la mer", "l'école", "la ville", "chanter, crier, rugir."),
      ("Mot qui n'en fait pas partie :", "brousse", "chantent", "crient", "rugit", "Lieu."),
      ("« s'éveille » est une", "personnification", "comparaison", "hyperbole", "litote", "Qualité humaine."),
      ("Synonyme de « rugit » ici :", "pousse son cri", "dort", "mange", "court", "Sens.")])]),
  d("svt", "SVT", 1, [
    ("Groupes d'aliments", "Repas : riz, poisson, huile, salade, lait.", [
      ("Aliment bâtisseur (protides) :", "poisson", "riz", "huile", "salade", "Construction."),
      ("Aliment énergétique riche en lipides :", "huile", "salade", "lait", "poisson", "Graisses."),
      ("Aliment riche en calcium :", "lait", "huile", "riz", "salade", "Os et dents."),
      ("Ce repas est", "équilibré", "sans protides", "sans vitamines", "sans glucides", "Groupes variés.")]),
    ("Maladies de carence", "Un enfant mal nourri a un gros ventre et des cheveux décolorés.", [
      ("Nom de la maladie :", "kwashiorkor", "paludisme", "rougeole", "goitre", "Carence en protéines."),
      ("Carence en cause :", "protéines", "eau", "sucre", "sel", "Cause."),
      ("Carence en iode :", "goitre", "scorbut", "rachitisme", "kwashiorkor", "Thyroïde."),
      ("Carence en vitamine D :", "rachitisme", "scorbut", "goitre", "paludisme", "Os.")]),
    ("Digestion", "Expérience : de l'amidon + de la salive à 37 °C ; au bout de 15 min, il n'y a plus d'amidon.", [
      ("Test de l'amidon :", "eau iodée (bleu-noir)", "eau de chaux", "liqueur de Fehling seule", "papier pH", "Réactif."),
      ("L'amidon a été transformé en", "sucre (maltose)", "protéine", "graisse", "eau", "Digestion."),
      ("Substance active de la salive :", "enzyme (amylase)", "acide", "sel", "vitamine", "Enzyme."),
      ("Température choisie :", "37 °C, celle du corps", "0 °C", "100 °C", "−10 °C", "Conditions.")])]),
  d("svt", "SVT", 2, [
    ("Respiration", "On place une souris sous une cloche avec de l'eau de chaux.", [
      ("L'eau de chaux se trouble car la souris rejette", "du CO₂", "de l'O₂", "de l'eau", "de l'azote", "Respiration."),
      ("Gaz consommé :", "dioxygène", "dioxyde de carbone", "azote", "vapeur", "Inspiration."),
      ("Organe respiratoire de la souris :", "poumons", "branchies", "trachées", "peau seule", "Mammifère."),
      ("Respiration du criquet :", "trachées", "poumons", "branchies", "peau seule", "Insecte.")]),
    ("Photosynthèse", "Une plante aquatique (élodée) éclairée dégage des bulles.", [
      ("Gaz des bulles :", "dioxygène", "dioxyde de carbone", "azote", "fumée", "Photosynthèse."),
      ("Si on éteint la lumière, les bulles", "s'arrêtent", "augmentent", "changent de couleur", "restent pareilles", "Lumière nécessaire."),
      ("Substance verte nécessaire :", "chlorophylle", "hémoglobine", "amidon", "salive", "Pigment."),
      ("La plante fabrique", "de la matière organique (sucres)", "du sable", "du pétrole", "du sel", "Production.")]),
    ("Reproduction des plantes", "On étudie la fleur d'hibiscus.", [
      ("Pièces colorées qui attirent les insectes :", "pétales", "sépales", "étamines", "racines", "Attraction."),
      ("Grains produits par les étamines :", "pollen", "ovules", "graines", "fruits", "Mâle."),
      ("Agent de pollinisation fréquent :", "insectes", "poissons", "pierres", "sel", "Abeilles."),
      ("Après fécondation, la fleur donne", "un fruit avec des graines", "une racine", "une feuille", "un bourgeon", "Transformation.")])]),
  d("svt", "SVT", 3, [
    ("Les insectes", "On observe une abeille.", [
      ("Nombre de pattes :", "6", "8", "4", "10", "Insecte."),
      ("Parties du corps :", "tête, thorax, abdomen", "tête et tronc", "céphalothorax et abdomen", "une seule", "Trois parties."),
      ("Rôle de l'abeille pour les plantes :", "pollinisation", "destruction", "arrosage", "rien", "Transport du pollen."),
      ("Produit de l'abeille :", "miel", "lait", "soie", "laine", "Ruche.")]),
    ("Les ravageurs", "Le criquet pèlerin peut détruire les récoltes du Sahel.", [
      ("Les criquets se déplacent en", "essaims", "troupeaux", "bancs", "meutes", "Groupe."),
      ("Ils mangent", "les végétaux", "le sable", "le bétail", "les poissons", "Herbivores."),
      ("Lutte possible :", "surveillance et traitement ciblé", "laisser faire", "brûler toute la brousse", "arroser", "Lutte."),
      ("Conséquence d'une invasion :", "famine", "inondation", "neige", "séisme", "Récoltes détruites.")]),
    ("Chaîne alimentaire", "Mil → criquet → poule → chacal.", [
      ("Producteur :", "mil", "criquet", "poule", "chacal", "Plante verte."),
      ("Consommateur primaire :", "criquet", "mil", "poule", "chacal", "Herbivore."),
      ("Si on tue tous les chacals, les poules", "augmentent", "diminuent", "disparaissent", "restent pareilles forcément", "Moins de prédateurs."),
      ("Les flèches signifient", "« est mangé par »", "« mange »", "« vit avec »", "« naît de »", "Convention.")])]),
  d("histoire", "Histoire", 1, [
    ("L'islam", "L'islam est né au VIIe siècle en Arabie.", [
      ("Date de l'Hégire :", "622", "632", "1076", "1235", "Départ vers Médine."),
      ("Ville vers laquelle le Prophète part en 622 :", "Médine", "La Mecque", "Jérusalem", "Bagdad", "Hégire."),
      ("Les cinq piliers comprennent", "la prière et le jeûne", "la chasse", "le commerce", "la guerre", "Obligations."),
      ("L'islam arrive en Afrique de l'Ouest d'abord par", "le commerce transsaharien", "les Portugais", "les chemins de fer", "les avions", "Diffusion.")]),
    ("Le Ghana", "L'empire du Ghana était appelé « pays de l'or ».", [
      ("Peuple fondateur :", "Soninké", "Mandingue", "Songhaï", "Sérère", "Wagadou."),
      ("Capitale :", "Koumbi Saleh", "Niani", "Gao", "Djenné", "Ghana."),
      ("Ses rois prélevaient", "des taxes sur le commerce", "des impôts sur internet", "rien", "seulement des poissons", "Richesse."),
      ("Déclin :", "XIe siècle, Almoravides", "XIXe siècle, Français", "XXe siècle", "Ve siècle", "1076.")]),
    ("Le commerce transsaharien", "Les caravanes reliaient le Maghreb et le Soudan occidental.", [
      ("Produit échangé contre l'or :", "sel", "pétrole", "café", "maïs", "Échange."),
      ("Animal des caravanes :", "dromadaire", "éléphant", "zèbre", "bœuf", "Désert."),
      ("Ville-étape :", "Tombouctou", "Dakar", "Lagos", "Abidjan", "Carrefour."),
      ("Conséquence :", "diffusion de l'islam", "fin des royaumes", "arrivée des avions", "aucune", "Contacts.")])]),
  d("histoire", "Histoire", 2, [
    ("Le Mali de Soundiata", "Soundiata Keïta bat Soumaoro Kanté à Kirina.", [
      ("Date approximative de Kirina :", "1235", "1076", "1591", "1960", "XIIIe siècle."),
      ("Soumaoro était roi du", "Sosso", "Ghana", "Djolof", "Maroc", "Adversaire."),
      ("Texte attribué à l'assemblée de Kouroukan Fouga :", "Charte du Manden", "Coran", "Code noir", "Déclaration de 1789", "Organisation sociale."),
      ("Source principale de l'histoire de Soundiata :", "tradition orale des griots", "journaux", "télévision", "photos", "Épopée.")]),
    ("Kankou Moussa", "En 1324, le mansa Kankou Moussa fait le pèlerinage à La Mecque.", [
      ("Titre du roi du Mali :", "mansa", "pharaon", "damel", "askia", "Titre."),
      ("Il emporte beaucoup de", "or", "pétrole", "sel seulement", "riz", "Richesse."),
      ("Au Caire, son passage fait", "baisser la valeur de l'or", "monter le prix du sable", "fermer les marchés", "rien", "Trop d'or."),
      ("Monument associé à son règne :", "mosquée Djingareyber à Tombouctou", "pyramides", "tour Eiffel", "Grande Mosquée de Touba", "Architecte Es-Saheli.")]),
    ("Le Songhaï", "L'empire songhaï domine la boucle du Niger aux XVe-XVIe siècles.", [
      ("Capitale :", "Gao", "Niani", "Koumbi Saleh", "Ségou", "Niger."),
      ("Grand souverain :", "Askia Mohammed", "Soundiata", "Ndiadiane Ndiaye", "Samory", "Askia."),
      ("Bataille de Tondibi :", "1591", "1235", "1324", "1076", "Fin de l'empire."),
      ("Avantage des Marocains :", "armes à feu", "éléphants", "bateaux", "chevaux ailés", "Arquebuses.")])]),
  d("histoire", "Histoire", 3, [
    ("Le Tekrour", "Le Tekrour s'étend dans la vallée du fleuve Sénégal.", [
      ("Région actuelle :", "Fouta Toro", "Casamance", "Cap-Vert", "Sine", "Vallée."),
      ("Roi converti à l'islam au XIe siècle :", "War Diabi", "Lat Dior", "Alboury", "Koli Tenguella", "Islam."),
      ("Peuple principal :", "Toucouleurs (Haalpulaar)", "Diola", "Bassari", "Lébou", "Fouta."),
      ("Dynastie fondée au XVIe siècle :", "Dényankobé (Koli Tenguella)", "Keïta", "Askia", "Guelwar", "Fouta.")]),
    ("Le Djolof", "Le Djolof est fondé au XIIIe-XIVe siècle.", [
      ("Fondateur légendaire :", "Ndiadiane Ndiaye", "War Diabi", "Soundiata", "Lat Dior", "Légende du Walo."),
      ("Titre du roi :", "Bourba", "Damel", "Brak", "Teigne", "Djolof."),
      ("Royaume du Cayor, roi :", "Damel", "Bourba", "Brak", "Mansa", "Cayor."),
      ("Fin de la confédération (XVIe siècle) :", "indépendance du Cayor (bataille de Danki)", "arrivée des Français en 1960", "invasion marocaine", "guerre mondiale", "Danki, vers 1549.")]),
    ("Repères du Moyen Âge africain", "On place les empires sur une frise.", [
      ("Ordre chronologique :", "Ghana, Mali, Songhaï", "Mali, Ghana, Songhaï", "Songhaï, Mali, Ghana", "Ghana, Songhaï, Mali", "Succession."),
      ("Fleuve commun aux trois empires :", "Niger", "Nil", "Congo", "Zambèze", "Boucle du Niger."),
      ("Ces empires sont dans la zone du", "Sahel et de la savane", "désert du Kalahari", "forêt équatoriale", "Maghreb", "Localisation."),
      ("Source pour connaître le Ghana :", "écrits de voyageurs arabes (El Bekri)", "journaux télévisés", "photos", "films", "Sources écrites.")])]),
  d("geo", "Géographie", 1, [
    ("Le relief de l'Afrique", "L'Afrique est un continent de plateaux.", [
      ("Plus haut sommet :", "Kilimandjaro", "mont Cameroun", "Atlas", "Fouta-Djalon", "Tanzanie."),
      ("Chaîne de montagnes du Maghreb :", "Atlas", "Drakensberg", "Andes", "Alpes", "Nord-Ouest."),
      ("Grand lac d'Afrique de l'Est :", "Victoria", "Tchad", "Guiers", "Retba", "Source du Nil blanc."),
      ("Fossé qui traverse l'Afrique de l'Est :", "Rift", "Sahel", "Sahara", "delta", "Faille.")]),
    ("Les fleuves africains", "On compare quelques fleuves.", [
      ("Fleuve le plus long :", "Nil", "Niger", "Congo", "Sénégal", "Environ 6 700 km."),
      ("Fleuve qui forme une boucle au Mali :", "Niger", "Nil", "Congo", "Gambie", "Boucle."),
      ("Fleuve qui naît au Fouta-Djalon :", "Sénégal (Bafing)", "Nil", "Congo", "Zambèze", "Château d'eau."),
      ("Grand barrage du fleuve Sénégal :", "Manantali", "Assouan", "Kariba", "Akosombo", "OMVS.")]),
    ("Le lac de Guiers", "Le lac de Guiers, au nord du Sénégal, alimente Dakar en eau.", [
      ("Le lac est alimenté par", "le fleuve Sénégal", "la mer", "le Niger", "la pluie seulement", "Taouey."),
      ("Usage principal :", "eau potable et irrigation", "pêche industrielle en haute mer", "navigation de paquebots", "extraction de pétrole", "Ressource."),
      ("Région :", "Saint-Louis / Louga", "Ziguinchor", "Tambacounda", "Kédougou", "Nord."),
      ("Lac rose près de Dakar :", "lac Retba", "lac de Guiers", "lac Tchad", "lac Victoria", "Sel.")])]),
  d("geo", "Géographie", 2, [
    ("Climats africains", "Climogramme A : pluie tous les mois, 2 000 mm. Climogramme B : 50 mm par an.", [
      ("Climat A :", "équatorial", "désertique", "méditerranéen", "sahélien", "Pluies toute l'année."),
      ("Climat B :", "désertique", "équatorial", "tropical humide", "tempéré", "Très sec."),
      ("Végétation du climat A :", "forêt dense", "steppe", "désert", "savane arborée", "Humide."),
      ("Exemple de lieu au climat B :", "Sahara", "bassin du Congo", "Casamance", "Gabon", "Désert.")]),
    ("La savane", "La savane couvre une grande partie de l'Afrique tropicale.", [
      ("Végétation :", "herbes hautes et arbres dispersés", "forêt sans herbe", "sable nu", "glace", "Définition."),
      ("Arbre typique :", "baobab", "sapin", "chêne", "palmier dattier seul", "Savane."),
      ("Saisons :", "une saison sèche et une saison des pluies", "4 saisons", "toujours pluvieux", "toujours sec", "Tropical."),
      ("Animal de savane :", "girafe", "ours polaire", "pingouin", "renne", "Faune.")]),
    ("La désertification", "Au Sahel, le désert avance.", [
      ("Cause naturelle :", "baisse des pluies", "trop d'arbres", "neige", "volcans", "Sécheresse."),
      ("Cause humaine :", "coupe abusive de bois", "reboisement", "jachère", "compost", "Déboisement."),
      ("Solution :", "Grande Muraille verte", "couper plus d'arbres", "feux de brousse", "surpâturage", "Reboisement."),
      ("Conséquence :", "baisse des récoltes", "plus de forêts", "plus de pluie", "aucune", "Sols pauvres.")])]),
  d("geo", "Géographie", 3, [
    ("Les États africains", "L'Afrique compte 54 États.", [
      ("Pays le plus peuplé d'Afrique :", "Nigeria", "Sénégal", "Égypte", "Algérie", "Plus de 200 millions."),
      ("Plus grand pays par la superficie :", "Algérie", "Nigeria", "Sénégal", "Gambie", "Superficie."),
      ("Plus petit pays continental d'Afrique :", "Gambie", "Sénégal", "Mali", "Niger", "Enclave."),
      ("Pays sans accès à la mer :", "Mali", "Sénégal", "Guinée", "Mauritanie", "Enclavé.")]),
    ("L'intégration", "La CEDEAO veut faciliter les échanges entre ses membres.", [
      ("Siège de la CEDEAO :", "Abuja", "Dakar", "Addis-Abeba", "Ouagadougou", "Nigeria."),
      ("Siège de l'Union africaine :", "Addis-Abeba", "Abuja", "Dakar", "Le Caire", "Éthiopie."),
      ("La BCEAO a son siège à", "Dakar", "Abidjan", "Lomé", "Bamako", "Banque centrale."),
      ("Avantage de la libre circulation :", "voyager et commercer plus facilement", "plus de frontières fermées", "plus de taxes", "moins d'échanges", "Intégration.")]),
    ("L'OMVS", "Le Sénégal, le Mali, la Mauritanie et la Guinée gèrent ensemble le fleuve Sénégal.", [
      ("OMVS signifie", "Organisation pour la mise en valeur du fleuve Sénégal", "Office mondial des villes du Sahel", "Organisation militaire", "Office du vent et du soleil", "Sigle."),
      ("Barrage anti-sel près de l'embouchure :", "Diama", "Manantali", "Assouan", "Kandadji", "Bloque la remontée de l'eau de mer."),
      ("Avantage des barrages :", "irrigation et électricité", "plus de sécheresse", "fin de la pêche", "plus de sel", "Usages."),
      ("Culture irriguée dans la vallée :", "riz", "cacao", "café", "blé d'hiver", "Riziculture.")])]),
  d("anglais", "Anglais", 1, [
    ("Past simple", "« Yesterday, Mariama got up early. She washed, had breakfast and went to school. »", [
      ("Past of « get up » :", "got up", "getted up", "gets up", "get up", "Irrégulier."),
      ("Past of « have » :", "had", "haved", "has", "having", "Irrégulier."),
      ("« washed » is", "regular", "irregular", "present", "future", "-ed."),
      ("Negative : She … go to the market.", "didn't", "doesn't", "wasn't", "not", "did not.")]),
    ("Questions", "Ask questions about the text.", [
      ("… did she go? — To school.", "Where", "When", "Who", "What", "Lieu."),
      ("… did she get up? — Early.", "When", "Where", "Who", "Why", "Temps."),
      ("… had breakfast? — Mariama.", "Who", "What", "Where", "How", "Personne."),
      ("Did she wash? — Yes, she …", "did", "does", "was", "washed", "Réponse courte.")]),
    ("Present simple or continuous", "Choose.", [
      ("My mother … (cook) now.", "is cooking", "cooks", "cook", "cooked", "Now."),
      ("She always … (cook) on Sunday.", "cooks", "is cooking", "cook", "cooking", "Habitude."),
      ("Look! It … (rain).", "is raining", "rains", "rain", "rained", "Look!"),
      ("I … (not like) onions.", "don't like", "am not liking", "doesn't like", "not like", "État.")])]),
  d("anglais", "Anglais", 2, [
    ("Comparatives", "« The Gambia is smaller than Senegal. Senegal is bigger than the Gambia. »", [
      ("Comparative of « small » :", "smaller", "more small", "smallest", "smaler", "Court."),
      ("Comparative of « hot » :", "hotter", "hoter", "more hot", "hottest", "Doublement."),
      ("Comparative of « interesting » :", "more interesting", "interestinger", "most interesting", "interestinger than", "Long."),
      ("Comparative of « good » :", "better", "gooder", "best", "more good", "Irrégulier.")]),
    ("Possessives", "Choose the right possessive.", [
      ("This is Awa's bag. It's … bag.", "her", "his", "their", "its", "Féminin."),
      ("These are our books. They are …", "ours", "our", "us", "we", "Pronom possessif."),
      ("The boys and … teacher.", "their", "there", "they're", "them", "Possessif pluriel."),
      ("« Le chien de Moussa » :", "Moussa's dog", "the dog Moussa", "Moussa dog's", "dog's Moussa", "Génitif.")]),
    ("Quantities", "« There is some milk and there are some eggs. There isn't any butter. »", [
      ("There … some eggs.", "are", "is", "be", "has", "Pluriel."),
      ("There isn't … butter.", "any", "some", "many", "few", "Négatif."),
      ("How … milk is there?", "much", "many", "few", "a", "Indénombrable."),
      ("How … eggs are there?", "many", "much", "little", "lot", "Dénombrable.")])]),
  d("anglais", "Anglais", 3, [
    ("Can", "« Ibou can play the guitar but he can't sing. »", [
      ("Can Ibou sing?", "No, he can't.", "Yes, he can.", "No, he doesn't.", "Yes, he does.", "Texte."),
      ("Can he play the guitar?", "Yes, he can.", "No, he can't.", "Yes, he is.", "No, he isn't.", "Texte."),
      ("« Can I open the window? » exprime", "une demande de permission", "un ordre", "le passé", "une interdiction", "Permission."),
      ("Can + verbe :", "base verbale sans to", "verbe en -ing", "to + verbe", "verbe au passé", "Modal.")]),
    ("Dates", "Read the dates.", [
      ("1st :", "first", "one", "oneth", "firsth", "Ordinal."),
      ("22nd :", "twenty-second", "twenty-two", "twenty-twoth", "second twenty", "Ordinal."),
      ("Independence Day of Senegal :", "the fourth of April", "the twentieth of August", "the first of January", "the fourteenth of July", "4 avril."),
      ("« 1960 » :", "nineteen sixty", "one nine six zero", "nineteen sixteen", "ninety sixty", "Lecture des années.")]),
    ("Vocabulary : jobs", "Match the job.", [
      ("He catches fish :", "fisherman", "farmer", "driver", "tailor", "Pêcheur."),
      ("She makes clothes :", "tailor (dressmaker)", "baker", "nurse", "teacher", "Couturière."),
      ("He drives a taxi :", "driver", "pilot", "farmer", "doctor", "Chauffeur."),
      ("She works in a hospital and helps doctors :", "nurse", "cook", "mechanic", "shopkeeper", "Infirmière.")])]),
])
