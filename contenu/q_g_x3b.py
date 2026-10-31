# QCM de série G, volume ×3 (suite) : nouveaux calculs d'économie et de comptabilité, et questions de cours.
from q_tle_plus import _q
from q_g_x3 import calc, f, nb, pc

v = lambda x: str(x).replace(".", ",")

# ---------- Économie
eco = {}
eco["agr"] = calc(
    [(f"Le PIB réel passe de {nb(a)} à {nb(b)} milliards F en un an et la population augmente de {p} %. La croissance du PIB par habitant est d'environ :",
      pc(round((b - a) / a * 100 - p, 1)), pc(round((b - a) / a * 100 + p, 1)), pc(round((b - a) / a * 100, 1)), pc(p),
      "Croissance par habitant ≈ croissance du PIB − croissance de la population.") for a, b, p in [(10000, 10600, 3), (8000, 8400, 2.5), (15000, 16200, 2.8), (6000, 6300, 2)]]
    + [(f"Une croissance de {g} % par an pendant 2 ans donne une hausse totale de :", pc(round(((1 + g / 100) ** 2 - 1) * 100, 2)), pc(2 * g), pc(g), pc(g * g),
        f"(1 + {v(g / 100)})² − 1 : les hausses se multiplient, elles ne s'additionnent pas.") for g in [10, 5, 20, 8]]
    + [(f"Un pays produit {p} milliards F de biens, avec {ci} milliards F de consommations intermédiaires et {imp} milliards F d'impôts sur les produits. PIB :",
        f"{nb(p - ci + imp)} milliards F", f"{nb(p - ci)} milliards F", f"{nb(p + imp)} milliards F", f"{nb(p + ci + imp)} milliards F",
        "PIB = somme des valeurs ajoutées + impôts sur les produits − subventions.") for p, ci, imp in [(20000, 9000, 1500), (12000, 5000, 800), (30000, 14000, 2500)]]
    + [(f"Indice du PIB en volume : {i0} en 2020 (base 100) et {i1} en 2024. Hausse sur la période :", pc(i1 - 100), pc(i1), pc((i1 - 100) / 4), pc(i1 / 100),
        "Indice − 100 donne directement la variation en % depuis la base.") for i0, i1 in [(100, 118), (100, 125), (100, 109), (100, 132)]]
)
eco["ent"] = calc(
    [(f"Une usine produit {q} unités avec {h} heures de travail. Productivité horaire :", f"{v(round(q / h, 1))} unités/h", f"{nb(q * h)} unités/h", f"{v(round(h / q, 3))} unités/h", f"{nb(q + h)} unités/h",
      "Production / nombre d'heures.") for q, h in [(4800, 160), (9000, 300), (2500, 125), (7200, 240)]]
    + [(f"La productivité passe de {a} à {b} unités par ouvrier. Gain de productivité :", pc(round((b - a) / a * 100, 1)), pc(b - a), pc(round((b - a) / b * 100, 1)), pc(round(b / a * 100, 1)),
        "(nouvelle − ancienne) / ancienne × 100.") for a, b in [(40, 46), (25, 30), (80, 84), (50, 65)]]
    + [(f"Coûts fixes {f(cf)}, coût variable unitaire {f(cv)}, prix de vente {f(pv)}. Seuil de rentabilité en quantité :", f"{nb(cf / (pv - cv))} unités", f"{nb(cf / pv)} unités", f"{nb(cf / cv)} unités", f"{nb(cf * (pv - cv))} unités",
        "Seuil = coûts fixes / marge unitaire (prix − coût variable).") for cf, cv, pv in [(600000, 2000, 5000), (1200000, 1500, 3500), (450000, 700, 1600), (2000000, 4000, 9000)]]
    + [(f"Une entreprise réalise {ca} M F de chiffre d'affaires sur un marché total de {m} M F. Sa part de marché est :", pc(round(ca / m * 100, 1)), pc(round(m / ca, 1)), pc(round(ca / (m - ca) * 100, 1)), pc(ca),
        "Ventes de l'entreprise / ventes totales × 100.") for ca, m in [(120, 800), (45, 300), (250, 1000), (18, 240)]]
)
eco["prix"] = calc(
    [(f"Le prix passe de {f(a)} à {f(b)} et la quantité demandée de {qa} à {qb}. Élasticité-prix de la demande :", v(round(((qb - qa) / qa) / ((b - a) / a), 2)), v(round(((b - a) / a) / ((qb - qa) / qa), 2)), v(round(abs((qb - qa) / qa) / ((b - a) / a), 2)) if (qb - qa) < 0 else "1", "0",
      "Variation relative de la quantité / variation relative du prix (négative : la demande baisse quand le prix monte).") for a, b, qa, qb in [(1000, 1100, 500, 450), (200, 250, 1000, 900), (500, 600, 200, 140), (400, 440, 800, 780)]]
    + [(f"Un salaire passe de {f(s0)} à {f(s1)} pendant que les prix augmentent de {i} %. Le pouvoir d'achat :", ("augmente" if s1 / s0 > 1 + i / 100 else "baisse") + f" d'environ {pc(round(abs(s1 / s0 / (1 + i / 100) - 1) * 100, 1))}",
        ("baisse" if s1 / s0 > 1 + i / 100 else "augmente") + f" d'environ {pc(round(abs(s1 / s0 / (1 + i / 100) - 1) * 100, 1))}", "ne change pas", f"augmente de {pc(round((s1 - s0) / s0 * 100, 1))}",
        "Pouvoir d'achat = salaire / indice des prix.") for s0, s1, i in [(100000, 105000, 2), (200000, 204000, 4), (150000, 162000, 3), (80000, 82000, 5)]]
    + [(f"Sur un marché, demande D = {a} − {b}p et offre O = {c} + {d}p (p en centaines de F). Prix d'équilibre :", f"{v((a - c) / (b + d))} (soit {nb((a - c) / (b + d) * 100)} F)", f"{v((a + c) / (b + d))}", f"{v((a - c) / (b - d)) if b != d else '0'}", f"{v(a / b)}",
        "À l'équilibre, D = O : on résout l'équation.") for a, b, c, d in [(100, 3, 20, 2), (200, 4, 50, 1), (90, 2, 30, 4)]]
)
eco["mon"] = calc(
    [(f"Taux de change fixe : 1 euro = 655,957 F CFA. {e} euros valent environ :", f(e * 655.957), f(e * 100), f(e / 655.957 * 1000), f(e * 6559.57),
      "Parité fixe du franc CFA avec l'euro.") for e in [50, 200, 1000, 15]]
    + [(f"{f(x)} correspondent à environ (1 € = 655,957 F CFA) :", f"{v(round(x / 655.957, 2))} €", f"{v(round(x * 655.957))} €", f"{v(round(x / 100))} €", f"{v(round(x / 6559.57, 2))} €",
        "Montant en F CFA divisé par 655,957.") for x in [100000, 655957, 32800]]
    + [(f"Un emprunt de {f(c)} à {t} % par an pendant {n} an(s), intérêts simples : intérêts payés :", f(c * t * n / 100), f(c * t / 100), f(c * (1 + t / 100) ** n - c), f(c + c * t * n / 100),
        "I = C × t × n / 100.") for c, t, n in [(500000, 8, 2), (1000000, 10, 3), (300000, 12, 1)]]
    + [(f"Un dépôt de {f(d)} dans une banque, avec un taux de réserve obligatoire de {r} % : la banque peut prêter au maximum (premier tour) :", f(d * (1 - r / 100)), f(d * r / 100), f(d), f(d / (r / 100)),
        "Elle garde la réserve obligatoire et peut prêter le reste.") for d, r in [(1000000, 10), (500000, 5), (2000000, 3)]]
)
eco["emp"] = calc(
    [(f"Population de {p} millions, dont {a} millions d'actifs. Taux d'activité :", pc(round(a / p * 100, 1)), pc(round(p / a * 100, 1)), pc(round((p - a) / p * 100, 1)), pc(a),
      "Actifs / population (en âge de travailler) × 100.") for p, a in [(10, 4), (18, 6.3), (12, 5.4), (8, 3.2)]]
    + [(f"Taux de chômage {t} % sur une population active de {nb(pa)} personnes. Nombre de chômeurs :", nb(pa * t / 100), nb(pa * (100 - t) / 100), nb(pa / t), nb(t * 1000),
        "Population active × taux de chômage.") for t, pa in [(12, 500000), (20, 250000), (8, 1500000), (15, 60000)]]
    + [(f"Le nombre de chômeurs passe de {nb(a)} à {nb(b)}. Variation :", pc(round((b - a) / a * 100, 1)), pc(round((a - b) / a * 100, 1)), pc(round((b - a) / b * 100, 1)), pc(b - a),
        "Taux de variation = (arrivée − départ) / départ × 100.") for a, b in [(40000, 36000), (25000, 30000), (80000, 72000)]]
)
eco["etat"] = calc(
    [(f"Recettes de l'État {nb(r)} milliards F, dépenses {nb(d)} milliards F, PIB {nb(p)} milliards F. Déficit en % du PIB :", pc(round((d - r) / p * 100, 1)), pc(round((d - r) / r * 100, 1)), pc(round(d / p * 100, 1)), pc(round(r / p * 100, 1)),
      "(Dépenses − recettes) / PIB × 100. Critère UEMOA : 3 % au plus.") for r, d, p in [(4000, 4600, 20000), (3500, 4200, 18000), (5000, 5450, 22000)]]
    + [(f"Recettes fiscales {nb(r)} milliards F pour un PIB de {nb(p)} milliards F. Pression fiscale :", pc(round(r / p * 100, 1)), pc(round(p / r, 1)), pc(round((p - r) / p * 100, 1)), pc(r / 100),
        "Recettes fiscales / PIB × 100 (critère UEMOA : au moins 20 %).") for r, p in [(3600, 20000), (2700, 18000), (4400, 22000)]]
    + [(f"Dette publique {nb(dt)} milliards F, PIB {nb(p)} milliards F. Taux d'endettement :", pc(round(dt / p * 100, 1)), pc(round(p / dt * 100, 1)), pc(round((p - dt) / p * 100, 1)), pc(dt / 100),
        "Dette / PIB × 100 (plafond UEMOA : 70 %).") for dt, p in [(14000, 20000), (12600, 18000), (9000, 22000)]]
    + [(f"Un revenu imposable de {f(r)} avec un barème : 0 % jusqu'à 630 000 F, puis {t} % au-delà. Impôt :", f((r - 630000) * t / 100), f(r * t / 100), f(630000 * t / 100), f(r - 630000),
        "Seule la part au-dessus du seuil est taxée (impôt par tranches simplifié).") for r, t in [(1630000, 20), (2630000, 20), (1130000, 20)]]
)
eco["ext"] = calc(
    [(f"Indice des prix à l'exportation {x}, indice des prix à l'importation {m}. Termes de l'échange :", v(round(x / m * 100, 1)), v(round(m / x * 100, 1)), v(x - m), v(x + m),
      "Indice des prix à l'export / indice des prix à l'import × 100. Supérieur à 100 : amélioration.") for x, m in [(110, 100), (95, 105), (120, 115), (90, 90)]]
    + [(f"Un pays exporte {nb(x)} milliards F de poisson sur {nb(t)} milliards F d'exportations totales. Part du poisson :", pc(round(x / t * 100, 1)), pc(round(t / x, 1)), pc(round((t - x) / t * 100, 1)), pc(x / 10),
        "Part = valeur du produit / total × 100.") for x, t in [(300, 1500), (450, 1800), (120, 2400)]]
    + [(f"Un produit importé coûte {f(p)} avec un droit de douane de {d} %. Prix après douane (hors TVA) :", f(p * (1 + d / 100)), f(p * d / 100), f(p * (1 - d / 100)), f(p + d),
        "Prix CAF × (1 + taux du droit de douane).") for p, d in [(100000, 20), (250000, 10), (40000, 35), (1000000, 5)]]
)

