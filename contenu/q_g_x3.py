# QCM de série G (1re et Tle G), volume ×3 : économie générale et techniques comptables.
# Les questions de calcul sont produites à partir de jeux de données fixes : chaque énoncé est différent,
# la bonne réponse et les distracteurs sont calculés, donc toujours justes.
from q_tle_plus import _q


def f(n):
    """Montant en francs avec espaces : 1 250 000."""
    n = round(n)
    return f"{n:,}".replace(",", " ") + " F"


def pc(x):
    s = f"{x:.1f}".replace(".", ",")
    return (s[:-2] if s.endswith(",0") else s) + " %"


def nb(x):
    """Nombre entier avec espaces : 12 600."""
    return f"{round(x):,}".replace(",", " ")


def _varier(ok, k):
    """Distracteur de secours : le nombre de la bonne réponse légèrement modifié (même unité)."""
    import re as _re
    m = _re.search(r"\d+(?: \d{3})*(?:,\d+)?", ok)
    if not m:
        return ok + " environ"
    v = float(m.group().replace(" ", "").replace(",", "."))
    w = v * [1.1, 0.9, 2, 0.5][k % 4]
    txt = (f"{w:.1f}".replace(".", ",").removesuffix(",0")) if "," in m.group() or w != round(w) and w < 100 else nb(w)
    return ok[:m.start()] + txt + ok[m.end():]


def distincts(ok, *autres):
    out = [ok]
    for a in autres:
        a = a.replace("-", "−") if a.startswith("-") else a
        if a not in out:
            out.append(a)
    for k in range(8):
        if len(out) >= 4:
            break
        c = _varier(ok, k)
        if c not in out:
            out.append(c)
    for c in ["aucune de ces réponses", "on ne peut pas savoir", "impossible à calculer"]:
        if len(out) < 4:
            out.append(c)
    return out[:4]


def calc(lst):
    """lst : (question, bonne, d1, d2, d3, explication) avec des valeurs déjà formatées."""
    out = []
    for q, ok, a, b, c, e in lst:
        ch = distincts(ok, a, b, c)
        out.append((q, ch, 0, e))
    return out


# ---------- Économie : calculs
VA = [(12, 7), (25, 16), (8, 3), (40, 31), (18, 11)]
eco_va = calc([(f"Une entreprise vend pour {p} M F et achète {c} M F de consommations intermédiaires. Sa valeur ajoutée est :",
                f"{p - c} M F", f"{p + c} M F", f"{c} M F", f"{p} M F", f"VA = production − consommations intermédiaires = {p} − {c}.") for p, c in VA])
CROIS = [(8000, 8400), (5000, 5150), (12000, 12600), (2000, 2070)]
eco_cr = calc([(f"Le PIB passe de {nb(a)} à {nb(b)} milliards F. Le taux de croissance est :", pc((b - a) / a * 100), pc((b - a) / b * 100), pc((b - a) / 100), pc(b / a * 100),
                f"({b} − {a}) / {a} × 100.") for a, b in CROIS])
REEL = [(6, 2), (5, 3), (7, 4), (4, 1)]
eco_reel = calc([(f"Le PIB nominal augmente de {n} % et les prix de {p} %. La croissance réelle est d'environ :", pc(n - p), pc(n + p), pc(n), pc(p),
                  f"Croissance réelle ≈ croissance nominale − inflation = {n} − {p}.") for n, p in REEL])
IPC = [(100, 104), (100, 112), (250, 260), (80, 84)]
eco_inf = calc([(f"Un panier de biens coûte {a} 000 F l'an dernier et {b} 000 F cette année. L'inflation est :", pc((b - a) / a * 100), pc(b - a), pc((b - a) / b * 100), pc(b / a * 100),
                 f"({b} − {a}) / {a} × 100.") for a, b in IPC])
CHOM = [(8, 1.2), (5, 0.6), (10, 2.5), (4, 0.5)]
eco_ch = calc([(f"Population active : {a} millions, dont {str(c).replace('.', ',')} million{'s' if c >= 2 else ''} de chômeurs. Le taux de chômage est :", pc(c / a * 100), pc(c / (a - c) * 100), pc(a / c), pc(c * 10),
                f"Chômeurs / population active × 100 = {c} / {a} × 100.".replace(".", ",")) for a, c in CHOM])
COUV = [(900, 1200), (1500, 1000), (600, 800), (2000, 2500)]
eco_cv = calc([(f"Exportations : {nb(x)} milliards F ; importations : {nb(m)} milliards F. Le taux de couverture est :", pc(x / m * 100), pc(m / x * 100), pc((x - m) / m * 100), pc(x - m),
                f"Exportations / importations × 100 = {x} / {m} × 100.") for x, m in COUV])
SOLDE = [(900, 1200), (1500, 1000), (600, 800)]
eco_sl = calc([(f"Exportations {nb(x)} Mds F, importations {nb(m)} Mds F : le solde commercial est :", f"{x - m:+d} Mds F".replace("+", "+ ").replace("-", "− "), f"{m - x:+d} Mds F".replace("+", "+ ").replace("-", "− "), f"{nb(x + m)} Mds F", "0 Mds F",
                "Solde = exportations − importations.") for x, m in SOLDE])
