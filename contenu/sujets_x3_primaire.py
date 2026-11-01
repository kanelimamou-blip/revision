# Devoirs types de l'élémentaire (CE1 à CM2) : 3 par matière, un par trimestre, et sujets types du CFEE en CM2.
# Rédigés pour l'appli à partir des exercices de chaque chapitre ; jamais présentés comme des sujets officiels.
from sujets_dev_common import D, pack, TRIM
from primaire import DEVS_PRIM

def _trois(chs):
    """3 exercices pris dans les chapitres donnés : d'abord les exercices type devoir, puis les exercices d'application."""
    pool = [d for d, _ in chs if d] + [e for _, e in chs]
    out = []
    for x in pool:
        if x not in out:
            out.append(x)
    return out[:3]

_items = []
for sid, (lv, name, chs) in DEVS_PRIM.items():
    n = len(chs)
    for k in (1, 2, 3):
        part = chs[(k - 1) * n // 3: k * n // 3]
        if len(_trois(part)) < 3:
            part = chs
        _items.append(D(f"dev-{sid}-{k}", lv, name, k, _trois(part), duration="1 h", label=TRIM[k]))
# CM2 : sujets types du CFEE (français, mathématiques, éveil) sur tout le programme
for sid, (lv, name, chs) in DEVS_PRIM.items():
    if lv != "CM2":
        continue
    devs = [d for d, _ in chs if d] or [e for _, e in chs]
    for k in (1, 2, 3):
        exos = [devs[(k - 1 + 3 * j) % len(devs)] for j in range(3)]
        if len({id(x) for x in exos}) == 3:
            _items.append(D(f"cfee-{sid}-{k}", lv, name, k, exos, exam="CFEE", duration="1 h 30", label=f"sujet type {k}"))
ANNALES_X, GUIDED_X = pack(_items)
