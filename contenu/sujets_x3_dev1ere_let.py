# Première (S, L, G) : devoirs types en plus de français, histoire-géographie, anglais et espagnol, 2 par trimestre.
# Rédigés pour l'appli sur le programme officiel, non officiels.
from sujets_dev_common import D, pack, TRIM
LV = ["1ère L", "1ère S", "1ère G"]
def d(s, name, n, exos):
    t = (n + 1) // 2
    an, g = D(f"dev-1ere-{s}-{n}", LV[0], name, n, exos, duration="3 h", label=f"{TRIM[t]} · devoir {2 - n % 2}")
    an["levels"] = LV
    return an, g

ANNALES_X, GUIDED_X = pack([
  # ================= Français
  d("francais", "Français", 1, [
    ("Le classicisme", "Le XVIIe siècle français.", [
      ("Règle classique du théâtre :", "les trois unités (temps, lieu, action)", "le mélange des genres", "l'absence de règles", "le vers libre", "Doctrine classique."),
      ("Auteur de « Le Cid » :", "Corneille", "Molière", "Racine", "Voltaire", "1637."),
      ("Auteur de « Phèdre » :", "Racine", "Corneille", "Molière", "Hugo", "Tragédie de 1677."),
      ("Idéal de l'homme classique :", "l'honnête homme", "le héros romantique", "le philosophe des Lumières", "le surhomme", "Mesure et raison.")]),
    ("La comédie de Molière", "Extrait : « HARPAGON : Au voleur ! au voleur ! à l'assassin ! au meurtrier ! » (L'Avare)", [
      ("Registre :", "comique", "tragique", "lyrique", "épique", "Exagération de l'avare."),
      ("Procédé comique :", "la répétition et la gradation", "la litote", "l'euphémisme", "l'alexandrin seul", "Comique de mots."),
      ("Défaut critiqué :", "l'avarice", "la jalousie", "la paresse", "le courage", "Caractère d'Harpagon."),
      ("Fonction de la comédie selon Molière :", "corriger les mœurs en faisant rire", "faire peur", "raconter l'histoire de France", "chanter l'amour", "Castigat ridendo mores.")]),
    ("Langue : versification", "« Va, je ne te hais point. » (Corneille)", [
      ("Figure de style :", "une litote", "une hyperbole", "une métaphore", "une anaphore", "Dire moins pour suggérer plus : « je t'aime »."),
      ("Vers de la tragédie classique :", "l'alexandrin", "l'octosyllabe", "le vers libre", "le décasyllabe", "12 syllabes."),
      ("La césure de l'alexandrin se place", "après la 6e syllabe", "après la 4e syllabe", "après la 8e syllabe", "il n'y en a pas", "Hémistiches."),
      ("Une diérèse consiste à", "prononcer en deux syllabes une suite de voyelles", "supprimer un e muet", "répéter un son", "changer de rime", "Ex. li-on.")])]),
  d("francais", "Français", 2, [
    ("Les Lumières", "Le XVIIIe siècle.", [
      ("Les philosophes des Lumières défendent", "la raison, la tolérance et la liberté", "la monarchie absolue de droit divin", "l'esclavage", "la censure", "Idéaux."),
      ("Œuvre collective dirigée par Diderot et d'Alembert :", "l'Encyclopédie", "Candide", "Les Misérables", "Le Cid", "1751-1772."),
      ("Auteur de « Candide » :", "Voltaire", "Rousseau", "Montesquieu", "Diderot", "Conte philosophique (1759)."),
      ("« De l'esprit des lois » défend", "la séparation des pouvoirs", "la monarchie absolue", "la religion d'État", "l'esclavage", "Montesquieu (1748).")]),
    ("L'ironie", "« Ceux dont il s'agit sont noirs depuis les pieds jusqu'à la tête ; et ils ont le nez si écrasé qu'il est presque impossible de les plaindre. » (Montesquieu, De l'esprit des lois, 1748, « De l'esclavage des nègres »)", [
      ("Procédé majeur du texte :", "l'ironie", "le lyrisme", "l'épopée", "la litote amoureuse", "L'auteur dit le contraire de sa pensée."),
      ("Montesquieu critique en réalité", "l'esclavage", "les Africains", "le commerce du sucre seulement", "la religion chrétienne seule", "Argumentation indirecte."),
      ("Ce type d'argumentation est", "indirect", "direct", "narratif", "descriptif", "Le lecteur doit déduire la thèse."),
      ("L'effet attendu sur le lecteur :", "l'indignation", "le rire léger", "la peur", "l'indifférence", "Les arguments absurdes choquent.")]),
    ("Le conte philosophique", "On étudie « Candide ».", [
      ("Un conte philosophique", "utilise un récit pour défendre des idées", "est un poème lyrique", "est une pièce de théâtre", "n'a pas de morale", "Genre des Lumières."),
      ("Cible de Voltaire dans Candide :", "l'optimisme naïf de Pangloss", "la science", "la liberté", "la tolérance", "« Tout est au mieux »."),
      ("Phrase finale célèbre :", "« Il faut cultiver notre jardin. »", "« Va, je ne te hais point. »", "« Je pense donc je suis. »", "« Liberté, égalité, fraternité. »", "Conclusion de Candide."),
      ("Épisode du nègre de Surinam dénonce", "l'esclavage", "la guerre seule", "le climat", "la religion musulmane", "« C'est à ce prix que vous mangez du sucre ».")])]),
  d("francais", "Français", 3, [
    ("Le romantisme", "Le XIXe siècle.", [
      ("Le romantisme exalte", "les sentiments, la nature et le moi", "la raison seule", "les règles classiques", "la science", "Lyrisme."),
      ("Chef de file du romantisme français :", "Victor Hugo", "Molière", "Zola", "Voltaire", "Préface de Cromwell."),
      ("« Le Lac » est un poème de", "Lamartine", "Baudelaire", "Rimbaud", "Senghor", "Fuite du temps."),
      ("Le drame romantique", "mélange le sublime et le grotesque", "respecte les trois unités", "est toujours comique", "est en prose seulement", "Rupture avec le classicisme.")]),
    ("Le réalisme et le naturalisme", "On compare Balzac et Zola.", [
      ("Le roman réaliste cherche à", "représenter fidèlement la société", "raconter des rêves", "chanter l'amour idéal", "décrire des mondes magiques", "Objectivité."),
      ("Auteur de « Germinal » :", "Zola", "Balzac", "Flaubert", "Hugo", "Naturalisme (1885)."),
      ("Cycle de romans de Balzac :", "La Comédie humaine", "Les Rougon-Macquart", "Les Fleurs du mal", "Les Contemplations", "Plus de 90 œuvres."),
      ("Le naturalisme insiste sur", "l'hérédité et le milieu", "le merveilleux", "les dieux", "la mythologie", "Méthode scientifique de Zola.")]),
    ("Commentaire", "« Demain, dès l'aube, à l'heure où blanchit la campagne, / Je partirai. » (Hugo, Les Contemplations)", [
      ("Registre :", "lyrique et élégiaque", "comique", "épique", "satirique", "Deuil de sa fille Léopoldine."),
      ("Temps dominant :", "futur", "passé simple", "imparfait", "présent de vérité générale", "« Je partirai »."),
      ("Effet du rejet « Je partirai » :", "mettre en valeur la détermination", "créer le rire", "faire une rime riche", "supprimer le sens", "Enjambement."),
      ("La chute du poème révèle", "qu'il se rend sur la tombe de sa fille", "un rendez-vous amoureux", "un voyage d'affaires", "une guerre", "Effet de surprise.")])]),
  d("francais", "Français", 4, [
    ("La Négritude", "Mouvement des années 1930.", [
      ("Fondateurs de la Négritude :", "Senghor, Césaire, Damas", "Hugo, Zola, Balzac", "Sembène, Bâ, Kane", "Voltaire, Rousseau, Diderot", "Étudiants à Paris."),
      ("Revue fondée en 1935 :", "L'Étudiant noir", "Présence Africaine seulement", "Le Figaro", "L'Encyclopédie", "Naissance du mouvement."),
      ("« Cahier d'un retour au pays natal » est de", "Aimé Césaire", "Senghor", "Damas", "Birago Diop", "1939."),
      ("Objectif de la Négritude :", "revendiquer et valoriser l'identité noire", "imiter la culture européenne", "abandonner l'écriture", "refuser toute langue", "Affirmation culturelle.")]),
    ("Le théâtre africain", "On étudie « L'Exil d'Albouri » de Cheikh Aliou Ndao.", [
      ("Albouri Ndiaye était le roi du", "Djolof", "Cayor", "Walo", "Sine", "Bourba Djolof."),
      ("Thème central :", "la résistance à la colonisation et le choix entre l'exil et la soumission", "un amour impossible", "un conflit d'argent", "une fête", "Drame historique."),
      ("Autre pièce historique africaine :", "« Chaka » de Senghor ou « La Mort de Chaka » de Seydou Badian", "« Le Cid »", "« Candide »", "« Germinal »", "Héros africains."),
      ("Fonction de ce théâtre :", "exalter l'histoire et les valeurs africaines", "faire rire seulement", "copier Molière", "décrire la science", "Engagement.")]),
    ("Poésie de la Négritude", "« Nous sommes les hommes de la danse, dont les pieds reprennent vigueur en frappant le sol dur. » (Senghor, extrait)", [
      ("Valeur mise en avant :", "le rythme et la danse", "la science", "l'argent", "la solitude", "Esthétique senghorienne."),
      ("Pronom « Nous » exprime", "une identité collective", "le poète seul", "les colons", "le lecteur européen seul", "Communauté."),
      ("Le verset senghorien est", "une longue phrase rythmée", "un alexandrin rimé", "un haïku", "un vers de 8 syllabes", "Forme libre."),
      ("Registre :", "lyrique", "comique", "satirique", "fantastique", "Célébration.")])]),
  d("francais", "Français", 5, [
    ("Convaincre et persuader", "On distingue les stratégies argumentatives.", [
      ("Convaincre, c'est s'adresser surtout", "à la raison", "aux sentiments", "aux sens", "à l'imagination seule", "Arguments logiques."),
      ("Persuader, c'est s'adresser surtout", "aux sentiments", "à la raison seule", "aux chiffres", "aux lois", "Émotion."),
      ("Argument d'autorité :", "s'appuyer sur un expert reconnu", "s'appuyer sur une rumeur", "insulter l'adversaire", "répéter sa thèse", "Ex. citer un médecin."),
      ("Raisonnement qui va du général au particulier :", "déductif", "inductif", "concessif", "par analogie", "Définition.")]),
    ("Dissertation", "Sujet : « La littérature doit-elle s'engager ? »", [
      ("Problématique possible :", "La littérature a-t-elle pour mission de défendre des causes ?", "Qui a écrit Candide ?", "Combien coûte un livre ?", "Quelle est la date de la Négritude ?", "Question qui reformule le sujet."),
      ("Exemple d'œuvre engagée :", "« Les Bouts de bois de Dieu » d'Ousmane Sembène", "un dictionnaire", "un annuaire", "une recette de cuisine", "Grève des cheminots."),
      ("Plan adapté :", "dialectique", "chronologique", "descriptif", "alphabétique", "Question fermée."),
      ("Pour la nuance, on peut citer", "l'art pour l'art (Gautier)", "uniquement des chiffres", "des slogans", "des recettes", "Autre conception.")]),
    ("Langue : connecteurs logiques", "Choisir le bon connecteur.", [
      ("Rapport de cause :", "car", "pourtant", "donc", "cependant", "Cause."),
      ("Rapport de conséquence :", "si bien que", "bien que", "puisque", "malgré", "Conséquence."),
      ("Rapport de concession :", "bien que", "parce que", "donc", "ainsi", "+ subjonctif."),
      ("Rapport d'addition :", "de plus", "néanmoins", "car", "afin que", "Ajout.")])]),
  d("francais", "Français", 6, [
    ("Figures de style", "Identifier la figure.", [
      ("« Cette obscure clarté qui tombe des étoiles » :", "oxymore", "métaphore filée", "litote", "anaphore", "Deux termes contradictoires."),
      ("« Paris a froid, Paris a faim » :", "anaphore", "chiasme", "oxymore", "antiphrase", "Répétition en tête."),
      ("« Il faut manger pour vivre et non vivre pour manger » :", "chiasme", "hyperbole", "litote", "personnification", "Structure ABBA."),
      ("« Le vent hurlait dans la nuit » :", "personnification", "comparaison", "litote", "euphémisme", "Le vent agit comme un être vivant.")]),
    ("Synthèse des mouvements", "Associe auteur et mouvement.", [
      ("Racine :", "classicisme", "romantisme", "Lumières", "Négritude", "XVIIe siècle."),
      ("Rousseau :", "Lumières", "classicisme", "réalisme", "Négritude", "XVIIIe siècle."),
      ("Flaubert :", "réalisme", "romantisme", "classicisme", "surréalisme", "Madame Bovary."),
      ("Damas :", "Négritude", "Lumières", "classicisme", "naturalisme", "Pigments (1937).")]),
    ("Méthode : le commentaire composé", "On prépare un commentaire.", [
      ("Le commentaire s'organise en", "axes de lecture (parties thématiques)", "lignes successives", "résumé du texte", "liste de figures sans analyse", "Méthode."),
      ("Chaque idée doit être", "justifiée par une citation analysée", "affirmée sans preuve", "recopiée du cours", "écrite en style télégraphique", "Analyse."),
      ("Situer le texte dans l'introduction, c'est donner", "l'auteur, l'œuvre, la date, le contexte", "son opinion", "le plan seulement", "la conclusion", "Présentation."),
      ("La paraphrase consiste à", "répéter le texte sans l'analyser (à éviter)", "analyser en profondeur", "citer correctement", "conclure", "Défaut fréquent.")])]),
  # ================= Histoire-Géographie
  d("hg", "Histoire-Géographie", 1, [
    ("La Première Guerre mondiale", "1914-1918.", [
      ("Événement déclencheur :", "l'assassinat de l'archiduc François-Ferdinand à Sarajevo", "l'invasion de la Pologne", "la crise de 1929", "Pearl Harbor", "28 juin 1914."),
      ("La Triple Entente regroupe", "France, Royaume-Uni, Russie", "Allemagne, Autriche-Hongrie, Italie", "États-Unis, Japon, Chine", "Sénégal, Mali, Guinée", "Alliance."),
      ("Bataille symbole de 1916 :", "Verdun", "Stalingrad", "Waterloo", "Dien Bien Phu", "Guerre de position."),
      ("Fin de la guerre :", "armistice du 11 novembre 1918", "8 mai 1945", "14 juillet 1789", "4 avril 1960", "Signature à Rethondes.")]),
    ("L'Afrique dans la Grande Guerre", "Les tirailleurs sénégalais.", [
      ("Député qui organise le recrutement en AOF en 1918 :", "Blaise Diagne", "Lamine Guèye", "Senghor", "Mamadou Dia", "Commissaire de la République."),
      ("Nombre approximatif de soldats d'AOF mobilisés :", "près de 200 000", "2 000", "2 millions", "20", "Effort de guerre."),
      ("Conséquence en Afrique :", "révoltes contre le recrutement forcé", "indépendance immédiate", "fin de la colonisation", "aucune", "Résistances."),
      ("Traité qui met fin à la guerre avec l'Allemagne :", "Versailles (1919)", "Berlin (1885)", "Paris (1947)", "Rome (1957)", "Conditions sévères.")]),
    ("Bilan", "Les conséquences de la guerre.", [
      ("Nombre de morts environ :", "10 millions de soldats", "1 000", "100 millions", "50 000", "Guerre totale."),
      ("Organisation créée en 1919-1920 :", "la SDN", "l'ONU", "l'OTAN", "l'UA", "Société des Nations."),
      ("Empires disparus :", "austro-hongrois et ottoman", "britannique et français", "japonais et chinois", "malien et songhaï", "Nouvelles frontières."),
      ("Révolution de 1917 :", "en Russie", "en France", "en Allemagne", "aux États-Unis", "Bolcheviks.")])]),
  d("hg", "Histoire-Géographie", 2, [
    ("La crise de 1929", "Le krach de Wall Street.", [
      ("Le krach boursier a lieu à", "New York", "Paris", "Berlin", "Londres", "Octobre 1929."),
      ("Conséquence majeure :", "chômage massif", "croissance rapide", "plein-emploi", "fin de l'industrie", "Grande Dépression."),
      ("Politique de Roosevelt :", "le New Deal", "le plan Marshall", "la NEP", "le Front populaire", "Intervention de l'État."),
      ("La crise touche les colonies car", "le prix des matières premières s'effondre", "elles deviennent riches", "elles sont indépendantes", "elles n'exportent rien", "Arachide moins chère.")]),
    ("Les totalitarismes", "Italie, Allemagne, URSS.", [
      ("Régime de Mussolini :", "le fascisme", "le nazisme", "le stalinisme", "la démocratie", "Italie, 1922."),
      ("Hitler arrive au pouvoir en", "1933", "1919", "1939", "1945", "Chancelier."),
      ("Caractéristique d'un régime totalitaire :", "parti unique et propagande", "élections libres", "liberté de la presse", "séparation des pouvoirs", "Contrôle total."),
      ("Dirigeant de l'URSS dans les années 1930 :", "Staline", "Lénine", "Gorbatchev", "Trotski", "Terreur et goulag.")]),
    ("Méthode : étudier une affiche de propagande", "On analyse une affiche des années 1930.", [
      ("Une propagande cherche à", "influencer l'opinion", "informer objectivement", "divertir seulement", "vendre un produit", "Manipulation."),
      ("On identifie d'abord", "l'auteur, la date et le contexte", "les couleurs préférées", "le prix", "la taille", "Présentation."),
      ("Procédé fréquent :", "le culte du chef", "la neutralité", "le débat contradictoire", "l'humour critique", "Image du chef."),
      ("La conclusion de l'analyse montre", "le message et ses limites", "seulement la date", "la beauté", "rien", "Esprit critique.")])]),
  d("hg", "Histoire-Géographie", 3, [
    ("La Seconde Guerre mondiale", "1939-1945.", [
      ("Début de la guerre :", "invasion de la Pologne par l'Allemagne (1er septembre 1939)", "Pearl Harbor", "Sarajevo", "le krach de 1929", "Déclaration de guerre."),
      ("Entrée en guerre des États-Unis :", "décembre 1941 après Pearl Harbor", "1939", "1945", "1914", "Attaque japonaise."),
      ("Tournant à l'Est :", "Stalingrad (1942-1943)", "Verdun", "la Marne", "Waterloo", "Défaite allemande."),
      ("Fin en Europe :", "8 mai 1945", "11 novembre 1918", "6 juin 1944", "2 septembre 1945", "Capitulation allemande.")]),
    ("L'Afrique dans la guerre", "Le rôle des colonies.", [
      ("Massacre de tirailleurs à Thiaroye :", "1er décembre 1944", "1918", "1960", "1939", "Ils réclamaient leurs soldes."),
      ("Ville devenue capitale de la France libre :", "Brazzaville", "Dakar", "Alger seulement", "Abidjan", "Conférence de 1944."),
      ("Conférence de Brazzaville (1944) annonce", "des réformes dans les colonies", "l'indépendance immédiate", "la fin de l'Afrique", "la guerre au Sénégal", "Promesses."),
      ("Bataille de Dakar (1940) :", "tentative des Alliés contre les forces de Vichy", "victoire allemande en Afrique", "combat contre le Japon", "révolte des tirailleurs", "Septembre 1940.")]),
    ("Bilan et génocide", "Conséquences.", [
      ("Génocide des Juifs :", "la Shoah", "le Rwanda", "Verdun", "Thiaroye", "Environ 6 millions de victimes."),
      ("Organisation créée en 1945 :", "l'ONU", "la SDN", "l'OUA", "la CEDEAO", "Charte de San Francisco."),
      ("Bombes atomiques en 1945 :", "Hiroshima et Nagasaki", "Berlin et Rome", "Londres et Paris", "Tokyo et Pékin", "Août 1945."),
      ("Nombre de morts total environ :", "plus de 50 millions", "10 000", "1 million", "500 millions", "Guerre la plus meurtrière.")])]),
  d("hg", "Histoire-Géographie", 4, [
    ("La mondialisation", "Notions.", [
      ("La mondialisation est", "l'intensification des échanges à l'échelle mondiale", "la fin du commerce", "la fermeture des frontières", "un phénomène local", "Définition."),
      ("Acteurs majeurs :", "les firmes transnationales", "les villages isolés", "les clubs de sport seulement", "les écoles primaires", "FTN."),
      ("Organisation qui régule le commerce mondial :", "l'OMC", "l'OMS", "l'UNESCO", "la FIFA", "Organisation mondiale du commerce."),
      ("Les flux de la mondialisation :", "marchandises, capitaux, personnes, informations", "seulement l'eau", "seulement l'air", "aucun", "Types de flux.")]),
    ("Les pôles de la mondialisation", "La Triade et les pays émergents.", [
      ("La Triade :", "Amérique du Nord, Europe, Asie orientale", "Afrique, Amérique du Sud, Océanie", "Sénégal, Mali, Mauritanie", "Chine, Inde, Brésil", "Centres de décision."),
      ("Pays émergents (BRICS) :", "Brésil, Russie, Inde, Chine, Afrique du Sud", "France, Allemagne, Italie", "Sénégal, Gambie, Guinée", "Japon, Corée, Taïwan", "Puissances en croissance."),
      ("Les ports et les conteneurs illustrent", "la maritimisation des échanges", "la fin du commerce", "l'agriculture", "le tourisme", "90 % du commerce par mer."),
      ("Les espaces en marge :", "certaines régions enclavées et pauvres", "les grandes métropoles", "les ports mondiaux", "les places boursières", "Inégalités.")]),
    ("Croquis : les flux mondiaux", "On réalise un croquis de la mondialisation.", [
      ("Les flux se représentent par", "des flèches", "des points seulement", "des hachures", "du texte", "Langage cartographique."),
      ("L'épaisseur d'une flèche indique", "l'importance du flux", "la couleur", "la date", "le nom du pays", "Proportionnalité."),
      ("Les métropoles mondiales se représentent par", "des cercles ou carrés", "des flèches", "des lignes", "rien", "Figurés ponctuels."),
      ("La légende doit être", "organisée en parties", "absente", "en désordre", "écrite en anglais seulement", "Clarté.")])]),
  d("hg", "Histoire-Géographie", 5, [
    ("Le Sénégal dans la mondialisation", "Atouts et contraintes.", [
      ("Atout majeur du Sénégal :", "sa position atlantique et le port de Dakar", "un relief montagneux", "l'absence de côtes", "la neige", "Porte de l'Afrique de l'Ouest."),
      ("Grand projet portuaire récent :", "le port de Ndayane", "le port de Kayar", "le port de Matam", "le port de Kédougou", "Port en eau profonde."),
      ("Hydrocarbures exploités en mer depuis 2024-2025 :", "Sangomar (pétrole) et GTA (gaz)", "Taïba", "Sabodala", "Diama", "Offshore."),
      ("Organisation régionale à laquelle appartient le Sénégal :", "la CEDEAO", "l'Union européenne", "l'ASEAN", "le Mercosur", "Afrique de l'Ouest.")]),
    ("Les échanges du Sénégal", "Commerce extérieur.", [
      ("Le Sénégal importe surtout", "riz, produits pétroliers, machines", "or", "arachide", "phosphates", "Dépendance alimentaire et énergétique."),
      ("Il exporte notamment", "or, produits halieutiques, acide phosphorique", "voitures", "avions", "blé", "Matières premières."),
      ("Les transferts des émigrés", "sont une source importante de revenus", "n'existent pas", "sont interdits", "sont négligeables", "Diaspora."),
      ("La balance commerciale du Sénégal est", "souvent déficitaire", "toujours très excédentaire", "toujours nulle", "inconnue", "Importations > exportations.")]),
    ("Plan Sénégal et développement", "Les stratégies nationales.", [
      ("Infrastructure de transport récente à Dakar :", "le TER", "le métro de Paris", "le canal de Suez", "le tunnel sous la Manche", "Train express régional."),
      ("Aéroport international ouvert en 2017 :", "AIBD (Blaise Diagne)", "Léopold Sédar Senghor", "Cap Skirring", "Ziguinchor", "Diass."),
      ("Ville nouvelle et pôle industriel :", "Diamniadio", "Gorée", "Podor", "Bakel", "Pôle urbain."),
      ("Défi du Sénégal dans la mondialisation :", "transformer ses ressources sur place", "tout exporter brut", "fermer ses ports", "abandonner l'école", "Valeur ajoutée.")])]),
  d("hg", "Histoire-Géographie", 6, [
    ("Synthèse histoire", "Révision des deux guerres.", [
      ("Ordre chronologique :", "Grande Guerre, crise de 1929, Seconde Guerre mondiale", "crise de 1929, Grande Guerre, Seconde Guerre", "Seconde Guerre, crise, Grande Guerre", "Grande Guerre, Seconde Guerre, crise de 1929", "Repères."),
      ("La SDN a échoué car", "elle n'avait pas d'armée et les grandes puissances l'ont quittée", "elle était trop puissante", "elle a gagné toutes les guerres", "elle n'existait pas", "Faiblesse."),
      ("Tirailleurs sénégalais :", "soldats africains de l'armée coloniale française", "pêcheurs", "commerçants", "députés", "Créés en 1857."),
      ("La Seconde Guerre mondiale accélère", "la décolonisation", "la colonisation", "la traite", "la féodalité", "Affaiblissement des métropoles.")]),
    ("Synthèse géographie", "Révision de la mondialisation.", [
      ("Une FTN est", "une entreprise implantée dans plusieurs pays", "une école", "un village", "une ONG locale", "Firme transnationale."),
      ("Exemple d'interface maritime :", "la Northern Range (ports d'Europe du Nord)", "le Sahara", "les Alpes", "le lac Tchad", "Façade portuaire."),
      ("La fracture numérique est", "l'inégal accès aux technologies", "la panne d'électricité", "un virus", "une loi", "Inégalités."),
      ("Le Sénégal est surtout", "un pays en développement intégré par ses ports et ses ressources", "une puissance de la Triade", "un pays enclavé", "un pays sans échanges", "Position.")]),
    ("Méthode : la composition", "Sujet : « Les conséquences de la Seconde Guerre mondiale ».", [
      ("Bonne problématique :", "En quoi la guerre bouleverse-t-elle le monde après 1945 ?", "Quand Hitler est-il né ?", "Quelle est la capitale de l'Allemagne ?", "Qui a gagné le match ?", "Question ouverte."),
      ("Plan thématique possible :", "bilan humain, bilan politique, bilan colonial", "1939, 1940, 1941", "Europe, Asie, Afrique sans idées", "introduction, conclusion", "Organisation."),
      ("Exemple précis :", "la création de l'ONU en 1945", "il y a eu des problèmes", "beaucoup de choses", "c'était triste", "Précision."),
      ("Ouverture de la conclusion :", "la guerre froide", "la Renaissance", "la préhistoire", "la Grande Guerre", "Suite logique.")])]),
  # ================= Anglais
  d("anglais", "Anglais", 1, [
    ("Inversion", "Choose the correct sentence.", [
      ("« Never ___ such a beautiful place. »", "have I seen", "I have seen", "I saw", "seen I have", "Inversion after a negative adverb."),
      ("« Hardly ___ arrived when it started to rain. »", "had we", "we had", "we have", "did we arrived", "Hardly + had + subject."),
      ("« Not only ___ clever, but she is also kind. »", "is she", "she is", "she does", "does she is", "Not only + inversion."),
      ("« Rarely ___ late. »", "does he come", "he comes", "comes he", "he does come", "Auxiliary do.")]),
    ("Past conditional", "Complete.", [
      ("If I had known, I ___ you.", "would have helped", "would help", "will help", "had helped", "Third conditional."),
      ("Had she worked harder, she ___ .", "would have succeeded", "will succeed", "succeeds", "succeeded", "Inversion of if."),
      ("I wish I ___ that.", "hadn't said", "didn't say", "don't say", "won't say", "Regret about the past."),
      ("If only he ___ earlier!", "had left", "leaves", "will leave", "has left", "Past regret.")]),
    ("Reading: migration", "« Many young Africans dream of going abroad. However, some of them take dangerous routes across the sea. Others choose to stay and build businesses at home. »", [
      ("What do many young Africans dream of?", "going abroad", "staying at home only", "becoming fishermen", "going to school", "Line 1."),
      ("« However » expresses", "contrast", "cause", "addition", "time", "Connector."),
      ("Why are some routes dangerous?", "they cross the sea", "they are expensive only", "they are too short", "they are forbidden roads", "Line 2."),
      ("What do others choose?", "to stay and build businesses", "to travel by plane", "to stop working", "to go to Europe", "Line 3.")])]),
  d("anglais", "Anglais", 2, [
    ("Modals in the past", "Choose.", [
      ("He isn't here. He ___ have missed the bus.", "must", "can't", "should", "needn't", "Logical deduction (certain)."),
      ("You ___ have told me! I was worried.", "should", "must", "can", "may not", "Reproach."),
      ("She ___ have seen you: she was in Thiès.", "can't", "must", "should", "might", "Impossibility."),
      ("You ___ have brought food: there was plenty.", "needn't", "mustn't", "can't", "should", "Unnecessary action.")]),
    ("Gerund and infinitive", "Choose.", [
      ("I remember ___ him at the market.", "seeing", "to see", "see", "saw", "Remember + -ing = past memory."),
      ("Remember ___ the door before leaving.", "to lock", "locking", "lock", "locked", "Remember + to = future duty."),
      ("He is interested in ___ medicine.", "studying", "to study", "study", "studied", "Preposition + -ing."),
      ("It's no use ___.", "crying", "to cry", "cry", "cried", "Fixed expression.")]),
    ("Vocabulary: technology", "Find the word.", [
      ("« un ordinateur portable » :", "a laptop", "a desktop phone", "a mobile table", "a portable order", "Vocabulary."),
      ("« télécharger » :", "to download", "to discharge", "to upload only", "to telecharge", "Verb."),
      ("« les réseaux sociaux » :", "social networks / social media", "social nets fishing", "society roads", "public networks only", "Expression."),
      ("« un mot de passe » :", "a password", "a passport", "a word pass", "a pass key word", "Vocabulary.")])]),
  d("anglais", "Anglais", 3, [
    ("Subjunctive and wishes", "Choose.", [
      ("I wish I ___ taller.", "were", "am", "will be", "be", "Present wish → past form (were)."),
      ("It's high time we ___.", "left", "leave", "will leave", "leaving", "It's time + past."),
      ("I'd rather you ___ here.", "stayed", "stay", "will stay", "staying", "Would rather + past."),
      ("The doctor suggested that he ___ rest.", "(should) rest", "rests", "rested", "resting", "Mandative subjunctive.")]),
    ("Structures", "Choose.", [
      ("He was ___ tired ___ he fell asleep.", "so / that", "such / that", "too / to", "enough / that", "So + adjective + that."),
      ("It was ___ a hot day ___ we stayed inside.", "such / that", "so / that", "too / to", "very / that", "Such + a + noun."),
      ("The more you read, ___ you learn.", "the more", "more", "the most", "most", "Double comparative."),
      ("She is ___ young ___ drive.", "too / to", "so / that", "such / that", "enough / to", "Too + adjective + to.")]),
    ("Reading: environment", "« The Great Green Wall is an African project to plant trees across the Sahel. It aims to stop desertification and create jobs. »", [
      ("Where are trees planted?", "across the Sahel", "in Europe", "in the sea", "in big cities only", "Line 1."),
      ("What does it aim to stop?", "desertification", "rain", "fishing", "tourism", "Line 2."),
      ("Another benefit:", "creating jobs", "closing schools", "building airports", "reducing rain", "Line 2."),
      ("« aims to » means", "a pour but de", "refuse de", "oublie de", "regrette de", "Vocabulary.")])]),
  d("anglais", "Anglais", 4, [
    ("Passive structures", "Transform.", [
      ("« People say he is rich. » →", "He is said to be rich.", "He says to be rich.", "He is saying rich.", "It says he rich.", "Personal passive."),
      ("« Someone stole my phone. » →", "My phone was stolen.", "My phone has stealing.", "My phone stole.", "My phone is steal.", "Past passive."),
      ("« I had my hair cut. » means", "someone cut my hair", "I cut my hair myself", "my hair was long", "I forgot my hair", "Causative have."),
      ("« The road is being repaired. » tense:", "present continuous passive", "simple past passive", "present perfect passive", "future passive", "Is being + PP.")]),
    ("Connectors", "Choose.", [
      ("___ the rain, the match took place.", "Despite", "Although", "Because", "So", "Despite + noun."),
      ("He studied hard ___ pass the exam.", "in order to", "so that he", "because", "although", "Purpose + infinitive."),
      ("___ he was tired, he kept working.", "Even though", "Despite", "Because of", "Due to", "Concession + clause."),
      ("She was ill; ___, she didn't come.", "therefore", "however", "although", "despite", "Consequence.")]),
    ("Writing: a formal letter", "You apply for a summer job.", [
      ("Opening when you don't know the name:", "Dear Sir or Madam,", "Hi guys,", "Dear friend,", "Hello you,", "Formal."),
      ("Closing after « Dear Sir or Madam »:", "Yours faithfully,", "Yours sincerely,", "Love,", "See you,", "Formal rule."),
      ("To express purpose:", "I am writing to apply for…", "I write for apply…", "I am writing for applying…", "I writing to apply…", "Correct form."),
      ("To mention attached documents:", "Please find attached my CV.", "Please find attach my CV.", "My CV is attaching.", "Find my CV attached me.", "Formula.")])]),
  d("anglais", "Anglais", 5, [
    ("Reading: education", "« In Senegal, many pupils study by the light of a mobile phone. Solar lamps could change their lives. »", [
      ("How do many pupils study?", "by the light of a mobile phone", "in libraries only", "during the day only", "with computers", "Line 1."),
      ("What could change their lives?", "solar lamps", "televisions", "cars", "phones", "Line 2."),
      ("« could » expresses", "possibility", "obligation", "past ability only", "prohibition", "Modal."),
      ("Best title:", "Light for learning", "Football in Senegal", "The history of phones", "Fishing at night", "Main idea.")]),
    ("Grammar: mixed", "Choose.", [
      ("I'm looking forward to ___ you.", "seeing", "see", "to see", "saw", "Look forward to + -ing."),
      ("He used to ___ in Ziguinchor.", "live", "living", "lived", "lives", "Used to + base verb."),
      ("By next year, she ___ her degree.", "will have finished", "will finish", "finishes", "finished", "Future perfect."),
      ("You'd better ___ now.", "go", "to go", "going", "gone", "Had better + base verb.")]),
    ("Vocabulary: society", "Translate.", [
      ("« le chômage » :", "unemployment", "employment", "job market place", "chomage", "Vocabulary."),
      ("« l'égalité des chances » :", "equal opportunities", "chance equality game", "lucky equality", "same chance only", "Expression."),
      ("« la pauvreté » :", "poverty", "poorness street", "property", "power", "Vocabulary."),
      ("« un droit » :", "a right", "a straight", "a law only", "a right hand", "Human rights.")])]),
  d("anglais", "Anglais", 6, [
    ("Synthesis: grammar", "Choose.", [
      ("Never ___ such a long speech.", "had I heard", "I had heard", "I heard", "heard I", "Inversion."),
      ("If I had had money, I ___ the bike.", "would have bought", "would buy", "will buy", "bought", "Third conditional."),
      ("He must ___ asleep; the light is off.", "be", "being", "to be", "been", "Deduction (present)."),
      ("I wish you ___ lie to me.", "wouldn't", "won't", "don't", "didn't have", "Wish + would: annoyance.")]),
    ("Synthesis: structures", "Choose.", [
      ("It was such ___ that everyone came.", "a good party", "good party", "so good party", "a so good party", "Such a + adj + noun."),
      ("The older he gets, ___ he becomes.", "the wiser", "wiser", "the wisest", "more wise", "Double comparative."),
      ("He is said ___ very rich.", "to be", "being", "be", "that he is", "Passive + infinitive."),
      ("Despite ___ tired, she went on.", "being", "to be", "she was", "was", "Despite + -ing.")]),
    ("Writing: opinion essay", "Topic: « Social media do more harm than good. »", [
      ("A good introduction", "presents the topic and announces your opinion", "lists all arguments in detail", "gives a conclusion", "tells a joke only", "Structure."),
      ("To introduce the opposite view:", "On the other hand,", "Furthermore,", "In addition,", "Moreover,", "Contrast."),
      ("To conclude:", "All things considered,", "First of all,", "For example,", "Besides,", "Conclusion."),
      ("Each paragraph should contain", "one main idea with an example", "five unrelated ideas", "only examples", "no sentence", "Paragraph.")])]),
  # ================= Espagnol
  d("espagnol", "Espagnol (LV2)", 1, [
    ("El presente de subjuntivo", "Elige la forma correcta.", [
      ("Quiero que tú (venir) ___ mañana.", "vengas", "vienes", "vendrás", "venir", "Querer que + subjuntivo."),
      ("Es necesario que nosotros (estudiar) ___.", "estudiemos", "estudiamos", "estudiaremos", "estudiar", "Expresión impersonal + subjuntivo."),
      ("Ojalá (llover) ___ pronto.", "llueva", "llueve", "lloverá", "llovía", "Deseo."),
      ("Cuando (ser, yo) ___ mayor, seré médico.", "sea", "soy", "seré", "era", "Cuando + futuro → subjuntivo.")]),
    ("Comprensión", "« Mi hermano trabaja en un hospital de Dakar. Dice que es importante que los jóvenes se vacunen. »", [
      ("¿Dónde trabaja el hermano?", "en un hospital de Dakar", "en una escuela", "en Madrid", "en un mercado", "Texto."),
      ("¿Qué es importante?", "que los jóvenes se vacunen", "que los jóvenes viajen", "que coman más", "que duerman", "Texto."),
      ("« se vacunen » está en", "presente de subjuntivo", "presente de indicativo", "pretérito", "futuro", "Es importante que + subjuntivo."),
      ("« hermano » significa", "frère", "cousin", "oncle", "voisin", "Vocabulario.")]),
    ("Vocabulario: la salud", "Traduce.", [
      ("« le médecin » :", "el médico", "la medicina", "el enfermo", "el hospital", "Salud."),
      ("« la maladie » :", "la enfermedad", "el enfermero", "la enfermería", "la mala", "Salud."),
      ("« avoir de la fièvre » :", "tener fiebre", "ser fiebre", "estar fiebre", "hacer fiebre", "Expresión."),
      ("« le paludisme » :", "el paludismo / la malaria", "la palabra", "el palo", "la pelota", "Enfermedad.")])]),
  d("espagnol", "Espagnol (LV2)", 2, [
    ("Pretérito perfecto y pluscuamperfecto", "Elige.", [
      ("Hoy (comer, yo) ___ arroz.", "he comido", "comí", "había comido", "comía", "Hoy → pretérito perfecto."),
      ("Cuando llegué, el tren ya (salir) ___.", "había salido", "ha salido", "salió", "sale", "Anterioridad en el pasado."),
      ("Participio de « escribir »:", "escrito", "escribido", "escribiendo", "escriba", "Irregular."),
      ("Participio de « volver »:", "vuelto", "volvido", "volviendo", "vuelva", "Irregular.")]),
    ("Comprensión: la emigración", "« Muchos jóvenes han salido de su pueblo para buscar trabajo en la ciudad. Algunos han vuelto con nuevas ideas. »", [
      ("¿Por qué han salido los jóvenes?", "para buscar trabajo", "para estudiar idiomas", "para jugar al fútbol", "para casarse", "Texto."),
      ("¿Adónde han ido?", "a la ciudad", "al campo", "al mar", "a la montaña", "Texto."),
      ("¿Qué han traído algunos?", "nuevas ideas", "dinero solamente", "animales", "nada", "Texto."),
      ("« pueblo » significa", "village", "peuple seulement", "pomme", "pont", "Vocabulario.")]),
    ("Expresión", "Elige la frase correcta.", [
      ("« Je n'ai jamais vu la mer » :", "Nunca he visto el mar", "Nunca he veído el mar", "No he visto nunca la mer", "Jamás veo el mar ayer", "Pretérito perfecto."),
      ("« Il avait déjà mangé » :", "Ya había comido", "Ya ha comido", "Ya comía", "Ya comió mañana", "Pluscuamperfecto."),
      ("« Nous sommes arrivés tard » :", "Hemos llegado tarde", "Somos llegados tarde", "Estamos llegado tarde", "Hemos llegando tarde", "Haber como auxiliar."),
      ("« Ils ont dit la vérité » :", "Han dicho la verdad", "Han decido la verdad", "Han diciendo la verdad", "Son dicho la verdad", "Participio irregular.")])]),
  d("espagnol", "Espagnol (LV2)", 3, [
    ("El condicional", "Elige.", [
      ("Yo (comprar) ___ una casa si tuviera dinero.", "compraría", "compraré", "compro", "compraba", "Condicional."),
      ("Condicional de « tener » (ella):", "tendría", "tenería", "tiene", "tendrá", "Irregular."),
      ("Condicional de « hacer » (nosotros):", "haríamos", "haceríamos", "hacemos", "hicimos", "Irregular."),
      ("« Pourriez-vous m'aider ? » :", "¿Podría ayudarme?", "¿Puede ayudarme ayer?", "¿Podré ayudarme?", "¿Pudiera ayudarme ayer?", "Cortesía.")]),
    ("La hipótesis", "Elige.", [
      ("Si (tener) ___ tiempo, iría a la playa.", "tuviera", "tengo", "tendría", "tuve", "Si + imperfecto de subjuntivo + condicional."),
      ("Si llueve, (quedarse, nosotros) ___ en casa.", "nos quedaremos", "nos quedaríamos", "nos quedáramos", "nos quedamos ayer", "Hipótesis real."),
      ("Si (ser, yo) ___ presidente, construiría escuelas.", "fuera", "soy", "sería", "seré", "Irreal del presente."),
      ("Imperfecto de subjuntivo de « estar » (yo):", "estuviera", "estaría", "estoy", "estaba", "Irregular.")]),
    ("Vocabulario: el trabajo", "Traduce.", [
      ("« le chômage » :", "el paro / el desempleo", "el trabajo", "la oficina", "el sueldo", "Economía."),
      ("« le salaire » :", "el sueldo / el salario", "la sal", "el saludo", "el ahorro", "Economía."),
      ("« chercher un emploi » :", "buscar trabajo", "mirar trabajo", "encontrar trabajo ya", "pedir trabajar", "Expresión."),
      ("« l'entreprise » :", "la empresa", "la emprenta", "el empresario", "la entrada", "Economía.")])]),
  d("espagnol", "Espagnol (LV2)", 4, [
    ("Conectores", "Elige.", [
      ("Estudió mucho; ___, aprobó el examen.", "por eso", "aunque", "sin embargo", "a pesar de", "Consecuencia."),
      ("___ hacía frío, salimos.", "Aunque", "Porque", "Por eso", "Así que", "Concesión."),
      ("No vino ___ estaba enfermo.", "porque", "aunque", "sin embargo", "pero sí", "Causa."),
      ("Es caro; ___, lo compro.", "sin embargo", "porque", "por eso", "así", "Oposición.")]),
    ("Comprensión: medio ambiente", "« Las playas de Dakar están llenas de plástico. Los jóvenes organizan jornadas de limpieza cada mes. »", [
      ("¿Cómo están las playas?", "llenas de plástico", "limpias", "vacías", "cerradas", "Texto."),
      ("¿Quién organiza las jornadas?", "los jóvenes", "el gobierno español", "los turistas", "los pescadores solos", "Texto."),
      ("¿Con qué frecuencia?", "cada mes", "cada año", "cada día", "nunca", "Texto."),
      ("« limpieza » significa", "nettoyage", "lumière", "limite", "lecture", "Vocabulario.")]),
    ("Expresión escrita", "Escribes tu opinión sobre el teléfono móvil.", [
      ("Para dar tu opinión:", "Pienso que…", "Pienso de que…", "Me pienso…", "Opino de…", "Expresión correcta."),
      ("Para añadir un argumento:", "Además,", "Sin embargo,", "Aunque", "Por fin de", "Adición."),
      ("Para concluir:", "En conclusión,", "Primero,", "Por ejemplo,", "Además,", "Conclusión."),
      ("« No creo que sea útil »: después de « no creo que »", "subjuntivo", "indicativo", "infinitivo", "gerundio", "Duda → subjuntivo.")])]),
  d("espagnol", "Espagnol (LV2)", 5, [
    ("Síntesis del subjuntivo", "Elige.", [
      ("Te llamo para que (venir) ___.", "vengas", "vienes", "vendrás", "venir", "Para que + subjuntivo."),
      ("Busco a alguien que (hablar) ___ wolof.", "hable", "habla", "hablará", "hablar", "Antecedente desconocido."),
      ("Me alegro de que (estar, tú) ___ aquí.", "estés", "estás", "estarás", "estar", "Sentimiento."),
      ("Antes de que (llegar) ___ tus padres, ordena tu cuarto.", "lleguen", "llegan", "llegarán", "llegar", "Antes de que + subjuntivo.")]),
    ("Civilización hispánica", "Elige.", [
      ("Autor de « Don Quijote »:", "Miguel de Cervantes", "Gabriel García Márquez", "Pablo Neruda", "Federico García Lorca", "1605."),
      ("Autor de « Cien años de soledad »:", "Gabriel García Márquez", "Cervantes", "Borges", "Octavio Paz", "Colombia."),
      ("Fiesta del 12 de octubre:", "Día de la Hispanidad", "Navidad", "Año Nuevo", "Semana Santa", "Llegada de Colón."),
      ("Pintor de « Guernica »:", "Pablo Picasso", "Goya", "Dalí", "Velázquez", "1937.")]),
    ("Comprensión: la familia", "« Mi abuela siempre decía que la familia es lo más importante. Ahora entiendo lo que quería decir. »", [
      ("¿Qué decía la abuela?", "que la familia es lo más importante", "que el dinero es importante", "que hay que viajar", "nada", "Texto."),
      ("Tiempo de « decía »:", "imperfecto", "pretérito indefinido", "presente", "futuro", "Hábito."),
      ("« Ahora entiendo » significa", "Maintenant je comprends", "Avant je comprenais", "Je ne comprends pas", "Demain je comprendrai", "Traducción."),
      ("« lo más importante » es", "un superlativo", "un comparativo", "un diminutivo", "un verbo", "Gramática.")])]),
  d("espagnol", "Espagnol (LV2)", 6, [
    ("Síntesis gramatical", "Elige.", [
      ("Si (poder, yo) ___, viajaría a México.", "pudiera", "puedo", "podría", "pude", "Hipótesis irreal."),
      ("Ya (terminar, nosotros) ___ los deberes.", "hemos terminado", "terminábamos", "terminaremos", "terminar", "Pretérito perfecto."),
      ("Es posible que (llegar, ellos) ___ tarde.", "lleguen", "llegan", "llegarán", "llegaron", "Posibilidad → subjuntivo."),
      ("Me (gustar) ___ visitar Madrid.", "gustaría", "gusto", "gustaré", "gustaba ayer", "Deseo cortés.")]),
    ("Traducción", "Elige la traducción correcta.", [
      ("« Il faut que tu travailles » :", "Es necesario que trabajes", "Hay que trabajas", "Debes que trabajar", "Es necesario trabajas", "Subjuntivo."),
      ("« Si j'étais riche » :", "Si fuera rico", "Si sería rico", "Si era rico", "Si soy rico ayer", "Imperfecto de subjuntivo."),
      ("« Nous avons fini » :", "Hemos terminado", "Somos terminados", "Tenemos terminado ya", "Hemos terminando", "Pretérito perfecto."),
      ("« bien que » :", "aunque", "porque", "así que", "pues", "Concesión.")]),
    ("Expresión oral", "Situaciones.", [
      ("Para pedir la opinión:", "¿Qué opinas?", "¿Qué hora es?", "¿Dónde vives?", "¿Cuántos años tienes?", "Debate."),
      ("Para mostrar acuerdo:", "Estoy de acuerdo", "No estoy de acuerdo", "Me da igual", "Ni idea", "Acuerdo."),
      ("Para matizar:", "Depende", "Claro que sí siempre", "Nunca jamás", "Por supuesto que no", "Matiz."),
      ("Para cortar educadamente:", "Perdona que te interrumpa", "¡Cállate!", "No hables", "Basta ya", "Cortesía.")])]),
])