ECO_TXT2 = {
  "Les agrégats : PIB, croissance, valeur ajoutée": _q([
    ("Le PIB vert ou « ajusté » cherche à tenir compte :", "de l'épuisement des ressources et de la pollution", "du nombre d'habitants", "de l'inflation seulement", "des exportations seulement", "Limite environnementale du PIB."),
    ("La FBCF (investissement) des entreprises comprend :", "l'achat de machines, de bâtiments et de logiciels", "les salaires", "les achats de matières premières", "les impôts", "Biens durables de production."),
    ("Les cycles économiques alternent :", "expansion et récession", "inflation et dévaluation", "importations et exportations", "épargne et impôt", "Fluctuations de l'activité."),
    ("Une dépression est :", "une baisse forte et durable de la production", "une hausse rapide du PIB", "une inflation faible", "une hausse des exportations", "Plus grave qu'une récession."),
    ("Le revenu disponible des ménages =", "revenus primaires + prestations sociales − impôts et cotisations", "salaires seulement", "PIB / population", "consommation + épargne des entreprises", "Ce qu'ils peuvent consommer ou épargner."),
    ("Le taux d'épargne des ménages =", "épargne / revenu disponible × 100", "consommation / revenu × 100", "revenu / épargne", "investissement / PIB", "Part du revenu non consommée."),
    ("La propension moyenne à consommer est :", "consommation / revenu", "épargne / revenu", "revenu / consommation", "investissement / revenu", "Ex. : 0,8 = 80 % du revenu consommé."),
    ("Le progrès technique favorise surtout :", "la croissance intensive par la productivité", "la baisse de la population", "le chômage frictionnel uniquement", "l'inflation importée", "Produire plus avec autant de facteurs."),
    ("Le capital humain désigne :", "les connaissances et compétences des travailleurs", "l'argent en banque", "les machines", "les bâtiments", "Éducation, santé, formation."),
    ("Les infrastructures (routes, ports, énergie) favorisent la croissance car elles :", "réduisent les coûts de production et de transport", "augmentent les impôts", "réduisent la population", "créent l'inflation", "Externalités positives."),
  ]),
  "Les secteurs d'activité et les entreprises": _q([
    ("Une SA doit avoir un capital minimum, dans l'espace OHADA, de :", "10 millions F CFA", "100 000 F CFA", "1 milliard F CFA", "aucun capital", "Acte uniforme sur les sociétés commerciales."),
    ("Le capital minimum d'une SARL dans l'OHADA est fixé :", "librement par les statuts (après la réforme de 2014)", "à 1 milliard F", "à 10 millions F obligatoirement", "par la BCEAO", "Souplesse pour les petites entreprises."),
    ("Une entreprise privée cherche avant tout :", "le profit", "le service public gratuit", "l'émission de monnaie", "la collecte de l'impôt", "But lucratif."),
    ("Une association loi 1901 (ou ONG) est à but :", "non lucratif", "lucratif", "fiscal", "monétaire", "Elle ne partage pas de bénéfices."),
    ("La concentration horizontale réunit des entreprises :", "qui font la même activité", "qui sont fournisseur et client", "de secteurs sans lien", "publiques uniquement", "Ex. : deux cimenteries."),
    ("La concentration verticale réunit des entreprises :", "d'étapes successives d'une même filière", "concurrentes", "de pays différents seulement", "toutes publiques", "Ex. : producteur d'arachide et huilerie."),
    ("Une filiale est :", "une société contrôlée par une autre (la société mère)", "un service de l'État", "une banque centrale", "une coopérative", "Plus de 50 % du capital."),
    ("Les charges fixes d'une entreprise :", "ne varient pas avec la quantité produite à court terme", "augmentent avec chaque unité", "sont toujours nulles", "dépendent des ventes du jour", "Loyer, assurance…"),
    ("L'innovation de produit consiste à :", "mettre sur le marché un produit nouveau ou amélioré", "baisser les salaires", "augmenter les impôts", "fermer une usine", "Schumpeter : destruction créatrice."),
    ("La responsabilité sociétale des entreprises (RSE) concerne :", "l'impact social et environnemental de l'entreprise", "uniquement le profit", "la création monétaire", "le vote des lois", "Développement durable en entreprise."),
  ]),
  "Le marché, les prix et l'inflation": _q([
    ("Un marché de concurrence monopolistique se caractérise par :", "de nombreux vendeurs de produits différenciés", "un seul vendeur", "deux vendeurs", "un seul acheteur", "Ex. : restaurants, marques de vêtements."),
    ("Un monopsone est un marché avec :", "un seul acheteur", "un seul vendeur", "deux vendeurs", "aucun acheteur", "Ex. : un seul acheteur de coton dans une zone."),
    ("La transparence du marché signifie que :", "tous connaissent les prix et la qualité des produits", "les prix sont secrets", "les produits sont invisibles", "l'État fixe tout", "Hypothèse de la concurrence pure."),
    ("Un prix plancher (minimum) fixé par l'État vise à :", "protéger les producteurs", "protéger les consommateurs", "supprimer le marché", "augmenter les importations", "Ex. : prix minimum de l'arachide au producteur."),
    ("Le contrôle des prix de denrées (riz, huile, sucre) au Sénégal vise :", "à protéger le pouvoir d'achat", "à augmenter les profits", "à supprimer la concurrence", "à dévaluer le franc CFA", "Prix homologués."),
    ("La désinflation est :", "un ralentissement de la hausse des prix", "une baisse générale des prix", "une hausse des prix", "un excès de monnaie", "Les prix montent moins vite."),
    ("L'inflation pénalise surtout :", "les créanciers et les revenus fixes", "les emprunteurs à taux fixe", "les débiteurs", "les exportateurs de pétrole", "La valeur réelle des sommes dues baisse."),
    ("L'IPC (indice des prix à la consommation) au Sénégal est calculé par :", "l'ANSD", "la BCEAO", "l'Assemblée nationale", "l'UEMOA seule", "Agence nationale de la statistique et de la démographie."),
    ("Un bien inférieur est un bien dont la demande :", "baisse quand le revenu augmente", "augmente avec le revenu", "ne dépend pas du revenu", "augmente avec son prix", "On le remplace par mieux quand on s'enrichit."),
    ("Une externalité négative est par exemple :", "la pollution d'une usine qui gêne les riverains", "une route construite par l'État", "une formation gratuite", "une vaccination", "Coût imposé à autrui sans compensation."),
  ]),
  "La monnaie et la banque centrale": _q([
    ("La masse monétaire M2 comprend :", "M1 et les dépôts à terme ou d'épargne", "uniquement les pièces", "les réserves d'or seulement", "les actions en bourse", "Agrégat plus large que M1."),
    ("L'inflation peut venir d'une création monétaire :", "plus rapide que la production", "plus lente que la production", "nulle", "égale aux exportations", "Théorie quantitative."),
    ("Le marché monétaire est le marché :", "de l'argent à court terme entre banques", "des actions à long terme", "des produits agricoles", "du travail", "Refinancement des banques."),
    ("La bourse régionale de l'UEMOA (BRVM) est installée à :", "Abidjan", "Dakar", "Bamako", "Lomé", "Bourse régionale des valeurs mobilières."),
    ("Une action est :", "un titre de propriété d'une part d'une société", "un titre de dette", "un billet de banque", "une facture", "Elle donne droit à des dividendes."),
    ("Une obligation est :", "un titre de créance (prêt à une entreprise ou à l'État)", "une part de capital", "une pièce de monnaie", "un impôt", "Rémunérée par des intérêts."),
    ("La bancarisation au Sénégal a progressé grâce :", "à la monnaie mobile et à la microfinance", "à la fermeture des banques", "à la suppression des comptes", "au troc", "Inclusion financière."),
    ("Le taux d'usure est :", "le taux d'intérêt maximal autorisé", "le taux d'inflation", "le taux de change", "le taux directeur", "Protection des emprunteurs."),
    ("La compensation bancaire permet :", "de régler entre banques les chèques et virements de leurs clients", "d'imprimer des billets", "de fixer le taux de change", "de voter le budget", "Chambre de compensation."),
    ("Le franc CFA est garanti en convertibilité par :", "le Trésor français (accords de coopération)", "la Banque mondiale", "le FMI", "la CEDEAO", "Réforme de 2019 vers l'« eco » en discussion."),
  ]),
  "L'emploi et le chômage": _q([
    ("Le taux de chômage des jeunes est souvent :", "plus élevé que celui de l'ensemble des actifs", "nul", "plus faible que la moyenne", "égal à 100 %", "Difficultés d'insertion."),
    ("Le contrat à durée indéterminée (CDI) :", "n'a pas de date de fin prévue", "dure 3 mois au plus", "est réservé aux fonctionnaires", "est un stage", "Emploi stable."),
    ("La flexibilité du travail permet aux entreprises :", "d'adapter le volume ou les horaires de travail", "de supprimer les salaires", "de fixer les prix", "d'émettre de la monnaie", "Contrats courts, intérim, horaires."),
    ("Les cotisations sociales financent :", "la protection sociale (retraite, santé…)", "les profits", "les exportations", "la BCEAO", "Prélèvées sur les salaires."),
    ("L'IPRES au Sénégal gère :", "les retraites des salariés du privé", "la monnaie", "les douanes", "les examens", "Institution de prévoyance retraite."),
    ("La CSS au Sénégal gère notamment :", "les allocations familiales et les accidents du travail", "les impôts", "les élections", "le transport", "Caisse de sécurité sociale."),
    ("Selon Keynes, le chômage peut venir :", "d'une demande globale insuffisante", "de salaires trop bas", "d'un excès de demande", "d'une inflation trop forte", "Chômage involontaire."),
    ("Selon les néoclassiques, le chômage vient surtout :", "d'un coût du travail trop élevé ou de rigidités", "d'un manque de demande", "de la création monétaire", "des exportations", "Le marché du travail ne s'ajuste pas."),
    ("Un emploi décent selon l'OIT suppose :", "un revenu juste, la sécurité et la protection sociale", "un salaire nul", "aucun contrat", "des horaires illimités", "Agenda du travail décent."),
    ("Le télétravail est :", "le travail effectué à distance grâce au numérique", "le travail à la télévision", "le chômage technique", "un stage obligatoire", "Il s'est développé après 2020."),
  ]),
  "L'État : impôts et politique budgétaire": _q([
    ("Un impôt proportionnel :", "applique le même taux quel que soit le revenu", "a un taux qui augmente avec le revenu", "est payé seulement par les riches", "n'existe pas", "Ex. : TVA."),
    ("La TVA est dite régressive par rapport au revenu car :", "elle pèse plus lourd dans le budget des pauvres", "son taux baisse avec le temps", "elle est remboursée aux riches", "elle ne touche que les entreprises", "Les pauvres consomment une plus grande part de leur revenu."),
    ("Le budget de l'État comprend des dépenses de fonctionnement comme :", "les salaires des fonctionnaires", "la construction d'une autoroute", "l'achat d'un port", "un barrage", "Dépenses courantes."),
    ("Une politique de relance par la demande vise surtout à :", "réduire le chômage en soutenant l'activité", "réduire l'inflation à tout prix", "augmenter le déficit commercial volontairement", "supprimer l'État", "Politique keynésienne."),
    ("L'effet d'éviction désigne :", "la baisse de l'investissement privé due à l'endettement de l'État", "l'expulsion de locataires", "la hausse des exportations", "la baisse des impôts", "L'État absorbe l'épargne disponible."),
    ("Les recettes non fiscales de l'État comprennent :", "les dividendes des entreprises publiques et les redevances", "la TVA", "l'impôt sur le revenu", "les droits de douane", "Revenus du domaine de l'État."),
    ("La décentralisation transfère des compétences :", "de l'État aux collectivités territoriales", "des communes à l'État", "de la BCEAO aux banques", "des entreprises à l'État", "Communes, départements."),
    ("Un emprunt obligataire de l'État permet :", "de financer un déficit en empruntant auprès d'épargnants", "d'imprimer des billets", "de supprimer l'impôt", "d'augmenter les exportations", "Ex. : APE (appel public à l'épargne)."),
    ("L'aide publique au développement est :", "un financement venant de pays riches ou d'institutions internationales", "un impôt local", "une dette des ménages", "un salaire", "Dons et prêts à taux faibles."),
    ("Le FMI intervient surtout pour :", "aider les pays en difficulté de balance des paiements", "fixer le prix de l'arachide", "organiser la CAN", "gérer les écoles", "Fonds monétaire international."),
  ]),
  "Le commerce extérieur": _q([
    ("Le Sénégal importe beaucoup de riz parce que :", "la production locale ne couvre pas la consommation", "il n'en consomme pas", "le riz est interdit au Sénégal", "il en exporte trop", "Dépendance alimentaire."),
    ("Une politique d'import-substitution vise à :", "produire localement ce qui était importé", "importer davantage", "supprimer les exportations", "fermer les usines", "Développement industriel protégé."),
    ("La promotion des exportations vise à :", "vendre davantage à l'étranger", "importer davantage", "réduire la production", "augmenter les droits de douane intérieurs", "Stratégie d'ouverture."),
    ("L'AGOA permet à des pays africains :", "d'exporter certains produits aux États-Unis sans droits de douane", "d'importer gratuitement du pétrole", "d'utiliser le dollar", "d'entrer dans l'Union européenne", "African Growth and Opportunity Act."),
    ("Un investissement direct étranger (IDE) est :", "une prise de contrôle ou la création d'une entreprise par un investisseur étranger", "un prêt de la BCEAO", "une importation de riz", "un don", "Implantation durable."),
    ("La « fuite des capitaux » désigne :", "la sortie massive de capitaux d'un pays", "la construction d'usines", "l'entrée d'IDE", "la hausse de l'épargne locale", "Elle affaiblit l'investissement."),
    ("Une appréciation de la monnaie rend les exportations :", "plus chères pour les étrangers", "moins chères", "gratuites", "impossibles", "Perte de compétitivité-prix."),
    ("L'Organisation mondiale du commerce a remplacé en 1995 :", "le GATT", "la SDN", "le FMI", "l'UEMOA", "Accord général sur les tarifs douaniers et le commerce."),
    ("Le commerce intra-africain représente :", "une faible part du commerce total des pays africains (environ 15 %)", "plus de 90 %", "0 %", "la totalité", "D'où la ZLECAf."),
    ("La compétitivité hors prix dépend :", "de la qualité, de l'innovation et du service", "uniquement du prix", "du taux de change seul", "des salaires seuls", "Image de marque, délais…"),
  ]),
}

