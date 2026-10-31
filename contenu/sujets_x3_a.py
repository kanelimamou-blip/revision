# Sujets types d'entraînement ×3 : Terminale, philosophie et français (sur le modèle de l'épreuve, pas des annales officielles).
from sujets_tle2 import P, noter, A, TOUTES

def _ph(n, sujet):
    return A(f"bac-type-philo-{n}", "Philosophie", TOUTES, "L, S et G", "4 h", [f"Dissertation : « {sujet} »"])

ANNALES_X = [
  _ph(5, "Peut-on se connaître soi-même ?"),
  _ph(6, "Être libre, est-ce faire ce que l'on veut ?"),
  _ph(7, "La vérité est-elle toujours bonne à dire ?"),
  _ph(8, "Le bonheur est-il le but de l'existence ?"),
  _ph(9, "L'État est-il l'ennemi de la liberté ?"),
  _ph(10, "Peut-on se passer de religion ?"),
  _ph(11, "L'art est-il inutile ?"),
  _ph(12, "Autrui est-il un obstacle à ma liberté ?"),
  A("bac-type-fr-5", "Français", TOUTES, "L, S et G", "4 h", ["Résumé et discussion : un texte sur les réseaux sociaux"]),
  A("bac-type-fr-6", "Français", TOUTES, "L, S et G", "4 h", ["Commentaire d'un poème de la Négritude"]),
  A("bac-type-fr-7", "Français", TOUTES, "L, S et G", "4 h", ["Dissertation : le théâtre, simple divertissement ?"]),
  A("bac-type-fr-8", "Français", TOUTES, "L, S et G", "4 h", ["Résumé et discussion : un texte sur l'exode rural"]),
  A("bac-type-fr-9", "Français", TOUTES, "L, S et G", "4 h", ["Commentaire d'un extrait de roman sur la tradition"]),
  A("bac-type-fr-10", "Français", TOUTES, "L, S et G", "4 h", ["Dissertation : la poésie et l'engagement"]),
  A("bac-type-fr-11", "Français", TOUTES, "L, S et G", "4 h", ["Résumé et discussion : un texte sur l'école et l'emploi"]),
  A("bac-type-fr-12", "Français", TOUTES, "L, S et G", "4 h", ["Dissertation : lire, est-ce s'évader ?"]),
]

