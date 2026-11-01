# Anglais à l'élémentaire (CE1 à CM2) : vocabulaire et petites phrases du quotidien, pour des enfants de 7 à 11 ans.
# Anglais britannique (colour, have got). Chaque chapitre = un thème : mots (anglais, français), phrases (anglais, français).
# Les QCM, l'exercice guidé et l'exercice type devoir sont fabriqués à partir de ces listes ; le même vocabulaire
# alimente les jeux et les questions à mots nouveaux (docs/vocab_en.js, écrit par build.py).
import random
from primaire_common import CH

T = {}  # niveau -> [(titre, id, cours, retenir, mots, phrases, piege)]

T["CE1"] = [
  ("Hello ! Saluer et se présenter", "en1-hello",
   ["En anglais, on salue avec « Hello » ou « Hi » et on dit au revoir avec « Goodbye » ou « Bye ».", "Pour se présenter : « My name is Awa. » ; pour demander le nom : « What's your name? »"],
   ["Good morning : bonjour (le matin).", "How are you? – I'm fine, thank you.", "Thank you : merci ; please : s'il te plaît.", "« I » (je) s'écrit toujours avec une majuscule."],
   [("hello", "bonjour"), ("hi", "salut"), ("goodbye", "au revoir"), ("good morning", "bonjour (le matin)"), ("good afternoon", "bon après-midi"), ("good evening", "bonsoir"),
    ("good night", "bonne nuit"), ("please", "s'il te plaît"), ("thank you", "merci"), ("yes", "oui"), ("no", "non"), ("sorry", "pardon"), ("boy", "garçon"), ("girl", "fille"),
    ("friend", "ami"), ("teacher", "maître, maîtresse"), ("name", "nom"), ("fine", "bien")],
   [("What's your name?", "Comment t'appelles-tu ?"), ("My name is Moussa.", "Je m'appelle Moussa."), ("How are you?", "Comment vas-tu ?"), ("I'm fine, thank you.", "Je vais bien, merci."),
    ("Nice to meet you.", "Enchanté de te connaître."), ("See you tomorrow!", "À demain !"), ("How old are you?", "Quel âge as-tu ?"), ("I am seven.", "J'ai sept ans.")],
   "Dire « I am seven years » sans « old » : on dit « I am seven » ou « I am seven years old »."),
  ("Numbers 1 to 20", "en1-numbers",
   ["On compte en anglais : one, two, three… jusqu'à twenty.", "De 13 à 19, les nombres finissent par « -teen » : thirteen, fourteen…"],
   ["11 : eleven ; 12 : twelve.", "13 à 19 : -teen (sixteen = 16).", "20 : twenty.", "How many? : combien ?"],
   [("one", "un"), ("two", "deux"), ("three", "trois"), ("four", "quatre"), ("five", "cinq"), ("six", "six"), ("seven", "sept"), ("eight", "huit"), ("nine", "neuf"), ("ten", "dix"),
    ("eleven", "onze"), ("twelve", "douze"), ("thirteen", "treize"), ("fourteen", "quatorze"), ("fifteen", "quinze"), ("sixteen", "seize"), ("seventeen", "dix-sept"),
    ("eighteen", "dix-huit"), ("nineteen", "dix-neuf"), ("twenty", "vingt")],
   [("How many pens?", "Combien de stylos ?"), ("Three pens.", "Trois stylos."), ("I have two brothers.", "J'ai deux frères."), ("Count to ten.", "Compte jusqu'à dix."),
    ("Five plus five is ten.", "Cinq plus cinq font dix."), ("I am eight.", "J'ai huit ans.")],
   "Confondre « thirteen » (13) et « thirty » (30)."),
  ("Colours", "en1-colours",
   ["Les couleurs se placent avant le nom : « a red car » (une voiture rouge).", "Pour demander une couleur : « What colour is it? » – « It's green. »"],
   ["En anglais, la couleur ne prend pas de « s » : « blue cars ».", "red, blue, green, yellow : les couleurs du drapeau du Sénégal sont green, yellow, red.", "« It's » = « It is ».", "colour (anglais britannique) = color (américain)."],
   [("red", "rouge"), ("blue", "bleu"), ("green", "vert"), ("yellow", "jaune"), ("black", "noir"), ("white", "blanc"), ("orange", "orange"), ("pink", "rose"), ("brown", "marron"),
    ("grey", "gris"), ("purple", "violet")],
   [("What colour is it?", "De quelle couleur est-ce ?"), ("It's blue.", "C'est bleu."), ("The sky is blue.", "Le ciel est bleu."), ("The grass is green.", "L'herbe est verte."),
    ("A red ball.", "Un ballon rouge."), ("I like yellow.", "J'aime le jaune.")],
   "Mettre la couleur après le nom comme en français : on dit « a red ball », pas « a ball red »."),
  ("My family", "en1-family",
   ["Pour présenter sa famille : « This is my mother. » (Voici ma mère.)", "« My » veut dire mon, ma, mes."],
   ["mother / mum : mère, maman ; father / dad : père, papa.", "brother : frère ; sister : sœur.", "grandmother : grand-mère ; grandfather : grand-père.", "I have got a brother : j'ai un frère."],
   [("mother", "mère"), ("father", "père"), ("mum", "maman"), ("dad", "papa"), ("brother", "frère"), ("sister", "sœur"), ("grandmother", "grand-mère"),
    ("grandfather", "grand-père"), ("baby", "bébé"), ("uncle", "oncle"), ("aunt", "tante"), ("cousin", "cousin"), ("family", "famille"), ("son", "fils"), ("daughter", "fille (enfant)")],
   [("This is my mother.", "Voici ma mère."), ("I have got two sisters.", "J'ai deux sœurs."), ("My dad is a fisherman.", "Mon papa est pêcheur."), ("I love my family.", "J'aime ma famille."),
    ("Who is he? He is my brother.", "Qui est-ce ? C'est mon frère."), ("My grandmother is old.", "Ma grand-mère est âgée.")],
   "Confondre « daughter » (fille, l'enfant de quelqu'un) et « girl » (fille, une petite fille)."),
  ("My body", "en1-body",
   ["Les parties du corps : head (tête), eyes (yeux), hands (mains)…", "« Touch your nose! » : touche ton nez !"],
   ["Un œil : an eye ; des yeux : eyes.", "Un pied : a foot ; des pieds : feet (pluriel irrégulier).", "Une dent : a tooth ; des dents : teeth.", "I have got two hands : j'ai deux mains."],
   [("head", "tête"), ("hair", "cheveux"), ("eye", "œil"), ("ear", "oreille"), ("nose", "nez"), ("mouth", "bouche"), ("tooth", "dent"), ("neck", "cou"), ("arm", "bras"),
    ("hand", "main"), ("finger", "doigt"), ("leg", "jambe"), ("foot", "pied"), ("knee", "genou"), ("back", "dos"), ("stomach", "ventre")],
   [("Touch your nose!", "Touche ton nez !"), ("Clap your hands!", "Tape dans tes mains !"), ("I have got two eyes.", "J'ai deux yeux."), ("Wash your hands.", "Lave-toi les mains."),
    ("Brush your teeth.", "Brosse-toi les dents."), ("Stamp your feet!", "Tape des pieds !")],
   "Dire « foots » ou « tooths » : les pluriels sont « feet » et « teeth »."),
  ("Animals", "en1-animals",
   ["Les animaux de la ferme, de la maison et de la savane ont un nom en anglais : cat, dog, lion…", "« I can see a lion. » : je vois un lion."],
   ["a dog, a cat : un chien, un chat.", "an elephant : « an » devant une voyelle.", "Le lion est le symbole du Sénégal : the lion.", "What is it? It's a goat."],
   [("cat", "chat"), ("dog", "chien"), ("cow", "vache"), ("goat", "chèvre"), ("sheep", "mouton"), ("horse", "cheval"), ("donkey", "âne"), ("chicken", "poulet, poule"),
    ("lion", "lion"), ("elephant", "éléphant"), ("monkey", "singe"), ("bird", "oiseau"), ("fish", "poisson"), ("snake", "serpent"), ("giraffe", "girafe"), ("crocodile", "crocodile"),
    ("hippo", "hippopotame"), ("rabbit", "lapin")],
   [("What is it? It's a goat.", "Qu'est-ce que c'est ? C'est une chèvre."), ("I can see a lion.", "Je vois un lion."), ("The cat is small.", "Le chat est petit."),
    ("The elephant is big.", "L'éléphant est grand."), ("Birds can fly.", "Les oiseaux savent voler."), ("I have got a dog.", "J'ai un chien.")],
   "Écrire « a elephant » : devant un son voyelle, on met « an » (an elephant)."),
  ("At school", "en1-school",
   ["Les objets de la classe : pen, pencil, book, bag…", "Les consignes du maître : « Open your book. », « Sit down. », « Stand up. »"],
   ["Open : ouvre ; close : ferme.", "Sit down : assieds-toi ; stand up : lève-toi.", "Listen : écoute ; look : regarde ; repeat : répète.", "This is my pencil : voici mon crayon."],
   [("pen", "stylo"), ("pencil", "crayon"), ("book", "livre"), ("exercise book", "cahier"), ("bag", "cartable, sac"), ("ruler", "règle"), ("rubber", "gomme"), ("chair", "chaise"),
    ("table", "table"), ("desk", "pupitre"), ("board", "tableau"), ("chalk", "craie"), ("classroom", "classe"), ("school", "école"), ("pupil", "élève"), ("door", "porte"), ("window", "fenêtre")],
   [("Open your book.", "Ouvre ton livre."), ("Close the door.", "Ferme la porte."), ("Sit down, please.", "Assieds-toi, s'il te plaît."), ("Stand up!", "Lève-toi !"),
    ("Listen and repeat.", "Écoute et répète."), ("This is my pencil.", "Voici mon crayon."), ("Look at the board.", "Regarde le tableau.")],
   "Confondre « rubber » (gomme, anglais britannique) et « ruler » (règle)."),
  ("Fruits and food", "en1-food",
   ["Les fruits et les aliments : mango, banana, rice, bread…", "« I like mangoes. » : j'aime les mangues ; « I don't like… » : je n'aime pas…"],
   ["I like : j'aime ; I don't like : je n'aime pas.", "an apple, an orange : « an » devant une voyelle.", "Pluriel : mango → mangoes, banana → bananas.", "I'm hungry : j'ai faim ; I'm thirsty : j'ai soif."],
   [("mango", "mangue"), ("banana", "banane"), ("orange", "orange"), ("apple", "pomme"), ("lemon", "citron"), ("watermelon", "pastèque"), ("coconut", "noix de coco"), ("rice", "riz"),
    ("bread", "pain"), ("fish", "poisson"), ("meat", "viande"), ("egg", "œuf"), ("milk", "lait"), ("water", "eau"), ("juice", "jus"), ("tomato", "tomate"), ("onion", "oignon")],
   [("I like mangoes.", "J'aime les mangues."), ("I don't like onions.", "Je n'aime pas les oignons."), ("I'm hungry.", "J'ai faim."), ("I'm thirsty.", "J'ai soif."),
    ("Can I have some water, please?", "Je peux avoir de l'eau, s'il te plaît ?"), ("Rice and fish.", "Du riz et du poisson.")],
   "Écrire « I am like » : on dit simplement « I like »."),
]

