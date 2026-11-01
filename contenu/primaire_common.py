# Élémentaire (CE1 à CM2), programme sénégalais : Curriculum de l'Éducation de Base (CEB) du ministère de l'Éducation nationale.
# Une matière = liste de chapitres dans l'ordre de l'année. Un chapitre donne en une fois :
#   le cours (notion), la synthèse, des QCM corrigés, l'exercice d'application guidé et un exercice type devoir.
# Tout est rédigé pour l'appli (aucun document privé repris).
from notions_prog import C

METH = {
  "maths": ("Résoudre un problème", ["Lire l'énoncé deux fois et souligner les nombres utiles.", "Chercher ce qu'on demande, puis choisir l'opération.", "Poser et calculer, puis vérifier avec un ordre de grandeur.", "Écrire une phrase réponse avec l'unité."]),
  "francais": ("Faire un exercice de langue", ["Lire toute la phrase.", "Trouver le mot ou le groupe demandé en posant la bonne question.", "Appliquer la règle de la leçon.", "Relire pour vérifier les accords."]),
  "sciences": ("Répondre en sciences", ["Observer le dessin, l'objet ou l'expérience.", "Utiliser les mots de la leçon.", "Expliquer en une ou deux phrases : ce que l'on voit, puis pourquoi."]),
  "histoire": ("Répondre en histoire", ["Repérer la date, le lieu et les personnages.", "Raconter les faits dans l'ordre.", "Dire pourquoi c'est important."]),
  "geo": ("Répondre en géographie", ["Situer le lieu (carte, points cardinaux).", "Décrire avec les mots justes.", "Expliquer le lien entre la nature et les activités des hommes."]),
  "civique": ("Répondre en vivre ensemble", ["Lire la situation.", "Dire ce qui est bien ou mal et pourquoi (règle, droit, devoir).", "Proposer le bon comportement."]),
}


def CH(t, nid, cours, retenir, exemples, piege, exam, ctx, steps, qcm, dev=None):
    """t : titre du chapitre ; cours : 2-3 phrases ; retenir : points clés ; exemples : [(titre, [lignes])] ;
    steps et qcm : (question, bonne réponse, faux1, faux2, faux3, explication) ; dev : (titre, contexte, étapes)."""
    for s in list(steps) + list(qcm) + list(dev[2] if dev else []):
        assert len(s) == 6 and len(set(s[1:5])) == 4, (nid, s)
    return {"t": t, "id": nid, "cours": cours, "retenir": retenir, "exemples": exemples, "piege": piege, "exam": exam,
            "ctx": ctx, "steps": steps, "qcm": qcm, "dev": dev}


def assemble(matieres):
    """matieres : [(sid, niveau, nom, famille, [chapitres])] -> dictionnaires au format de build.py."""
    subjects, prog, qcm, notions, synth, devs = [], {}, {}, {}, {}, {}
    for sid, lv, name, fam, chs in matieres:
        subjects.append((sid, [lv], name, []))
        prog[sid] = [(c["t"], []) for c in chs]
        qcm[sid] = {c["t"]: [(q, [a, b, d, e], 0, x) for q, a, b, d, e, x in c["qcm"]] for c in chs}
        notions[sid] = [C(c["t"], f"p-{c['id']}", c["cours"], c["retenir"], c["exemples"], c["ctx"], c["steps"]) for c in chs]
        synth[sid] = [{"t": c["t"], "p": i, "cles": c["cours"] + c["retenir"], "methodes": [METH[fam]], "pieges": [c["piege"]],
                       "exemple": c["exemples"][0], "exemples": c["exemples"][1:], "exam": c["exam"]} for i, c in enumerate(chs)]
        devs[sid] = (lv, name, [(c["dev"], (c["t"], c["ctx"], c["steps"])) for c in chs])
    return subjects, prog, qcm, notions, synth, devs
