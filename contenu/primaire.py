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
SUBJECTS_PRIM, PROG_PRIM, QCM_PRIM, NOTIONS_PRIM, SYNTH_PRIM, DEVS_PRIM = assemble(MATIERES)