T["CE2"] = [
  ("Numbers 1 to 100", "en2-numbers",
   ["Les dizaines : twenty (20), thirty (30), forty (40), fifty (50)… one hundred (100).", "Pour 21 à 99, on met un tiret : twenty-one, thirty-five, ninety-nine."],
   ["forty (40) s'écrit sans « u ».", "thirteen (13) ≠ thirty (30).", "one hundred = 100.", "How old are you? I'm nine."],
   [("twenty", "vingt"), ("thirty", "trente"), ("forty", "quarante"), ("fifty", "cinquante"), ("sixty", "soixante"), ("seventy", "soixante-dix"), ("eighty", "quatre-vingts"),
    ("ninety", "quatre-vingt-dix"), ("one hundred", "cent"), ("twenty-one", "vingt et un"), ("thirty-five", "trente-cinq"), ("forty-two", "quarante-deux"),
    ("fifty-six", "cinquante-six"), ("sixty-eight", "soixante-huit"), ("seventy-three", "soixante-treize"), ("eighty-four", "quatre-vingt-quatre"), ("ninety-nine", "quatre-vingt-dix-neuf")],
   [("How much is it?", "Combien ça coûte ?"), ("It's fifty francs.", "C'est cinquante francs."), ("There are thirty pupils in my class.", "Il y a trente élèves dans ma classe."),
    ("Twenty plus ten is thirty.", "Vingt plus dix font trente."), ("My grandfather is seventy.", "Mon grand-père a soixante-dix ans."), ("Count from ten to one hundred.", "Compte de dix à cent.")],
   "Écrire « fourty » : 40 s'écrit « forty »."),
  ("Days and months", "en2-days",
   ["Les jours et les mois prennent une majuscule en anglais : Monday, January.", "« What day is it today? » – « It's Monday. »"],
   ["Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.", "On Monday : lundi (le jour) ; in January : en janvier.", "today : aujourd'hui ; tomorrow : demain ; yesterday : hier.", "My birthday is in May : mon anniversaire est en mai."],
   [("Monday", "lundi"), ("Tuesday", "mardi"), ("Wednesday", "mercredi"), ("Thursday", "jeudi"), ("Friday", "vendredi"), ("Saturday", "samedi"), ("Sunday", "dimanche"),
    ("January", "janvier"), ("February", "février"), ("March", "mars"), ("April", "avril"), ("May", "mai"), ("June", "juin"), ("July", "juillet"), ("August", "août"),
    ("September", "septembre"), ("October", "octobre"), ("November", "novembre"), ("December", "décembre"), ("today", "aujourd'hui"), ("tomorrow", "demain"), ("yesterday", "hier"), ("week", "semaine")],
   [("What day is it today?", "Quel jour sommes-nous ?"), ("It's Friday.", "C'est vendredi."), ("My birthday is in April.", "Mon anniversaire est en avril."),
    ("There is no school on Sunday.", "Il n'y a pas école le dimanche."), ("See you on Monday!", "À lundi !"), ("Independence Day is on the 4th of April.", "La fête de l'indépendance est le 4 avril.")],
   "Oublier la majuscule : en anglais on écrit « Monday », « April »."),
  ("Clothes", "en2-clothes",
   ["Les vêtements : shirt, dress, trousers, shoes…", "« I am wearing a blue shirt. » : je porte une chemise bleue."],
   ["trousers (pantalon) et shorts sont toujours au pluriel.", "a pair of shoes : une paire de chaussures.", "Put on your hat : mets ton chapeau.", "school uniform : tenue scolaire."],
   [("shirt", "chemise"), ("T-shirt", "tee-shirt"), ("dress", "robe"), ("skirt", "jupe"), ("trousers", "pantalon"), ("shorts", "short"), ("shoes", "chaussures"), ("sandals", "sandales"),
    ("socks", "chaussettes"), ("hat", "chapeau"), ("cap", "casquette"), ("jacket", "veste"), ("coat", "manteau"), ("boubou", "boubou"), ("uniform", "uniforme"), ("scarf", "écharpe, foulard")],
   [("I am wearing a red dress.", "Je porte une robe rouge."), ("Put on your shoes.", "Mets tes chaussures."), ("Take off your hat.", "Enlève ton chapeau."),
    ("My uniform is blue.", "Mon uniforme est bleu."), ("These trousers are too big.", "Ce pantalon est trop grand."), ("Where are my sandals?", "Où sont mes sandales ?")],
   "Dire « a trouser » : on dit « trousers » ou « a pair of trousers »."),
  ("My house", "en2-house",
   ["Les pièces de la maison : kitchen, bedroom, bathroom, living room…", "« There is a bed in my bedroom. » : il y a un lit dans ma chambre."],
   ["There is + un objet ; there are + plusieurs objets.", "in : dans ; on : sur ; under : sous.", "upstairs : en haut ; downstairs : en bas.", "yard : cour ; garden : jardin."],
   [("house", "maison"), ("kitchen", "cuisine"), ("bedroom", "chambre"), ("bathroom", "salle de bain"), ("living room", "salon"), ("yard", "cour"), ("garden", "jardin"), ("roof", "toit"),
    ("bed", "lit"), ("table", "table"), ("chair", "chaise"), ("cupboard", "placard"), ("fridge", "réfrigérateur"), ("lamp", "lampe"), ("mat", "natte, tapis"), ("toilet", "toilettes"), ("stairs", "escalier")],
   [("There is a bed in my bedroom.", "Il y a un lit dans ma chambre."), ("There are four chairs in the kitchen.", "Il y a quatre chaises dans la cuisine."),
    ("My mum is in the kitchen.", "Ma maman est dans la cuisine."), ("The cat is under the table.", "Le chat est sous la table."), ("The book is on the bed.", "Le livre est sur le lit."),
    ("We eat in the yard.", "Nous mangeons dans la cour.")],
   "Dire « there is three chairs » : avec un pluriel, on dit « there are »."),
  ("Food and drinks", "en2-food",
   ["Les repas : breakfast (petit-déjeuner), lunch (déjeuner), dinner (dîner).", "Pour commander poliment : « Can I have a juice, please? »"],
   ["I like / I don't like / I love.", "Do you like fish? – Yes, I do. / No, I don't.", "some rice : du riz ; some water : de l'eau.", "delicious : délicieux."],
   [("breakfast", "petit-déjeuner"), ("lunch", "déjeuner"), ("dinner", "dîner"), ("rice", "riz"), ("millet", "mil"), ("couscous", "couscous"), ("bread", "pain"), ("butter", "beurre"),
    ("sugar", "sucre"), ("salt", "sel"), ("tea", "thé"), ("coffee", "café"), ("milk", "lait"), ("juice", "jus"), ("chicken", "poulet"), ("beans", "haricots"), ("peanuts", "arachides"), ("soup", "soupe")],
   [("Do you like fish? Yes, I do.", "Aimes-tu le poisson ? Oui."), ("I don't like coffee.", "Je n'aime pas le café."), ("I have bread for breakfast.", "Je mange du pain au petit-déjeuner."),
    ("Can I have some juice, please?", "Je peux avoir du jus, s'il te plaît ?"), ("Thieboudienne is delicious!", "Le thiéboudiène est délicieux !"), ("We eat lunch at two o'clock.", "Nous déjeunons à deux heures.")],
   "Répondre « Yes, I like » : on répond « Yes, I do. »."),
  ("Weather and seasons", "en2-weather",
   ["Pour parler du temps : « What's the weather like? » – « It's sunny. »", "Au Sénégal, il y a la saison sèche (dry season) et la saison des pluies (rainy season)."],
   ["It's sunny : il fait soleil ; it's hot : il fait chaud.", "It's raining : il pleut ; it's windy : il y a du vent.", "It's cloudy : c'est nuageux ; it's cold : il fait froid.", "rainy season : hivernage."],
   [("sun", "soleil"), ("rain", "pluie"), ("wind", "vent"), ("cloud", "nuage"), ("sunny", "ensoleillé"), ("rainy", "pluvieux"), ("windy", "venteux"), ("cloudy", "nuageux"),
    ("hot", "chaud"), ("cold", "froid"), ("warm", "doux, tiède"), ("storm", "orage"), ("dry season", "saison sèche"), ("rainy season", "saison des pluies"), ("sky", "ciel")],
   [("What's the weather like?", "Quel temps fait-il ?"), ("It's sunny and hot.", "Il fait soleil et chaud."), ("It's raining today.", "Il pleut aujourd'hui."),
    ("Take your umbrella!", "Prends ton parapluie !"), ("The rainy season starts in July.", "La saison des pluies commence en juillet."), ("It's windy at the beach.", "Il y a du vent à la plage.")],
   "Dire « It's rain » : on dit « It's raining » ou « It's rainy »."),
  ("Actions: I can…", "en2-actions",
   ["« I can » veut dire « je sais » ou « je peux » : « I can swim. » (je sais nager).", "La négation : « I can't fly. » (je ne sais pas voler)."],
   ["can ne prend pas de « s » : he can, she can.", "can't = cannot.", "Can you run? – Yes, I can. / No, I can't.", "Le verbe après can reste simple : I can jump."],
   [("run", "courir"), ("jump", "sauter"), ("swim", "nager"), ("dance", "danser"), ("sing", "chanter"), ("read", "lire"), ("write", "écrire"), ("draw", "dessiner"), ("climb", "grimper"),
    ("walk", "marcher"), ("fly", "voler"), ("ride a bike", "faire du vélo"), ("play football", "jouer au football"), ("cook", "cuisiner"), ("count", "compter"), ("speak", "parler")],
   [("I can swim.", "Je sais nager."), ("I can't fly.", "Je ne sais pas voler."), ("Can you dance? Yes, I can.", "Sais-tu danser ? Oui."), ("Birds can fly.", "Les oiseaux savent voler."),
    ("She can ride a bike.", "Elle sait faire du vélo."), ("Fish can't walk.", "Les poissons ne savent pas marcher.")],
   "Écrire « he cans » ou « I can to swim » : on dit « he can », « I can swim »."),
  ("Feelings", "en2-feelings",
   ["Pour dire comment on se sent : « I'm happy. », « I'm tired. »", "Pour demander : « How do you feel? »"],
   ["I'm = I am.", "happy : content ; sad : triste ; angry : fâché.", "hungry : qui a faim ; thirsty : qui a soif.", "scared : qui a peur ; tired : fatigué."],
   [("happy", "content, heureux"), ("sad", "triste"), ("angry", "en colère"), ("tired", "fatigué"), ("hungry", "qui a faim"), ("thirsty", "qui a soif"), ("scared", "qui a peur"),
    ("sick", "malade"), ("hot", "qui a chaud"), ("cold", "qui a froid"), ("bored", "qui s'ennuie"), ("excited", "très content, impatient"), ("proud", "fier"), ("shy", "timide")],
   [("How do you feel?", "Comment te sens-tu ?"), ("I'm happy today.", "Je suis content aujourd'hui."), ("She is sad.", "Elle est triste."), ("I'm tired, I want to sleep.", "Je suis fatigué, je veux dormir."),
    ("Are you hungry? Yes, I am.", "As-tu faim ? Oui."), ("He is scared of dogs.", "Il a peur des chiens.")],
   "Dire « I have hungry » : en anglais on dit « I am hungry » (je suis affamé)."),
]