MULT = [(0.8, 100), (0.75, 40), (0.5, 60)]
eco_mu = calc([(f"Propension marginale à consommer {str(c).replace('.', ',')} : une dépense publique de {d} Mds F augmente le revenu d'environ :", f"{round(d / (1 - c))} Mds F", f"{d} Mds F", f"{round(d * c)} Mds F", f"{round(d / c)} Mds F",
                f"Multiplicateur k = 1 / (1 − c) = {round(1 / (1 - c), 2)}.".replace(".", ",")) for c, d in MULT])
PIBH = [(16000, 18), (9000, 15), (30000, 25)]
eco_ph = calc([(f"PIB : {nb(a)} milliards F ; population : {p} millions. Le PIB par habitant est d'environ :", f(a * 1e9 / (p * 1e6)), f(a * 1e6 / (p * 1e6)), f(a / p), f(a * 1e9 / p),
                "PIB / population.") for a, p in PIBH])

ECO_TXT = {
  "Les agrégats : PIB, croissance, valeur ajoutée": _q([
    ("Le PIB nominal est mesuré :", "aux prix de l'année en cours", "aux prix d'une année de base", "en volume seulement", "en dollars toujours", "Il inclut l'effet de l'inflation."),
    ("La production non marchande des administrations est évaluée :", "à son coût de production", "à son prix de vente", "à zéro", "au prix du marché noir", "Écoles, hôpitaux publics…"),
    ("Le PNB (ou RNB) diffère du PIB par :", "les revenus reçus de l'extérieur moins ceux versés à l'extérieur", "les impôts", "l'inflation", "les importations", "Critère de nationalité au lieu de territoire."),
    ("L'autoconsommation d'un paysan qui mange sa récolte est :", "estimée et ajoutée au PIB", "toujours ignorée", "comptée deux fois", "une importation", "Production pour soi."),
    ("Le travail domestique non rémunéré :", "n'est pas compté dans le PIB", "est compté au SMIG", "est une exportation", "est une consommation intermédiaire", "Limite du PIB."),
    ("Une croissance extensive repose surtout sur :", "plus de facteurs de production (travail, capital)", "le progrès technique", "la baisse des prix", "les exportations seulement", "La croissance intensive repose sur la productivité."),
    ("Le Plan Sénégal émergent (PSE), lancé en 2014, visait :", "une croissance forte et durable pour l'émergence", "la fermeture de l'économie", "la suppression des impôts", "l'abandon de l'agriculture", "Référentiel de politique économique."),
    ("Le développement se distingue de la croissance car il inclut :", "l'amélioration du bien-être (santé, éducation, niveau de vie)", "uniquement la hausse du PIB", "la baisse de la population", "l'inflation", "Notion qualitative."),
    ("L'IDH varie entre :", "0 et 1", "0 et 100 000", "−1 et 1", "1 et 10", "Plus il est proche de 1, plus le développement humain est élevé."),
    ("Les trois optiques du PIB (production, revenu, dépense) donnent :", "le même résultat", "trois résultats très différents", "seulement des valeurs en volume", "des valeurs nulles", "Égalité comptable."),
  ]),
  "Les secteurs d'activité et les entreprises": _q([
    ("Une entreprise qui transforme l'arachide en huile appartient au secteur :", "secondaire", "primaire", "tertiaire", "quaternaire", "Transformation industrielle."),
    ("Une banque appartient au secteur :", "tertiaire", "primaire", "secondaire", "informel", "Services."),
    ("La forme juridique la plus simple pour un commerçant seul est :", "l'entreprise individuelle", "la SA", "le GIE", "la coopérative", "Un seul propriétaire, responsabilité illimitée."),
    ("Dans une SARL, la responsabilité des associés est :", "limitée à leurs apports", "illimitée", "nulle", "solidaire et illimitée", "Société à responsabilité limitée."),
    ("Un GIE (groupement d'intérêt économique) permet :", "à des entreprises de mettre des moyens en commun", "de créer une banque centrale", "d'émettre de la monnaie", "de fixer les impôts", "Courant au Sénégal (GIE de femmes…)."),
    ("La productivité du travail se mesure par :", "la production divisée par le nombre de travailleurs (ou d'heures)", "le salaire moyen", "le nombre d'entreprises", "le prix de vente", "Production par unité de travail."),
    ("Un atelier produit 600 pièces avec 20 ouvriers. Productivité par ouvrier :", "30 pièces", "12 000 pièces", "620 pièces", "580 pièces", "600 / 20."),
    ("Les économies d'échelle signifient que :", "le coût unitaire baisse quand la production augmente", "les prix augmentent toujours", "l'entreprise produit moins", "les salaires baissent", "Coûts fixes répartis sur plus d'unités."),
    ("L'APIX au Sénégal a pour mission :", "de promouvoir l'investissement et faciliter la création d'entreprises", "d'émettre la monnaie", "de collecter l'impôt", "de gérer les écoles", "Guichet unique."),
    ("Le secteur informel au Sénégal représente :", "une très grande part des emplois", "presque aucun emploi", "uniquement l'agriculture d'exportation", "les grandes entreprises", "Plus de 90 % des unités économiques."),
  ]),
  "Le marché, les prix et l'inflation": _q([
    ("La loi de la demande dit qu'en général, quand le prix augmente :", "la quantité demandée diminue", "la quantité demandée augmente", "rien ne change", "l'offre diminue", "Relation inverse."),
    ("La loi de l'offre dit qu'en général, quand le prix augmente :", "la quantité offerte augmente", "la quantité offerte diminue", "la demande augmente", "le marché disparaît", "Les producteurs sont incités à produire."),
    ("Un excès de demande sur un marché provoque :", "une hausse du prix", "une baisse du prix", "une baisse de la demande", "un prix nul", "Pénurie."),
    ("Un excès d'offre provoque :", "une baisse du prix", "une hausse du prix", "une pénurie", "une hausse de la demande", "Surproduction."),
    ("L'élasticité-prix de la demande mesure :", "la sensibilité de la demande à une variation du prix", "le prix d'équilibre", "le revenu des ménages", "l'inflation", "Variation en % de la quantité / variation en % du prix."),
    ("Un bien de première nécessité (riz, sucre) a une demande :", "peu élastique au prix", "très élastique", "nulle", "toujours croissante avec le prix", "On en achète même s'il est plus cher."),
    ("Des biens complémentaires sont par exemple :", "une voiture et le carburant", "le riz et le mil", "le thé et le café", "deux marques de savon", "Ils sont consommés ensemble."),
    ("L'inflation par la demande apparaît quand :", "la demande globale dépasse les capacités de production", "les salaires baissent", "les importations sont nulles", "la population diminue", "Trop de monnaie pour pas assez de biens."),
    ("L'inflation par les coûts peut venir :", "d'une hausse du prix du pétrole ou des salaires", "d'une baisse des impôts", "d'une baisse de la demande", "d'une hausse du chômage seule", "Les entreprises répercutent leurs coûts."),
    ("La BCEAO vise une inflation d'environ :", "2 % (dans une fourchette de 1 à 3 %)", "10 %", "0 % exactement", "20 %", "Objectif de stabilité des prix."),
  ]),
  "La monnaie et la banque centrale": _q([
    ("La monnaie divisionnaire est constituée :", "des pièces", "des billets", "des chèques", "des virements", "Elle facilite les petits paiements."),
    ("La création monétaire par les banques commerciales se fait surtout :", "en accordant des crédits", "en imprimant des billets", "en collectant l'impôt", "en vendant de l'or", "« Les crédits font les dépôts »."),
    ("Le remboursement d'un crédit entraîne :", "une destruction de monnaie", "une création de monnaie", "une dévaluation", "une hausse du taux directeur", "La monnaie créée disparaît."),
    ("La BCEAO a son siège à :", "Dakar", "Abidjan", "Paris", "Lomé", "Banque centrale des États de l'Afrique de l'Ouest."),
    ("L'UEMOA compte :", "8 pays", "15 pays", "5 pays", "54 pays", "Bénin, Burkina, Côte d'Ivoire, Guinée-Bissau, Mali, Niger, Sénégal, Togo."),
    ("La parité fixe du franc CFA est :", "1 euro = 655,957 F CFA", "1 euro = 100 F CFA", "1 dollar = 655,957 F CFA", "flottante", "Depuis 1999."),
    ("Une hausse du taux directeur de la banque centrale vise à :", "freiner le crédit et l'inflation", "augmenter l'inflation", "relancer fortement le crédit", "dévaluer la monnaie", "Politique monétaire restrictive."),
    ("La thésaurisation consiste à :", "garder de la monnaie inactive (hors circuit)", "placer en banque", "investir", "consommer", "Ex. : argent caché à la maison."),
    ("La monnaie électronique (Wave, Orange Money) est réglementée par :", "la BCEAO", "le ministère de la Santé", "l'UEFA", "les communes", "Établissements de monnaie électronique agréés."),
    ("Le taux d'intérêt est :", "le prix de l'argent emprunté", "le prix de l'or", "le taux de change", "le taux d'inflation", "Rémunération du prêteur."),
  ]),
  "L'emploi et le chômage": _q([
    ("Un étudiant à plein temps qui ne cherche pas d'emploi est :", "inactif", "chômeur", "actif occupé", "sous-employé", "Il n'est pas dans la population active."),
    ("Le chômage conjoncturel est lié :", "à un ralentissement de l'activité économique", "aux saisons", "au changement d'emploi", "aux machines uniquement", "Il varie avec la conjoncture."),
    ("Le chômage structurel vient :", "d'une inadéquation durable entre offre et demande de travail", "d'une crise de quelques mois", "de la pluie", "des vacances", "Qualifications, secteurs en déclin…"),
    ("Le salaire est :", "le prix du travail", "le prix du capital", "un impôt", "une subvention", "Rémunération du facteur travail."),
    ("Le SMIG au Sénégal est :", "le salaire minimum interprofessionnel garanti", "un impôt", "une banque", "une allocation de chômage", "Revalorisé en 2018."),
    ("Le chômage déguisé correspond :", "à des personnes occupées mais très peu productives", "à des chômeurs inscrits", "aux étudiants", "aux retraités", "Fréquent dans l'agriculture traditionnelle."),
    ("La formation professionnelle aide à réduire :", "le chômage structurel", "l'inflation importée", "la dette publique", "le déficit commercial seulement", "Meilleure adéquation des qualifications."),
    ("L'émigration des jeunes peut s'expliquer par :", "le manque d'emplois et l'espoir de meilleurs revenus", "l'excès d'emplois", "la baisse de la population", "la hausse des salaires au Sénégal uniquement", "Facteurs répulsifs et attractifs."),
    ("Le sous-emploi visible correspond à :", "un temps de travail involontairement réduit", "un salaire trop élevé", "un emploi de cadre", "un chômage nul", "Temps partiel subi."),
    ("La DER/FJ au Sénégal finance :", "des projets d'entrepreneuriat des jeunes et des femmes", "les retraites", "l'armée", "les élections", "Délégation à l'entrepreneuriat rapide."),
  ]),
  "L'État : impôts et politique budgétaire": _q([
    ("Un impôt direct est payé :", "directement par la personne qui le supporte (ex. impôt sur le revenu)", "par le consommateur dans le prix", "par l'étranger", "par la banque centrale", "Contribuable = redevable."),
    ("La TVA est un impôt :", "indirect sur la consommation", "direct sur le revenu", "sur le patrimoine", "sur les sociétés uniquement", "Incluse dans le prix."),
    ("Le budget de l'État est en déficit quand :", "les dépenses dépassent les recettes", "les recettes dépassent les dépenses", "les impôts augmentent", "la dette est nulle", "Solde budgétaire négatif."),
    ("La pression fiscale est :", "le rapport des prélèvements fiscaux au PIB", "le montant de la TVA", "le taux d'inflation", "le nombre de contribuables", "Critère UEMOA : au moins 20 %."),
    ("Une politique budgétaire restrictive consiste à :", "réduire les dépenses ou augmenter les impôts", "augmenter fortement les dépenses", "baisser les taux d'intérêt", "dévaluer la monnaie", "Pour réduire le déficit."),
    ("L'État-providence intervient surtout pour :", "protéger les individus (santé, retraites, aides sociales)", "fabriquer des voitures", "fixer tous les prix", "supprimer les impôts", "Fonction de redistribution."),
    ("Les transferts sociaux sont :", "des revenus versés par l'État aux ménages (bourses, pensions…)", "des impôts", "des exportations", "des salaires privés", "Redistribution."),
    ("La loi de finances est votée par :", "l'Assemblée nationale", "la BCEAO", "le Conseil constitutionnel", "les communes", "Autorisation annuelle des recettes et dépenses."),
    ("Le critère UEMOA sur la dette publique fixe un plafond de :", "70 % du PIB", "10 % du PIB", "200 % du PIB", "3 % du PIB", "Critère de convergence."),
    ("Les droits de douane sont :", "des impôts sur les importations", "des impôts sur le revenu", "des salaires de douaniers", "des subventions", "Ils protègent aussi la production nationale."),
  ]),
  "Le commerce extérieur": _q([
    ("Une importation est :", "un achat de biens ou de services à l'étranger", "une vente à l'étranger", "un impôt", "une production nationale", "Sortie de devises."),
    ("La CEDEAO compte :", "15 pays membres (avant le retrait des pays de l'AES)", "8 pays", "54 pays", "3 pays", "Communauté économique des États de l'Afrique de l'Ouest."),
    ("Le tarif extérieur commun (TEC) de la CEDEAO s'applique :", "aux importations venant de pays hors de la zone", "au commerce entre membres", "aux salaires", "à la TVA", "Union douanière."),
    ("L'avantage comparatif de Ricardo conseille de se spécialiser dans :", "la production où l'on est relativement le plus efficace", "toutes les productions", "aucune production", "la production la plus chère", "Gains à l'échange même sans avantage absolu."),
    ("Une balance commerciale déficitaire signifie :", "importations supérieures aux exportations", "exportations supérieures aux importations", "commerce nul", "inflation forte", "Cas habituel du Sénégal."),
    ("La dégradation des termes de l'échange pour un pays exportateur de matières premières signifie :", "qu'il doit exporter plus pour importer autant", "qu'il s'enrichit automatiquement", "que ses importations sont gratuites", "que sa monnaie disparaît", "Prix à l'export relatifs en baisse."),
    ("Le dumping consiste à :", "vendre à l'étranger moins cher que sur le marché national", "fermer les frontières", "taxer les importations", "subventionner l'éducation", "Pratique déloyale."),
    ("Une zone de libre-échange supprime :", "les droits de douane entre ses membres", "toutes les monnaies", "les frontières politiques", "les impôts intérieurs", "Ex. : ZLECAf."),
    ("Les recettes d'exportation du Sénégal ont été renforcées depuis 2024 par :", "le pétrole et le gaz", "le cacao", "le café", "les diamants", "Champs Sangomar et GTA."),
    ("Le compte courant de la balance des paiements inclut :", "les biens, les services, les revenus et les transferts courants", "uniquement les investissements", "les réserves d'or seulement", "les impôts intérieurs", "Transactions courantes avec l'extérieur."),
  ]),
}