# ---------- Comptabilité
cpt = {}
cpt["bil"] = calc(
    [(f"Immobilisations {a} M, stocks {s} M, créances {c} M, banque {b} M. Total de l'actif :", f"{a + s + c + b} M F", f"{a + s + c} M F", f"{a} M F", f"{s + c + b} M F", "On additionne tous les emplois.") for a, s, c, b in [(30, 8, 6, 4), (55, 12, 9, 2), (18, 5, 7, 3), (42, 10, 11, 5), (75, 20, 14, 6)]]
    + [(f"Capitaux propres {cp} M, dettes financières {d} M, total du bilan {t} M. Ratio d'autonomie financière (CP / dettes financières) :", v(round(cp / d, 2)), v(round(d / cp, 2)), v(round(cp / t, 2)), v(round(t / d, 2)),
        "Supérieur à 1 : l'entreprise est plus financée par ses propriétaires que par ses prêteurs.") for cp, d, t in [(24, 12, 50), (15, 20, 45), (40, 10, 70), (30, 25, 80), (18, 6, 35)]]
    + [(f"Actif circulant {ac} M, passif circulant {p} M. Ratio de liquidité générale :", v(round(ac / p, 2)), v(round(p / ac, 2)), f"{ac - p}", v(round((ac + p) / p, 2)),
        "AC / PC ; supérieur à 1 : les actifs à court terme couvrent les dettes à court terme.") for ac, p in [(18, 12), (9, 10), (30, 15), (14, 8), (22, 20)]]
    + [(f"Stocks {s} M, créances clients {c} M, dettes fournisseurs {fo} M. BFR d'exploitation :", f"{s + c - fo} M F", f"{s + c + fo} M F", f"{s - c + fo} M F", f"{c - fo} M F",
        "BFR = stocks + créances − dettes d'exploitation.") for s, c, fo in [(10, 8, 6), (4, 9, 7), (20, 15, 25), (12, 6, 5), (7, 13, 9)]]
)
cpt["res"] = calc(
    [(f"Chiffre d'affaires {ca} M, consommations de l'exercice {ci} M. Valeur ajoutée :", f"{ca - ci} M F", f"{ca + ci} M F", f"{ci} M F", f"{ca} M F", "VA = production de l'exercice − consommations en provenance des tiers.") for ca, ci in [(60, 35), (25, 17), (120, 80), (48, 30), (90, 52)]]
    + [(f"Valeur ajoutée {va} M, charges de personnel {cp} M, impôts et taxes {it} M. EBE :", f"{va - cp - it} M F", f"{va - cp} M F", f"{va + cp + it} M F", f"{cp + it} M F", "EBE = VA − charges de personnel − impôts et taxes (+ subventions).") for va, cp, it in [(25, 12, 1), (40, 25, 3), (18, 9, 2), (60, 33, 4), (12, 7, 1)]]
    + [(f"EBE {e} M, dotations aux amortissements {d} M. Résultat d'exploitation (simplifié) :", f"{e - d} M F", f"{e + d} M F", f"{d} M F", f"{e} M F", "On retire les charges calculées.") for e, d in [(12, 4), (20, 7), (9, 6), (15, 5), (30, 12)]]
    + [(f"Résultat net {r} M, dotations aux amortissements {d} M (sans autre charge calculée). CAF :", f"{r + d} M F", f"{r - d} M F", f"{r} M F", f"{d} M F", "CAF = résultat net + charges calculées − produits calculés.") for r, d in [(5, 3), (8, 6), (2, 4), (11, 5), (3, 7)]]
    + [(f"Résultat avant impôt {r} M F, impôt sur les sociétés {t} %. Résultat net :", f"{v(round(r * (1 - t / 100), 2))} M F", f"{v(round(r * t / 100, 2))} M F", f"{r} M F", f"{v(round(r * (1 + t / 100), 2))} M F", "Résultat net = résultat avant impôt − impôt.") for r, t in [(10, 30), (4, 30), (25, 30), (16, 30)]]
)
cpt["ops"] = calc(
    [(f"Facture : prix brut {f(b)}, remise {r} %, TVA 18 %. Net à payer TTC :", f(b * (1 - r / 100) * 1.18), f(b * 1.18), f(b * (1 - r / 100)), f(b * (1 - r / 100) * 0.18), "Brut − remise = net commercial HT ; on ajoute ensuite la TVA.") for b, r in [(500000, 10), (800000, 5), (200000, 20), (1500000, 8), (350000, 15), (90000, 10)]]
    + [(f"Un prix TTC de {f(t)} (TVA 18 %). Montant de la TVA :", f(t - t / 1.18), f(t * 0.18), f(t / 1.18), f(t * 0.82), "TVA = TTC − TTC / 1,18.") for t in [118000, 590000, 236000, 47200, 1180000, 354000]]
    + [(f"Salaire brut {f(b)} ; retenues salariales {r} %. Salaire net :", f(b * (1 - r / 100)), f(b * r / 100), f(b * (1 + r / 100)), f(b - r), "Net = brut − retenues (cotisations et impôt).") for b, r in [(250000, 12), (400000, 15), (180000, 10), (600000, 18), (120000, 8)]]
    + [(f"Stock : 100 unités à {f(p1)} puis 300 unités à {f(p2)}. Coût unitaire moyen pondéré (CUMP) :", f((100 * p1 + 300 * p2) / 400), f((p1 + p2) / 2), f(p2), f(p1), "CUMP = valeur totale / quantité totale.") for p1, p2 in [(1000, 1200), (500, 700), (2000, 1600), (800, 1000), (3000, 2600)]]
)
cpt["jgl"] = calc(
    [(f"Compte 411 Clients : débits {f(d)}, crédits {f(c)}. Son solde est :", ("débiteur de " + f(d - c)) if d > c else ("créditeur de " + f(c - d)), ("créditeur de " + f(d - c)) if d > c else ("débiteur de " + f(c - d)), f(d + c), "nul",
      "Solde = total le plus fort − total le plus faible, du côté du plus fort.") for d, c in [(1200000, 900000), (300000, 450000), (2500000, 1750000), (90000, 140000)]]
    + [(f"Compte 401 Fournisseurs : débits {f(d)}, crédits {f(c)}. Il reste à payer aux fournisseurs :", f(c - d), f(c + d), f(d), f(c), "Solde créditeur = dette restante.") for d, c in [(600000, 1000000), (250000, 900000), (1100000, 1500000), (75000, 400000), (2000000, 2600000)]]
    + [(f"Total des débits de la balance : {f(t)}. Le total des crédits doit être :", f(t), f(t / 2), f(2 * t), "0 F", "Égalité des totaux (partie double).") for t in [12500000, 3400000, 870000]]
)
cpt["amo"] = calc(
    [(f"Dégressif : bien de {f(b)}, taux dégressif {t} %. Première annuité (acquis le 1er janvier) :", f(b * t / 100), f(b * t / 200), f(b * (1 - t / 100)), f(b / 5), "Annuité = VNC début × taux dégressif.") for b, t in [(5000000, 40), (2000000, 37.5), (3000000, 50), (8000000, 40)]]
    + [(f"Dégressif : bien de {f(b)}, taux {t} %. Deuxième annuité :", f(b * (1 - t / 100) * t / 100), f(b * t / 100), f(b * (1 - t / 100)), f(b * (1 - t / 100) ** 2), "On applique le taux à la VNC de début de 2e année.") for b, t in [(5000000, 40), (2000000, 37.5), (3000000, 50)]]
    + [(f"Taux linéaire de {t} % : durée d'amortissement :", f"{round(100 / t)} ans", f"{t} ans", f"{round(t / 10)} ans", f"{round(200 / t)} ans", "Durée = 100 / taux.") for t in [20, 25, 10, 12.5, 5]]
    + [(f"Bien de {f(b)} acquis le 1er septembre, linéaire à {t} %, clôture au 31 décembre. Dotation de la 1re année :", f(b * t / 100 * 4 / 12), f(b * t / 100), f(b * t / 100 * 8 / 12), f(b * t / 100 / 4), "4 mois (septembre à décembre) sur 12.") for b, t in [(1800000, 20), (6000000, 10), (900000, 25), (2400000, 20)]]
)

