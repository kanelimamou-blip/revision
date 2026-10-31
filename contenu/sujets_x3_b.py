# Sujets types d'entraînement ×3 : Terminale, histoire-géographie, anglais, espagnol.
from sujets_tle2 import P, noter, A, TOUTES

def _hg(n, h, g):
    return A(f"bac-type-hg-{n}", "Histoire-Géographie", TOUTES, "L, S et G", "4 h", [f"Histoire : {h}", f"Géographie : {g}"])
def _en(n, t):
    return A(f"bac-type-anglais-{n}", "Anglais", TOUTES, "L, S et G", "3 h", [f"Reading : {t}", "Language in use", "Writing"])
def _es(n, t):
    return A(f"bac-type-espagnol-{n}", "Espagnol (LV2)", TOUTES, "L, S et G", "3 h", [f"Comprensión : {t}", "Gramática", "Expresión"])

ANNALES_X = [
  _hg(4, "la décolonisation de l'Afrique", "le Sénégal, défis du développement"),
  _hg(5, "les relations Est-Ouest et la détente", "l'Union européenne, une puissance économique"),
  _hg(6, "l'ONU et la coopération internationale", "le Japon, une puissance économique"),
  _hg(7, "la Chine de Mao à nos jours", "le Brésil, puissance du Sud"),
  _hg(8, "le monde arabe et le conflit israélo-palestinien", "la mondialisation et ses acteurs"),
  _hg(9, "l'Union africaine et l'unité du continent", "la Russie, une puissance en reconstruction"),
  _en(4, "climate change in the Sahel"),
  _en(5, "technology and young people"),
  _en(6, "health and malaria prevention"),
  _en(7, "unemployment and entrepreneurship"),
  _en(8, "traditions and modern life"),
  _en(9, "democracy and citizenship"),
  _es(4, "las nuevas tecnologías"),
  _es(5, "la familia"),
  _es(6, "el deporte"),
  _es(7, "la salud"),
  _es(8, "la mujer en la sociedad"),
  _es(9, "el turismo"),
]