# ---------- Comptabilité : calculs
BILAN = [(15, 6, 4), (40, 22, 10), (9, 5, 1), (60, 35, 12)]
cpt_cp = calc([(f"Actif total {a} M F, dettes financières {d} M F, dettes circulantes {c} M F : capitaux propres =", f"{a - d - c} M F", f"{a - d} M F", f"{a + d + c} M F", f"{d + c} M F",
                "Actif = capitaux propres + dettes, donc CP = actif − dettes.") for a, d, c in BILAN])
RES = [(48, 41), (12, 13), (90, 72), (5, 4), (33, 36), (150, 128)]
cpt_res = calc([(f"Produits de l'exercice {p} M F, charges {c} M F : le résultat est :", (f"bénéfice de {p - c} M F" if p > c else f"perte de {c - p} M F"), (f"perte de {p - c} M F" if p > c else f"bénéfice de {c - p} M F"), f"{p + c} M F", f"{p} M F",
                 "Résultat = produits − charges.") for p, c in RES])
MARGE = [(800, 500, 50, 70), (1200, 700, 100, 80), (450, 300, 20, 40), (2000, 1400, 150, 90), (600, 420, 30, 30)]
cpt_mc = calc([(f"Ventes de marchandises {f(v * 1000)}, achats {f(a * 1000)}, stock initial {f(si * 1000)}, stock final {f(sf * 1000)}. Marge commerciale :", f(1000 * (v - (a + si - sf))), f(1000 * (v - a)), f(1000 * (v - (a - si + sf))), f(1000 * (a + si - sf)),
                f"Coût d'achat des marchandises vendues = achats + SI − SF = {f((a + si - sf) * 1000)} ; marge = ventes − ce coût.") for v, a, si, sf in MARGE])