GUIDED_X = {
  "bac-type-philo-5": noter([
    P("1. Analyser le sujet", "Sujet : « Peut-on se connaître soi-même ? »", [
      ("« Se connaître soi-même » signifie ici :", "savoir ce que l'on est vraiment : pensées, désirs, caractère", "connaître son nom et son âge", "connaître ses voisins", "savoir lire", "Connaissance de soi, pas état civil."),
      ("« Peut-on » interroge :", "la possibilité et les limites de cette connaissance", "l'autorisation de la loi", "la politesse", "le droit de vote", "Pouvoir au sens de capacité."),
      ("La difficulté centrale du sujet :", "le sujet qui connaît est aussi l'objet à connaître", "il n'existe aucun homme", "la science interdit d'y penser", "le sujet est trop simple", "On n'a pas de recul sur soi."),
    ]),
    P("2. Bâtir le plan", "Thèse, antithèse, dépassement.", [
      ("Partie 1 : oui, par la conscience, car :", "« Je pense donc je suis » : la pensée se saisit elle-même avec certitude", "on se voit dans un miroir", "les autres décident pour nous", "on naît savant", "Descartes, Méditations."),
      ("Partie 2 : la limite majeure vient de :", "l'inconscient, qui agit en nous sans que nous le sachions", "la météo", "l'écriture", "l'argent", "Freud : « le moi n'est pas maître dans sa propre maison »."),
      ("Partie 3 : on se connaît mieux :", "par ses actes, par autrui et par un travail sur soi jamais achevé", "en refusant de réfléchir", "en dormant", "jamais, donc il faut renoncer", "Sartre : autrui médiateur ; Socrate : « connais-toi toi-même »."),
    ]),
    P("3. Rédiger", "Introduction et conclusion.", [
      ("Une amorce pertinente :", "la devise de Delphes « Connais-toi toi-même » reprise par Socrate", "la date de naissance de Freud recopiée", "un proverbe sans rapport", "la conclusion", "Amener le sujet."),
      ("Un exemple pour la partie 2 :", "un lapsus qui révèle un désir caché", "une équation", "un match de football", "une recette", "Acte manqué chez Freud."),
      ("La conclusion répond :", "la connaissance de soi est possible mais toujours partielle et à poursuivre", "on se connaît parfaitement", "le sujet est absurde", "par une nouvelle question sans lien", "Réponse nuancée et claire."),
    ]),
  ]),
  "bac-type-philo-6": noter([
    P("1. Analyser le sujet", "Sujet : « Être libre, est-ce faire ce que l'on veut ? »", [
      ("La définition spontanée examinée :", "la liberté comme absence de contrainte et satisfaction des désirs", "la liberté comme obéissance aveugle", "la liberté comme richesse", "la liberté comme sommeil", "Opinion commune à discuter."),
      ("« Ce que l'on veut » peut désigner :", "des caprices dictés par les désirs ou une volonté réfléchie", "uniquement la loi", "les ordres des parents", "le hasard", "Ambiguïté du vouloir."),
      ("Problématique adaptée :", "Suivre ses désirs, est-ce être libre ou esclave de ses passions ?", "Combien de lois existe-t-il ?", "Qui est le plus riche ?", "La liberté se vend-elle ?", "Oppose désir et liberté."),
    ]),
    P("2. Bâtir le plan", "Thèse, antithèse, dépassement.", [
      ("Partie 1 : la liberté semble être :", "le pouvoir d'agir sans obstacle selon sa volonté", "l'absence de volonté", "la soumission", "la peur", "Définition commune (Hobbes)."),
      ("Partie 2 : obéir à tous ses désirs, c'est :", "être esclave de ses passions", "être sage", "être juste", "être raisonnable", "Rousseau : « l'impulsion du seul appétit est esclavage »."),
      ("Partie 3 : la vraie liberté est :", "l'autonomie : obéir à la loi qu'on s'est prescrite par la raison", "faire n'importe quoi", "n'avoir aucune règle", "obéir au plus fort", "Rousseau, Kant."),
    ]),
    P("3. Rédiger", "Exemples et conclusion.", [
      ("Un exemple pour la partie 2 :", "le fumeur qui veut arrêter mais n'y arrive pas", "un élève qui révise", "une loi votée", "une élection", "Dépendance au désir."),
      ("Citation utile pour la partie 3 :", "« L'obéissance à la loi qu'on s'est prescrite est liberté »", "« Après moi le déluge »", "« Le temps c'est de l'argent »", "« Qui vivra verra »", "Rousseau, Du contrat social."),
      ("La conclusion répond :", "être libre, c'est vouloir de façon réfléchie, pas céder à chaque envie", "la liberté n'existe pas", "il faut supprimer toute loi", "faire ce qu'on veut sans limite", "Réponse nuancée."),
    ]),
  ]),
  "bac-type-philo-7": noter([
    P("1. Analyser le sujet", "Sujet : « La vérité est-elle toujours bonne à dire ? »", [
      ("La vérité désigne ici :", "l'accord entre ce que l'on dit et la réalité", "une opinion à la mode", "un mensonge poli", "une croyance religieuse seulement", "Adéquation du discours au réel."),
      ("« Toujours bonne » pose la question :", "morale des conséquences de la vérité", "de la grammaire", "du prix de la vérité", "de la vitesse de parole", "Domaine moral."),
      ("Problématique adaptée :", "Faut-il dire la vérité en toutes circonstances, même quand elle peut blesser ?", "Qu'est-ce qu'un dictionnaire ?", "Faut-il parler fort ?", "La vérité est-elle une marchandise ?", "Devoir de vérité contre conséquences."),
    ]),
    P("2. Bâtir le plan", "Thèse, antithèse, dépassement.", [
      ("Partie 1 : oui, car le mensonge :", "détruit la confiance qui fonde les relations humaines", "est toujours utile", "rend riche", "n'a aucune conséquence", "Kant : la véracité est un devoir absolu."),
      ("Partie 2 : non, la vérité peut :", "blesser ou mettre en danger un innocent", "toujours guérir", "ne jamais choquer", "remplacer la loi", "Benjamin Constant contre Kant."),
      ("Partie 3 : dépassement :", "dire la vérité avec tact, au bon moment, sans renoncer à la sincérité", "mentir systématiquement", "ne plus jamais parler", "dire n'importe quoi", "Prudence et respect d'autrui."),
    ]),
    P("3. Rédiger", "Exemples et conclusion.", [
      ("Un exemple pour la partie 2 :", "le médecin qui annonce une maladie grave avec précaution", "un vendeur qui baisse ses prix", "un match nul", "une addition", "Vérité et souffrance."),
      ("Un exemple pour la partie 1 :", "un témoin qui ment au tribunal fait condamner un innocent", "un poème", "une fête", "un repas", "Le mensonge produit l'injustice."),
      ("La conclusion :", "la vérité reste une valeur, mais sa manière de la dire relève de la sagesse", "il faut toujours mentir", "la vérité n'existe pas", "le sujet n'a pas de sens", "Réponse claire et nuancée."),
    ]),
  ]),
  "bac-type-philo-8": noter([
    P("1. Analyser le sujet", "Sujet : « Le bonheur est-il le but de l'existence ? »", [
      ("Le bonheur est :", "un état de satisfaction durable et complète", "un plaisir d'un instant", "la richesse", "la célébrité", "Distinguer bonheur et plaisir."),
      ("« Le but de l'existence » signifie :", "ce vers quoi tend toute la vie humaine", "la fin d'une journée", "la mort uniquement", "une destination de voyage", "Finalité de la vie."),
      ("Problématique adaptée :", "Vivons-nous pour être heureux ou pour quelque chose de plus haut ?", "Où trouver du travail ?", "Le bonheur est-il cher ?", "Faut-il dormir ?", "Bonheur contre devoir ou sens."),
    ]),
    P("2. Bâtir le plan", "Thèse, antithèse, dépassement.", [
      ("Partie 1 : oui, car selon Aristote :", "tous les hommes recherchent le bonheur comme bien suprême", "personne ne veut être heureux", "le bonheur est interdit", "le malheur est le but", "Éthique à Nicomaque."),
      ("Partie 2 : le bonheur n'est pas le but, car :", "le devoir moral passe avant la recherche du bonheur", "le bonheur est facile", "il suffit d'acheter", "rien ne compte", "Kant : se rendre digne d'être heureux."),
      ("Partie 3 : dépassement :", "le bonheur vient de surcroît d'une vie juste et pleine de sens", "il faut fuir toute joie", "seul l'argent compte", "on ne peut rien faire", "Épicure, Spinoza : bonheur et sagesse."),
    ]),
    P("3. Rédiger", "Références et conclusion.", [
      ("Pour Épicure, le bonheur est :", "l'absence de trouble de l'âme et de douleur du corps (ataraxie)", "l'accumulation de plaisirs", "la gloire", "la guerre", "Lettre à Ménécée."),
      ("Un exemple pour la partie 2 :", "un médecin qui sacrifie son confort pour soigner lors d'une épidémie", "un touriste", "un joueur", "un acheteur", "Devoir avant bonheur."),
      ("La conclusion :", "le bonheur est visé, mais il dépend d'une vie morale et sensée", "le bonheur est impossible", "il faut être égoïste", "seul le plaisir compte", "Réponse nuancée."),
    ]),
  ]),
  "bac-type-philo-9": noter([
    P("1. Analyser le sujet", "Sujet : « L'État est-il l'ennemi de la liberté ? »", [
      ("L'État est :", "l'autorité politique souveraine qui gouverne une société sur un territoire", "une famille", "une entreprise", "une association de quartier", "Pouvoir institutionnel."),
      ("La tension du sujet :", "l'État impose des lois mais protège aussi les libertés", "l'État n'existe pas", "la liberté est illégale", "l'État est une personne", "Contrainte et protection."),
      ("Problématique adaptée :", "Les lois de l'État limitent-elles la liberté ou la rendent-elles possible ?", "Qui est le président ?", "Combien coûte l'État ?", "L'État aime-t-il ?", "Question politique."),
    ]),
    P("2. Bâtir le plan", "Thèse, antithèse, dépassement.", [
      ("Partie 1 : oui, l'État peut menacer la liberté :", "par la censure, la répression et la dictature", "par les écoles", "par les hôpitaux", "par les routes", "Totalitarisme (Arendt)."),
      ("Partie 2 : sans État, selon Hobbes :", "c'est « la guerre de tous contre tous »", "tout le monde est libre et en paix", "la nature est douce", "on n'a besoin de rien", "État de nature, Léviathan."),
      ("Partie 3 : l'État garantit la liberté s'il est :", "un État de droit avec séparation des pouvoirs", "une monarchie absolue", "un État sans lois", "dirigé par la force seule", "Montesquieu : « le pouvoir arrête le pouvoir »."),
    ]),
    P("3. Rédiger", "Exemples et conclusion.", [
      ("Un exemple pour la partie 2 :", "la loi protège le faible contre le plus fort", "la loi interdit de respirer", "la loi crée la pluie", "la loi fait les saisons", "Rôle protecteur de la loi."),
      ("Notion utile :", "le contrat social : chacun accepte des lois communes pour vivre en sécurité", "le contrat de travail", "le contrat de mariage", "un bail", "Hobbes, Locke, Rousseau."),
      ("La conclusion :", "l'État n'est pas l'ennemi de la liberté s'il reste limité et contrôlé par les citoyens", "il faut supprimer l'État", "l'État doit tout contrôler", "la liberté est un mythe", "Réponse nuancée."),
    ]),
  ]),
  "bac-type-philo-10": noter([
    P("1. Analyser le sujet", "Sujet : « Peut-on se passer de religion ? »", [
      ("La religion désigne :", "un ensemble de croyances et de rites qui relient l'homme au sacré", "une science exacte", "un parti politique", "une langue", "Du latin religare : relier."),
      ("« Se passer de » signifie :", "vivre sans en avoir besoin", "traverser un lieu", "réussir un examen", "oublier quelque chose", "Question du besoin."),
      ("Problématique adaptée :", "L'homme peut-il trouver sans religion un sens à sa vie et une morale ?", "Combien y a-t-il de mosquées ?", "Qui a construit l'église ?", "La religion est-elle chère ?", "Besoin de sens et de morale."),
    ]),
    P("2. Bâtir le plan", "Thèse, antithèse, dépassement.", [
      ("Partie 1 : la religion semble nécessaire car elle :", "donne un sens à la vie, console et unit une communauté", "remplace la médecine", "fait pousser les plantes", "n'a aucun rôle", "Durkheim : fonction sociale de la religion."),
      ("Partie 2 : certains pensent s'en passer car :", "la raison et la science peuvent expliquer le monde et fonder une morale", "la religion est interdite", "personne n'a jamais cru", "les rites sont trop longs", "Kant : morale fondée sur la raison."),
      ("Critique célèbre de la religion :", "« La religion est l'opium du peuple » (Marx)", "« Je pense donc je suis »", "« L'homme est un loup pour l'homme »", "« Connais-toi toi-même »", "Religion comme consolation illusoire."),
    ]),
    P("3. Rédiger", "Dépassement et conclusion.", [
      ("Partie 3 : dépassement :", "le besoin de sens demeure ; la religion est une réponse parmi d'autres, librement choisie", "il faut interdire toute croyance", "il faut imposer une religion", "le sens n'existe pas", "Liberté de conscience."),
      ("Un principe utile pour la partie 3 :", "la laïcité : l'État garantit la liberté de croire ou de ne pas croire", "le monopole religieux", "la censure", "le parti unique", "Constitution du Sénégal."),
      ("Ton à adopter :", "respectueux et argumenté, sans jugement sur les croyants", "moqueur", "violent", "prosélyte", "Exigence d'objectivité."),
    ]),
  ]),
  "bac-type-philo-11": noter([
    P("1. Analyser le sujet", "Sujet : « L'art est-il inutile ? »", [
      ("L'art désigne ici :", "la création d'œuvres qui visent la beauté ou l'expression", "un métier manuel uniquement", "une marchandise seulement", "une science", "Beaux-arts."),
      ("« Inutile » signifie :", "qui ne sert à rien de pratique ou de rentable", "qui est beau", "qui est cher", "qui est interdit", "Utile = qui sert un besoin."),
      ("Problématique adaptée :", "L'art, qui ne nourrit pas, n'a-t-il vraiment aucune fonction pour l'homme ?", "Qui a peint la Joconde ?", "Combien coûte un tableau ?", "L'art est-il récent ?", "Utilité matérielle contre utilité humaine."),
    ]),
    P("2. Bâtir le plan", "Thèse, antithèse, dépassement.", [
      ("Partie 1 : l'art paraît inutile car :", "il ne satisfait pas les besoins vitaux comme manger ou se loger", "il nourrit le corps", "il soigne toutes les maladies", "il remplace l'école", "Kant : « finalité sans fin »."),
      ("Partie 2 : l'art est utile car il :", "éduque le regard, exprime une culture et transmet des valeurs", "est toujours rentable", "est obligatoire", "remplace le travail", "Fonction sociale et éducative."),
      ("Exemple africain pour la partie 2 :", "le masque africain, objet rituel et social", "le téléphone", "la voiture", "l'ordinateur", "Senghor : art fonctionnel et collectif."),
    ]),
    P("3. Rédiger", "Dépassement et conclusion.", [
      ("Partie 3 : dépassement :", "l'inutilité apparente de l'art fait sa valeur : il libère de la logique du profit", "il faut supprimer l'art", "l'art doit seulement rapporter de l'argent", "l'art n'a pas de sens", "Liberté et contemplation."),
      ("Citation utile :", "« L'art est un anti-destin » (Malraux)", "« Le temps c'est de l'argent »", "« Diviser pour régner »", "« L'union fait la force »", "L'art résiste à la mort."),
      ("La conclusion :", "l'art est inutile matériellement mais indispensable humainement", "l'art est une perte de temps", "l'art est une science", "il faut l'interdire", "Réponse nuancée."),
    ]),
  ]),
  "bac-type-philo-12": noter([
    P("1. Analyser le sujet", "Sujet : « Autrui est-il un obstacle à ma liberté ? »", [
      ("Autrui désigne :", "l'autre homme, à la fois semblable et différent de moi", "un objet", "un animal", "Dieu", "Alter ego."),
      ("La tension du sujet :", "autrui me limite mais il m'aide aussi à me construire", "autrui n'existe pas", "je suis seul au monde", "la liberté est un objet", "Limite ou condition."),
      ("Problématique adaptée :", "Autrui limite-t-il ma liberté ou en est-il la condition ?", "Combien ai-je d'amis ?", "Faut-il vivre seul ?", "Qui est mon voisin ?", "Question centrale."),
    ]),
    P("2. Bâtir le plan", "Thèse, antithèse, dépassement.", [
      ("Partie 1 : autrui est un obstacle car :", "son regard me juge et me fige", "il me rend invisible", "il n'a pas d'avis", "il ne me voit pas", "Sartre : « L'enfer, c'est les autres » (Huis clos)."),
      ("Partie 2 : autrui est la condition de ma liberté car :", "sans les autres, pas de langage, d'éducation ni de culture", "il décide à ma place", "il m'empêche d'apprendre", "il me rend esclave", "L'enfant sauvage sans société."),
      ("Partie 3 : ma liberté s'accomplit :", "dans la reconnaissance mutuelle et le respect réciproque", "en éliminant les autres", "en fuyant toute relation", "en dominant autrui", "Hegel : dialectique de la reconnaissance."),
    ]),
    P("3. Rédiger", "Exemples et conclusion.", [
      ("Notion africaine utile :", "« Nit nitay garabam » : l'homme est le remède de l'homme", "« Chacun pour soi »", "« Après moi le déluge »", "« L'argent d'abord »", "Solidarité, teranga."),
      ("Un exemple pour la partie 1 :", "la timidité devant le regard des autres en classe", "une addition", "un coucher de soleil", "un arbre", "Le regard d'autrui gêne."),
      ("La conclusion :", "autrui limite ma liberté mais la rend aussi possible et réelle", "autrui est mon ennemi absolu", "il faut vivre seul", "la liberté n'existe pas", "Réponse nuancée."),
    ]),
  ]),
  "bac-type-fr-5": noter([
    P("1. Comprendre le texte", "Texte (d'entraînement, environ 400 mots) : un essayiste montre que les réseaux sociaux rapprochent les gens éloignés, mais qu'ils enferment chacun dans ses opinions et favorisent les fausses nouvelles.", [
      ("Thème du texte :", "les effets des réseaux sociaux sur la société", "l'histoire de l'imprimerie", "la vie rurale", "le football", "Idée générale."),
      ("Thèse de l'auteur :", "les réseaux sociaux ont des avantages réels mais des dangers sérieux", "les réseaux sociaux sont parfaits", "il faut interdire Internet", "seuls les jeunes les utilisent", "Position nuancée."),
      ("Un argument du texte :", "les réseaux enferment chacun dans des opinions qui lui ressemblent", "les réseaux font pousser le mil", "les réseaux remplacent le sommeil", "les réseaux sont gratuits", "Bulle de filtre."),
    ]),
    P("2. Résumer", "Réduire le texte au quart, environ 100 mots, avec une marge de 10 %.", [
      ("Le résumé doit :", "suivre l'ordre du texte et garder le système d'énonciation de l'auteur", "donner son avis", "recopier des phrases", "inverser le plan", "Fidélité au texte."),
      ("Dans un résumé, il faut :", "reformuler avec ses propres mots", "citer les exemples un à un", "ajouter des idées", "écrire « l'auteur dit que »", "Pas de citations, pas de commentaire."),
      ("Indiquer le nombre de mots :", "à la fin du résumé, comme exigé", "jamais", "au début du devoir", "dans le titre", "Consigne de l'épreuve."),
    ]),
    P("3. Discuter", "Sujet de discussion : « Les réseaux sociaux nous rapprochent-ils vraiment des autres ? »", [
      ("Plan adapté :", "dialectique : oui, ils rapprochent / mais ils isolent aussi / usage responsable", "un seul paragraphe", "une liste de sites", "le résumé à nouveau", "Discussion argumentée."),
      ("Un bon exemple pour « ils rapprochent » :", "les familles qui gardent le contact avec un parent émigré", "le nombre de téléphones vendus", "une panne d'électricité", "un roman de Zola", "Exemple concret et sénégalais."),
      ("La conclusion de la discussion :", "prend clairement position et propose une ouverture", "répète le résumé", "reste vide", "change de sujet", "Bilan personnel argumenté."),
    ]),
  ]),
  "bac-type-fr-6": noter([
    P("1. Situer et comprendre", "Texte : extrait d'un poème de Senghor célébrant la femme noire et l'Afrique (« Femme nue, femme noire… »).", [
      ("Le mouvement littéraire du poème :", "la Négritude", "le romantisme français", "le classicisme", "le surréalisme seul", "Senghor, Césaire, Damas."),
      ("Thème principal :", "l'éloge de la femme noire, image de l'Afrique", "la guerre", "la ville moderne", "l'argent", "Femme-Afrique."),
      ("Projet de lecture possible :", "Comment le poète fait-il de la femme noire un symbole de l'Afrique ?", "Combien de vers compte le poème ?", "Qui est l'éditeur ?", "Quelle est la date ?", "Problématique de commentaire."),
    ]),
    P("2. Analyser", "Repérer les procédés.", [
      ("L'apostrophe « Femme nue, femme noire » produit :", "une adresse solennelle et affective", "une description technique", "une moquerie", "une question", "Lyrisme."),
      ("Les images de la nature (savane, fruit mûr) servent à :", "associer la femme à la terre africaine", "décrire une recette", "critiquer la campagne", "parler de météo", "Métaphores telluriques."),
      ("Le verset long et les répétitions créent :", "un rythme proche du chant et des tam-tams", "un texte de loi", "un dialogue de théâtre", "une liste de courses", "Rythme senghorien."),
    ]),
    P("3. Rédiger le commentaire", "Introduction, deux axes, conclusion.", [
      ("Plan adapté :", "I. Un éloge sensuel de la femme / II. Un symbole de l'Afrique et de la Négritude", "I. Biographie / II. Bibliographie", "I. Résumé / II. Avis", "Un seul paragraphe", "Axes liés au projet."),
      ("Dans chaque paragraphe, il faut :", "une idée, une citation, l'analyse du procédé et son effet", "uniquement des citations", "uniquement son avis", "la biographie de l'auteur", "Méthode : idée, preuve, analyse."),
      ("L'ouverture de la conclusion peut :", "rapprocher le poème de « Cahier d'un retour au pays natal » de Césaire", "annoncer le plan", "recopier le poème", "poser une question sans lien", "Ouverture littéraire."),
    ]),
  ]),
  "bac-type-fr-7": noter([
    P("1. Comprendre le sujet", "Sujet : « Le théâtre n'est-il qu'un divertissement ? » Vous discuterez en vous appuyant sur des pièces étudiées.", [
      ("Le mot clé « divertissement » signifie :", "ce qui amuse et détourne des soucis", "une leçon de morale", "un examen", "un roman", "Fonction de plaisir."),
      ("« N'est-il qu' » invite à :", "montrer que le théâtre a aussi d'autres fonctions", "approuver sans nuance", "parler du cinéma", "résumer une pièce", "Restriction à discuter."),
      ("Type de plan adapté :", "dialectique", "chronologique", "descriptif", "thématique sans lien", "Thèse puis dépassement."),
    ]),
    P("2. Arguments et exemples", "Choisir des pièces pertinentes.", [
      ("Le théâtre divertit par :", "le comique de situation, de mots et de gestes", "les notes de bas de page", "les statistiques", "les cartes", "Comédie, Molière."),
      ("Le théâtre instruit, selon la formule classique :", "« castigat ridendo mores » : il corrige les mœurs en riant", "il ne corrige rien", "il remplace l'école", "il est réservé aux rois", "Fonction morale."),
      ("Une pièce africaine qui dénonce un pouvoir :", "La Tragédie du roi Christophe (Césaire)", "Le Malade imaginaire", "Les Fleurs du mal", "Candide", "Théâtre engagé."),
    ]),
    P("3. Rédiger", "Introduction et conclusion.", [
      ("Une pièce sénégalaise utile :", "L'Exil d'Albouri (Cheik Aliou Ndao)", "Phèdre", "Le Cid", "Hamlet", "Théâtre historique et résistance."),
      ("La conclusion :", "le théâtre divertit, mais il fait aussi réfléchir et peut changer la société", "le théâtre est inutile", "le théâtre est seulement triste", "il faut lire des romans", "Réponse nuancée."),
      ("L'ouverture possible :", "le rôle du théâtre populaire et des séries télévisées au Sénégal", "la date de la pièce", "un résumé", "la biographie de Molière", "Ouverture actuelle."),
    ]),
  ]),
  "bac-type-fr-8": noter([
    P("1. Comprendre le texte", "Texte (d'entraînement) : un sociologue explique que les jeunes quittent les villages pour les villes à cause de la pauvreté rurale, mais qu'ils y trouvent souvent chômage et précarité.", [
      ("Thème du texte :", "l'exode rural et ses conséquences", "la pêche en mer", "l'histoire de Dakar", "la musique", "Idée générale."),
      ("Thèse :", "l'exode rural est une fausse solution qui déplace la pauvreté", "la ville garantit la richesse", "les villages sont vides", "il faut fermer les villes", "Position de l'auteur."),
      ("Cause de l'exode citée :", "le manque de revenus et d'équipements à la campagne", "le froid", "les vacances", "le football", "Facteur de départ."),
    ]),
    P("2. Résumer", "Réduire le texte au quart.", [
      ("Première étape du résumé :", "repérer les idées essentielles et les connecteurs logiques", "compter les mots du titre", "écrire son avis", "recopier l'introduction", "Lecture active."),
      ("Les exemples chiffrés du texte :", "sont supprimés ou résumés en une idée", "sont tous recopiés", "sont multipliés", "sont inventés", "Garder l'essentiel."),
      ("Le résumé est rédigé :", "à la même personne que le texte, sans « l'auteur dit »", "à la première personne du lecteur", "sous forme de liste", "en style télégraphique", "Contraction fidèle."),
    ]),
    P("3. Discuter", "Sujet : « Faut-il retenir les jeunes à la campagne ? »", [
      ("Argument pour :", "développer l'agriculture et les services ruraux crée des emplois sur place", "les villes sont interdites", "les jeunes n'aiment pas la ville", "la campagne est toujours riche", "Développement local."),
      ("Argument contre une obligation :", "chacun est libre de chercher sa chance où il veut", "la ville n'existe pas", "l'agriculture est inutile", "les villages n'ont pas d'habitants", "Liberté de circulation."),
      ("Exemple concret utile :", "les domaines agricoles communautaires ou des projets d'irrigation", "un film américain", "un roman du XIXe siècle", "une équation", "Exemple local."),
    ]),
  ]),
  "bac-type-fr-9": noter([
    P("1. Comprendre l'extrait", "Texte : extrait de L'Aventure ambiguë (Cheikh Hamidou Kane) : la Grande Royale explique qu'il faut envoyer les enfants à l'école nouvelle « pour apprendre l'art de vaincre sans avoir raison ».", [
      ("Le dilemme posé par l'extrait :", "aller à l'école étrangère au risque de perdre ses valeurs", "choisir un métier", "partir en vacances", "construire une maison", "Tradition et modernité."),
      ("La Grande Royale propose :", "d'envoyer les enfants à l'école des Blancs malgré le risque", "de fermer l'école", "de fuir le pays", "de renoncer à l'avenir", "Choix stratégique."),
      ("Projet de lecture :", "Comment le discours de la Grande Royale met-il en scène un choix douloureux ?", "Combien de personnages ?", "Quel est le prix du livre ?", "Où habite l'auteur ?", "Problématique."),
    ]),
    P("2. Analyser", "Procédés du discours.", [
      ("Les phrases courtes et les antithèses montrent :", "la force de conviction et le déchirement du choix", "l'hésitation de l'auteur", "un texte comique", "une description de paysage", "Rhétorique de la persuasion."),
      ("Le registre dominant :", "tragique et argumentatif", "comique", "fantastique", "épistolaire", "Choix sans issue heureuse."),
      ("« Vaincre sans avoir raison » signifie :", "dominer par la technique sans avoir la vérité morale", "gagner un match", "perdre un procès", "avoir toujours raison", "Paradoxe de la colonisation."),
    ]),
    P("3. Rédiger", "Commentaire composé.", [
      ("Plan adapté :", "I. Un discours persuasif / II. Le drame d'un peuple entre deux mondes", "I. Auteur / II. Œuvre", "I. Résumé / II. Opinion", "Un plan en dix parties", "Axes liés au projet."),
      ("Une citation doit être :", "courte, entre guillemets et analysée", "longue et sans explication", "inventée", "mise en note", "Méthode."),
      ("Ouverture possible :", "le destin tragique de Samba Diallo à la fin du roman", "le prix Nobel", "la date de naissance", "la couverture du livre", "Ouverture sur l'œuvre."),
    ]),
  ]),
  "bac-type-fr-10": noter([
    P("1. Comprendre le sujet", "Sujet : « La poésie doit-elle servir une cause ? » Vous discuterez en vous appuyant sur des poèmes étudiés.", [
      ("« Servir une cause » signifie :", "s'engager pour défendre des idées ou un peuple", "être vendue cher", "rimer obligatoirement", "être courte", "Poésie engagée."),
      ("La position opposée :", "la poésie cherche d'abord la beauté (l'art pour l'art)", "la poésie n'existe pas", "la poésie est un roman", "la poésie est une science", "Gautier, Parnasse."),
      ("Problématique adaptée :", "La poésie doit-elle être engagée ou rester libre de chercher la beauté ?", "Combien de rimes faut-il ?", "Qui est le meilleur poète ?", "La poésie est-elle facile ?", "Tension engagement / esthétique."),
    ]),
    P("2. Arguments et exemples", "Choisir des poèmes.", [
      ("Exemple de poésie engagée :", "Cahier d'un retour au pays natal (Césaire)", "un poème sur une fleur sans message", "un dictionnaire", "un manuel de maths", "Négritude."),
      ("Exemple de poésie engagée contre l'oppression :", "« Liberté » de Paul Éluard, écrit sous l'Occupation", "« Le Lac » seulement", "une chanson publicitaire", "un horaire de bus", "Résistance."),
      ("Argument pour l'art pour l'art :", "un poème engagé peut devenir propagande et perdre sa beauté", "la beauté est interdite", "la poésie doit être payée", "tout poème est politique", "Limite de l'engagement."),
    ]),
    P("3. Rédiger", "Dépassement et conclusion.", [
      ("Partie 3 possible :", "le meilleur engagement passe par la beauté de la forme", "il faut supprimer la poésie", "seule la rime compte", "le poète doit se taire", "Union du fond et de la forme."),
      ("Un poème africain à citer :", "« Afrique » de David Diop", "« Le Corbeau et le Renard »", "« Phèdre »", "« Germinal »", "Poésie de combat."),
      ("La conclusion :", "la poésie peut servir une cause sans renoncer à être un art", "la poésie est inutile", "seule la forme compte", "seul le message compte", "Réponse nuancée."),
    ]),
  ]),
  "bac-type-fr-11": noter([
    P("1. Comprendre le texte", "Texte (d'entraînement) : un économiste affirme que l'école forme trop de diplômés sans débouchés et plaide pour la formation professionnelle et l'apprentissage.", [
      ("Thème :", "le lien entre l'école et l'emploi", "la santé publique", "la musique traditionnelle", "le climat", "Idée générale."),
      ("Thèse :", "l'école doit mieux préparer aux métiers réels", "il faut supprimer l'école", "tous les diplômés ont un emploi", "l'apprentissage est inutile", "Position de l'auteur."),
      ("Un argument du texte :", "beaucoup de diplômés restent au chômage faute de compétences pratiques", "les élèves dorment en classe", "les diplômes sont gratuits", "les écoles sont trop grandes", "Inadéquation formation-emploi."),
    ]),
    P("2. Résumer", "Réduire au quart.", [
      ("Le nombre de mots autorisé avec 10 % de marge pour 100 mots :", "entre 90 et 110 mots", "entre 50 et 150", "exactement 100", "moins de 80", "Tolérance de la consigne."),
      ("Les connecteurs logiques du texte :", "doivent être gardés ou reformulés pour montrer l'enchaînement", "doivent être supprimés", "doivent être inversés", "ne comptent pas", "Logique du raisonnement."),
      ("Une erreur à éviter :", "insérer son opinion dans le résumé", "reformuler", "respecter l'ordre", "compter les mots", "Le résumé est neutre."),
    ]),
    P("3. Discuter", "Sujet : « Le diplôme est-il encore la clé de la réussite ? »", [
      ("Argument pour le diplôme :", "il atteste des connaissances et ouvre l'accès à certains métiers", "il remplace le travail", "il est inutile", "il se vend au marché", "Rôle du diplôme."),
      ("Argument nuancé :", "les compétences pratiques, l'esprit d'entreprise et le réseau comptent aussi", "seule la chance compte", "il faut abandonner l'école", "seul l'âge compte", "Autres clés de réussite."),
      ("Exemple pertinent :", "un jeune diplômé qui crée sa propre entreprise après une formation", "un roman de science-fiction", "un match de lutte", "une recette de thiéboudienne", "Exemple concret."),
    ]),
  ]),
  "bac-type-fr-12": noter([
    P("1. Comprendre le sujet", "Sujet : « Lire, est-ce seulement s'évader ? » Vous discuterez en vous appuyant sur vos lectures.", [
      ("« S'évader » signifie ici :", "fuir le quotidien en entrant dans un autre monde", "sortir de prison", "partir en voyage réel", "dormir", "Fonction d'évasion."),
      ("« Seulement » invite à montrer :", "que la lecture apporte aussi autre chose", "que lire est inutile", "que lire est obligatoire", "que lire coûte cher", "Restriction à discuter."),
      ("Type de plan :", "dialectique", "chronologique", "biographique", "aucun", "Thèse, antithèse, synthèse."),
    ]),
    P("2. Arguments et exemples", "Choisir des œuvres.", [
      ("La lecture permet de s'évader par :", "l'imaginaire, les voyages et les aventures des personnages", "les notes de bas de page", "le prix du livre", "le nombre de pages", "Plaisir de lire."),
      ("La lecture fait aussi :", "réfléchir, comprendre le monde et se connaître", "oublier d'apprendre", "perdre son temps", "dormir", "Fonction de connaissance."),
      ("Un roman qui fait réfléchir sur la société sénégalaise :", "Une si longue lettre (Mariama Bâ)", "Les Trois Mousquetaires", "Le Petit Prince", "Harry Potter", "Lecture et prise de conscience."),
    ]),
    P("3. Rédiger", "Introduction et conclusion.", [
      ("Une amorce possible :", "une citation : « La lecture, une porte ouverte sur un monde enchanté » (Mauriac)", "le nombre de livres vendus", "la définition du mot livre", "la conclusion", "Amener le sujet."),
      ("La conclusion :", "lire, c'est s'évader mais aussi revenir au réel plus lucide", "lire est une fuite", "lire est inutile", "il faut regarder la télé", "Réponse nuancée."),
      ("Les transitions doivent :", "faire le bilan d'une partie et annoncer la suivante", "être absentes", "répéter le sujet", "contenir un exemple nouveau", "Cohérence du devoir."),
    ]),
  ]),
}