T["CM1"] = [
  ("Telling the time", "en3-time",
   ["Pour demander l'heure : « What time is it? » – « It's eight o'clock. »", "half past : et demie ; quarter past : et quart ; quarter to : moins le quart."],
   ["o'clock : heure pile.", "half past seven : 7 h 30.", "quarter past nine : 9 h 15 ; quarter to ten : 9 h 45.", "in the morning, in the afternoon, in the evening."],
   [("o'clock", "heure pile"), ("half past", "et demie"), ("quarter past", "et quart"), ("quarter to", "moins le quart"), ("minute", "minute"), ("hour", "heure"),
    ("morning", "matin"), ("afternoon", "après-midi"), ("evening", "soir"), ("night", "nuit"), ("early", "tôt"), ("late", "en retard, tard"), ("clock", "horloge"), ("watch", "montre"), ("noon", "midi"), ("midnight", "minuit")],
   [("What time is it?", "Quelle heure est-il ?"), ("It's seven o'clock.", "Il est sept heures."), ("It's half past three.", "Il est trois heures et demie."),
    ("It's quarter past nine.", "Il est neuf heures et quart."), ("School starts at eight o'clock.", "L'école commence à huit heures."), ("I go to bed at nine in the evening.", "Je me couche à neuf heures du soir.")],
   "Dire « half past three » pour 2 h 30 : « half past three » = 3 h 30."),
  ("Jobs", "en3-jobs",
   ["Pour dire un métier : « She is a doctor. » ; on met « a » ou « an » devant le métier.", "« What does your father do? » – « He is a farmer. »"],
   ["a teacher, a doctor, an engineer (« an » devant une voyelle).", "farmer : cultivateur ; fisherman : pêcheur.", "I want to be a pilot : je veux être pilote.", "He works in a hospital : il travaille dans un hôpital."],
   [("teacher", "enseignant"), ("doctor", "médecin"), ("nurse", "infirmier"), ("farmer", "cultivateur"), ("fisherman", "pêcheur"), ("driver", "chauffeur"), ("tailor", "tailleur"),
    ("baker", "boulanger"), ("mechanic", "mécanicien"), ("police officer", "policier"), ("engineer", "ingénieur"), ("pilot", "pilote"), ("shopkeeper", "commerçant"), ("cook", "cuisinier"),
    ("builder", "maçon"), ("footballer", "footballeur"), ("journalist", "journaliste")],
   [("What does your father do?", "Que fait ton père ?"), ("He is a fisherman.", "Il est pêcheur."), ("My mother is a nurse.", "Ma mère est infirmière."),
    ("I want to be a doctor.", "Je veux être médecin."), ("The tailor makes clothes.", "Le tailleur fait des vêtements."), ("A farmer grows millet.", "Un cultivateur fait pousser du mil.")],
   "Oublier l'article : on dit « She is a nurse », pas « She is nurse »."),
  ("Places in town", "en3-town",
   ["Les lieux de la ville : market, hospital, school, mosque, church, bank…", "« Where is the market? » – « It's near the school. »"],
   ["near : près de ; next to : à côté de ; opposite : en face de.", "between : entre ; behind : derrière ; in front of : devant.", "I go to the market : je vais au marché.", "There is a bank in my town."],
   [("market", "marché"), ("hospital", "hôpital"), ("school", "école"), ("mosque", "mosquée"), ("church", "église"), ("bank", "banque"), ("post office", "poste"), ("shop", "magasin, boutique"),
    ("pharmacy", "pharmacie"), ("bus station", "gare routière"), ("airport", "aéroport"), ("beach", "plage"), ("stadium", "stade"), ("street", "rue"), ("bridge", "pont"), ("port", "port"), ("library", "bibliothèque")],
   [("Where is the hospital?", "Où est l'hôpital ?"), ("It's next to the bank.", "C'est à côté de la banque."), ("The market is near the mosque.", "Le marché est près de la mosquée."),
    ("I go to the beach on Sunday.", "Je vais à la plage le dimanche."), ("The library is opposite the school.", "La bibliothèque est en face de l'école."), ("We buy medicine at the pharmacy.", "Nous achetons des médicaments à la pharmacie.")],
   "Confondre « library » (bibliothèque) et « librairie » (bookshop)."),
  ("Daily routine", "en3-routine",
   ["Pour raconter sa journée, on utilise le présent simple : « I get up at six. »", "Avec he, she, it, on ajoute un « s » au verbe : « She goes to school. »"],
   ["I get up / he gets up.", "I wash / she washes ; I go / he goes.", "first, then, after that, finally : d'abord, puis, après, enfin.", "every day : chaque jour ; always : toujours ; never : jamais."],
   [("get up", "se lever"), ("wake up", "se réveiller"), ("wash", "se laver"), ("brush my teeth", "me brosser les dents"), ("get dressed", "s'habiller"), ("have breakfast", "prendre le petit-déjeuner"),
    ("go to school", "aller à l'école"), ("study", "étudier"), ("go home", "rentrer à la maison"), ("do my homework", "faire mes devoirs"), ("have dinner", "dîner"), ("go to bed", "aller au lit"),
    ("every day", "chaque jour"), ("always", "toujours"), ("never", "jamais"), ("sometimes", "parfois")],
   [("I get up at six o'clock.", "Je me lève à six heures."), ("She goes to school by bus.", "Elle va à l'école en bus."), ("He does his homework after school.", "Il fait ses devoirs après l'école."),
    ("We have dinner at eight.", "Nous dînons à huit heures."), ("I always brush my teeth.", "Je me brosse toujours les dents."), ("My brother never gets up early.", "Mon frère ne se lève jamais tôt.")],
   "Oublier le « s » avec he/she : on dit « she goes », « he plays »."),
  ("Where is it? in, on, under", "en3-prepositions",
   ["Les prépositions de lieu disent où se trouve quelque chose : in, on, under, behind…", "« Where is the ball? » – « It's under the table. »"],
   ["in : dans ; on : sur ; under : sous.", "behind : derrière ; in front of : devant.", "next to : à côté de ; between : entre.", "Where are the books? They are on the shelf."],
   [("in", "dans"), ("on", "sur"), ("under", "sous"), ("behind", "derrière"), ("in front of", "devant"), ("next to", "à côté de"), ("between", "entre"), ("near", "près de"),
    ("far from", "loin de"), ("opposite", "en face de"), ("above", "au-dessus de"), ("inside", "à l'intérieur"), ("outside", "dehors")],
   [("The cat is under the bed.", "Le chat est sous le lit."), ("The pen is in the bag.", "Le stylo est dans le sac."), ("The book is on the table.", "Le livre est sur la table."),
    ("Moussa is behind Awa.", "Moussa est derrière Awa."), ("The school is far from my house.", "L'école est loin de ma maison."), ("The bird is above the tree.", "L'oiseau est au-dessus de l'arbre.")],
   "Confondre « on » (sur) et « in » (dans)."),
  ("Have got / has got", "en3-havegot",
   ["« I have got » veut dire « j'ai » (posséder) : « I have got a bike. »", "Avec he, she, it : « has got » : « She has got long hair. »"],
   ["I've got = I have got ; she's got = she has got.", "Négation : I haven't got / he hasn't got.", "Question : Have you got a pen? – Yes, I have. / No, I haven't.", "Has she got a brother? – Yes, she has."],
   [("have got", "avoir (je, tu, nous, vous, ils)"), ("has got", "a (il, elle)"), ("haven't got", "n'avoir pas"), ("hasn't got", "n'a pas"), ("bike", "vélo"), ("ball", "ballon"),
    ("toy", "jouet"), ("phone", "téléphone"), ("doll", "poupée"), ("kite", "cerf-volant"), ("pet", "animal de compagnie"), ("long hair", "cheveux longs"), ("short hair", "cheveux courts"), ("big eyes", "grands yeux")],
   [("I have got a red bike.", "J'ai un vélo rouge."), ("She has got two brothers.", "Elle a deux frères."), ("Have you got a pen? Yes, I have.", "As-tu un stylo ? Oui."),
    ("He hasn't got a phone.", "Il n'a pas de téléphone."), ("We have got a big yard.", "Nous avons une grande cour."), ("Has she got a cat? No, she hasn't.", "A-t-elle un chat ? Non.")],
   "Dire « she have got » : avec he/she/it, c'est « has got »."),
  ("Sports and hobbies", "en3-hobbies",
   ["Pour parler de ses loisirs : « I like playing football. », « My hobby is reading. »", "Avec « like », le verbe prend souvent « -ing » : swimming, dancing."],
   ["play + jeu de ballon : play football, play basketball.", "go + -ing : go swimming, go fishing.", "My favourite sport is wrestling : la lutte.", "How often? once a week : une fois par semaine."],
   [("football", "football"), ("basketball", "basket-ball"), ("wrestling", "lutte"), ("swimming", "natation"), ("running", "course à pied"), ("cycling", "cyclisme"), ("drawing", "dessin"),
    ("reading", "lecture"), ("singing", "chant"), ("dancing", "danse"), ("music", "musique"), ("game", "jeu"), ("team", "équipe"), ("match", "match"), ("win", "gagner"), ("lose", "perdre")],
   [("I like playing football.", "J'aime jouer au football."), ("My hobby is drawing.", "Mon loisir, c'est le dessin."), ("Wrestling is popular in Senegal.", "La lutte est populaire au Sénégal."),
    ("We go swimming on Saturday.", "Nous allons nager le samedi."), ("Our team won the match.", "Notre équipe a gagné le match."), ("She loves dancing.", "Elle adore danser.")],
   "Dire « I like play football » : on dit « I like playing football »."),
  ("Plurals and a / an", "en3-plurals",
   ["Le pluriel se forme le plus souvent avec « s » : a book → books.", "« a » devant un son consonne, « an » devant un son voyelle : a dog, an egg."],
   ["Après s, sh, ch, x, o : -es (buses, boxes, mangoes).", "-y après consonne → -ies : baby → babies.", "Pluriels irréguliers : man → men, woman → women, child → children, foot → feet.", "an hour : le « h » ne se prononce pas."],
   [("child", "children"), ("man", "men"), ("woman", "women"), ("foot", "feet"), ("tooth", "teeth"), ("mouse", "mice"), ("baby", "babies"), ("box", "boxes"), ("bus", "buses"),
    ("mango", "mangoes"), ("city", "cities"), ("leaf", "leaves"), ("knife", "knives"), ("sheep", "sheep"), ("fish", "fish"), ("watch", "watches")],
   [("Two children are playing.", "Deux enfants jouent."), ("I have got an orange and a banana.", "J'ai une orange et une banane."), ("There are three buses.", "Il y a trois bus."),
    ("The women are at the market.", "Les femmes sont au marché."), ("An elephant is big.", "Un éléphant est grand."), ("I wait for an hour.", "J'attends une heure.")],
   "Écrire « childs » ou « mans » : on écrit « children » et « men »."),
]