TVA = [(500000, 18), (1200000, 18), (85000, 18), (2400000, 18)]
cpt_tva = calc([(f"Une facture hors taxes de {f(h)} (TVA {t} %) : montant TTC :", f(h * 1.18), f(h * 0.18), f(h * 0.82), f(h + 18), f"TTC = HT × 1,18 ; TVA = {f(h * 0.18)}.") for h, t in TVA])
TVAD = [(900000, 540000), (1500000, 1700000), (300000, 120000), (720000, 450000), (2500000, 1900000)]
cpt_td = calc([(f"TVA facturée sur les ventes {f(c)}, TVA récupérable sur les achats {f(d)} : TVA à payer à l'État :", (f(c - d) if c > d else "0 F (crédit de TVA de " + f(d - c) + ")"), f(c + d), f(d - c) if d > c else f(d), (f(c) if c != d else "0 F"),
                "TVA due = TVA collectée − TVA déductible ; si négatif, crédit de TVA.") for c, d in TVAD])
AMO = [(3000000, 5), (6000000, 10), (1500000, 3), (8000000, 4), (900000, 5)]
cpt_al = calc([(f"Un matériel de {f(v)} est amorti en linéaire sur {n} ans. L'annuité est :", f(v / n), f(v * n), f(v / (n + 1)), f(v * 0.2 if n != 5 else v * 0.25), f"Annuité = valeur d'origine / durée = {f(v)} / {n}.") for v, n in AMO])
VNC = [(3000000, 5, 2), (6000000, 10, 3), (8000000, 4, 1), (1200000, 6, 4), (5000000, 5, 3), (2000000, 8, 5)]
cpt_vnc = calc([(f"Bien de {f(v)} amorti en linéaire sur {n} ans. VNC après {k} an{'s' if k > 1 else ''} :", f(v - k * v / n), f(k * v / n), f(v), f(v - v / n), f"VNC = valeur d'origine − amortissements cumulés = {f(v)} − {k} × {f(v / n)}.") for v, n, k in VNC])
PRO = [(2400000, 5, 4), (3600000, 4, 7), (1200000, 10, 10)]
cpt_pro = calc([(f"Bien de {f(v)} acquis le 1er {['', '', '', '', 'avril', '', '', 'juillet', '', '', 'octobre'][m]}, linéaire sur {n} ans, clôture au 31 décembre. Dotation de la 1re année :", f(v / n * (13 - m) / 12), f(v / n), f(v / n * (m - 1) / 12), f(v * (13 - m) / 12), f"Prorata temporis : {13 - m} mois sur 12.") for v, n, m in PRO])
DEG = [(5, 2.0, 40), (4, 1.5, 37.5), (6, 2.0, 33.33)]
cpt_dg = calc([(f"Amortissement dégressif, durée {n} ans (coefficient {str(k).replace('.', ',')}) : le taux dégressif est :", pc(100 / n * k), pc(100 / n), pc(100 / n * (k + 0.5)), pc(100 * k), f"Taux linéaire {pc(100 / n)} × coefficient {str(k).replace('.', ',')}.") for n, k, _ in DEG])
CES = [(1000000, 400000, 750000), (2500000, 2000000, 300000), (600000, 600000, 50000), (4000000, 2400000, 1200000), (1800000, 900000, 1000000)]
cpt_ces = calc([(f"Bien de valeur d'origine {f(v)}, amortissements cumulés {f(a)}, cédé pour {f(p)}. Résultat de cession :", (("plus-value de " + f(p - (v - a))) if p > v - a else ("moins-value de " + f((v - a) - p))), f(p - v), f(p), f(v - a), f"VNC = {f(v - a)} ; résultat = prix de cession − VNC.") for v, a, p in CES])
FR = [(20, 14, 9, 7), (35, 30, 12, 10), (50, 42, 15, 18), (28, 20, 11, 6), (60, 48, 20, 14)]
cpt_fr = calc([(f"Ressources stables {rs} M, actif immobilisé {ai} M, actif circulant {ac} M, passif circulant {pcir} M. Trésorerie nette :", f"{(rs - ai) - (ac - pcir)} M F".replace("-", "− "), f"{rs - ai} M F", f"{ac - pcir} M F", f"{(rs - ai) + (ac - pcir)} M F",
                "FR = RS − AI ; BFR = AC − PC ; TN = FR − BFR.") for rs, ai, ac, pcir in FR])
