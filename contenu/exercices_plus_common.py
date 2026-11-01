# Exercices guidés en plus (type devoir, rédigés pour l'appli : ce ne sont pas des sujets officiels).
SRC = "Exercice type devoir (rédigé pour l'appli, non officiel)"

def X(sid, level, subject, chapter, n, title, context, steps, free=False):
    """steps : (question, bonne réponse, faux1, faux2, faux3, explication)."""
    for s in steps:
        assert len(set(s[1:5])) == 4, (chapter, s[0])
    return {"id": f"exp-{chapter}-{n}", "levels": [level], "subject": subject, "free": free, "chapter": chapter,
            "title": title, "src": SRC,
            "parts": [{"title": title, "context": context, "steps": [[s[0], list(s[1:5]), 0, s[5], 1] for s in steps]}]}