T["CM2"] = [
  ("What are you doing? Present continuous", "en4-continuous",
   ["Pour dire ce qu'on est en train de faire : be + verbe-ing : « I am reading. »", "Question : « What are you doing? » – « I'm doing my homework. »"],
   ["I am / you are / he is / we are / they are + -ing.", "write → writing (on enlève le e) ; swim → swimming (on double la consonne).", "now, right now : maintenant.", "Négation : She isn't sleeping."],
   [("reading", "en train de lire"), ("writing", "en train d'écrire"), ("eating", "en train de manger"), ("sleeping", "en train de dormir"), ("playing", "en train de jouer"),
    ("swimming", "en train de nager"), ("running", "en train de courir"), ("cooking", "en train de cuisiner"), ("watching TV", "en train de regarder la télé"), ("listening", "en train d'écouter"),
    ("working", "en train de travailler"), ("crying", "en train de pleurer"), ("laughing", "en train de rire"), ("waiting", "en train d'attendre")],
   [("What are you doing?", "Qu'est-ce que tu fais ?"), ("I'm doing my homework.", "Je fais mes devoirs."), ("She is cooking rice.", "Elle prépare du riz."), ("They are playing football.", "Ils jouent au football."),
    ("It's raining now.", "Il pleut maintenant."), ("He isn't sleeping, he is reading.", "Il ne dort pas, il lit.")],
   "Oublier « be » : on dit « I am reading », pas « I reading »."),
  ("Yesterday: was, were and the past", "en4-past",
   ["Pour parler du passé : « I was at school yesterday. » ; les verbes réguliers prennent « -ed » : play → played.", "Quelques verbes irréguliers : go → went, eat → ate, see → saw, have → had."],
   ["I/he/she/it was ; we/you/they were.", "Verbes réguliers : walk → walked, visit → visited.", "Irréguliers : go → went ; come → came ; buy → bought ; do → did.", "yesterday, last week, ago : hier, la semaine dernière, il y a."],
   [("go", "went"), ("eat", "ate"), ("see", "saw"), ("have", "had"), ("come", "came"), ("buy", "bought"), ("do", "did"), ("make", "made"), ("take", "took"), ("write", "wrote"),
    ("play", "played"), ("visit", "visited"), ("watch", "watched"), ("help", "helped"), ("swim", "swam"), ("drink", "drank"), ("get", "got"), ("give", "gave")],
   [("I was at school yesterday.", "J'étais à l'école hier."), ("We went to Saint-Louis last week.", "Nous sommes allés à Saint-Louis la semaine dernière."),
    ("She played with her friends.", "Elle a joué avec ses amies."), ("They were tired.", "Ils étaient fatigués."), ("I ate rice and fish.", "J'ai mangé du riz et du poisson."),
    ("He bought a ball two days ago.", "Il a acheté un ballon il y a deux jours.")],
   "Écrire « goed » ou « eated » : go → went, eat → ate."),
  ("Asking the way", "en4-directions",
   ["Pour demander son chemin : « Excuse me, where is the station? »", "Pour indiquer : « Go straight on, then turn left. »"],
   ["turn left : tourne à gauche ; turn right : tourne à droite.", "go straight on : va tout droit.", "cross the road : traverse la route.", "It's on your left / on your right."],
   [("left", "gauche"), ("right", "droite"), ("straight on", "tout droit"), ("turn", "tourner"), ("cross", "traverser"), ("road", "route"), ("corner", "coin"), ("traffic lights", "feux"),
    ("roundabout", "rond-point"), ("map", "carte"), ("north", "nord"), ("south", "sud"), ("east", "est"), ("west", "ouest"), ("far", "loin"), ("near", "près")],
   [("Excuse me, where is the market?", "Excusez-moi, où est le marché ?"), ("Go straight on.", "Allez tout droit."), ("Turn left at the traffic lights.", "Tournez à gauche aux feux."),
    ("Cross the road carefully.", "Traversez la route prudemment."), ("It's on your right.", "C'est sur votre droite."), ("Senegal is in West Africa.", "Le Sénégal est en Afrique de l'Ouest.")],
   "Confondre « left » (gauche) et « right » (droite)."),
  ("Shopping and money", "en4-shopping",
   ["Pour acheter : « How much is it? » – « It's 500 francs. »", "« Can I have two kilos of rice, please? »"],
   ["How much…? : combien (prix) ; How many…? : combien (nombre).", "cheap : bon marché ; expensive : cher.", "change : monnaie ; price : prix.", "a kilo of, a bag of, a bottle of."],
   [("shop", "boutique"), ("price", "prix"), ("money", "argent"), ("change", "monnaie"), ("cheap", "bon marché"), ("expensive", "cher"), ("buy", "acheter"), ("sell", "vendre"), ("pay", "payer"),
    ("customer", "client"), ("seller", "vendeur"), ("a kilo of", "un kilo de"), ("a bottle of", "une bouteille de"), ("a bag of", "un sac de"), ("bill", "addition, facture"), ("coin", "pièce")],
   [("How much is it?", "Combien ça coûte ?"), ("It's two hundred francs.", "C'est deux cents francs."), ("Can I have a kilo of rice, please?", "Je peux avoir un kilo de riz, s'il vous plaît ?"),
    ("It's too expensive.", "C'est trop cher."), ("Here is your change.", "Voici votre monnaie."), ("I want to buy a bottle of water.", "Je veux acheter une bouteille d'eau.")],
   "Confondre « How much » (prix, quantité non comptable) et « How many » (nombre d'objets)."),
  ("Health: at the doctor's", "en4-health",
   ["Pour dire où on a mal : « I have got a headache. » (j'ai mal à la tête).", "Le médecin demande : « What's the matter? » (qu'est-ce qui ne va pas ?)"],
   ["headache : mal de tête ; stomachache : mal de ventre ; toothache : mal de dents.", "I have got a cold : j'ai un rhume ; a fever : de la fièvre.", "You should rest : tu devrais te reposer.", "Wash your hands, sleep under a mosquito net."],
   [("headache", "mal de tête"), ("stomachache", "mal de ventre"), ("toothache", "mal de dents"), ("fever", "fièvre"), ("cough", "toux"), ("cold", "rhume"), ("medicine", "médicament"),
    ("doctor", "médecin"), ("nurse", "infirmier"), ("hospital", "hôpital"), ("rest", "se reposer"), ("mosquito net", "moustiquaire"), ("malaria", "paludisme"), ("healthy", "en bonne santé"), ("ill", "malade")],
   [("What's the matter?", "Qu'est-ce qui ne va pas ?"), ("I have got a headache.", "J'ai mal à la tête."), ("She has got a fever.", "Elle a de la fièvre."),
    ("You should stay in bed.", "Tu devrais rester au lit."), ("Sleep under a mosquito net.", "Dors sous une moustiquaire."), ("Take this medicine three times a day.", "Prends ce médicament trois fois par jour.")],
   "Dire « I have mal at the head » : on dit « I have got a headache »."),
  ("Comparing: bigger than", "en4-comparing",
   ["Pour comparer : adjectif court + -er + than : « A lion is bigger than a cat. »", "Adjectif long : more + adjectif + than : « more beautiful than »."],
   ["big → bigger (on double la consonne) ; happy → happier.", "good → better ; bad → worse (irréguliers).", "Le plus : the biggest, the most beautiful.", "as tall as : aussi grand que."],
   [("big", "bigger"), ("small", "smaller"), ("tall", "taller"), ("short", "shorter"), ("fast", "faster"), ("slow", "slower"), ("old", "older"), ("young", "younger"), ("hot", "hotter"),
    ("happy", "happier"), ("good", "better"), ("bad", "worse"), ("long", "longer"), ("heavy", "heavier"), ("strong", "stronger")],
   [("An elephant is bigger than a lion.", "Un éléphant est plus gros qu'un lion."), ("Awa is taller than her sister.", "Awa est plus grande que sa sœur."),
    ("A car is faster than a bike.", "Une voiture est plus rapide qu'un vélo."), ("The Nile is the longest river in Africa.", "Le Nil est le plus long fleuve d'Afrique."),
    ("This book is better than that one.", "Ce livre est meilleur que celui-là."), ("Dakar is bigger than Kaolack.", "Dakar est plus grande que Kaolack.")],
   "Dire « more big » ou « gooder » : on dit « bigger » et « better »."),
  ("Countries and nationalities", "en4-countries",
   ["Les pays et les nationalités prennent une majuscule : Senegal, Senegalese.", "« Where are you from? » – « I'm from Senegal. I'm Senegalese. »"],
   ["Senegal → Senegalese ; Mali → Malian ; Nigeria → Nigerian.", "France → French ; England → English ; America → American.", "the capital of Senegal is Dakar.", "I speak Wolof, French and English."],
   [("Senegal", "Sénégal"), ("Senegalese", "sénégalais"), ("Mali", "Mali"), ("Gambia", "Gambie"), ("Mauritania", "Mauritanie"), ("Guinea", "Guinée"), ("Nigeria", "Nigeria"),
    ("Ghana", "Ghana"), ("Morocco", "Maroc"), ("Egypt", "Égypte"), ("France", "France"), ("England", "Angleterre"), ("Africa", "Afrique"), ("Europe", "Europe"), ("country", "pays"), ("capital", "capitale")],
   [("Where are you from?", "D'où viens-tu ?"), ("I'm from Senegal.", "Je viens du Sénégal."), ("Dakar is the capital of Senegal.", "Dakar est la capitale du Sénégal."),
    ("He speaks English and French.", "Il parle anglais et français."), ("Gambia is inside Senegal.", "La Gambie est à l'intérieur du Sénégal."), ("Ghana is an English-speaking country.", "Le Ghana est un pays anglophone.")],
   "Oublier la majuscule : on écrit « English », « Senegalese »."),
  ("Describing people", "en4-describing",
   ["Pour décrire quelqu'un : « She is tall and kind. She has got short black hair. »", "be pour le caractère et la taille ; have got pour les cheveux et les yeux."],
   ["tall / short : grand / petit ; thin / fat : mince / gros.", "kind : gentil ; funny : drôle ; clever : intelligent ; lazy : paresseux.", "She has got curly hair : cheveux frisés.", "L'adjectif ne prend jamais de « s » : two kind girls."],
   [("tall", "grand"), ("short", "petit"), ("thin", "mince"), ("strong", "fort"), ("kind", "gentil"), ("funny", "drôle"), ("clever", "intelligent"), ("lazy", "paresseux"),
    ("brave", "courageux"), ("polite", "poli"), ("beautiful", "beau, belle"), ("handsome", "beau (homme)"), ("curly hair", "cheveux frisés"), ("straight hair", "cheveux raides"), ("beard", "barbe"), ("glasses", "lunettes")],
   [("My teacher is tall and kind.", "Mon maître est grand et gentil."), ("She has got curly black hair.", "Elle a les cheveux noirs et frisés."), ("He is very funny.", "Il est très drôle."),
    ("My grandfather has got a white beard.", "Mon grand-père a une barbe blanche."), ("They are clever pupils.", "Ce sont des élèves intelligents."), ("Is she polite? Yes, she is.", "Est-elle polie ? Oui.")],
   "Dire « she is long hair » : on dit « she has got long hair »."),
]