CAISSE = [(250000, 900000, 700000), (80000, 300000, 310000), (1000000, 2500000, 3000000), (150000, 640000, 520000), (40000, 95000, 110000)]
cpt_cs = calc([(f"Caisse : solde initial {f(s)}, entrées {f(e)}, sorties {f(o)}. Solde final :", f(s + e - o), f(s + e + o), f(e - o), f(s - e + o), "Solde final = solde initial + entrées − sorties (jamais créditeur pour la caisse).") for s, e, o in CAISSE])
SAL = [(300000, 5.6, 3.6), (500000, 5.6, 3.6)]
REMISE = [(400000, 10, 2), (1000000, 5, 3), (250000, 20, 1), (600000, 15, 2), (80000, 10, 5)]
cpt_rm = calc([(f"Prix brut {f(b)}, remise {r} %, puis escompte de règlement {e} % : net à payer (hors taxes) :", f(b * (1 - r / 100) * (1 - e / 100)), f(b * (1 - (r + e) / 100)), f(b * (1 - r / 100)), f(b - r - e),
                "Les réductions se calculent en cascade : brut × (1 − remise) × (1 − escompte).") for b, r, e in REMISE])

CPT_TXT = {
  "Le cadre comptable : SYSCOHADA": _q([
    ("La classe 4 du SYSCOHADA regroupe :", "les comptes de tiers (fournisseurs, clients, État, personnel)", "les immobilisations", "les stocks", "les charges", "Comptes de tiers."),
    ("La classe 6 regroupe :", "les charges des activités ordinaires", "les produits", "les capitaux", "les stocks", "Classe de gestion."),
    ("Le compte 2441 correspond à :", "matériel et outillage industriel", "fournisseurs", "ventes", "banque", "Classe 2 : immobilisations corporelles."),
    ("Le compte 24 regroupe :", "le matériel (immobilisations corporelles)", "les stocks de marchandises", "les clients", "les dettes fiscales", "Matériel, mobilier, transport…"),
    ("Le compte 31 correspond aux :", "stocks de marchandises", "clients", "terrains", "achats", "Classe 3."),
    ("Le compte 661 correspond aux :", "rémunérations directes versées au personnel", "achats de marchandises", "ventes", "intérêts reçus", "Charges de personnel."),
    ("Le compte 681 correspond aux :", "dotations aux amortissements d'exploitation", "ventes de produits", "achats", "impôts", "Charge non décaissée."),
    ("Le compte 701 correspond aux :", "ventes de marchandises", "achats de marchandises", "salaires", "loyers payés", "Classe 7."),
    ("Le principe de continuité d'exploitation suppose que :", "l'entreprise poursuivra son activité", "l'entreprise va fermer", "les comptes sont tenus en dollars", "les stocks sont nuls", "Sinon, on évalue à la valeur liquidative."),
    ("Le principe de non-compensation interdit :", "de compenser des dettes avec des créances (ou charges avec produits)", "d'amortir", "de tenir un journal", "de faire un bilan", "Chaque élément est présenté pour son montant brut."),
    ("Le principe de régularité impose :", "de respecter les règles et procédures en vigueur", "de ne jamais changer d'entreprise", "de payer comptant", "d'avoir un bénéfice", "Conformité au droit comptable."),
    ("L'Acte uniforme relatif au droit comptable est adopté par :", "l'OHADA", "la BCEAO", "la CEDEAO", "l'ONU", "Organisation pour l'harmonisation en Afrique du droit des affaires."),
    ("Les comptes de classe 9 servent :", "à la comptabilité analytique (ou des engagements)", "aux immobilisations", "aux charges", "aux tiers", "Comptabilité de gestion."),
    ("Le système minimal de trésorerie (SMT) s'adresse :", "aux très petites entreprises", "aux grandes sociétés cotées", "aux banques", "à l'État", "Comptabilité simplifiée de caisse."),
  ]),
  "Le bilan": _q([
    ("Le bilan est une photographie du patrimoine de l'entreprise :", "à une date donnée", "sur toute l'année", "sur 10 ans", "au jour de la création seulement", "Généralement au 31 décembre."),
    ("Les immobilisations sont des biens :", "destinés à rester durablement dans l'entreprise", "destinés à être vendus rapidement", "consommés en un mois", "appartenant aux clients", "Plus d'un an."),
    ("Les capitaux propres comprennent :", "le capital, les réserves et le résultat", "les emprunts", "les fournisseurs", "la banque", "Ressources propres."),
    ("Les dettes financières sont des ressources :", "stables (à long et moyen terme)", "de trésorerie", "d'exploitation à court terme", "propres", "Emprunts bancaires."),
    ("La trésorerie-actif comprend :", "la banque (solde débiteur) et la caisse", "les clients", "les stocks", "le capital", "Disponibilités."),
    ("La trésorerie-passif comprend notamment :", "les découverts et crédits de trésorerie", "le capital", "les immobilisations", "la caisse", "Concours bancaires courants."),
    ("Un fonds de roulement négatif signifie que :", "des immobilisations sont financées par des ressources à court terme", "l'entreprise est très riche", "la trésorerie est forcément positive", "le capital est nul", "Situation risquée."),
    ("Le BFR (besoin de financement de l'exploitation) vient surtout :", "des stocks et des crédits accordés aux clients", "du capital", "des immobilisations", "des emprunts", "Décalage entre encaissements et décaissements."),
    ("Réduire le délai de paiement accordé aux clients :", "diminue le BFR", "augmente le BFR", "augmente les stocks", "augmente le capital", "Encaissement plus rapide."),
    ("Le ratio de liquidité générale compare :", "l'actif circulant au passif circulant", "le capital aux réserves", "les ventes aux achats", "le résultat aux salaires", "Capacité à payer les dettes à court terme."),
  ]),
  "Le compte de résultat": _q([
    ("Le compte de résultat décrit l'activité :", "de toute l'exercice (flux)", "à une date précise", "des 10 prochaines années", "d'un seul jour", "Charges et produits de l'année."),
    ("Le chiffre d'affaires comprend :", "les ventes de marchandises, de produits et de services", "les apports en capital", "les emprunts", "les achats", "Activité commerciale."),
    ("Le résultat des activités ordinaires (RAO) =", "résultat d'exploitation + résultat financier", "résultat HAO", "chiffre d'affaires", "valeur ajoutée − salaires", "Avant opérations HAO et impôt."),
    ("Le résultat net =", "RAO + résultat HAO − impôt sur le résultat", "chiffre d'affaires − achats", "valeur ajoutée", "EBE + salaires", "Dernier solde."),
    ("La production vendue concerne :", "les entreprises industrielles et de services", "uniquement les commerçants", "les banques centrales", "l'État", "Ventes de produits fabriqués ou de services."),
    ("Une variation de stock de marchandises positive (SF > SI) :", "diminue le coût des achats consommés", "augmente les charges", "augmente les ventes", "est un produit HAO", "Une partie des achats n'a pas été vendue."),
    ("Les charges financières comprennent :", "les intérêts des emprunts", "les salaires", "le loyer", "les achats", "Coût de l'endettement."),
    ("L'impôt minimum forfaitaire (IMF) est dû :", "même en cas de perte", "seulement en cas de bénéfice", "par les salariés", "par les clients", "Minimum fiscal pour les sociétés."),
    ("La CAF (capacité d'autofinancement) sert à :", "financer les investissements et rembourser les emprunts", "payer la TVA", "augmenter le capital social", "calculer les salaires", "Ressource interne."),
    ("Une charge calculée (non décaissée) est par exemple :", "la dotation aux amortissements", "le salaire", "le loyer", "l'achat de marchandises", "Elle ne fait pas sortir d'argent."),
  ]),
  "Les comptes et la partie double": _q([
    ("Toute opération touche au moins :", "deux comptes, l'un débité, l'autre crédité", "un seul compte", "trois comptes toujours", "aucun compte", "Partie double."),
    ("L'augmentation d'un compte d'actif s'inscrit :", "au débit", "au crédit", "dans les deux colonnes", "nulle part", "Emplois au débit."),
    ("L'augmentation d'un compte de passif s'inscrit :", "au crédit", "au débit", "au solde", "dans la balance seulement", "Ressources au crédit."),
    ("Achat de marchandises à crédit : on crédite :", "401 Fournisseurs", "601 Achats", "571 Caisse", "701 Ventes", "La dette envers le fournisseur augmente."),
    ("Achat de marchandises à crédit : on débite :", "601 Achats de marchandises", "401 Fournisseurs", "521 Banque", "411 Clients", "La charge augmente."),
    ("Un client règle sa dette par chèque remis en banque : on crédite :", "411 Clients", "521 Banque", "701 Ventes", "401 Fournisseurs", "La créance diminue."),
    ("Paiement du loyer en espèces : on débite :", "622 Locations", "571 Caisse", "401 Fournisseurs", "101 Capital", "Charge de location."),
    ("Paiement du loyer en espèces : on crédite :", "571 Caisse", "622 Locations", "521 Banque", "411 Clients", "La caisse diminue."),
    ("Achat d'un véhicule payé par chèque : on débite :", "245 Matériel de transport", "601 Achats", "401 Fournisseurs", "571 Caisse", "Immobilisation."),
    ("Le solde d'un compte est :", "la différence entre le total débit et le total crédit", "la somme des débits", "le premier montant inscrit", "toujours nul", "Débiteur ou créditeur."),
    ("Le compte « 4011 Fournisseurs » a normalement un solde :", "créditeur", "débiteur", "nul", "négatif", "C'est une dette."),
    ("Le compte « 4111 Clients » a normalement un solde :", "débiteur", "créditeur", "nul", "variable chaque jour sans règle", "C'est une créance."),
  ]),
  "Journal, grand livre et balance": _q([
    ("Chaque page du journal se termine par :", "les totaux à reporter sur la page suivante", "le bilan", "la signature du client", "le résultat de l'année", "Reports de page."),
    ("Le grand livre présente les opérations :", "compte par compte", "jour par jour seulement", "par client uniquement", "par facture", "Report des écritures du journal."),
    ("Une écriture de journal comporte notamment :", "la date, les comptes, le libellé et les montants", "seulement le montant", "le nom du comptable uniquement", "le solde de la banque", "Avec la pièce justificative."),
    ("La balance est équilibrée si :", "total des débits = total des crédits", "tous les soldes sont nuls", "il y a un bénéfice", "la caisse est positive", "Contrôle arithmétique."),
    ("Une erreur de compte (bon montant, mauvais compte de même sens) :", "n'est pas détectée par la balance", "déséquilibre la balance", "est impossible", "annule le bilan", "Limite du contrôle."),
    ("Le libellé d'une écriture sert à :", "expliquer la nature de l'opération", "calculer la TVA", "fixer le prix", "équilibrer la balance", "Ex. : « Facture n° 25, client Diop »."),
    ("Le brouillard est :", "un registre provisoire avant l'enregistrement définitif", "le grand livre", "le bilan", "une facture", "Livre de premier jet."),
    ("Les journaux auxiliaires (achats, ventes, caisse, banque) servent à :", "répartir le travail par type d'opérations", "remplacer le bilan", "calculer l'impôt", "payer les salaires", "Centralisés ensuite."),
    ("La durée légale de conservation des documents comptables est souvent de :", "10 ans", "1 an", "3 mois", "50 ans", "Obligation de conservation."),
    ("Une erreur se corrige dans le journal par :", "une écriture de contre-passation ou de rectification", "un effacement au correcteur", "une rature", "une page arrachée", "Pas de rature : le journal est probant."),
  ]),
  "Les amortissements": _q([
    ("L'amortissement répartit le coût d'une immobilisation :", "sur sa durée d'utilisation", "sur un seul mois", "sur la vie du propriétaire", "sur 100 ans", "Constat de la dépréciation."),
    ("Les terrains ne s'amortissent pas en général car :", "ils ne se déprécient pas par l'usage", "ils sont gratuits", "ils sont des stocks", "ils sont loués", "Pas d'usure."),
    ("L'écriture de dotation : on débite :", "681 Dotations aux amortissements", "28 Amortissements", "521 Banque", "245 Matériel", "Charge de l'exercice."),
    ("L'écriture de dotation : on crédite :", "28 Amortissements (du bien)", "681 Dotations", "571 Caisse", "401 Fournisseurs", "Le cumul des amortissements augmente."),
    ("La base amortissable est en général :", "le coût d'acquisition (hors TVA récupérable)", "le prix de revente", "la valeur du marché", "le capital", "Prix d'achat + frais accessoires."),
    ("Le taux linéaire pour une durée de 4 ans est :", "25 %", "40 %", "4 %", "20 %", "100 / 4."),
    ("En amortissement dégressif, les annuités sont :", "plus fortes au début, puis décroissantes", "constantes", "croissantes", "nulles la première année", "Taux appliqué à la VNC."),
    ("Le coefficient dégressif pour une durée de 5 ou 6 ans est :", "2", "1,5", "2,5", "3", "1,5 pour 3-4 ans ; 2 pour 5-6 ans ; 2,5 au-delà."),
    ("Un tableau d'amortissement comporte :", "base, annuité, cumul et VNC pour chaque année", "le chiffre d'affaires", "les salaires", "le prix de vente", "Plan d'amortissement."),
    ("Un bien totalement amorti mais encore utilisé :", "reste à l'actif avec une VNC nulle", "est supprimé du bilan", "est réévalué automatiquement", "devient une charge", "Jusqu'à sa sortie."),
  ]),
}

