# 2nde L, 1re L et 1re G : devoirs types en plus pour les matières propres à ces séries (maths L, maths G, économie, comptabilité).
# Rédigés pour l'appli sur le programme officiel, non officiels.
from sujets_dev_common import D, pack, TRIM

def mk(prefix, levels, s, name, n, exos, dur="2 h"):
    t = min(3, (n + 1) // 2 + (1 if n == 4 else 0))
    an, g = D(f"dev-{prefix}-{s}-{n}", levels[0], name, n, exos, duration=dur, label=f"{TRIM[t]} · devoir {n}")
    an["levels"] = levels
    return an, g

L2L, L1L, L1G = ["2nde L"], ["1ère L"], ["1ère G"]

ANNALES_X, GUIDED_X = pack([
  # ================= 2nde L : mathématiques
  mk("2ndel", L2L, "maths", "Mathématiques", 1, [
    ("Calcul numérique", "On donne A = 3/4 + 5/6 et B = (2/3) × (9/8).", [
      ("A =", "19/12", "8/10", "15/24", "4/5", "9/12 + 10/12."),
      ("B =", "3/4", "18/24 + 1", "11/11", "6/8 + 1", "18/24 = 3/4."),
      ("A − B =", "5/6", "1/2", "16/12", "7/12", "19/12 − 9/12 = 10/12."),
      ("10⁵ × 10⁻³ =", "10²", "10⁸", "10⁻¹⁵", "1", "On additionne les exposants.")]),
    ("Pourcentages", "Un téléphone coûte 80 000 F. Le vendeur fait une remise de 15 %.", [
      ("Montant de la remise :", "12 000 F", "15 000 F", "8 000 F", "68 000 F", "80 000 × 0,15."),
      ("Prix payé :", "68 000 F", "65 000 F", "92 000 F", "78 500 F", "80 000 − 12 000."),
      ("Coefficient multiplicateur :", "0,85", "1,15", "0,15", "85", "1 − 0,15."),
      ("Une hausse de 20 % puis une baisse de 20 % donnent au total", "une baisse de 4 %", "aucun changement", "une hausse de 4 %", "une baisse de 20 %", "1,2 × 0,8 = 0,96.")]),
    ("Équations", "Résoudre.", [
      ("2x + 7 = 15 :", "x = 4", "x = 11", "x = −4", "x = 8", "2x = 8."),
      ("5x − 3 = 2x + 9 :", "x = 4", "x = 2", "x = −4", "x = 6", "3x = 12."),
      ("x/3 = 7 :", "x = 21", "x = 7/3", "x = 10", "x = 4", "Produit en croix."),
      ("(x − 5)(x + 2) = 0 :", "x = 5 ou x = −2", "x = −5 ou x = 2", "x = 5 seulement", "x = 3", "Produit nul.")])]),
  mk("2ndel", L2L, "maths", "Mathématiques", 2, [
    ("Fonctions affines", "Un taxi de Dakar facture 500 F de prise en charge plus 300 F par km : f(x) = 300x + 500.", [
      ("Prix pour 6 km :", "2 300 F", "1 800 F", "3 000 F", "2 100 F", "300 × 6 + 500."),
      ("Distance pour 3 500 F :", "10 km", "11,6 km", "12 km", "9 km", "(3 500 − 500)/300."),
      ("Coefficient directeur :", "300", "500", "800", "6", "f(x) = ax + b."),
      ("La représentation graphique est", "une droite", "une parabole", "un cercle", "une courbe en cloche", "Fonction affine.")]),
    ("Statistiques", "Âges de 10 joueurs : 16, 17, 17, 18, 18, 18, 19, 19, 20, 21.", [
      ("Moyenne :", "18,3", "18", "17,5", "19", "183 / 10."),
      ("Mode :", "18", "17", "19", "21", "Effectif le plus grand."),
      ("Médiane :", "18", "18,5", "17", "19", "Moyenne des 5e et 6e valeurs : (18 + 18)/2."),
      ("Fréquence des joueurs de 18 ans :", "30 %", "18 %", "3 %", "10 %", "3/10.")]),
    ("Proportionnalité", "Une recette de thiéboudienne pour 4 personnes utilise 1 kg de riz.", [
      ("Riz pour 10 personnes :", "2,5 kg", "2 kg", "4 kg", "10 kg", "1 × 10/4."),
      ("Personnes avec 3 kg :", "12", "10", "7", "3", "4 × 3."),
      ("Sur une carte au 1/50 000, 4 cm représentent", "2 km", "20 km", "200 m", "50 km", "4 × 50 000 cm = 200 000 cm."),
      ("Vitesse de 90 km/h en 2 h 30 : distance", "225 km", "180 km", "250 km", "36 km", "90 × 2,5.")])]),
  mk("2ndel", L2L, "maths", "Mathématiques", 3, [
    ("Géométrie", "Un champ rectangulaire mesure 40 m sur 30 m.", [
      ("Diagonale :", "50 m", "70 m", "35 m", "1 200 m", "Pythagore : √(1 600 + 900)."),
      ("Aire :", "1 200 m²", "140 m²", "70 m²", "2 400 m²", "40 × 30."),
      ("Aire en ares :", "12 a", "120 a", "1,2 a", "0,12 a", "1 a = 100 m²."),
      ("Périmètre :", "140 m", "70 m", "1 200 m", "120 m", "2 × (40 + 30).")]),
    ("Vecteurs et repère", "A(1 ; 2) et B(5 ; 6).", [
      ("Milieu de [AB] :", "(3 ; 4)", "(6 ; 8)", "(2 ; 2)", "(4 ; 4)", "Moyenne des coordonnées."),
      ("Coordonnées de AB→ :", "(4 ; 4)", "(6 ; 8)", "(−4 ; −4)", "(3 ; 4)", "B − A."),
      ("Longueur AB :", "4√2", "8", "16", "32", "√(16 + 16)."),
      ("Coefficient directeur de (AB) :", "1", "4", "−1", "2", "4/4.")]),
    ("Inéquations", "Résoudre.", [
      ("x + 4 > 9 :", "x > 5", "x < 5", "x > 13", "x < 13", "On soustrait 4."),
      ("−3x ≤ 12 :", "x ≥ −4", "x ≤ −4", "x ≥ 4", "x ≤ 4", "Division par un négatif : le sens change."),
      ("Intervalle des x tels que 2 ≤ x < 7 :", "[2 ; 7[", "]2 ; 7]", "[2 ; 7]", "]2 ; 7[", "Crochets."),
      ("Un forfait coûte 2 000 F + 50 F/min. Budget 5 000 F : minutes possibles au maximum", "60", "100", "40", "50", "2 000 + 50x ≤ 5 000.")])]),
  mk("2ndel", L2L, "maths", "Mathématiques", 4, [
    ("Synthèse : budget familial", "Une famille gagne 250 000 F par mois. Le loyer représente 30 % et la nourriture 40 %.", [
      ("Loyer :", "75 000 F", "30 000 F", "100 000 F", "7 500 F", "250 000 × 0,3."),
      ("Nourriture :", "100 000 F", "40 000 F", "75 000 F", "125 000 F", "250 000 × 0,4."),
      ("Reste pour le reste des dépenses :", "75 000 F", "100 000 F", "50 000 F", "25 000 F", "30 %."),
      ("Si le salaire augmente de 10 %, nouveau salaire :", "275 000 F", "260 000 F", "350 000 F", "252 500 F", "× 1,1.")]),
    ("Synthèse : fonctions", "g(x) = −2x + 8.", [
      ("g(0) =", "8", "−2", "0", "6", "Ordonnée à l'origine."),
      ("g(x) = 0 pour", "x = 4", "x = −4", "x = 8", "x = 2", "−2x + 8 = 0."),
      ("g est", "décroissante", "croissante", "constante", "nulle", "a < 0."),
      ("g(x) > 0 pour", "x < 4", "x > 4", "x > 8", "tout x", "Avant la racine.")]),
    ("Synthèse : statistiques", "Notes : 12 (3 élèves), 14 (5 élèves), 16 (2 élèves).", [
      ("Effectif total :", "10", "3", "42", "16", "3 + 5 + 2."),
      ("Moyenne :", "13,8", "14", "14,2", "13", "(36 + 70 + 32)/10."),
      ("Fréquence de la note 14 :", "50 %", "14 %", "5 %", "35 %", "5/10."),
      ("Note la plus fréquente :", "14", "12", "16", "13,8", "Mode.")])]),
  # ================= 1re L : mathématiques
  mk("1erel", L1L, "maths-l", "Mathématiques", 1, [
    ("Pourcentages successifs", "Le prix du sac de sucre passe de 20 000 F à 22 000 F puis baisse de 10 %.", [
      ("Taux de la hausse :", "10 %", "20 %", "2 %", "11 %", "2 000/20 000."),
      ("Prix après la baisse :", "19 800 F", "20 000 F", "19 000 F", "21 780 F", "22 000 × 0,9."),
      ("Évolution globale :", "−1 %", "0 %", "+1 %", "−10 %", "1,1 × 0,9 = 0,99."),
      ("Taux réciproque d'une hausse de 25 % :", "−20 %", "−25 %", "−75 %", "+20 %", "1/1,25 = 0,8.")]),
    ("Équations du second degré", "Résoudre x² − 7x + 10 = 0.", [
      ("Δ =", "9", "89", "49", "−9", "49 − 40."),
      ("Solutions :", "2 et 5", "−2 et −5", "1 et 10", "3 et 4", "(7 ± 3)/2."),
      ("Somme des solutions :", "7", "10", "−7", "3", "−b/a."),
      ("Produit des solutions :", "10", "7", "−10", "1", "c/a.")]),
    ("Systèmes", "Au marché, 2 mangues et 3 oranges coûtent 700 F ; 1 mangue et 1 orange coûtent 300 F.", [
      ("Système :", "2m + 3o = 700 et m + o = 300", "2m + 3o = 300 et m + o = 700", "m + 3o = 700", "5(m + o) = 1 000", "Mise en équation."),
      ("Prix d'une orange :", "100 F", "200 F", "150 F", "50 F", "2(300 − o) + 3o = 700 donne o = 100."),
      ("Prix d'une mangue :", "200 F", "100 F", "250 F", "300 F", "300 − 100."),
      ("Vérification : 2 × 200 + 3 × 100 =", "700", "600", "800", "500", "Correct.")])]),
  mk("1erel", L1L, "maths-l", "Mathématiques", 2, [
    ("Suites", "Une tontine : chaque membre verse 5 000 F le 1er mois et 1 000 F de plus chaque mois.", [
      ("Versement du 5e mois :", "9 000 F", "10 000 F", "25 000 F", "8 000 F", "5 000 + 4 × 1 000."),
      ("Nature de la suite :", "arithmétique", "géométrique", "constante", "aucune", "On ajoute 1 000."),
      ("Total versé en 5 mois :", "35 000 F", "45 000 F", "25 000 F", "30 000 F", "5 × (5 000 + 9 000)/2."),
      ("Une épargne qui augmente de 5 % par mois forme une suite", "géométrique de raison 1,05", "arithmétique de raison 5", "géométrique de raison 5", "constante", "On multiplie.")]),
    ("Fonctions", "f(x) = x² − 4x + 3.", [
      ("f(0) =", "3", "0", "−4", "1", "Terme constant."),
      ("Abscisse du sommet :", "2", "−2", "4", "3", "−b/2a."),
      ("Minimum :", "−1", "3", "0", "2", "f(2) = 4 − 8 + 3."),
      ("f(x) = 0 pour", "x = 1 et x = 3", "x = −1 et x = −3", "x = 2", "x = 4", "Factorisation (x − 1)(x − 3).")]),
    ("Lecture graphique", "Une courbe montre la température de Matam sur une journée : 25 °C à 6 h, 42 °C à 15 h, 30 °C à 22 h.", [
      ("Maximum de la journée :", "42 °C à 15 h", "25 °C à 6 h", "30 °C à 22 h", "42 °C à 6 h", "Lecture."),
      ("Variation entre 6 h et 15 h :", "+17 °C", "−17 °C", "+9 °C", "+42 °C", "42 − 25."),
      ("Entre 15 h et 22 h, la température", "diminue", "augmente", "reste constante", "double", "Lecture."),
      ("Amplitude de la journée :", "17 °C", "12 °C", "42 °C", "5 °C", "Max − min.")])]),
  mk("1erel", L1L, "maths-l", "Mathématiques", 3, [
    ("Statistiques à deux caractères", "Dépenses (en milliers de F) selon le revenu : (100 ; 80), (150 ; 115), (200 ; 150).", [
      ("Point moyen G :", "(150 ; 115)", "(100 ; 80)", "(200 ; 150)", "(450 ; 345)", "Moyennes des x et des y."),
      ("Coefficient directeur de la droite passant par les points extrêmes :", "0,7", "1,5", "0,5", "7", "(150 − 80)/(200 − 100)."),
      ("Prévision de dépense pour un revenu de 250 :", "185", "200", "250", "170", "150 + 0,7 × 50."),
      ("Les points sont", "alignés", "dispersés au hasard", "sur une parabole", "sur un cercle", "Pente constante 0,7.")]),
    ("Pourcentages et indices", "Population d'une ville : 200 000 en 2015, 250 000 en 2025 (base 100 en 2015).", [
      ("Indice en 2025 :", "125", "250", "25", "150", "250/200 × 100."),
      ("Taux d'évolution :", "+25 %", "+50 %", "+20 %", "+125 %", "Indice − 100."),
      ("Si l'indice est 90, la valeur a", "baissé de 10 %", "augmenté de 90 %", "baissé de 90 %", "augmenté de 10 %", "90 − 100."),
      ("Une population passe de 80 à 100 : hausse", "25 %", "20 %", "80 %", "125 %", "20/80.")]),
    ("Problème", "Un commerçant achète des pagnes à 3 000 F l'unité et les revend 4 500 F.", [
      ("Bénéfice par pagne :", "1 500 F", "4 500 F", "3 000 F", "7 500 F", "4 500 − 3 000."),
      ("Taux de marge sur le prix d'achat :", "50 %", "33 %", "150 %", "15 %", "1 500/3 000."),
      ("Bénéfice pour 40 pagnes :", "60 000 F", "180 000 F", "120 000 F", "45 000 F", "40 × 1 500."),
      ("Nombre de pagnes pour 90 000 F de bénéfice :", "60", "30", "20", "90", "90 000/1 500.")])]),
  mk("1erel", L1L, "maths-l", "Mathématiques", 4, [
    ("Synthèse", "Révision de l'année.", [
      ("x² = 16 :", "x = 4 ou x = −4", "x = 4", "x = 8", "x = 16", "Racines carrées."),
      ("Suite géométrique u₀ = 3, q = 2 : u₃ =", "24", "9", "12", "6", "3 × 2³."),
      ("Hausse de 50 % puis baisse de 50 % :", "−25 %", "0 %", "+25 %", "−50 %", "1,5 × 0,5 = 0,75."),
      ("Moyenne de 8, 12, 13, 15 :", "12", "13", "11", "48", "48/4.")]),
    ("Fonction et problème", "Le bénéfice d'un atelier de couture est B(x) = −x² + 60x − 500 (milliers de F) pour x tenues.", [
      ("B(10) =", "0", "100", "−500", "500", "−100 + 600 − 500."),
      ("Nombre de tenues pour le bénéfice maximal :", "30", "10", "60", "50", "−b/2a."),
      ("Bénéfice maximal :", "400", "900", "500", "300", "−900 + 1 800 − 500."),
      ("B(x) > 0 pour x entre", "10 et 50", "0 et 30", "30 et 60", "50 et 60", "Racines 10 et 50.")]),
    ("Statistiques", "Salaires de 5 employés (milliers de F) : 100, 120, 120, 150, 510.", [
      ("Moyenne :", "200", "120", "150", "1 000", "1 000/5."),
      ("Médiane :", "120", "200", "150", "135", "Valeur du milieu."),
      ("Indicateur le plus représentatif ici :", "la médiane", "la moyenne", "le maximum", "l'étendue", "La valeur 510 tire la moyenne vers le haut."),
      ("Étendue :", "410", "510", "100", "390", "510 − 100.")])]),
  # ================= 1re G : mathématiques
  mk("1ereg", L1G, "maths-g", "Mathématiques", 1, [
    ("Intérêts simples", "Un commerçant place 600 000 F à 6 % par an en intérêts simples.", [
      ("Intérêt annuel :", "36 000 F", "6 000 F", "360 000 F", "60 000 F", "600 000 × 6/100."),
      ("Intérêt pour 8 mois :", "24 000 F", "36 000 F", "48 000 F", "18 000 F", "36 000 × 8/12."),
      ("Valeur acquise après 2 ans :", "672 000 F", "636 000 F", "720 000 F", "612 000 F", "600 000 + 2 × 36 000."),
      ("Formule de l'intérêt simple :", "I = C × t × n", "I = C × (1 + t)ⁿ", "I = C/t", "I = C + t", "n en années.")]),
    ("Escompte", "Un effet de 500 000 F à échéance dans 90 jours est escompté au taux de 8 % (année de 360 jours).", [
      ("Escompte commercial :", "10 000 F", "40 000 F", "8 000 F", "20 000 F", "500 000 × 0,08 × 90/360."),
      ("Valeur actuelle :", "490 000 F", "460 000 F", "510 000 F", "500 000 F", "500 000 − 10 000."),
      ("L'escompte est payé par", "le porteur qui cède l'effet à la banque", "la banque", "l'État", "personne", "Avance de trésorerie."),
      ("Nombre de jours dans l'année commerciale :", "360", "365", "366", "300", "Usage bancaire.")]),
    ("Pourcentages commerciaux", "Prix d'achat d'un article : 40 000 F ; prix de vente HT : 50 000 F ; TVA 18 %.", [
      ("Marge brute :", "10 000 F", "50 000 F", "9 000 F", "18 000 F", "50 000 − 40 000."),
      ("Taux de marge (sur coût d'achat) :", "25 %", "20 %", "10 %", "18 %", "10 000/40 000."),
      ("Taux de marque (sur prix de vente) :", "20 %", "25 %", "10 %", "80 %", "10 000/50 000."),
      ("Prix TTC :", "59 000 F", "50 018 F", "68 000 F", "47 200 F", "50 000 × 1,18.")])]),
  mk("1ereg", L1G, "maths-g", "Mathématiques", 2, [
    ("Systèmes", "Une boutique vend des cahiers et des stylos. 3 cahiers + 2 stylos = 1 300 F ; 1 cahier + 4 stylos = 1 100 F.", [
      ("Prix d'un stylo :", "200 F", "150 F", "250 F", "100 F", "c = 1 100 − 4s ; 3(1 100 − 4s) + 2s = 1 300 → 10s = 2 000."),
      ("Prix d'un cahier :", "300 F", "400 F", "200 F", "350 F", "1 100 − 800."),
      ("Vérification : 3 × 300 + 2 × 200 =", "1 300", "1 100", "1 500", "1 200", "Correct."),
      ("Méthode utilisée :", "substitution", "dérivation", "intégration", "factorisation", "On remplace une inconnue.")]),
    ("Fonctions affines et seuil de rentabilité", "Charges fixes : 300 000 F ; marge par unité : 1 500 F. Résultat R(x) = 1 500x − 300 000.", [
      ("Seuil de rentabilité :", "200 unités", "300 unités", "150 unités", "2 000 unités", "1 500x = 300 000."),
      ("Résultat pour 300 unités :", "150 000 F", "450 000 F", "−150 000 F", "300 000 F", "450 000 − 300 000."),
      ("Pour 100 unités, l'entreprise", "fait une perte de 150 000 F", "fait un bénéfice", "est à l'équilibre", "ne vend rien", "150 000 − 300 000."),
      ("R est une fonction", "affine croissante", "affine décroissante", "constante", "du second degré", "a = 1 500 > 0.")]),
    ("Second degré", "Coût total C(x) = x² + 20x + 100 et recette R(x) = 60x (en milliers de F).", [
      ("Bénéfice B(x) = R(x) − C(x) =", "−x² + 40x − 100", "x² + 40x + 100", "−x² + 80x − 100", "x² − 40x − 100", "60x − x² − 20x − 100."),
      ("Quantité qui maximise B :", "20", "40", "10", "60", "−b/2a = 40/2."),
      ("Bénéfice maximal :", "300", "400", "100", "200", "−400 + 800 − 100."),
      ("B(0) =", "−100", "0", "100", "60", "Charges fixes.")])]),
  mk("1ereg", L1G, "maths-g", "Mathématiques", 3, [
    ("Statistiques", "Chiffre d'affaires mensuel (millions F) d'une PME : 4, 5, 5, 6, 7, 9.", [
      ("Moyenne :", "6", "5", "5,5", "7", "36/6."),
      ("Médiane :", "5,5", "5", "6", "6,5", "(5 + 6)/2."),
      ("Étendue :", "5", "9", "4", "6", "9 − 4."),
      ("Variance :", "8/3 ≈ 2,67", "6", "2", "16", "(4 + 1 + 1 + 0 + 1 + 9)/6 = 16/6.")]),
    ("Proportionnalité et partage", "Trois associés apportent 2, 3 et 5 millions F. Le bénéfice de 4 millions F est partagé proportionnellement.", [
      ("Part du premier :", "800 000 F", "2 000 000 F", "1 000 000 F", "400 000 F", "4 × 2/10."),
      ("Part du deuxième :", "1 200 000 F", "1 500 000 F", "3 000 000 F", "800 000 F", "4 × 3/10."),
      ("Part du troisième :", "2 000 000 F", "1 000 000 F", "5 000 000 F", "1 200 000 F", "4 × 5/10."),
      ("Coefficient de proportionnalité :", "0,4", "2,5", "4", "10", "4/10.")]),
    ("Pourcentages", "Le chiffre d'affaires passe de 50 à 60 millions F, puis de 60 à 54 millions F.", [
      ("Première évolution :", "+20 %", "+10 %", "+16,7 %", "+60 %", "10/50."),
      ("Deuxième évolution :", "−10 %", "−6 %", "−11 %", "−54 %", "−6/60."),
      ("Évolution globale :", "+8 %", "+10 %", "+4 %", "0 %", "1,2 × 0,9 = 1,08."),
      ("Taux moyen par période ≈", "3,9 %", "5 %", "4 %", "10 %", "√1,08 ≈ 1,039.")])]),
  mk("1ereg", L1G, "maths-g", "Mathématiques", 4, [
    ("Synthèse : placements", "Deux placements de 1 000 000 F : A à 5 % d'intérêts simples, B à 4,5 % d'intérêts simples plus une prime de 10 000 F.", [
      ("Intérêt de A sur 1 an :", "50 000 F", "5 000 F", "500 000 F", "45 000 F", "1 000 000 × 0,05."),
      ("Gain de B sur 1 an :", "55 000 F", "45 000 F", "10 000 F", "50 000 F", "45 000 + 10 000."),
      ("Meilleur placement sur 1 an :", "B", "A", "les deux sont égaux", "aucun", "55 000 > 50 000."),
      ("Sur 4 ans, A rapporte", "200 000 F, B rapporte 190 000 F", "autant que B", "moins que B", "50 000 F", "A : 4 × 50 000 ; B : 4 × 45 000 + 10 000.")]),
    ("Synthèse : TVA et facture", "Facture : 3 articles à 15 000 F HT, remise 10 %, TVA 18 %.", [
      ("Montant brut HT :", "45 000 F", "15 000 F", "40 500 F", "53 100 F", "3 × 15 000."),
      ("Net commercial après remise :", "40 500 F", "45 000 F", "4 500 F", "36 000 F", "45 000 × 0,9."),
      ("TVA :", "7 290 F", "8 100 F", "4 500 F", "18 000 F", "40 500 × 0,18."),
      ("Net à payer TTC :", "47 790 F", "53 100 F", "45 000 F", "40 500 F", "40 500 + 7 290.")]),
    ("Synthèse : fonctions", "f(x) = 2x² − 8x + 6.", [
      ("Racines :", "1 et 3", "2 et 6", "−1 et −3", "4 et 6", "Δ = 64 − 48 = 16 ; (8 ± 4)/4."),
      ("Minimum atteint en x =", "2", "4", "1", "3", "−b/2a = 8/4."),
      ("Valeur du minimum :", "−2", "6", "0", "2", "8 − 16 + 6."),
      ("f(x) ≥ 0 pour", "x ≤ 1 ou x ≥ 3", "1 ≤ x ≤ 3", "x ≥ 2", "tout x", "Signe de a à l'extérieur des racines.")])]),
  # ================= 1re G : économie
  mk("1ereg", L1G, "eco", "Économie", 1, [
    ("Les agrégats", "Une entreprise de jus achète 2 millions F de fruits et d'emballages et vend sa production 5 millions F.", [
      ("Valeur ajoutée :", "3 millions F", "5 millions F", "7 millions F", "2 millions F", "Production − consommations intermédiaires."),
      ("Les fruits achetés sont des", "consommations intermédiaires", "investissements", "salaires", "impôts", "Détruits dans la production."),
      ("Le PIB est la somme", "des valeurs ajoutées produites sur le territoire", "des salaires seulement", "des exportations", "des importations", "Définition."),
      ("Le PIB par habitant mesure", "la richesse moyenne par personne", "le nombre d'habitants", "le chômage", "l'inflation", "PIB / population.")]),
    ("La croissance", "Le PIB passe de 16 000 à 17 120 milliards F.", [
      ("Taux de croissance :", "7 %", "1,12 %", "12 %", "70 %", "1 120/16 000."),
      ("Croissance réelle si l'inflation est de 3 % :", "environ 4 %", "10 %", "7 %", "3 %", "Croissance nominale − inflation (approximation)."),
      ("La croissance mesure", "l'augmentation de la production", "la baisse des prix", "le nombre d'entreprises", "le taux d'intérêt", "Définition."),
      ("Le développement intègre en plus", "le bien-être, la santé et l'éducation", "seulement le PIB", "les exportations", "la population", "Notion plus large (IDH).")]),
    ("Les secteurs", "Classer les activités.", [
      ("La pêche à Kayar :", "secteur primaire", "secteur secondaire", "secteur tertiaire", "aucun", "Exploitation des ressources naturelles."),
      ("Une cimenterie à Rufisque :", "secteur secondaire", "secteur primaire", "secteur tertiaire", "aucun", "Transformation."),
      ("Une banque à Dakar :", "secteur tertiaire", "secteur primaire", "secteur secondaire", "aucun", "Services."),
      ("Le secteur informel désigne", "les activités non déclarées", "les grandes entreprises cotées", "l'administration", "les banques centrales", "Très important au Sénégal.")])]),
  mk("1ereg", L1G, "eco", "Économie", 2, [
    ("Le marché et les prix", "Sur le marché de l'oignon, l'offre baisse à cause de la saison sèche.", [
      ("Conséquence sur le prix :", "il augmente", "il baisse", "il ne change pas", "il devient nul", "Rareté."),
      ("Le prix d'équilibre est atteint quand", "l'offre égale la demande", "l'offre est nulle", "la demande est nulle", "l'État fixe tout", "Définition."),
      ("Si le prix augmente, la demande en général", "diminue", "augmente", "reste identique", "double", "Loi de la demande."),
      ("Mesure de l'État pour protéger les consommateurs :", "l'homologation des prix", "la suppression des marchés", "l'interdiction de vendre", "la hausse des taxes", "Contrôle des prix.")]),
    ("L'inflation", "L'indice des prix passe de 100 à 104 en un an.", [
      ("Taux d'inflation :", "4 %", "104 %", "0,4 %", "40 %", "104 − 100."),
      ("L'inflation est", "une hausse générale et durable des prix", "une baisse des prix", "une hausse d'un seul prix", "une hausse des salaires", "Définition."),
      ("Effet sur le pouvoir d'achat si les salaires ne bougent pas :", "il baisse", "il augmente", "il ne change pas", "il double", "Moins de biens achetés."),
      ("Organisme qui lutte contre l'inflation dans l'UEMOA :", "la BCEAO", "le FMI", "la CEDEAO", "l'ONU", "Politique monétaire.")]),
    ("La monnaie", "Le franc CFA de l'UEMOA.", [
      ("Fonctions de la monnaie :", "intermédiaire des échanges, unité de compte, réserve de valeur", "seulement décorer", "produire des biens", "payer l'État seulement", "Trois fonctions."),
      ("Banque centrale de l'UEMOA :", "la BCEAO", "la BEAC", "la BCE", "la Banque mondiale", "Siège à Dakar."),
      ("Le paiement par téléphone (Wave, Orange Money) est", "de la monnaie électronique", "du troc", "de l'or", "illégal", "Monnaie scripturale/électronique."),
      ("Parité fixe du franc CFA avec l'euro :", "1 euro = 655,957 F CFA", "1 euro = 100 F CFA", "1 euro = 1 000 F CFA", "variable chaque jour", "Taux fixe.")])]),
  mk("1ereg", L1G, "eco", "Économie", 3, [
    ("L'emploi et le chômage", "Population active : 5 millions ; chômeurs : 600 000.", [
      ("Taux de chômage :", "12 %", "6 %", "60 %", "1,2 %", "600 000/5 000 000."),
      ("Un chômeur est une personne", "sans emploi qui en cherche un", "qui ne veut pas travailler", "à la retraite", "élève", "Définition BIT."),
      ("Le sous-emploi désigne", "un travail insuffisant ou mal rémunéré", "le plein-emploi", "un chômage nul", "la retraite", "Fréquent dans l'informel."),
      ("Mesure contre le chômage des jeunes :", "la formation professionnelle", "la fermeture des écoles", "la hausse des impôts sur l'embauche", "l'arrêt des investissements", "Employabilité.")]),
    ("L'État et le budget", "Recettes de l'État : 4 000 milliards ; dépenses : 4 600 milliards.", [
      ("Solde budgétaire :", "−600 milliards (déficit)", "+600 milliards", "8 600 milliards", "0", "Recettes − dépenses."),
      ("Principale recette fiscale :", "la TVA", "les dons", "les amendes", "les loteries", "Impôt indirect."),
      ("Un impôt direct :", "l'impôt sur le revenu", "la TVA", "les droits de douane", "la taxe sur l'essence", "Payé directement par le contribuable."),
      ("Pour financer un déficit, l'État peut", "emprunter", "imprimer librement des francs CFA", "supprimer la monnaie", "fermer les banques", "Dette publique.")]),
    ("Le commerce extérieur", "Exportations : 2 500 milliards ; importations : 4 000 milliards.", [
      ("Balance commerciale :", "−1 500 milliards", "+1 500 milliards", "6 500 milliards", "0", "X − M."),
      ("Taux de couverture :", "62,5 %", "160 %", "37,5 %", "100 %", "X/M × 100."),
      ("Le Sénégal importe beaucoup de", "riz et produits pétroliers", "arachide", "poisson", "phosphates", "Dépendance."),
      ("Le protectionnisme consiste à", "protéger la production nationale par des taxes ou quotas", "supprimer toutes les douanes", "exporter sans limite", "interdire la production", "Définition.")])]),
  mk("1ereg", L1G, "eco", "Économie", 4, [
    ("L'entreprise", "Types d'entreprises au Sénégal.", [
      ("Une SARL est", "une société à responsabilité limitée", "une entreprise publique", "une association", "un GIE obligatoirement", "Forme juridique."),
      ("Un GIE est", "un groupement d'intérêt économique", "une banque", "un impôt", "un ministère", "Très utilisé par les femmes et les jeunes."),
      ("Facteurs de production :", "travail et capital", "impôts et taxes", "prix et inflation", "exportations", "Combinaison."),
      ("L'investissement est", "l'achat de biens de production durables", "l'achat de nourriture", "le paiement des salaires", "une dépense de loisirs", "FBCF.")]),
    ("Synthèse : circuit économique", "Agents et flux.", [
      ("Les ménages fournissent aux entreprises", "du travail", "des impôts", "des subventions", "des crédits obligatoires", "Facteur travail."),
      ("Les entreprises versent aux ménages", "des salaires", "des impôts", "des dons", "des amendes", "Revenus."),
      ("Les banques", "collectent l'épargne et accordent des crédits", "produisent des biens agricoles", "votent les lois", "fixent la TVA", "Intermédiaires financiers."),
      ("Le reste du monde intervient par", "les importations et les exportations", "les salaires", "les impôts locaux", "les loyers", "Échanges extérieurs.")]),
    ("Synthèse : calculs", "Révision.", [
      ("VA = 8 ; CI = 12 : production =", "20", "4", "96", "8", "P = VA + CI."),
      ("Prix de 2 000 F à 2 100 F : hausse", "5 %", "10 %", "100 %", "2,1 %", "100/2 000."),
      ("Taux de chômage avec 300 chômeurs pour 2 000 actifs :", "15 %", "6,7 %", "30 %", "1,5 %", "300/2 000."),
      ("PIB de 1 000 et population de 50 : PIB par habitant", "20", "50 000", "1 050", "950", "1 000/50.")])]),
  # ================= 1re G : comptabilité
  mk("1ereg", L1G, "compta", "Techniques comptables", 1, [
    ("Le bilan", "Une boutique possède : matériel 2 000 000, stock 800 000, banque 500 000, caisse 200 000 ; dettes fournisseurs 900 000 ; emprunt 1 000 000.", [
      ("Total de l'actif :", "3 500 000", "1 900 000", "5 400 000", "2 800 000", "2 000 000 + 800 000 + 500 000 + 200 000."),
      ("Total des dettes :", "1 900 000", "900 000", "1 000 000", "3 500 000", "900 000 + 1 000 000."),
      ("Capital (capitaux propres) :", "1 600 000", "3 500 000", "1 900 000", "5 400 000", "Actif − dettes."),
      ("Le bilan est toujours", "équilibré (actif = passif)", "déséquilibré", "positif seulement", "en perte", "Principe.")]),
    ("La partie double", "Achat de marchandises à crédit pour 300 000 F.", [
      ("Compte débité :", "601 Achats de marchandises", "401 Fournisseurs", "521 Banque", "571 Caisse", "Charge."),
      ("Compte crédité :", "401 Fournisseurs", "601 Achats", "411 Clients", "701 Ventes", "Dette envers le fournisseur."),
      ("Principe de la partie double :", "total des débits = total des crédits", "on débite seulement", "on crédite seulement", "un seul compte par opération", "Équilibre."),
      ("Référentiel comptable en vigueur au Sénégal :", "SYSCOHADA", "IFRS seul", "Plan comptable français de 1982", "aucun", "Espace OHADA.")]),
    ("Les comptes de trésorerie", "Encaissement d'un client par chèque : 150 000 F.", [
      ("Compte débité :", "521 Banque", "411 Clients", "401 Fournisseurs", "601 Achats", "Entrée d'argent en banque."),
      ("Compte crédité :", "411 Clients", "521 Banque", "701 Ventes", "571 Caisse", "Diminution de la créance."),
      ("Classe des comptes de trésorerie :", "5", "4", "6", "2", "SYSCOHADA."),
      ("Classe des comptes de tiers :", "4", "5", "6", "7", "Clients, fournisseurs.")])]),
  mk("1ereg", L1G, "compta", "Techniques comptables", 2, [
    ("Le compte de résultat", "Ventes 5 000 000 ; achats consommés 2 800 000 ; transports 300 000 ; salaires 900 000 ; impôts et taxes 200 000.", [
      ("Total des charges :", "4 200 000", "3 100 000", "5 000 000", "2 800 000", "2 800 000 + 300 000 + 900 000 + 200 000."),
      ("Résultat :", "800 000 (bénéfice)", "−800 000", "5 000 000", "4 200 000", "Produits − charges."),
      ("Les ventes de marchandises sont enregistrées en classe", "7", "6", "4", "2", "Produits."),
      ("Les salaires sont des", "charges de personnel (classe 6)", "produits", "immobilisations", "dettes à long terme", "Compte 66.")]),
    ("Le journal", "Vente de marchandises au comptant (espèces) : 250 000 F.", [
      ("Compte débité :", "571 Caisse", "701 Ventes", "411 Clients", "521 Banque", "Entrée d'espèces."),
      ("Compte crédité :", "701 Ventes de marchandises", "571 Caisse", "601 Achats", "401 Fournisseurs", "Produit."),
      ("Le journal enregistre les opérations", "par ordre chronologique", "par compte", "au hasard", "une fois par an", "Livre-journal."),
      ("Le grand livre regroupe", "l'ensemble des comptes", "les factures seulement", "les salaires", "les chèques", "Comptes mouvementés.")]),
    ("La balance", "On vérifie les écritures.", [
      ("La balance présente pour chaque compte", "total débit, total crédit et solde", "seulement le nom", "le bilan", "la TVA", "Contrôle."),
      ("Le total des soldes débiteurs égale", "le total des soldes créditeurs", "zéro toujours", "le résultat", "l'actif", "Équilibre."),
      ("Un compte de banque débité de 900 000 et crédité de 650 000 a un solde", "débiteur de 250 000", "créditeur de 250 000", "nul", "débiteur de 1 550 000", "900 000 − 650 000."),
      ("Un solde créditeur de compte fournisseur signifie", "une dette envers le fournisseur", "une créance", "de l'argent en caisse", "une vente", "Passif.")])]),
  mk("1ereg", L1G, "compta", "Techniques comptables", 3, [
    ("Les amortissements", "Un véhicule acheté 6 000 000 F est amorti en linéaire sur 5 ans.", [
      ("Taux d'amortissement :", "20 %", "5 %", "25 %", "50 %", "100/5."),
      ("Annuité :", "1 200 000 F", "6 000 000 F", "300 000 F", "1 500 000 F", "6 000 000 × 20 %."),
      ("Valeur nette comptable après 2 ans :", "3 600 000 F", "4 800 000 F", "2 400 000 F", "1 200 000 F", "6 000 000 − 2 × 1 200 000."),
      ("L'amortissement constate", "la dépréciation d'une immobilisation", "une vente", "une recette", "un emprunt", "Usure.")]),
    ("Écriture d'amortissement", "Dotation de l'année : 1 200 000 F.", [
      ("Compte débité :", "681 Dotations aux amortissements", "284 Amortissements du matériel de transport", "245 Matériel de transport", "521 Banque", "Charge."),
      ("Compte crédité :", "284 Amortissements du matériel", "681 Dotations", "601 Achats", "401 Fournisseurs", "Compte d'amortissement."),
      ("Effet sur le résultat :", "il diminue", "il augmente", "aucun", "il double", "Charge non décaissée."),
      ("L'amortissement entraîne une sortie d'argent ?", "non", "oui, chaque année", "oui, le premier jour", "seulement si on vend", "Charge calculée.")]),
    ("La TVA", "Achat de marchandises : 400 000 F HT, TVA 18 %, payé par chèque.", [
      ("TVA déductible :", "72 000 F", "18 000 F", "400 000 F", "472 000 F", "400 000 × 0,18."),
      ("Montant TTC :", "472 000 F", "418 000 F", "400 000 F", "328 000 F", "400 000 + 72 000."),
      ("Compte de TVA récupérable :", "445 État, TVA récupérable", "443 État, TVA facturée", "701 Ventes", "601 Achats", "Créance sur l'État."),
      ("Compte crédité :", "521 Banque pour 472 000", "601 Achats pour 472 000", "445 pour 72 000", "401 pour 400 000", "Paiement par chèque.")])]),
  mk("1ereg", L1G, "compta", "Techniques comptables", 4, [
    ("Synthèse : du journal au bilan", "Révision.", [
      ("Ordre du cycle comptable :", "journal, grand livre, balance, états financiers", "bilan, journal, balance", "balance, journal, grand livre", "grand livre, bilan, journal", "Étapes."),
      ("Le résultat de l'exercice apparaît", "au compte de résultat et au passif du bilan", "seulement à l'actif", "dans le journal seulement", "nulle part", "Lien entre états."),
      ("Un bénéfice augmente", "les capitaux propres", "les dettes", "les immobilisations", "les stocks", "Passif."),
      ("Les immobilisations sont en classe", "2", "3", "5", "7", "Actif immobilisé.")]),
    ("Synthèse : écritures", "Paiement d'un fournisseur par virement : 500 000 F.", [
      ("Compte débité :", "401 Fournisseurs", "521 Banque", "601 Achats", "411 Clients", "Dette éteinte."),
      ("Compte crédité :", "521 Banque", "401 Fournisseurs", "571 Caisse", "701 Ventes", "Sortie d'argent."),
      ("Retrait d'espèces à la banque pour la caisse : compte débité", "571 Caisse", "521 Banque", "601 Achats", "411 Clients", "Virement interne."),
      ("Apport en capital en banque : compte crédité", "101 Capital", "521 Banque", "401 Fournisseurs", "701 Ventes", "Capitaux propres.")]),
    ("Synthèse : calculs", "Révision.", [
      ("Matériel 3 000 000 amorti sur 10 ans : annuité", "300 000", "3 000 000", "30 000", "100 000", "3 000 000/10."),
      ("Ventes 2 000 000, charges 1 700 000 : résultat", "300 000", "3 700 000", "−300 000", "1 700 000", "Produits − charges."),
      ("Actif 5 000 000, dettes 3 200 000 : capitaux propres", "1 800 000", "8 200 000", "3 200 000", "5 000 000", "Actif − dettes."),
      ("TVA 18 % sur 250 000 HT :", "45 000", "18 000", "250 018", "295 000", "250 000 × 0,18.")])]),
])