CPT_TXT2 = {
  "Le cadre comptable : SYSCOHADA": _q([
    ("Le SYSCOHADA s'applique dans :", "les 17 États membres de l'OHADA", "seulement au Sénégal", "l'Union européenne", "le monde entier", "Plan comptable commun."),
    ("La comptabilité générale a pour but principal :", "d'enregistrer les opérations et de présenter les états financiers", "de fixer les prix de vente", "de recruter le personnel", "de payer les impôts à la place de l'État", "Information financière fiable."),
    ("Les utilisateurs des états financiers sont notamment :", "les dirigeants, les banques, l'État et les associés", "uniquement les clients", "uniquement les salariés", "personne", "Information externe et interne."),
    ("Le principe d'importance significative permet :", "de ne pas détailler les informations sans influence sur le jugement", "de cacher les pertes", "de ne pas tenir de comptabilité", "de modifier les comptes après clôture", "Seuil de signification."),
    ("La classe 8 du SYSCOHADA enregistre :", "les autres charges et produits (dont HAO)", "les stocks", "les immobilisations", "les tiers", "Comptes des autres charges et produits."),
    ("Le compte 6031 correspond à :", "la variation des stocks de marchandises", "les ventes", "les salaires", "la banque", "SI − SF de marchandises."),
    ("Le compte 641 correspond aux :", "impôts et taxes directs", "achats", "intérêts reçus", "ventes", "Patente, contribution foncière…"),
    ("Le compte 671 correspond aux :", "intérêts des emprunts", "salaires", "ventes de produits", "loyers reçus", "Frais financiers."),
    ("Le compte 707 ou 701, 702… commence par 70 :", "ventes", "achats", "stocks", "capital", "Chiffre d'affaires."),
    ("Le compte 104 correspond au :", "compte de l'exploitant", "capital social", "fournisseur", "client", "Apports et retraits de l'entrepreneur individuel."),
  ]),
  "Le bilan": _q([
    ("Les écarts de conversion apparaissent au bilan lors :", "d'opérations en devises étrangères", "de ventes en F CFA", "de paiements en espèces", "de dons", "Variation du taux de change."),
    ("Le capital social d'une SARL figure :", "au passif, dans les capitaux propres", "à l'actif", "dans le compte de résultat", "dans les charges", "Ressource apportée par les associés."),
    ("Les réserves proviennent :", "de bénéfices non distribués", "d'emprunts", "de ventes à crédit", "de subventions d'exploitation", "Mises en réserve."),
    ("Le report à nouveau est :", "un bénéfice (ou une perte) laissé en attente d'affectation", "une dette fournisseur", "une immobilisation", "un stock", "Capitaux propres."),
    ("Un bilan d'ouverture est établi :", "au début de l'activité ou de l'exercice", "à la fin de l'activité uniquement", "chaque jour", "jamais", "Point de départ."),
    ("Un emprunt remboursable dans 6 mois figure :", "en dettes à court terme (passif circulant ou trésorerie)", "dans les capitaux propres", "à l'actif immobilisé", "dans les stocks", "Moins d'un an."),
    ("Les charges constatées d'avance sont :", "des charges payées concernant l'exercice suivant (actif)", "des dettes", "des produits", "des capitaux propres", "Régularisation."),
    ("Les provisions pour risques figurent :", "au passif", "à l'actif", "dans les stocks", "en trésorerie actif", "Dettes probables."),
    ("La trésorerie nette positive signifie :", "le fonds de roulement couvre le BFR", "l'entreprise est en faillite", "les dettes sont nulles", "le capital est négatif", "TN = FR − BFR > 0."),
    ("Augmenter le capital par apport en numéraire améliore :", "le fonds de roulement et la trésorerie", "le BFR", "les stocks", "les créances clients", "Ressource stable nouvelle."),
  ]),
  "Le compte de résultat": _q([
    ("Le résultat financier =", "produits financiers − charges financières", "ventes − achats", "VA − salaires", "résultat net − impôt", "Intérêts reçus moins intérêts payés…"),
    ("Le résultat HAO concerne les opérations :", "hors activités ordinaires (cessions, événements exceptionnels)", "courantes", "de vente de marchandises", "de paiement des salaires", "Classe 8."),
    ("La marge brute sur matières concerne :", "les entreprises industrielles", "les commerçants uniquement", "les banques", "l'État", "Production vendue − matières consommées."),
    ("Les subventions d'exploitation sont :", "des produits", "des charges", "des capitaux propres", "des dettes", "Elles augmentent l'EBE."),
    ("La participation des travailleurs est prélevée :", "sur le résultat", "sur le capital", "sur les stocks", "sur les ventes", "Partage du bénéfice."),
    ("Un rabais obtenu d'un fournisseur hors facture :", "diminue les achats", "augmente les achats", "est une vente", "est une immobilisation", "Réduction pour défaut ou retard."),
    ("Les frais de transport sur ventes sont :", "des charges (services extérieurs)", "des produits", "des immobilisations", "des capitaux propres", "Transport sur ventes."),
    ("Le seuil de rentabilité est le chiffre d'affaires pour lequel :", "le résultat est nul", "le résultat est maximal", "les charges sont nulles", "la TVA est nulle", "Ni perte ni bénéfice."),
    ("La marge sur coût variable =", "chiffre d'affaires − charges variables", "chiffre d'affaires − charges fixes", "charges fixes − charges variables", "résultat + impôt", "Elle doit couvrir les charges fixes."),
    ("Le taux de marge sur coût variable sert à :", "calculer le seuil de rentabilité", "calculer la TVA", "fixer le capital", "amortir les biens", "SR = charges fixes / taux de MCV."),
  ]),
  "Les comptes et la partie double": _q([
    ("Un apport en numéraire de l'exploitant versé en banque : on débite :", "521 Banque", "101 Capital", "601 Achats", "411 Clients", "La banque augmente."),
    ("Un apport en numéraire de l'exploitant : on crédite :", "101 Capital (ou 104 Compte de l'exploitant)", "521 Banque", "401 Fournisseurs", "701 Ventes", "Ressource propre."),
    ("Une vente de marchandises à crédit : on crédite :", "701 Ventes de marchandises", "411 Clients", "571 Caisse", "601 Achats", "Produit."),
    ("La TVA facturée sur une vente s'inscrit au crédit du compte :", "443 État, TVA facturée", "445 État, TVA récupérable", "601 Achats", "411 Clients", "Dette envers l'État."),
    ("La TVA payée sur un achat s'inscrit au débit du compte :", "445 État, TVA récupérable", "443 TVA facturée", "701 Ventes", "401 Fournisseurs", "Créance sur l'État."),
    ("Le paiement d'une facture fournisseur par chèque : on débite :", "401 Fournisseurs", "521 Banque", "601 Achats", "571 Caisse", "La dette diminue."),
    ("Un prélèvement de marchandises par l'exploitant pour son usage personnel :", "diminue les achats et le compte de l'exploitant", "est une vente", "est une immobilisation", "est un produit HAO", "Prélèvement en nature."),
    ("Une avance reçue d'un client avant livraison est :", "une dette envers le client", "une vente", "une charge", "un capital", "Compte 419."),
    ("Une avance versée à un fournisseur est :", "une créance sur le fournisseur", "un achat", "un produit", "un emprunt", "Compte 409."),
    ("Un effet à recevoir est :", "une créance matérialisée par une lettre de change", "une dette", "un stock", "une immobilisation", "Compte 412."),
  ]),
  "Journal, grand livre et balance": _q([
    ("Le journal est coté et paraphé :", "par une autorité (tribunal) pour garantir son authenticité", "par le client", "par le fournisseur", "par la banque", "Livre obligatoire."),
    ("La centralisation mensuelle consiste à :", "reporter les totaux des journaux auxiliaires au journal général", "supprimer les journaux", "établir le bilan chaque jour", "calculer l'impôt", "Système centralisateur."),
    ("Un compte soldé a :", "un solde nul (débits = crédits)", "un solde débiteur", "un solde créditeur", "plusieurs soldes", "Compte équilibré."),
    ("La balance avant inventaire est établie :", "avant les écritures de fin d'exercice", "après le bilan", "au début de l'exercice", "chaque heure", "Puis viennent les régularisations."),
    ("Les travaux d'inventaire comprennent notamment :", "les amortissements, les provisions et les variations de stocks", "les ventes du jour", "l'embauche", "l'ouverture du magasin", "Écritures de fin d'année."),
    ("Le rapprochement bancaire explique les écarts entre :", "le compte 521 de l'entreprise et le relevé de la banque", "la caisse et les stocks", "les clients et les fournisseurs", "le bilan et le compte de résultat", "Opérations non encore enregistrées par l'un ou l'autre."),
    ("Un chèque émis non encore présenté à la banque explique que :", "le solde du relevé bancaire est plus élevé que celui du compte 521", "le compte 521 est plus élevé", "le relevé est faux", "la caisse est négative", "Décalage de date."),
    ("Des frais bancaires prélevés et non encore enregistrés doivent être :", "comptabilisés dans le compte 521 (crédit) et en charges", "ignorés", "payés en espèces", "ajoutés aux ventes", "Régularisation après rapprochement."),
    ("Le grand livre général contient :", "tous les comptes utilisés par l'entreprise", "seulement les clients", "seulement la caisse", "les factures", "Document de synthèse des comptes."),
    ("La balance auxiliaire des clients donne :", "le solde de chaque client", "le total des achats", "le capital", "la TVA due", "Suivi des créances."),
  ]),
  "Les amortissements": _q([
    ("La dotation aux amortissements est une charge :", "non décaissable", "payée au fournisseur", "versée à l'État", "versée aux salariés", "Aucune sortie d'argent."),
    ("Le mode linéaire répartit le coût :", "de manière égale chaque année", "surtout la première année", "surtout la dernière année", "au hasard", "Annuités constantes."),
    ("En dégressif, la dernière année l'annuité est égale :", "à la VNC restante", "à zéro", "à la valeur d'origine", "au prix de cession", "Le bien est totalement amorti."),
    ("L'amortissement d'un bien commence :", "à sa date de mise en service", "à la date de commande", "au début de l'exercice suivant toujours", "à la date de cession", "Prorata temporis."),
    ("Les frais d'installation d'une machine :", "s'ajoutent à son coût d'acquisition et sont amortis", "sont des ventes", "ne sont jamais comptabilisés", "sont des capitaux propres", "Frais accessoires."),
    ("La sortie d'un bien cédé : on crédite le compte d'immobilisation pour :", "sa valeur d'origine", "son prix de cession", "sa VNC", "zéro", "Le bien sort du patrimoine."),
    ("Le prix de cession d'une immobilisation est enregistré :", "en produit HAO (compte 82)", "en vente de marchandises", "en capital", "en stock", "Produits des cessions d'immobilisations."),
    ("La VNC d'un bien cédé est enregistrée :", "en charge HAO (compte 81)", "en produit", "en capital", "en stock", "Valeur comptable des cessions."),
    ("L'amortissement permet aussi de :", "reconstituer des moyens pour renouveler le bien", "augmenter les impôts", "augmenter le chiffre d'affaires", "réduire le capital", "Autofinancement."),
    ("Un logiciel acheté est :", "une immobilisation incorporelle amortissable", "un stock", "une charge de personnel", "un capital", "Classe 21."),
  ]),
}