# chapitres de grammaire où la 2e colonne n'est pas une traduction
FORMES = {"en3-plurals": "Pluriel de", "en4-past": "Passé de", "en4-comparing": "Comparatif de"}


def _qcm(rng, cid, mots, phrases):
    out, mots = [], list(mots)
    rng.shuffle(mots)
    forme = FORMES.get(cid)
    for k, (en, fr) in enumerate(mots[:4]):
        autres = [m for m in mots if m[0] != en]
        if forme:
            f = [x[1] for x in autres if x[1] != fr][:3]
            out.append((f"{forme} « {en} » :", fr, *f, f"{en} → {fr}."))
        elif k % 2 == 0:
            f = [x[0] for x in autres if x[0] != en][:3]
            out.append((f"Comment dit-on « {fr} » en anglais ?", en, *f, f"{fr} = {en}."))
        else:
            f = [x[1] for x in autres if x[1] != fr][:3]
            out.append((f"Que veut dire « {en} » ?", fr, *f, f"{en} = {fr}."))
    ph = list(phrases)
    rng.shuffle(ph)
    for en, fr in ph[:2]:
        f = [x[1] for x in phrases if x[0] != en][:3]
        out.append((f"Que veut dire « {en} » ?", fr, *f, f"{en} = {fr}."))
    return out


