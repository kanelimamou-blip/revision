# Devoirs types (6e-4e) et sujets types BFEM (3e) : rédigés pour l'appli, sur le modèle des devoirs et de l'épreuve, jamais présentés comme officiels.
TRIM = {1: "1er trimestre", 2: "2e trimestre", 3: "3e trimestre"}

def D(ids, level, subject, n, exos, exam="Devoir", duration="2 h", coef=None, label=None):
    """exos : 3 exercices (titre, contexte, étapes) ; étapes : (question, bonne, faux1, faux2, faux3, explication).
    Barème sur 20 : 6, 6 et 8 points répartis également entre les étapes de chaque exercice."""
    assert len(exos) == 3, ids
    poids = [6, 6, 8]
    parts, guided = [], []
    for k, ((titre, ctx, steps), w) in enumerate(zip(exos, poids), 1):
        assert len(steps) >= 3, (ids, titre)
        pts = round(w / len(steps), 2)
        st = []
        for s in steps:
            assert len(set(s[1:5])) == 4, (ids, s[0])
            st.append((s[0], list(s[1:5]), 0, s[5], pts))
        # ajuste le dernier pas pour que l'exercice fasse exactement w points
        q, c, a, e, p = st[-1]
        st[-1] = (q, c, a, e, round(w - pts * (len(st) - 1), 2))
        guided.append({"title": f"Exercice {k} : {titre} ({w} pts)", "context": ctx, "steps": st})
        parts.append(f"Exercice {k} ({w} pts) : {titre}")
    an = {"id": ids, "exam": exam, "year": label or f"type {n}", "series": "", "subject": subject, "levels": [level],
          "duration": duration, "modele": True, "parts": parts}
    if coef:
        an["coef"] = coef
    return an, guided

def pack(items):
    A, G = [], {}
    for an, g in items:
        A.append(an)
        G[an["id"]] = g
    return A, G