QCM_G_X3B = {
  "g-eco": {
    "Les agrégats : PIB, croissance, valeur ajoutée": ECO_TXT2["Les agrégats : PIB, croissance, valeur ajoutée"] + eco["agr"],
    "Les secteurs d'activité et les entreprises": ECO_TXT2["Les secteurs d'activité et les entreprises"] + eco["ent"],
    "Le marché, les prix et l'inflation": ECO_TXT2["Le marché, les prix et l'inflation"] + eco["prix"],
    "La monnaie et la banque centrale": ECO_TXT2["La monnaie et la banque centrale"] + eco["mon"],
    "L'emploi et le chômage": ECO_TXT2["L'emploi et le chômage"] + eco["emp"],
    "L'État : impôts et politique budgétaire": ECO_TXT2["L'État : impôts et politique budgétaire"] + eco["etat"],
    "Le commerce extérieur": ECO_TXT2["Le commerce extérieur"] + eco["ext"],
  },
  "g-compta": {
    "Le cadre comptable : SYSCOHADA": CPT_TXT2["Le cadre comptable : SYSCOHADA"],
    "Le bilan": CPT_TXT2["Le bilan"] + cpt["bil"],
    "Le compte de résultat": CPT_TXT2["Le compte de résultat"] + cpt["res"],
    "Les comptes et la partie double": CPT_TXT2["Les comptes et la partie double"] + cpt["ops"],
    "Journal, grand livre et balance": CPT_TXT2["Journal, grand livre et balance"] + cpt["jgl"],
    "Les amortissements": CPT_TXT2["Les amortissements"] + cpt["amo"],
  },
}
