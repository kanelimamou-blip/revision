# Élémentaire CE1 à CM2 (programme sénégalais, CEB) : rassemble les classes au format de build.py.
import importlib
from primaire_common import assemble

CLASSES_PRIM = ["CE1", "CE2", "CM1", "CM2"]
_MODS = ["primaire_ce1", "primaire_ce2", "primaire_cm1", "primaire_cm2"]
MATIERES = []
for _m in _MODS:
    try:
        MATIERES += importlib.import_module(_m).MATIERES
    except ModuleNotFoundError as e:
        if e.name != _m:
            raise
# anglais : une matière par classe, fabriquée depuis primaire_anglais.py ; le vocabulaire part aussi vers docs/vocab_en.js (jeux)
import os as _os
from primaire_anglais import chapitres as _en_chapitres, vocab_js as _vocab_js
for _lv in CLASSES_PRIM:
    MATIERES.append((f"{_lv.lower()}-anglais", _lv, "Anglais", "anglais", _en_chapitres(_lv)))
with open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "docs", "vocab_en.js"), "w", encoding="utf-8") as _f:
    _f.write(_vocab_js())
SUBJECTS_PRIM, PROG_PRIM, QCM_PRIM, NOTIONS_PRIM, SYNTH_PRIM, DEVS_PRIM = assemble(MATIERES)