def _steps(rng, choix, phrases, mots, forme):
    ph = list(choix)
    rng.shuffle(ph)
    st = []
    for en, fr in ph[:2]:
        f = [x[1] for x in phrases if x[0] != en]
        rng.shuffle(f)
        f = f[:3]
        st.append((f"« {en} » veut dire :", fr, *f, f"{en} = {fr}."))
    m = list(mots)
    rng.shuffle(m)
    for en, fr in m[:2]:
        if forme:
            f = [x[1] for x in mots if x[0] != en][:3]
            st.append((f"{forme} « {en} » :", fr, *f, f"{en} → {fr}."))
        else:
            f = [x[0] for x in mots if x[0] != en][:3]
            st.append((f"En anglais, « {fr} » se dit :", en, *f, f"{fr} = {en}."))
    return st


def chapitres(lv):
    rng = random.Random(f"anglais-{lv}")
    out = []
    for t, cid, cours, retenir, mots, phrases, piege in T[lv]:
        forme = FORMES.get(cid)
        ex = [("Les mots", [f"{en} : {fr}" for en, fr in mots[:8]]), ("Les phrases", [f"{en} = {fr}" for en, fr in phrases[:4]])]
        ctx = "Petit dialogue : " + " ".join(f"« {en} »" for en, _ in phrases[:3])
        ctx2 = "À la maison : " + " ".join(f"« {en} »" for en, _ in phrases[3:6])
        out.append(CH(t, cid, cours, retenir, ex, piege, f"Comprendre et utiliser les mots et les phrases : {t}.", ctx, _steps(rng, phrases[:3], phrases, mots, forme),
                      _qcm(rng, cid, mots, phrases), dev=(f"{t} : à la maison", ctx2, _steps(rng, phrases[3:], phrases, mots, forme))))
    return out


def vocab_js():
    """Vocabulaire pour les jeux et les questions à mots nouveaux (docs/vocab_en.js)."""
    import json
    data = {lv: [{"t": t, "id": cid, "forme": FORMES.get(cid), "mots": mots, "phrases": phrases} for t, cid, _, _, mots, phrases, _ in T[lv]] for lv in T}
    return "// Écrit par contenu/build.py depuis contenu/primaire_anglais.py : ne pas modifier à la main.\nconst VOCAB_EN = " + json.dumps(data, ensure_ascii=False) + ";\n"
