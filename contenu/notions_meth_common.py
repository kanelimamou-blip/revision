# Fiches méthode (demande d'Est du 2026-11-01 : « pas assez riche » de la 6e à la 3e).
# Chaque fiche : à quoi ça sert, étapes de la méthode, erreurs fréquentes, deux exemples corrigés, exercice guidé de 5 étapes.
from notions_prog import C

def M(prog, nid, cours, methode, erreurs, ex1, ex2, steps):
    enonce = [f"Étape {i} : {m}" for i, m in enumerate(methode, 1)] + [f"⚠ Erreur fréquente : {e}" for e in erreurs]
    return C(prog, nid, cours, enonce, [ex1, ex2], "Méthode : " + prog + ".", steps, title="Méthode et pièges : " + prog)
