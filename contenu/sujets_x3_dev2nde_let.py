# Seconde (S et L) : devoirs types de français, histoire-géographie, anglais et espagnol, 2 par trimestre.
# Rédigés pour l'appli sur le programme officiel, non officiels. Les textes cités sont de courts extraits ou des textes écrits pour l'appli.
from sujets_dev_common import D, pack, TRIM
LV = ["2nde L", "2nde S"]
def d(s, name, n, exos):
    t = (n + 1) // 2
    an, g = D(f"dev-2nde-{s}-{n}", LV[0], name, n, exos, label=f"{TRIM[t]} · devoir {2 - n % 2}")
    an["levels"] = LV
    return an, g

ANNALES_X, GUIDED_X = pack([
  # ================= Français
  d("francais", "Français", 1, [
    ("L'épopée", "Extrait adapté de Soundjata ou l'épopée mandingue (D. T. Niane) : « L'enfant infirme se leva d'un coup, s'appuya sur la barre de fer qui se courba en arc, et la foule poussa un cri. »", [
      ("Ce texte relève du genre", "épique", "comique", "lyrique", "épistolaire", "Exploit extraordinaire d'un héros."),
      ("Qui transmettait traditionnellement cette épopée ?", "le griot", "le roi", "le marabout", "le forgeron", "Tradition orale mandingue."),
      ("« la barre de fer se courba en arc » souligne", "la force surhumaine du héros", "la faiblesse du fer", "la peur de la foule", "la colère de la mère", "Hyperbole épique."),
      ("Le héros de l'épopée est", "Soundjata Keïta", "Soumaoro Kanté", "Kankou Moussa", "Lat Dior", "Fondateur de l'empire du Mali.")]),
    ("Les caractéristiques de l'épopée", "On compare plusieurs épopées africaines.", [
      ("Un trait commun aux épopées :", "le merveilleux et le surnaturel", "le dialogue amoureux", "la rime obligatoire", "l'absence de héros", "Interventions magiques."),
      ("L'épopée exalte", "les valeurs d'un peuple", "la vie privée d'un inconnu", "la science moderne", "le commerce", "Récit fondateur."),
      ("Procédé fréquent :", "l'hyperbole", "la litote", "l'euphémisme", "l'ironie", "Exagération héroïque."),
      ("Autre épopée de la région :", "l'épopée de Ségou", "Une si longue lettre", "L'Aventure ambiguë", "Les Bouts de bois de Dieu", "Épopée bambara.")]),
    ("Langue : la phrase complexe", "« Quand le griot commença, tous se turent parce qu'ils voulaient entendre l'histoire. »", [
      ("Nombre de propositions :", "3", "2", "1", "4", "Trois verbes conjugués."),
      ("« Quand le griot commença » est une subordonnée", "de temps", "de cause", "relative", "complétive", "Conjonction quand."),
      ("« parce qu'ils voulaient entendre l'histoire » exprime", "la cause", "le but", "la conséquence", "l'opposition", "Parce que."),
      ("Temps de « commença » :", "passé simple", "imparfait", "passé composé", "plus-que-parfait", "Action de premier plan.")])]),
  d("francais", "Français", 2, [
    ("Le résumé", "On doit résumer un texte de 400 mots au quart.", [
      ("Longueur attendue :", "environ 100 mots", "environ 200 mots", "environ 40 mots", "400 mots", "Un quart."),
      ("Dans un résumé, on écrit", "à la place de l'auteur, sans donner son avis", "son opinion personnelle", "des citations longues", "à la troisième personne en disant « l'auteur dit »", "Contraction fidèle."),
      ("On conserve", "l'ordre et les idées essentielles du texte", "les exemples détaillés", "les répétitions", "les noms de tous les personnages secondaires", "Fidélité."),
      ("Tolérance habituelle sur le nombre de mots :", "plus ou moins 10 %", "plus ou moins 50 %", "aucune", "le double", "Règle du résumé.")]),
    ("L'argumentation", "« La lecture est indispensable aux jeunes : elle enrichit le vocabulaire. Par exemple, un élève qui lit un roman par mois écrit mieux. »", [
      ("Thèse défendue :", "la lecture est indispensable aux jeunes", "les jeunes ne lisent pas", "les romans sont chers", "il faut écrire des romans", "Opinion principale."),
      ("« elle enrichit le vocabulaire » est", "un argument", "un exemple", "une thèse adverse", "une conclusion", "Raison qui soutient la thèse."),
      ("« un élève qui lit un roman par mois écrit mieux » est", "un exemple", "une thèse", "un argument adverse", "une concession", "Illustration concrète."),
      ("Connecteur qui introduit une opposition :", "cependant", "donc", "par exemple", "d'abord", "Opposition.")]),
    ("Le texte argumentatif", "On prépare une dissertation sur l'école.", [
      ("Plan dialectique :", "thèse, antithèse, synthèse", "introduction seulement", "chronologique", "descriptif", "Deux points de vue puis dépassement."),
      ("L'introduction comprend", "amorce, sujet, problématique, annonce du plan", "seulement la conclusion", "les arguments détaillés", "un résumé de tout le devoir", "Structure classique."),
      ("Une concession consiste à", "reconnaître en partie l'idée adverse", "refuser tout argument", "raconter une histoire", "répéter sa thèse", "« Certes…, mais… »."),
      ("Connecteur de conséquence :", "par conséquent", "pourtant", "bien que", "car", "Conséquence.")])]),
  d("francais", "Français", 3, [
    ("Les registres", "Texte A : « Ô nuit ! ô nuit d'Afrique, tu berces mes rêves… » Texte B : « Le médecin, très sérieux, ausculta… la chaise. »", [
      ("Registre du texte A :", "lyrique", "comique", "tragique", "polémique", "Expression des sentiments, apostrophe."),
      ("Registre du texte B :", "comique", "lyrique", "épique", "pathétique", "Situation absurde qui fait rire."),
      ("« Ô nuit ! » est", "une apostrophe", "une comparaison", "une litote", "une antithèse", "On s'adresse à la nuit."),
      ("Le registre pathétique cherche à", "émouvoir et faire pitié", "faire rire", "instruire", "décrire objectivement", "Pathos.")]),
    ("Le registre polémique et satirique", "« Ces messieurs de la ville, si savants, n'ont jamais tenu une houe. »", [
      ("Registre dominant :", "satirique", "lyrique", "épique", "fantastique", "Moquerie d'un groupe social."),
      ("« si savants » est employé de façon", "ironique", "sincère", "scientifique", "neutre", "On dit le contraire de ce qu'on pense."),
      ("Le texte critique", "le mépris du travail manuel", "les paysans", "l'agriculture", "la science", "Cible de la satire."),
      ("Le registre polémique sert à", "attaquer une opinion ou une personne", "raconter un rêve", "décrire un paysage", "chanter l'amour", "Combat d'idées.")]),
    ("Langue : les figures de style", "Relève la figure de style.", [
      ("« Le soleil, ce lion jaune, rugit sur la plaine » :", "métaphore", "comparaison", "litote", "anaphore", "Rapprochement sans outil de comparaison."),
      ("« Il est fort comme un baobab » :", "comparaison", "métaphore", "hyperbole", "antithèse", "Outil « comme »."),
      ("« Je meurs de soif » :", "hyperbole", "litote", "euphémisme", "personnification", "Exagération."),
      ("« Il nous a quittés » pour « il est mort » :", "euphémisme", "hyperbole", "antithèse", "oxymore", "Atténuation.")])]),
  d("francais", "Français", 4, [
    ("Le théâtre", "Extrait de théâtre : « AWA (à part) : Il ne sait pas que j'ai tout entendu… / MODOU : Awa, tu dors ? »", [
      ("« (à part) » est", "une didascalie", "une réplique", "une tirade", "un monologue", "Indication de mise en scène."),
      ("Un aparté est", "une parole que les autres personnages ne sont pas censés entendre", "un long discours", "une scène sans paroles", "un changement de décor", "Destiné au public."),
      ("Une longue réplique continue s'appelle", "une tirade", "une stichomythie", "une didascalie", "un acte", "Définition."),
      ("La double énonciation signifie que les paroles s'adressent", "aux personnages et au public", "seulement au public", "seulement au metteur en scène", "à l'auteur", "Spécificité du théâtre.")]),
    ("Comédie et tragédie", "On compare les genres théâtraux.", [
      ("La tragédie se termine en général", "par la mort ou le malheur du héros", "par un mariage heureux", "par une fête", "sans dénouement", "Fatalité."),
      ("La comédie cherche surtout à", "faire rire en critiquant les mœurs", "faire pleurer", "raconter une épopée", "décrire la nature", "Castigat ridendo mores."),
      ("Pièce de Cheikh Aliou Ndao :", "L'Exil d'Albouri", "Une si longue lettre", "Climbié", "Soundjata", "Drame historique sénégalais."),
      ("Une pièce est divisée en", "actes et scènes", "chapitres", "strophes", "paragraphes", "Structure.")]),
    ("Langue : discours direct et indirect", "« Le roi déclara : “Je partirai demain.” »", [
      ("Au discours indirect :", "Le roi déclara qu'il partirait le lendemain.", "Le roi déclara qu'il partira demain.", "Le roi déclara : je partirai le lendemain.", "Le roi déclara que je partirai demain.", "Concordance des temps et des repères."),
      ("« demain » devient", "le lendemain", "hier", "aujourd'hui", "demain", "Repère relatif au passé."),
      ("« je » devient", "il", "je", "tu", "nous", "Changement de personne."),
      ("Le futur devient", "le conditionnel présent", "le passé simple", "l'imparfait du subjonctif", "le futur antérieur", "Futur dans le passé.")])]),
  d("francais", "Français", 5, [
    ("La poésie : versification", "« Femme nue, femme noire / Vêtue de ta couleur qui est vie… » (L. S. Senghor, Chants d'ombre)", [
      ("Ce poème est écrit en", "vers libres", "alexandrins réguliers", "sonnet", "prose", "Pas de mètre fixe."),
      ("La répétition de « femme » en début de vers est", "une anaphore", "une rime", "une antithèse", "une litote", "Répétition en tête."),
      ("Mouvement littéraire de Senghor :", "la Négritude", "le Romantisme", "le Surréalisme seulement", "le Classicisme", "Avec Césaire et Damas."),
      ("Registre dominant :", "lyrique", "comique", "polémique", "tragique", "Célébration et sentiments.")]),
    ("Le vers et la rime", "« Je suis le ténébreux, — le veuf, — l'inconsolé » (Nerval)", [
      ("Nombre de syllabes :", "12 (alexandrin)", "10", "8", "14", "Je/suis/le/té/né/breux/le/veuf/l'in/con/so/lé."),
      ("Rimes AABB :", "plates (suivies)", "croisées", "embrassées", "libres", "Définition."),
      ("Rimes ABAB :", "croisées", "plates", "embrassées", "riches", "Définition."),
      ("Un sonnet comporte", "14 vers : deux quatrains et deux tercets", "12 vers", "4 strophes de 4 vers", "un nombre libre de vers", "Forme fixe.")]),
    ("Commentaire de poème", "On prépare le commentaire d'un poème de Birago Diop, « Souffles » : « Écoute plus souvent / Les choses que les êtres… »", [
      ("Thème du poème :", "la présence des ancêtres morts dans la nature", "la guerre", "l'amour", "la ville moderne", "« Les morts ne sont pas morts »."),
      ("« Écoute » est à", "l'impératif", "l'indicatif", "le subjonctif", "l'infinitif", "Ordre ou conseil."),
      ("Le poème s'inspire", "des croyances traditionnelles africaines", "de la mythologie grecque", "de la science", "du roman policier", "Animisme."),
      ("Un commentaire s'organise", "en axes de lecture", "en résumé ligne par ligne", "en liste de figures", "en dialogue", "Méthode.")])]),
  d("francais", "Français", 6, [
    ("Le récit", "« Ce matin-là, Samba quitta son village avant l'aube. Il ne savait pas encore que ce voyage changerait sa vie. »", [
      ("Le narrateur est", "externe à l'histoire (3e personne)", "le personnage principal", "un personnage secondaire qui dit « je »", "absent", "« Il »."),
      ("« Il ne savait pas encore… » révèle un point de vue", "omniscient", "interne", "externe", "théâtral", "Le narrateur sait plus que le personnage."),
      ("Temps du premier plan :", "passé simple", "imparfait", "présent", "futur", "« quitta »."),
      ("La phrase finale crée", "une attente (anticipation)", "une conclusion", "une description", "un dialogue", "Suspense.")]),
    ("Roman et nouvelle", "On compare des œuvres au programme.", [
      ("Une nouvelle est", "un récit bref avec peu de personnages", "un long roman", "une pièce de théâtre", "un poème", "Définition."),
      ("Auteure d'« Une si longue lettre » :", "Mariama Bâ", "Aminata Sow Fall", "Ken Bugul", "Fatou Diome", "Roman épistolaire (1979)."),
      ("Auteur de « L'Aventure ambiguë » :", "Cheikh Hamidou Kane", "Ousmane Sembène", "Camara Laye", "Birago Diop", "Roman de 1961."),
      ("Roman épistolaire :", "écrit sous forme de lettres", "écrit en vers", "sans personnages", "écrit au futur", "Genre de Mariama Bâ.")]),
    ("Le schéma narratif", "On analyse un conte.", [
      ("Première étape :", "la situation initiale", "le dénouement", "les péripéties", "l'élément perturbateur", "Ordre."),
      ("Ce qui déclenche l'action :", "l'élément perturbateur (ou de complication)", "la situation finale", "la morale", "le titre", "Rupture de l'équilibre."),
      ("Les péripéties sont", "les actions et épreuves du héros", "la fin de l'histoire", "le cadre", "la morale", "Développement."),
      ("Dans le schéma actantiel, celui qui aide le héros est", "l'adjuvant", "l'opposant", "le destinataire", "l'objet", "Rôle.")])]),
  # ================= Histoire-Géographie
  d("hg", "Histoire-Géographie", 1, [
    ("La Grèce antique", "Athènes au Ve siècle av. J.-C.", [
      ("Régime politique d'Athènes à l'époque de Périclès :", "la démocratie", "la monarchie absolue", "l'empire", "la dictature militaire", "Pouvoir des citoyens."),
      ("Assemblée des citoyens athéniens :", "l'Ecclésia", "le Sénat", "le Parlement", "la Boulè seulement", "Vote des lois."),
      ("Étaient exclus de la citoyenneté :", "les femmes, les esclaves et les métèques", "les paysans", "les soldats", "les riches", "Démocratie limitée."),
      ("Ve siècle av. J.-C. : années", "500 à 401 av. J.-C.", "401 à 500 apr. J.-C.", "1 à 100", "400 à 301 av. J.-C.", "Siècle avant notre ère.")]),
    ("Rome", "De la République à l'Empire.", [
      ("Premier empereur romain :", "Auguste", "Jules César", "Néron", "Constantin", "27 av. J.-C."),
      ("Sous la République, les deux magistrats suprêmes sont", "les consuls", "les empereurs", "les pharaons", "les rois", "Élus pour un an."),
      ("La « paix romaine » se dit", "Pax romana", "Mare nostrum", "Res publica", "Senatus", "Ier-IIe siècles."),
      ("Empereur qui autorise le christianisme en 313 :", "Constantin", "Auguste", "Néron", "Trajan", "Édit de Milan.")]),
    ("Méthode : la frise chronologique", "On place des événements de l'Antiquité.", [
      ("Événement le plus ancien :", "construction des pyramides de Gizeh", "fondation de Rome", "naissance de Jésus-Christ", "chute de Rome", "Vers 2500 av. J.-C."),
      ("Fondation légendaire de Rome :", "753 av. J.-C.", "476 apr. J.-C.", "1492", "27 av. J.-C.", "Date traditionnelle."),
      ("Fin de l'Empire romain d'Occident :", "476", "753 av. J.-C.", "1453", "313", "Fin de l'Antiquité."),
      ("Durée entre 753 av. J.-C. et 476 apr. J.-C. :", "1 228 ans", "277 ans", "1 129 ans", "1 300 ans", "753 + 476 − 1, car il n'y a pas d'année 0.")])]),
  d("hg", "Histoire-Géographie", 2, [
    ("Préhistoire", "Les grandes étapes de l'humanité.", [
      ("L'Afrique est considérée comme", "le berceau de l'humanité", "le dernier continent peuplé", "sans préhistoire", "peuplée au Moyen Âge", "Fossiles les plus anciens."),
      ("La révolution néolithique est marquée par", "l'agriculture et l'élevage", "l'écriture", "la machine à vapeur", "l'imprimerie", "Sédentarisation."),
      ("Fossile célèbre découvert en Éthiopie :", "Lucy", "Toumaï", "Cro-Magnon", "Néandertal", "Australopithèque, 3,2 millions d'années."),
      ("La préhistoire se termine avec", "l'invention de l'écriture", "le feu", "l'agriculture", "la roue", "Début de l'histoire.")]),
    ("Le Moyen Âge en Afrique", "Les grands empires d'Afrique de l'Ouest.", [
      ("Empire dont la capitale était Koumbi Saleh :", "Ghana", "Mali", "Songhaï", "Djolof", "VIIIe-XIe siècles."),
      ("Ressource qui fit la richesse de ces empires :", "le commerce de l'or et du sel", "le pétrole", "le café", "le caoutchouc", "Commerce transsaharien."),
      ("Ville du savoir sous le Mali et le Songhaï :", "Tombouctou", "Saint-Louis", "Dakar", "Kano", "Mosquée de Sankoré."),
      ("Empereur du Mali célèbre pour son pèlerinage en 1324 :", "Kankou Moussa", "Soundjata", "Askia Mohammed", "Sonni Ali", "Il distribua beaucoup d'or.")]),
    ("Le Moyen Âge en Europe et dans le monde musulman", "Ve-XVe siècles.", [
      ("Système de liens entre seigneur et vassal :", "la féodalité", "la démocratie", "la république", "le capitalisme", "Fief et hommage."),
      ("Hégire (début du calendrier musulman) :", "622", "476", "1492", "800", "Départ du Prophète vers Médine."),
      ("Charlemagne est couronné empereur en", "800", "622", "1066", "1453", "Empire carolingien."),
      ("Prise de Constantinople par les Ottomans :", "1453", "1492", "800", "1789", "Fin du Moyen Âge.")])]),
  d("hg", "Histoire-Géographie", 3, [
    ("Humanisme et Renaissance", "XVe-XVIe siècles en Europe.", [
      ("L'humanisme place au centre", "l'homme et le savoir", "la guerre", "le commerce seulement", "le roi", "Redécouverte de l'Antiquité."),
      ("Invention qui diffuse les idées :", "l'imprimerie (Gutenberg)", "la machine à vapeur", "le téléphone", "la boussole", "Vers 1450."),
      ("Artiste de la Renaissance :", "Léonard de Vinci", "Napoléon", "Victor Hugo", "Picasso", "La Joconde."),
      ("Berceau de la Renaissance :", "l'Italie", "l'Angleterre", "la Russie", "le Portugal seulement", "Florence."),
      ]),
    ("Les grandes découvertes", "Les voyages européens.", [
      ("Christophe Colomb atteint l'Amérique en", "1492", "1498", "1453", "1519", "Pour l'Espagne."),
      ("Vasco de Gama atteint l'Inde en", "1498", "1492", "1415", "1522", "En contournant l'Afrique."),
      ("Les Portugais arrivent sur les côtes sénégalaises au", "XVe siècle", "XIXe siècle", "XIIe siècle", "XXe siècle", "Vers 1444-1445."),
      ("Conséquence pour l'Afrique :", "le développement de la traite atlantique", "la fin du commerce", "l'industrialisation", "l'indépendance", "Commerce triangulaire.")]),
    ("Méthode : analyser un document", "On étudie une carte des routes maritimes du XVIe siècle.", [
      ("Premier réflexe :", "lire le titre, la source et la date", "recopier la carte", "donner son opinion", "chercher une photo", "Présentation du document."),
      ("La légende sert à", "comprendre les signes et couleurs", "décorer", "donner la date", "indiquer l'auteur", "Lecture de carte."),
      ("Une source primaire est", "un document de l'époque étudiée", "un manuel scolaire récent", "un résumé", "une opinion d'élève", "Témoignage direct."),
      ("Pour critiquer un document, on se demande", "qui l'a produit, quand et pourquoi", "s'il est joli", "s'il est long", "s'il est en couleur", "Esprit critique.")])]),
  d("hg", "Histoire-Géographie", 4, [
    ("Développement durable", "Notions de base.", [
      ("Le développement durable répond aux besoins", "du présent sans compromettre ceux des générations futures", "des seuls pays riches", "de l'industrie seulement", "du futur seulement", "Rapport Brundtland (1987)."),
      ("Ses trois piliers :", "économique, social, environnemental", "militaire, politique, religieux", "agricole, minier, industriel", "local, national, mondial", "Définition."),
      ("Énergie renouvelable :", "le solaire", "le pétrole", "le charbon", "le gaz naturel", "Inépuisable à l'échelle humaine."),
      ("Exemple au Sénégal :", "la centrale solaire de Bokhol ou le parc éolien de Taïba Ndiaye", "la centrale à charbon seule", "les sachets plastiques", "le déboisement", "Énergies propres.")]),
    ("Environnement et risques", "Les problèmes environnementaux au Sénégal.", [
      ("L'érosion côtière menace particulièrement", "Saint-Louis (Langue de Barbarie)", "Kédougou", "Tambacounda", "Matam", "Avancée de la mer."),
      ("Grand projet africain contre la désertification :", "la Grande Muraille verte", "le barrage de Diama", "le TER", "l'AIBD", "Reboisement du Sahel."),
      ("Cause de la désertification :", "le déboisement et la sécheresse", "les pluies abondantes", "les mangroves", "les aires protégées", "Facteurs humains et naturels."),
      ("Loi sénégalaise de 2015 :", "interdiction des sachets plastiques fins", "interdiction du riz", "fin de la pêche", "fin du solaire", "Lutte contre la pollution.")]),
    ("Croquis et carte", "On réalise un croquis des ressources naturelles du Sénégal.", [
      ("Un croquis doit avoir", "un titre, une légende et une orientation", "seulement des couleurs", "aucune légende", "un texte long", "Règles."),
      ("Ressource minière de Taïba :", "phosphates", "or", "pétrole", "fer", "Industries chimiques du Sénégal."),
      ("Or : région de", "Kédougou", "Dakar", "Louga", "Ziguinchor", "Sabodala."),
      ("Pétrole offshore exploité depuis 2024 :", "Sangomar", "Kayar", "Diama", "Taïba", "Gisement en mer.")])]),
  d("hg", "Histoire-Géographie", 5, [
    ("Population de l'Afrique", "L'Afrique compte plus de 1,4 milliard d'habitants.", [
      ("Caractéristique démographique majeure :", "une population très jeune", "une population vieillissante", "une baisse de population", "une natalité très faible", "Plus de 40 % de moins de 15 ans."),
      ("Taux de natalité − taux de mortalité =", "accroissement naturel", "solde migratoire", "densité", "espérance de vie", "Définition."),
      ("La densité se calcule en", "habitants par km²", "km² par habitant", "habitants par an", "naissances pour 1 000", "Population / superficie."),
      ("Sénégal : environ 18 millions d'habitants pour 196 712 km², densité ≈", "92 hab/km²", "9 hab/km²", "920 hab/km²", "1 000 hab/km²", "18 000 000 / 196 712.")]),
    ("Les villes africaines", "L'urbanisation de l'Afrique est rapide.", [
      ("L'exode rural est", "le départ des campagnes vers les villes", "le retour à la campagne", "l'émigration vers l'Europe", "la natalité urbaine", "Définition."),
      ("Problème fréquent des grandes villes :", "les quartiers spontanés et les embouteillages", "le manque d'habitants", "l'absence de commerce", "le froid", "Croissance rapide."),
      ("Ville la plus peuplée du Nigeria :", "Lagos", "Abuja", "Kano", "Ibadan", "Plus de 15 millions d'habitants ; Abuja est la capitale."),
      ("Ville nouvelle sénégalaise :", "Diamniadio", "Gorée", "Podor", "Joal", "Pôle urbain.")]),
    ("Ressources et développement", "Les ressources de l'Afrique.", [
      ("L'Afrique exporte surtout", "des matières premières", "des produits de haute technologie", "des voitures", "des avions", "Économie extravertie."),
      ("Principal produit d'exportation historique du Sénégal :", "l'arachide", "le café", "le cacao", "le caoutchouc", "Bassin arachidier."),
      ("Pour développer, il faut", "transformer les ressources sur place", "tout exporter brut", "abandonner l'agriculture", "fermer les écoles", "Valeur ajoutée."),
      ("L'IDH mesure", "santé, éducation et niveau de vie", "seulement la richesse", "la superficie", "la population", "Indice de développement humain.")])]),
  d("hg", "Histoire-Géographie", 6, [
    ("Synthèse histoire", "Révision de l'année.", [
      ("Ordre chronologique correct :", "Antiquité, Moyen Âge, Renaissance", "Renaissance, Antiquité, Moyen Âge", "Moyen Âge, Antiquité, Renaissance", "Antiquité, Renaissance, Moyen Âge", "Périodes."),
      ("Le Moyen Âge va de", "476 à 1453 (ou 1492)", "753 av. J.-C. à 476", "1492 à 1789", "1789 à 1914", "Repères."),
      ("La démocratie est née à", "Athènes", "Rome", "Tombouctou", "Paris", "Ve siècle av. J.-C."),
      ("Empire fondé par Soundjata :", "Mali", "Ghana", "Songhaï", "Djolof", "XIIIe siècle.")]),
    ("Synthèse géographie", "Révision de l'année.", [
      ("Les trois piliers du développement durable :", "économie, société, environnement", "ville, campagne, mer", "eau, air, sol", "école, santé, travail", "Définition."),
      ("Région la plus peuplée du Sénégal :", "Dakar", "Kédougou", "Matam", "Sédhiou", "Concentration urbaine."),
      ("Ressource qui se renouvelle :", "la forêt bien gérée", "le pétrole", "le phosphate", "l'or", "Renouvelable si on replante."),
      ("Problème lié à la croissance urbaine :", "la gestion des déchets", "l'excès de forêts", "le manque de jeunes", "le froid", "Assainissement.")]),
    ("Méthode : la dissertation en histoire-géographie", "On prépare une composition.", [
      ("Une composition commence par", "une introduction qui pose une problématique", "la conclusion", "une liste de dates sans phrases", "un dessin", "Méthode."),
      ("Chaque partie doit contenir", "des idées illustrées par des exemples précis", "seulement des opinions", "une seule phrase", "des citations sans explication", "Argumentation."),
      ("La conclusion", "répond à la problématique et ouvre le sujet", "répète l'introduction", "est facultative", "donne de nouvelles parties", "Bilan."),
      ("Un bon exemple est", "localisé et daté", "vague", "inventé", "très long", "Précision.")])]),
  # ================= Anglais
  d("anglais", "Anglais", 1, [
    ("Reading comprehension", "« Fatou lives in Thiès. She has been studying English for three years. Last summer, she visited her cousin in Banjul and spoke English every day. »", [
      ("Where does Fatou live?", "In Thiès", "In Banjul", "In Dakar", "In London", "Line 1."),
      ("How long has she been studying English?", "For three years", "Since three years", "Three years ago", "For last summer", "Present perfect continuous + for."),
      ("Where did she go last summer?", "To Banjul", "To Thiès", "To Dakar", "To London", "Simple past."),
      ("« spoke » is the past of", "speak", "spoke", "spike", "spend", "Irregular verb.")]),
    ("Grammar: tenses", "Choose the correct form.", [
      ("I ___ to Saint-Louis twice.", "have been", "was", "am", "had being", "Present perfect: experience."),
      ("Yesterday, we ___ a football match.", "watched", "have watched", "watch", "watching", "Yesterday → simple past."),
      ("When I arrived, the bus ___ already ___.", "had / left", "has / left", "was / leave", "did / leave", "Past perfect: earlier past."),
      ("She ___ here since 2020.", "has lived", "lives", "lived", "is living since", "Since + present perfect.")]),
    ("Vocabulary: school life", "Find the right word.", [
      ("A person who teaches:", "a teacher", "a pupil", "a headmaster's car", "a classroom", "Definition."),
      ("« un emploi du temps » :", "a timetable", "a time", "a schedule bag", "a homework", "Translation."),
      ("« faire ses devoirs » :", "to do one's homework", "to make one's homework", "to do one's housework", "to have homeworks", "Fixed expression."),
      ("Opposite of « succeed »:", "fail", "pass", "win", "learn", "Antonym.")])]),
  d("anglais", "Anglais", 2, [
    ("Grammar: passive voice", "Put into the passive.", [
      ("« The pupils clean the classroom. » →", "The classroom is cleaned by the pupils.", "The classroom was cleaned by the pupils.", "The classroom cleans the pupils.", "The pupils are cleaned by the classroom.", "Present simple passive: is + past participle."),
      ("« Ousmane Sembène wrote this novel. » →", "This novel was written by Ousmane Sembène.", "This novel is written by Ousmane Sembène.", "This novel wrote Ousmane Sembène.", "This novel has written by Ousmane Sembène.", "Past passive: was + written."),
      ("« They will build a new school. » →", "A new school will be built.", "A new school will built.", "A new school is built.", "A new school would be build.", "Future passive."),
      ("Past participle of « build »:", "built", "builded", "build", "building", "Irregular.")]),
    ("Grammar: reported speech", "Report the sentences.", [
      ("He said: « I am tired. » → He said that he ___ tired.", "was", "is", "has been", "be", "Backshift."),
      ("She said: « I will come. » → She said that she ___ come.", "would", "will", "can", "shall", "Will → would."),
      ("« Do you like rice? » he asked. → He asked me ___ I liked rice.", "if", "that", "what", "do", "Yes/no question → if/whether."),
      ("« Close the door! » → She told me ___ the door.", "to close", "close", "closing", "that I close", "Order → tell + to.")]),
    ("Writing: an email", "You write an email to a pen friend in Ghana.", [
      ("Best opening:", "Dear Kwame,", "To whom it may concern,", "Hey you!", "Sir,", "Informal email to a friend."),
      ("Best closing:", "Best wishes, Aminata", "Yours faithfully", "Goodbye forever", "End", "Informal closing."),
      ("« J'ai hâte de te lire » :", "I look forward to hearing from you.", "I look forward to hear from you.", "I wait reading you.", "I am hurry to read you.", "Look forward to + -ing."),
      ("To introduce yourself:", "My name is Aminata and I'm 16.", "I have 16 years.", "I am 16 years old name Aminata.", "Me Aminata 16.", "Age with to be.")])]),
  d("anglais", "Anglais", 3, [
    ("Grammar: conditionals", "Complete.", [
      ("If it rains, we ___ at home.", "will stay", "would stay", "stayed", "would have stayed", "First conditional."),
      ("If I were rich, I ___ a hospital.", "would build", "will build", "built", "build", "Second conditional."),
      ("If she had studied, she ___ the exam.", "would have passed", "would pass", "will pass", "passed", "Third conditional."),
      ("Unless you hurry, you ___ the bus.", "will miss", "would miss", "miss", "missed", "Unless = if not.")]),
    ("Grammar: modals", "Choose the right modal.", [
      ("You ___ wear a helmet on a motorbike. It's the law.", "must", "may", "might", "could", "Obligation."),
      ("You ___ smoke here. It's forbidden.", "mustn't", "don't have to", "needn't", "can", "Prohibition."),
      ("It's Sunday: you ___ get up early.", "don't have to", "mustn't", "must", "should to", "Absence of obligation."),
      ("You look ill. You ___ see a doctor.", "should", "mustn't", "can't", "might not", "Advice.")]),
    ("Reading: health", "« Malaria is a disease carried by mosquitoes. Sleeping under a treated net is one of the best ways to prevent it. »", [
      ("Malaria is carried by", "mosquitoes", "flies", "water", "food", "Line 1."),
      ("Best way to prevent it:", "sleeping under a treated net", "drinking milk", "running", "eating fish", "Line 2."),
      ("« prevent » means", "éviter, prévenir", "soigner", "attraper", "transmettre", "Vocabulary."),
      ("« treated net » =", "moustiquaire imprégnée", "filet de pêche", "drap propre", "rideau", "Translation.")])]),
  d("anglais", "Anglais", 4, [
    ("Grammar: gerund or infinitive", "Choose.", [
      ("I enjoy ___ football.", "playing", "to play", "play", "played", "Enjoy + -ing."),
      ("She decided ___ medicine.", "to study", "studying", "study", "studied", "Decide + to."),
      ("He stopped ___ two years ago.", "smoking", "to smoke", "smoke", "smoked", "Stop + -ing = arrêter de."),
      ("I'm used to ___ early.", "getting up", "get up", "got up", "to get up", "Be used to + -ing.")]),
    ("Grammar: relative pronouns", "Complete.", [
      ("The girl ___ won the prize is my sister.", "who", "which", "whose", "where", "Person subject."),
      ("This is the book ___ I bought.", "which", "who", "whose", "where", "Thing."),
      ("The man ___ car was stolen called the police.", "whose", "who", "which", "whom", "Possession."),
      ("This is the village ___ I was born.", "where", "which", "who", "whose", "Place.")]),
    ("Vocabulary: environment", "Find the right word.", [
      ("« le réchauffement climatique » :", "global warming", "global heating up of air", "climate cold", "hot weather", "Expression."),
      ("« recycler » :", "to recycle", "to rebuild", "to reuse a bike", "to recover", "Verb."),
      ("« la sécheresse » :", "drought", "draught beer", "flood", "storm", "Natural disaster."),
      ("« déforestation » :", "deforestation", "unforesting", "tree cutting law", "forestry", "Same word.")])]),
  d("anglais", "Anglais", 5, [
    ("Connectors", "Choose the right link word.", [
      ("It was raining; ___, the match went on.", "however", "because", "so", "and then because", "Contrast."),
      ("She was ill, ___ she stayed at home.", "so", "although", "however", "despite", "Consequence."),
      ("___ he is poor, he is happy.", "Although", "Because", "So", "Therefore", "Concession + clause."),
      ("He failed ___ he didn't work.", "because", "although", "however", "despite", "Cause.")]),
    ("Reading: society", "« In many African cities, young people use mobile money to pay for goods. This has changed the way people trade. »", [
      ("What do young people use?", "mobile money", "cheques", "gold", "only cash", "Line 1."),
      ("« goods » means", "marchandises", "bonnes personnes", "dieux", "routes", "Vocabulary."),
      ("What has changed?", "the way people trade", "the weather", "the language", "the schools", "Line 2."),
      ("Tense of « has changed »:", "present perfect", "simple past", "past perfect", "present continuous", "Have + past participle.")]),
    ("Writing: arguments", "You write about « Should pupils use phones at school? »", [
      ("To give your opinion:", "In my opinion,", "In my opinion's,", "For me thinking,", "According me,", "Correct expression."),
      ("To add an argument:", "Moreover,", "However,", "Although", "Despite of", "Addition."),
      ("To conclude:", "To sum up,", "Firstly,", "For example,", "Besides of,", "Conclusion."),
      ("To give an example:", "For instance,", "In conclusion,", "Nevertheless,", "Whereas,", "Example.")])]),
  d("anglais", "Anglais", 6, [
    ("Synthesis: tenses and voice", "Choose the correct answer.", [
      ("By the time we arrived, the film ___.", "had started", "has started", "starts", "was start", "Past perfect."),
      ("The results ___ next week.", "will be published", "will publish", "are publishing", "published", "Future passive."),
      ("I ___ him since we were children.", "have known", "know", "knew", "am knowing", "Since + present perfect."),
      ("Look! It ___.", "is raining", "rains", "rained", "has rain", "Present continuous.")]),
    ("Synthesis: reported speech and conditionals", "Choose the correct answer.", [
      ("He said he ___ the next day.", "would come", "will come", "comes", "came tomorrow", "Backshift."),
      ("If I ___ you, I would apologise.", "were", "am", "will be", "had", "Second conditional."),
      ("She asked me where I ___.", "lived", "do live", "live do", "living", "Indirect question: no inversion."),
      ("If they had left earlier, they ___ the train.", "wouldn't have missed", "won't miss", "don't miss", "hadn't missed", "Third conditional.")]),
    ("Vocabulary: Senegal and the world", "Translate.", [
      ("« la pêche » (activity):", "fishing", "peach", "sin", "fish market", "Activity."),
      ("« l'indépendance » :", "independence", "independancy", "freedom day only", "independent", "Noun."),
      ("« un griot » is a", "traditional storyteller and singer", "farmer", "fisherman", "soldier", "Culture."),
      ("« Teranga » is often translated as", "hospitality", "fishing", "dance", "wrestling", "Culture.")])]),
  # ================= Espagnol
  d("espagnol", "Espagnol (LV2)", 1, [
    ("El imperfecto", "Elige la forma correcta.", [
      ("Cuando era niño, (vivir) ___ en Kaolack.", "vivía", "viví", "vivo", "viviré", "Imperfecto: hábito en el pasado."),
      ("Nosotros (jugar) ___ al fútbol cada tarde.", "jugábamos", "jugamos ayer", "jugaremos", "juguemos", "-ar → -ábamos."),
      ("Imperfecto de « ser » (yo):", "era", "fui", "soy", "sería", "Irregular."),
      ("Imperfecto de « ir » (ellos):", "iban", "fueron", "van", "irían", "Irregular.")]),
    ("Comprensión", "« Me llamo Moussa. Vivo en Dakar con mi familia. Me gusta leer y escuchar música. »", [
      ("¿Dónde vive Moussa?", "En Dakar", "En Madrid", "En Thiès", "En Kaolack", "Texto."),
      ("¿Con quién vive?", "Con su familia", "Solo", "Con sus amigos", "Con su profesor", "Texto."),
      ("« Me gusta leer » significa", "J'aime lire", "Je dois lire", "Je lis mal", "Je vais lire", "Gustar."),
      ("« escuchar » significa", "écouter", "écrire", "chercher", "chanter", "Vocabulario.")]),
    ("Vocabulario: la familia", "Traduce.", [
      ("« le frère » :", "el hermano", "el primo", "el tío", "el abuelo", "Familia."),
      ("« la grand-mère » :", "la abuela", "la madre", "la tía", "la hermana", "Familia."),
      ("« les parents » :", "los padres", "los parientes lejanos", "los hijos", "los tíos", "Padres = père et mère."),
      ("« le cousin » :", "el primo", "el sobrino", "el hermano", "el nieto", "Familia.")])]),
  d("espagnol", "Espagnol (LV2)", 2, [
    ("El imperativo", "Elige la forma correcta.", [
      ("(tú, hablar) ¡___ más despacio!", "Habla", "Hablas", "Hable", "Hablad", "Imperativo tú = 3a persona del presente."),
      ("(vosotros, escuchar) ¡___ al profesor!", "Escuchad", "Escuchan", "Escuche", "Escuchas", "-ar → -ad."),
      ("(tú, venir) ¡___ aquí!", "Ven", "Viene", "Venga", "Venid", "Irregular."),
      ("Negativo (tú, comer): ¡No ___ eso!", "comas", "come", "comed", "comer", "No + subjuntivo.")]),
    ("La obligación", "Completa.", [
      ("« Il faut étudier » :", "Hay que estudiar", "Tiene estudiar", "Es estudiar", "Debo de estudiar mucho siempre", "Obligación impersonal."),
      ("« Je dois partir » :", "Tengo que irme", "Hay que yo irme", "Soy que irme", "Estoy irme", "Obligación personal."),
      ("« Tu dois travailler » :", "Debes trabajar", "Hay trabajar", "Tienes trabajar", "Eres que trabajar", "Deber + infinitivo."),
      ("« Il ne faut pas fumer » :", "No hay que fumar", "No tengo fumar", "Hay no fumar", "No es fumar", "Negación.")]),
    ("Vocabulario: el colegio", "Traduce.", [
      ("« le professeur » :", "el profesor", "el alumno", "el director de banco", "el libro", "Escuela."),
      ("« le cahier » :", "el cuaderno", "el bolígrafo", "la mesa", "la pizarra", "Material."),
      ("« la récréation » :", "el recreo", "la recreación teatral", "la clase", "el examen", "Escuela."),
      ("« le tableau » :", "la pizarra", "el cuadro de pintura", "la tabla de multiplicar", "la puerta", "En clase.")])]),
  d("espagnol", "Espagnol (LV2)", 3, [
    ("Comparativos", "Elige.", [
      ("Dakar es ___ grande ___ Thiès.", "más / que", "tan / que", "más / como", "menos / de", "Superioridad."),
      ("Awa es ___ alta ___ Fatou.", "tan / como", "tan / que", "más / como", "tanto / que", "Igualdad."),
      ("Comparativo de « bueno »:", "mejor", "más bueno", "bueno más", "óptimo", "Irregular."),
      ("Comparativo de « malo »:", "peor", "más malo que nunca", "malísimo", "pésimo", "Irregular.")]),
    ("Superlativos", "Elige.", [
      ("Es el alumno ___ trabajador de la clase.", "más", "muy", "tan", "mucho", "Superlativo relativo: el más… de."),
      ("Superlativo absoluto de « rápido »:", "rapidísimo", "más rápido", "rápido muy", "el rápido", "-ísimo."),
      ("« le plus grand pays d'Afrique » :", "el país más grande de África", "el país más grande que África", "el más país grande de África", "el país grandísimo en África", "Estructura."),
      ("« très intéressant » :", "muy interesante", "mucho interesante", "tan interesante", "más interesante", "Muy + adjetivo.")]),
    ("Comprensión: la ciudad", "« En Madrid hay mucho tráfico, pero el metro es rápido y barato. »", [
      ("¿Qué hay en Madrid?", "mucho tráfico", "poco tráfico", "un río grande", "playas", "Texto."),
      ("El metro es", "rápido y barato", "lento y caro", "rápido y caro", "peligroso", "Texto."),
      ("« barato » significa", "bon marché", "cher", "rapide", "bateau", "Vocabulario."),
      ("« pero » significa", "mais", "pour", "donc", "parce que", "Conector.")])]),
  d("espagnol", "Espagnol (LV2)", 4, [
    ("Pronombres complementos", "Sustituye.", [
      ("Veo a María → ___ veo.", "La", "Le", "Lo", "Les", "COD femenino."),
      ("Doy el libro a Pedro → ___ doy el libro.", "Le", "Lo", "La", "Se", "COI."),
      ("Doy el libro a Pedro → ___ ___ doy.", "Se lo", "Le lo", "Lo le", "Se la", "Le + lo → se lo."),
      ("Quiero comprarlo = ___ quiero comprar.", "Lo", "Le", "La", "Se", "Pronombre antepuesto o enclítico.")]),
    ("El pretérito indefinido", "Elige.", [
      ("Ayer (comprar, yo) ___ pan.", "compré", "compraba", "compro", "compraré", "Acción puntual."),
      ("El año pasado (ir, nosotros) ___ a Saint-Louis.", "fuimos", "íbamos", "vamos", "iremos", "Irregular."),
      ("(hacer, él) ___ los deberes.", "hizo", "hació", "hace", "hacía ayer una vez", "Irregular."),
      ("(estar, ellos) ___ en casa.", "estuvieron", "estaron", "estuveron", "estaban siempre ayer", "Irregular.")]),
    ("Expresión escrita", "Escribes una carta a un amigo español.", [
      ("Saludo:", "Querido amigo:", "Muy señor mío:", "Adiós:", "Hasta luego:", "Carta informal."),
      ("Despedida:", "Un abrazo", "Atentamente le saluda", "Buenos días", "Bienvenido", "Informal."),
      ("« J'espère que tu vas bien » :", "Espero que estés bien", "Espero que estás bien", "Espero tú bien", "Esperar que bien", "Esperar que + subjuntivo."),
      ("« À bientôt » :", "Hasta pronto", "Hasta ayer", "Pronto hasta", "Adiós para siempre", "Expresión.")])]),
  d("espagnol", "Espagnol (LV2)", 5, [
    ("Comprensión: el medio ambiente", "« Debemos proteger los árboles porque producen oxígeno y dan sombra. »", [
      ("¿Qué debemos proteger?", "los árboles", "los coches", "las casas", "los ríos", "Texto."),
      ("Los árboles producen", "oxígeno", "plástico", "petróleo", "humo", "Texto."),
      ("« sombra » significa", "ombre", "sombre", "soleil", "pluie", "Vocabulario."),
      ("« porque » expresa", "la causa", "la consecuencia", "la oposición", "el tiempo", "Conector.")]),
    ("Gramática: ser y estar", "Elige.", [
      ("Mi madre ___ profesora.", "es", "está", "hay", "tiene", "Profesión → ser."),
      ("Hoy ___ cansado.", "estoy", "soy", "hay", "tengo", "Estado pasajero → estar."),
      ("Dakar ___ en Senegal.", "está", "es", "hay", "tiene", "Localización → estar."),
      ("La mesa ___ de madera.", "es", "está", "hay", "tiene", "Materia → ser.")]),
    ("Vocabulario: el tiempo libre", "Traduce.", [
      ("« la lutte » (sport):", "la lucha", "la luz", "el lujo", "la lluvia", "Deporte tradicional."),
      ("« aller au cinéma » :", "ir al cine", "ir a la cine", "andar cine", "ver cine ir", "Expresión."),
      ("« la plage » :", "la playa", "la plaza", "la plaga", "la página", "Ocio."),
      ("« danser » :", "bailar", "cantar", "dansar", "bajar", "Verbo.")])]),
  d("espagnol", "Espagnol (LV2)", 6, [
    ("Síntesis gramatical", "Elige la forma correcta.", [
      ("Cuando (ser, yo) ___ pequeño, (jugar) ___ mucho.", "era / jugaba", "fui / jugué", "soy / juego", "sería / jugaría", "Imperfecto."),
      ("¡No (hablar, tú) ___ en clase!", "hables", "hablas", "habla", "hablar", "Imperativo negativo."),
      ("Es el día ___ feliz de mi vida.", "más", "muy", "tan", "mucho", "Superlativo."),
      ("Hay que ___ los deberes.", "hacer", "hago", "hace", "haciendo", "Hay que + infinitivo.")]),
    ("Síntesis de comprensión", "« El sábado pasado fui al mercado con mi abuela. Compramos pescado y verduras. »", [
      ("¿Cuándo fue al mercado?", "el sábado pasado", "el domingo", "hoy", "mañana", "Texto."),
      ("¿Con quién?", "con su abuela", "con su madre", "solo", "con su primo", "Texto."),
      ("¿Qué compraron?", "pescado y verduras", "carne y pan", "ropa", "libros", "Texto."),
      ("« fui » es el pretérito de", "ir (o ser)", "hacer", "estar", "fumar", "Irregular.")]),
    ("Civilización", "Elige.", [
      ("Capital de España:", "Madrid", "Barcelona", "Sevilla", "Valencia", "Cultura general."),
      ("Lengua oficial de México:", "el español", "el portugués", "el inglés", "el francés", "Hispanoamérica."),
      ("País de Sudamérica de lengua portuguesa:", "Brasil", "Argentina", "Chile", "Perú", "No hispanohablante."),
      ("País africano de lengua oficial española:", "Guinea Ecuatorial", "Senegal", "Ghana", "Mali", "Antigua colonia española.")])]),
])