QCM_G_X3 = {
  "g-eco": {
    "Les agrégats : PIB, croissance, valeur ajoutée": ECO_TXT["Les agrégats : PIB, croissance, valeur ajoutée"] + eco_va + eco_cr + eco_reel + eco_ph,
    "Les secteurs d'activité et les entreprises": ECO_TXT["Les secteurs d'activité et les entreprises"],
    "Le marché, les prix et l'inflation": ECO_TXT["Le marché, les prix et l'inflation"] + eco_inf,
    "La monnaie et la banque centrale": ECO_TXT["La monnaie et la banque centrale"],
    "L'emploi et le chômage": ECO_TXT["L'emploi et le chômage"] + eco_ch,
    "L'État : impôts et politique budgétaire": ECO_TXT["L'État : impôts et politique budgétaire"] + eco_mu,
    "Le commerce extérieur": ECO_TXT["Le commerce extérieur"] + eco_cv + eco_sl,
  },
  "g-compta": {
    "Le cadre comptable : SYSCOHADA": CPT_TXT["Le cadre comptable : SYSCOHADA"],
    "Le bilan": CPT_TXT["Le bilan"] + cpt_cp + cpt_fr,
    "Le compte de résultat": CPT_TXT["Le compte de résultat"] + cpt_res + cpt_mc + cpt_rm,
    "Les comptes et la partie double": CPT_TXT["Les comptes et la partie double"] + cpt_tva + cpt_td,
    "Journal, grand livre et balance": CPT_TXT["Journal, grand livre et balance"] + cpt_cs,
    "Les amortissements": CPT_TXT["Les amortissements"] + cpt_al + cpt_vnc + cpt_pro + cpt_dg + cpt_ces,
  },
}