GUIDED_X = {
  "bac-type-hg-4": noter([
    P("1. Histoire : dissertation", "Sujet : « La décolonisation de l'Afrique noire (1945-1960) : causes et modalités. »", [
      ("Une cause externe de la décolonisation :", "l'affaiblissement des puissances coloniales après la Seconde Guerre mondiale", "la découverte de l'Amérique", "la révolution industrielle", "la chute de l'Empire romain", "Contexte de 1945."),
      ("Rôle de l'ONU et des deux Grands :", "ils soutiennent le droit des peuples à disposer d'eux-mêmes", "ils renforcent les colonies", "ils interdisent l'indépendance", "ils restent neutres", "Charte de l'ONU, art. 1."),
      ("Une conférence qui encourage les peuples colonisés :", "Bandung (1955)", "Yalta (1945)", "Berlin (1885)", "Versailles (1919)", "Afro-asiatisme."),
      ("Le Sénégal accède à l'indépendance :", "en 1960, de façon négociée", "en 1945 par la guerre", "en 1990", "jamais", "Après l'éphémère Fédération du Mali."),
      ("Exemple de décolonisation violente en Afrique :", "l'Algérie (1954-1962)", "le Sénégal", "le Bénin", "le Gabon", "Guerre d'indépendance."),
    ]),
    P("2. Géographie : commentaire", "Document : tableau d'indicateurs du Sénégal (population, IDH, part de l'agriculture dans l'emploi, taux d'urbanisation).", [
      ("L'IDH combine :", "santé (espérance de vie), éducation et niveau de vie", "seulement le PIB", "la superficie", "le climat", "Indicateur du PNUD."),
      ("Un défi démographique du Sénégal :", "une population très jeune qui demande écoles et emplois", "une population très âgée", "une population en baisse", "aucun défi", "Plus de la moitié a moins de 20 ans."),
      ("Un atout économique récent :", "l'exploitation du pétrole et du gaz", "l'industrie automobile lourde", "les mines de charbon", "les stations de ski", "Sangomar, GTA."),
      ("Un plan de développement du Sénégal :", "le Plan Sénégal émergent puis la vision Sénégal 2050", "le plan Marshall", "le New Deal", "le plan quinquennal soviétique", "Politique publique."),
    ]),
  ]),
  "bac-type-hg-5": noter([
    P("1. Histoire : dissertation", "Sujet : « De la crise de Cuba à la détente (1962-1975). »", [
      ("La crise de Cuba (1962) oppose :", "les États-Unis et l'URSS à propos de missiles soviétiques", "la France et l'Allemagne", "la Chine et le Japon", "le Sénégal et le Mali", "Point culminant de la guerre froide."),
      ("Conséquence directe de la crise :", "l'installation du « téléphone rouge » entre Washington et Moscou", "une guerre nucléaire", "la chute du mur de Berlin", "la fin de l'ONU", "Dialogue direct."),
      ("Un accord de la détente :", "les accords SALT I (1972) de limitation des armes", "le traité de Versailles", "le pacte de Varsovie", "le plan Marshall", "Contrôle des armements."),
      ("Les accords d'Helsinki (1975) portent sur :", "la sécurité en Europe et les droits de l'homme", "la décolonisation", "le pétrole", "le sport", "Conférence sur la sécurité."),
    ]),
    P("2. Géographie : commentaire", "Document : carte de l'Union européenne et graphique de son commerce extérieur.", [
      ("L'UE est née du traité de :", "Rome (1957), qui crée la CEE", "Dakar", "Bandung", "Tokyo", "Six pays fondateurs."),
      ("La monnaie commune de nombreux pays de l'UE :", "l'euro", "le franc CFA", "le dollar", "le yen", "Depuis 1999-2002."),
      ("Un atout de l'UE :", "un grand marché unique riche et une forte industrie", "un territoire désertique", "une population très jeune", "l'absence de commerce", "Puissance commerciale."),
      ("Une limite de l'UE :", "des inégalités entre régions et une faible unité politique", "une absence totale d'industrie", "une monnaie unique pour le monde entier", "aucune ville", "Faiblesses."),
      ("Le partenariat UE-Afrique se traduit par :", "des accords commerciaux et une aide au développement", "une colonisation nouvelle", "une monnaie unique africaine européenne", "aucun échange", "Accords de Cotonou, puis de Samoa."),
    ]),
  ]),
  "bac-type-hg-6": noter([
    P("1. Histoire : dissertation", "Sujet : « L'ONU, instrument de paix et de coopération depuis 1945. »", [
      ("L'ONU est créée en :", "1945, à San Francisco", "1919, à Versailles", "1960, à Dakar", "1989, à Berlin", "Charte de San Francisco."),
      ("L'organe qui décide des sanctions et des interventions :", "le Conseil de sécurité", "l'UNICEF", "la FAO", "l'OMS", "15 membres dont 5 permanents."),
      ("Le droit de veto appartient :", "aux 5 membres permanents du Conseil de sécurité", "à tous les États", "au Secrétaire général seul", "à l'Afrique", "États-Unis, Russie, Chine, France, Royaume-Uni."),
      ("Un exemple d'action de l'ONU en Afrique :", "les Casques bleus au Mali (MINUSMA)", "la colonisation du Congo", "la traite négrière", "le partage de Berlin", "Opération de maintien de la paix."),
      ("Une critique faite à l'ONU :", "la paralysie du Conseil de sécurité par le veto", "trop de pays africains au Conseil permanent", "l'absence d'Assemblée générale", "elle n'a aucun membre", "Réforme réclamée par l'Afrique."),
    ]),
    P("2. Géographie : commentaire", "Document : carte des industries et des ports du Japon.", [
      ("Le cœur industriel du Japon :", "la mégalopole littorale de Tokyo à Osaka", "l'île d'Hokkaido", "les montagnes du centre", "les forêts", "Façade Pacifique."),
      ("Un handicap naturel du Japon :", "un relief montagneux et des séismes fréquents", "un climat désertique", "l'absence de côtes", "un territoire trop plat", "Contraintes."),
      ("Le Japon compense le manque de matières premières par :", "l'importation et la transformation industrielle", "l'agriculture extensive", "les mines d'or", "l'isolement", "Économie de transformation."),
      ("Un problème démographique du Japon :", "le vieillissement de la population", "une natalité très forte", "une population très jeune", "une immigration massive", "Défi actuel."),
    ]),
  ]),
  "bac-type-hg-7": noter([
    P("1. Histoire : dissertation", "Sujet : « La Chine de 1949 à nos jours : du communisme maoïste à la puissance mondiale. »", [
      ("La République populaire de Chine est proclamée en 1949 par :", "Mao Zedong", "Deng Xiaoping", "Tchang Kaï-chek", "Sun Yat-sen", "Victoire communiste."),
      ("Le « Grand Bond en avant » (1958) visait :", "une industrialisation rapide, avec un échec et une famine", "l'ouverture au capitalisme", "la conquête spatiale", "la démocratie", "Échec tragique."),
      ("La Révolution culturelle (1966-1976) :", "une campagne de Mao contre ses opposants avec les Gardes rouges", "un festival artistique", "une réforme agricole réussie", "une guerre contre le Japon", "Violences politiques."),
      ("Les réformes de Deng Xiaoping après 1978 :", "ouverture économique et zones économiques spéciales", "retour de l'empereur", "fermeture totale du pays", "abandon de l'industrie", "Socialisme de marché."),
    ]),
    P("2. Géographie : commentaire", "Document : tableau de l'économie du Brésil (PIB, exportations, inégalités).", [
      ("Le Brésil est membre :", "des BRICS", "du G7", "de l'Union européenne", "de la CEDEAO", "Pays émergent."),
      ("Un atout agricole du Brésil :", "il est un grand exportateur de soja, café et viande", "il importe tout", "il n'a pas de terres", "il ne cultive que le riz", "Agro-industrie."),
      ("Une forte inégalité au Brésil se voit dans :", "les favelas à côté des quartiers riches", "l'absence de villes", "l'égalité parfaite des revenus", "la neige", "Fractures sociales."),
      ("Un enjeu environnemental majeur :", "la déforestation de l'Amazonie", "la fonte des glaciers alpins", "la désertification du Sahara", "la pollution du Danube", "Front pionnier."),
      ("Le pôle économique majeur du Brésil :", "São Paulo", "Manaus", "Brasília", "Recife", "Métropole industrielle."),
    ]),
  ]),
  "bac-type-hg-8": noter([
    P("1. Histoire : dissertation", "Sujet : « Le conflit israélo-palestinien depuis 1948. »", [
      ("L'État d'Israël est proclamé en :", "1948", "1917", "1967", "1993", "Fin du mandat britannique."),
      ("La guerre des Six Jours (1967) aboutit à :", "l'occupation par Israël de la Cisjordanie, de Gaza, du Golan et du Sinaï", "la création de la Palestine", "la paix définitive", "la fin d'Israël", "Territoires occupés."),
      ("Les accords d'Oslo (1993) prévoient :", "une reconnaissance mutuelle et une autonomie palestinienne", "la disparition d'Israël", "l'annexion de Gaza par l'Égypte", "rien", "Rabin et Arafat."),
      ("Un obstacle à la paix :", "la colonisation, le statut de Jérusalem et les violences", "l'absence de frontières naturelles", "le climat", "la langue", "Questions non réglées."),
    ]),
    P("2. Géographie : commentaire", "Document : carte des flux mondiaux de marchandises et des grandes firmes.", [
      ("La mondialisation est :", "l'intensification des échanges à l'échelle de la planète", "la fermeture des frontières", "le retour à l'autarcie", "la fin du commerce", "Définition."),
      ("Un acteur majeur de la mondialisation :", "les firmes multinationales", "les petits villages", "les nomades seuls", "les clubs de sport amateurs", "FMN."),
      ("La « Triade » regroupe :", "l'Amérique du Nord, l'Europe et l'Asie orientale", "l'Afrique, l'Amérique du Sud, l'Océanie", "trois pays africains", "les pôles", "Centres d'impulsion."),
      ("Une organisation qui encadre le commerce mondial :", "l'OMC", "l'OMS", "l'UNESCO", "la FIFA", "Organisation mondiale du commerce."),
      ("Une limite de la mondialisation pour l'Afrique :", "une faible part du commerce mondial et la dépendance aux matières premières", "une part majoritaire du commerce", "trop d'usines", "aucun échange", "Intégration inégale."),
    ]),
  ]),
  "bac-type-hg-9": noter([
    P("1. Histoire : dissertation", "Sujet : « De l'OUA à l'Union africaine : la recherche de l'unité africaine. »", [
      ("L'OUA est créée en 1963 à :", "Addis-Abeba", "Dakar", "Lagos", "Le Caire", "25 mai 1963."),
      ("Un objectif de l'OUA :", "achever la décolonisation et défendre la souveraineté des États", "recoloniser l'Afrique", "créer une monnaie mondiale", "interdire le commerce", "Charte de l'OUA."),
      ("Une critique faite à l'OUA :", "la non-ingérence l'empêchait d'agir dans les conflits internes", "elle avait trop de pouvoir militaire", "elle n'avait aucun membre", "elle était européenne", "Limites."),
      ("L'Union africaine remplace l'OUA en :", "2002", "1960", "1975", "2020", "Sommet de Durban."),
      ("Un projet économique récent de l'UA :", "la Zone de libre-échange continentale africaine (ZLECAf)", "le plan Marshall", "l'euro africain obligatoire", "la fermeture des frontières", "Marché commun africain."),
    ]),
    P("2. Géographie : commentaire", "Document : carte des ressources et de la population de la Russie.", [
      ("La Russie est le pays :", "le plus vaste du monde", "le plus peuplé du monde", "le plus petit d'Europe", "le plus chaud", "17 millions de km²."),
      ("Principale richesse exportée :", "le pétrole et le gaz", "le café", "le cacao", "l'arachide", "Rente énergétique."),
      ("Un handicap de la Russie :", "un climat rude et des régions sibériennes peu peuplées", "l'absence de ressources", "une population très jeune", "aucune côte", "Contraintes."),
      ("La population russe se concentre :", "à l'ouest, dans la partie européenne", "en Sibérie orientale", "au pôle Nord", "sur les îles", "Déséquilibre."),
    ]),
  ]),
  "bac-type-anglais-4": noter([
    P("1. Reading comprehension", "Text (training): « In the Sahel, rains are becoming irregular. Farmers in Matam lose part of their harvest, and many young people leave for the cities. Planting trees and saving water are now vital. »", [
      ("The text is mainly about:", "the effects of climate change on Sahel farmers", "football in Dakar", "a wedding ceremony", "the history of Rome", "Main idea."),
      ("« Irregular » rains are rains that:", "do not come at the expected time or quantity", "fall every day", "are always heavy", "never stop", "Vocabulary."),
      ("According to the text, many young people:", "leave for the cities", "become fishermen in the desert", "go to the moon", "stay at home all day", "Rural exodus."),
      ("A solution mentioned in the text:", "planting trees and saving water", "cutting all the forests", "building more cars", "burning crops", "Adaptation."),
    ]),
    P("2. Language in use", "Choose the correct form.", [
      ("If farmers ___ trees, the soil would be better protected.", "planted", "plant", "will plant", "planting", "Second conditional: if + preterite."),
      ("The harvest ___ by the drought last year.", "was destroyed", "destroyed", "is destroying", "has destroy", "Passive voice, past."),
      ("The opposite of « increase » is:", "decrease", "raise", "grow", "improve", "Antonym."),
    ]),
    P("3. Writing", "Write a letter (about 150 words) to your local mayor suggesting actions to protect the environment.", [
      ("A formal letter begins with:", "Dear Sir or Madam,", "Hi buddy!", "Yo Mayor,", "See you,", "Register."),
      ("A good way to make a suggestion:", "I would suggest that the town plant more trees.", "You must do it now or else.", "Trees are bad.", "I don't care.", "Polite suggestion."),
      ("A formal letter ends with:", "Yours faithfully,", "Love,", "Bye!", "Cheers,", "Closing formula when the name is unknown."),
    ]),
  ]),
  "bac-type-anglais-5": noter([
    P("1. Reading comprehension", "Text (training): « Smartphones help students find information quickly, but many spend hours on social media at night. Teachers say that tired pupils lose concentration in class. »", [
      ("The text deals with:", "the advantages and dangers of smartphones for students", "the price of rice", "a trip to Saint-Louis", "wrestling champions", "Main idea."),
      ("One advantage mentioned:", "students find information quickly", "phones cook meals", "phones replace teachers", "phones cure diseases", "Positive point."),
      ("Why do pupils lose concentration?", "They are tired after using social media at night.", "The classroom is too big.", "They are hungry.", "The teacher is absent.", "Cause and effect."),
    ]),
    P("2. Language in use", "Grammar and vocabulary.", [
      ("Students ___ use their phones in the exam room.", "mustn't", "don't have", "needn't to", "aren't must", "Prohibition."),
      ("She asked me where I ___ my phone.", "had put", "have put", "put will", "am putting", "Reported speech: past perfect."),
      ("« Addicted » means:", "unable to stop doing something", "very happy", "very rich", "well educated", "Vocabulary."),
      ("The more you sleep, ___ you concentrate.", "the better", "the good", "best", "more good", "Double comparative."),
    ]),
    P("3. Writing", "Essay (about 150 words): « Should mobile phones be banned in schools? »", [
      ("A good essay structure:", "introduction, arguments for and against, conclusion", "only a list of words", "one long sentence", "a dialogue only", "Organisation."),
      ("A useful linking word to add an idea:", "Moreover", "However", "Although", "Despite", "Addition."),
      ("A useful linking word to contrast:", "On the other hand", "Furthermore", "In addition", "Besides", "Opposition."),
    ]),
  ]),
  "bac-type-anglais-6": noter([
    P("1. Reading comprehension", "Text (training): « Malaria still kills thousands of children in Africa. Sleeping under a treated mosquito net and removing stagnant water are simple ways to prevent it. »", [
      ("The text is about:", "the prevention of malaria", "the history of medicine in Europe", "a football match", "school holidays", "Main idea."),
      ("Malaria is transmitted by:", "mosquitoes", "dogs", "water bottles", "bread", "General knowledge in the text."),
      ("A simple way to prevent malaria:", "sleeping under a treated mosquito net", "drinking cold water", "eating more sugar", "staying in the sun", "Prevention."),
    ]),
    P("2. Language in use", "Choose the correct answer.", [
      ("Stagnant water ___ be removed around houses.", "should", "should to", "musts", "is should", "Modal + base verb."),
      ("Thousands of children ___ from malaria every year.", "die", "dies", "dying", "is dying", "Subject-verb agreement."),
      ("« Prevent » is closest in meaning to:", "stop something from happening", "cause", "cure", "forget", "Synonym."),
      ("Choose the noun: « to prevent » → ___", "prevention", "preventive", "preventing", "prevented", "Word formation."),
    ]),
    P("3. Writing", "Write an article (about 150 words) for your school magazine about health habits.", [
      ("An article needs:", "a catchy title and clear paragraphs", "no title", "a phone number", "a recipe only", "Format."),
      ("A good piece of advice:", "Wash your hands before eating.", "Never sleep.", "Eat only sweets.", "Avoid all doctors.", "Relevant content."),
      ("To finish the article you can:", "encourage readers to act", "start a new topic", "copy the title again", "write your address", "Conclusion."),
    ]),
  ]),
  "bac-type-anglais-7": noter([
    P("1. Reading comprehension", "Text (training): « Awa could not find a job after university. She started selling local juices online. Two years later, she employs five young people. »", [
      ("The text tells the story of:", "a young graduate who created her own business", "a farmer who lost his land", "a footballer", "a teacher on strike", "Main idea."),
      ("Why did Awa start a business?", "She could not find a job.", "She wanted to travel.", "Her parents forced her.", "She failed her exams.", "Cause."),
      ("How many people does she employ now?", "five", "two", "ten", "none", "Detail."),
    ]),
    P("2. Language in use", "Grammar.", [
      ("She ___ juices online for two years.", "has been selling", "sells since", "is sell", "sold since", "Present perfect continuous with « for »."),
      ("If she had not tried, she ___ successful.", "would not have been", "will not be", "is not", "would not be had", "Third conditional."),
      ("An « entrepreneur » is someone who:", "starts and runs a business", "works for the government", "never works", "studies abroad", "Vocabulary."),
    ]),
    P("3. Writing", "Write a short speech (about 150 words) encouraging young people to create businesses.", [
      ("A speech starts by:", "greeting the audience", "giving the conclusion", "insulting people", "writing the date", "Oral register."),
      ("A persuasive sentence:", "Don't wait for a job: create one!", "Business is boring.", "Nobody can succeed.", "Stay at home.", "Persuasion."),
      ("An example that supports the speech:", "Awa's juice business that employs five people", "a film about space", "the price of petrol", "a wrestling match", "Use the text."),
    ]),
  ]),
  "bac-type-anglais-8": noter([
    P("1. Reading comprehension", "Text (training): « In many families, grandparents tell stories in the evening. Today, television and phones often replace these moments, and some fear that traditions will disappear. »", [
      ("The text is about:", "traditions threatened by modern life", "a new phone model", "the rainy season", "school fees", "Main idea."),
      ("What replaces evening stories today?", "television and phones", "books", "radio only", "nothing", "Detail."),
      ("Some people fear that:", "traditions will disappear", "phones will become cheaper", "grandparents will move", "schools will close", "Concern."),
    ]),
    P("2. Language in use", "Grammar.", [
      ("Grandparents ___ tell stories every evening when I was a child.", "used to", "use to", "were use", "uses to", "Past habit."),
      ("Traditions ___ be preserved by schools.", "can", "can to", "cans", "are can", "Modal."),
      ("The word « heritage » means:", "what is passed down from past generations", "a new invention", "a type of food", "a sport", "Vocabulary."),
      ("Neither television ___ phones can replace grandparents.", "nor", "or", "and", "but", "Neither … nor."),
    ]),
    P("3. Writing", "Write a dialogue (about 150 words) between a pupil and a grandparent about traditions.", [
      ("A dialogue shows:", "the names of speakers before each line", "only one speaker", "no punctuation", "a title only", "Format."),
      ("A polite question to a grandparent:", "Could you tell me how weddings were celebrated?", "Tell me now!", "You're too old.", "Go away.", "Register."),
      ("The dialogue should end with:", "a clear conclusion, for example a promise to keep traditions alive", "an insult", "a new character", "nothing", "Coherence."),
    ]),
  ]),
  "bac-type-anglais-9": noter([
    P("1. Reading comprehension", "Text (training): « Voting is a right and a duty. Yet many young people do not register on electoral lists. Citizenship also means respecting laws and taking part in community life. »", [
      ("The main idea:", "citizenship includes voting and active participation", "voting is forbidden", "laws are useless", "young people all vote", "Main idea."),
      ("The problem mentioned:", "many young people do not register to vote", "elections are cancelled", "there are no laws", "people vote twice", "Detail."),
      ("According to the text, citizenship also means:", "respecting laws and taking part in community life", "avoiding taxes", "staying at home", "ignoring neighbours", "Detail."),
    ]),
    P("2. Language in use", "Grammar.", [
      ("Young people ___ register on electoral lists.", "ought to", "ought", "oughts to", "are ought", "Advice."),
      ("Elections ___ every five years in many countries.", "are held", "hold", "are holding them", "held is", "Passive present."),
      ("The opposite of « responsible » is:", "irresponsible", "unresponsible", "disresponsible", "nonresponsable", "Prefix."),
    ]),
    P("3. Writing", "Essay (about 150 words): « Why should young people take part in elections? »", [
      ("A strong first argument:", "Voting allows young people to choose their future leaders.", "Voting is boring.", "Elections are noisy.", "Nobody listens.", "Relevant argument."),
      ("A useful phrase to conclude:", "To sum up,", "Once upon a time,", "First of all,", "By the way,", "Conclusion."),
      ("Your essay should:", "give your opinion with reasons and examples", "copy the text", "be only one line", "avoid any opinion", "Argumentation."),
    ]),
  ]),
  "bac-type-espagnol-4": noter([
    P("1. Comprensión", "Texto (de entrenamiento): « Los jóvenes pasan horas con el móvil. Internet les ayuda a estudiar, pero también puede aislarlos de su familia. »", [
      ("El tema del texto es:", "las nuevas tecnologías y los jóvenes", "la agricultura", "la historia de España", "la cocina", "Idea general."),
      ("Una ventaja de Internet según el texto:", "ayuda a estudiar", "cura enfermedades", "da dinero", "hace llover", "Detalle."),
      ("Un peligro mencionado:", "aislar a los jóvenes de su familia", "romper los ordenadores", "cerrar las escuelas", "subir los precios", "Detalle."),
    ]),
    P("2. Gramática", "Elegir la forma correcta.", [
      ("Ayer yo ___ dos horas en Internet.", "pasé", "paso", "pasaré", "pasaba mañana", "Pretérito indefinido."),
      ("Es importante que los jóvenes ___ menos tiempo con el móvil.", "pasen", "pasan", "pasar", "pasarán", "Subjuntivo tras « es importante que »."),
      ("« Aislar » significa:", "separar de los demás", "juntar", "ayudar", "comprar", "Vocabulario."),
    ]),
    P("3. Expresión", "Redacta unas 120 palabras: ¿Internet es útil para los estudiantes?", [
      ("Para dar tu opinión puedes escribir:", "En mi opinión,", "Había una vez,", "Hasta luego,", "Buenos días,", "Expresar opinión."),
      ("Para oponer dos ideas:", "Sin embargo,", "Además,", "Por eso,", "Primero,", "Conector de oposición."),
      ("Para concluir:", "En conclusión,", "Por ejemplo,", "Además,", "Al principio,", "Conclusión."),
    ]),
  ]),
  "bac-type-espagnol-5": noter([
    P("1. Comprensión", "Texto: « En la familia de Fatou viven abuelos, padres y niños en la misma casa. Todos comparten las comidas y se ayudan mutuamente. »", [
      ("El texto describe:", "una familia extensa que vive unida", "una familia que vive sola", "un viaje", "un partido de fútbol", "Idea general."),
      ("¿Quiénes viven en la casa?", "abuelos, padres y niños", "solo los padres", "solo los niños", "amigos", "Detalle."),
      ("Un valor de esta familia:", "la solidaridad", "el egoísmo", "la violencia", "la soledad", "Valor."),
    ]),
    P("2. Gramática", "Elegir la forma correcta.", [
      ("Mis abuelos ___ muy simpáticos.", "son", "están", "es", "somos", "Ser para cualidades."),
      ("Cuando era niño, ___ con mis abuelos.", "vivía", "viví mañana", "viviré", "vivo ayer", "Imperfecto: costumbre."),
      ("El plural de « la casa grande » es:", "las casas grandes", "los casas grande", "la casas grandes", "las casa grandes", "Concordancia."),
      ("« Compartir » significa:", "dar una parte a otros", "esconder", "vender", "romper", "Vocabulario."),
    ]),
    P("3. Expresión", "Describe a tu familia (unas 120 palabras).", [
      ("Para presentar a un miembro:", "Mi hermano mayor se llama Moussa.", "Moussa llamar hermano.", "Hermano Moussa es llama.", "Me Moussa hermano.", "Frase correcta."),
      ("Para hablar de una costumbre familiar:", "Los domingos comemos juntos.", "Domingos comer juntos ayer.", "Comemos domingo juntos mañana ayer.", "Juntos los domingo comen yo.", "Presente habitual."),
      ("Una buena conclusión:", "Para mí, la familia es lo más importante.", "Adiós familia.", "No sé.", "Familia es casa.", "Opinión final."),
    ]),
  ]),
  "bac-type-espagnol-6": noter([
    P("1. Comprensión", "Texto: « El deporte es bueno para la salud. En Senegal, la lucha y el fútbol unen a la gente, pero algunos jóvenes sueñan solo con ser campeones y dejan los estudios. »", [
      ("El tema del texto:", "el deporte, sus ventajas y sus riesgos", "la pesca", "la música", "el clima", "Idea general."),
      ("Dos deportes populares en Senegal según el texto:", "la lucha y el fútbol", "el esquí y el golf", "el hockey y el rugby", "la natación y el tenis", "Detalle."),
      ("Un riesgo mencionado:", "algunos jóvenes dejan los estudios", "el deporte mata", "los estadios cierran", "nadie juega", "Detalle."),
    ]),
    P("2. Gramática", "Elegir la forma correcta.", [
      ("Si ___ deporte cada día, estarás en forma.", "haces", "harías", "hiciera", "hacer", "Si + presente → futuro."),
      ("El fútbol es ___ popular que el baloncesto.", "más", "mucho", "tan", "muy", "Comparativo de superioridad."),
      ("« Los jóvenes sueñan con ser campeones »: el verbo es:", "soñar", "sonar", "sueño", "sonreír", "Infinitivo (diptongo o → ue)."),
    ]),
    P("3. Expresión", "¿Se puede hacer deporte y estudiar al mismo tiempo? (unas 120 palabras)", [
      ("Un buen argumento:", "El deporte ayuda a concentrarse mejor en los estudios.", "El deporte es aburrido.", "Estudiar es inútil.", "No hay escuelas.", "Argumento pertinente."),
      ("Para añadir una idea:", "Además,", "Sin embargo,", "Pero,", "Aunque,", "Conector de adición."),
      ("Un consejo final:", "Hay que organizar bien el tiempo.", "Hay que dejar la escuela.", "No hay que jugar nunca.", "Hay que dormir en clase.", "Conclusión."),
    ]),
  ]),
  "bac-type-espagnol-7": noter([
    P("1. Comprensión", "Texto: « El paludismo sigue siendo un problema grave. Dormir bajo un mosquitero y acudir pronto al médico salva vidas. »", [
      ("El texto trata de:", "la prevención del paludismo", "un viaje a Madrid", "la escuela", "la moda", "Idea general."),
      ("Un consejo del texto:", "dormir bajo un mosquitero", "beber agua sucia", "no ir al médico", "dormir fuera", "Detalle."),
      ("« Acudir pronto al médico » significa:", "ir rápidamente al médico", "llamar a un amigo", "comprar medicinas sin receta", "esperar mucho tiempo", "Comprensión."),
    ]),
    P("2. Gramática", "Elegir la forma correcta.", [
      ("___ bajo un mosquitero cada noche. (consejo, tú)", "Duerme", "Dormir tú", "Durmió", "Dormirás ayer", "Imperativo afirmativo."),
      ("No ___ agua sucia. (tú)", "bebas", "bebes", "bebe", "beber", "Imperativo negativo = subjuntivo."),
      ("« Salud » es lo contrario de:", "enfermedad", "vida", "fuerza", "alegría", "Antónimo."),
      ("El médico me ___ que descansara.", "dijo", "dice ayer", "dirá", "decir", "Estilo indirecto en pasado."),
    ]),
    P("3. Expresión", "Escribe consejos para cuidar la salud (unas 120 palabras).", [
      ("Una estructura útil para aconsejar:", "Te aconsejo que comas frutas.", "Te aconsejo comes frutas.", "Aconsejar tú frutas.", "Comas frutas aconsejo yo.", "Aconsejar que + subjuntivo."),
      ("Otro consejo pertinente:", "Hay que lavarse las manos antes de comer.", "Hay que comer solo dulces.", "No hay que dormir.", "Hay que fumar.", "Contenido."),
      ("Para terminar:", "Por último, cuidar la salud es responsabilidad de todos.", "Hola a todos.", "Erase una vez.", "No sé nada.", "Conclusión."),
    ]),
  ]),
  "bac-type-espagnol-8": noter([
    P("1. Comprensión", "Texto: « Hoy muchas mujeres senegalesas dirigen empresas y trabajan en la política, pero muchas niñas del campo todavía no van a la escuela. »", [
      ("El tema del texto:", "el lugar de la mujer en la sociedad", "la pesca", "la tecnología espacial", "el deporte", "Idea general."),
      ("Un progreso mencionado:", "muchas mujeres dirigen empresas", "las mujeres no trabajan", "las niñas no estudian", "nadie vota", "Detalle."),
      ("Un problema que persiste:", "muchas niñas del campo no van a la escuela", "hay demasiadas escuelas", "las mujeres no comen", "las ciudades están vacías", "Detalle."),
    ]),
    P("2. Gramática", "Elegir la forma correcta.", [
      ("Es necesario que todas las niñas ___ a la escuela.", "vayan", "van", "ir", "irán", "Subjuntivo de ir."),
      ("Las mujeres ___ trabajado mucho por la igualdad.", "han", "ha", "hemos", "habéis", "Pretérito perfecto, 3.ª plural."),
      ("« Igualdad » significa:", "mismos derechos para todos", "diferencia", "pobreza", "riqueza", "Vocabulario."),
    ]),
    P("3. Expresión", "¿Cómo mejorar la situación de las mujeres? (unas 120 palabras)", [
      ("Una propuesta pertinente:", "Escolarizar a todas las niñas.", "Prohibir el trabajo femenino.", "Cerrar las escuelas.", "No hacer nada.", "Propuesta."),
      ("Para expresar un deseo:", "Ojalá todas las niñas estudien.", "Ojalá todas las niñas estudian.", "Ojalá estudiar niñas.", "Ojalá estudiaron mañana.", "Ojalá + subjuntivo."),
      ("Una buena conclusión:", "La igualdad beneficia a toda la sociedad.", "Las mujeres no importan.", "Adiós.", "No sé.", "Opinión final."),
    ]),
  ]),
  "bac-type-espagnol-9": noter([
    P("1. Comprensión", "Texto: « El turismo trae dinero y empleo en la Petite-Côte y en Casamance. Pero también puede contaminar las playas y cambiar las costumbres locales. »", [
      ("El tema del texto:", "las ventajas y los inconvenientes del turismo", "la vida de un futbolista", "una receta", "la escuela", "Idea general."),
      ("Una ventaja del turismo:", "trae dinero y empleo", "destruye empleos", "cierra hoteles", "no tiene ventajas", "Detalle."),
      ("Un inconveniente:", "puede contaminar las playas", "hace llover", "baja la temperatura", "construye escuelas", "Detalle."),
    ]),
    P("2. Gramática", "Elegir la forma correcta.", [
      ("El año pasado muchos turistas ___ a Saly.", "vinieron", "vienen", "vendrán", "venían mañana", "Pretérito indefinido de venir."),
      ("Las playas ___ limpias si todos respetamos la naturaleza.", "estarán", "serán ayer", "están ayer", "estuvieron mañana", "Futuro con estar."),
      ("« Costumbres » significa:", "tradiciones, hábitos", "ropa", "monedas", "playas", "Vocabulario."),
    ]),
    P("3. Expresión", "Escribe un folleto para atraer turistas a tu región (unas 120 palabras).", [
      ("Un folleto turístico utiliza:", "frases cortas y atractivas, imperativos", "solo números", "frases tristes", "un diálogo de teatro", "Formato."),
      ("Una frase de folleto:", "¡Descubre las playas de la Petite-Côte!", "Las playas son malas.", "No vengas nunca.", "Hace mucho calor siempre, quédate en casa.", "Imperativo atractivo."),
      ("Para un turismo responsable puedes añadir:", "Respeta la naturaleza y las costumbres locales.", "Tira la basura en la playa.", "Ignora a los habitantes.", "Compra marfil.", "Mensaje responsable."),
    ]),
  ]),
}
