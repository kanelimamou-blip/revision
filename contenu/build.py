"""Construit les données de l'appli Révision BAC et BFEM (docs/revision/data/).

python contenu/build.py               -> questions.json et config.json
python contenu/build.py --codes 200   -> ajoute 200 codes premium ; la liste en clair
                                          est écrite hors du dépôt (public), seul le hachage est publié.
"""
import argparse
import hashlib
import json
import random
import re
from pathlib import Path
import unicodedata
import secrets
from pathlib import Path

from annales import ANNALES, GUIDED, HOST
from sujets_types import MODELE_ANNALES, MODELE_GUIDED
from sujets_lg import ANNALES_LG, GUIDED_LG
from sujets_tle2 import ANNALES_T2, GUIDED_T2
from sujets_tle3 import ANNALES_T3, GUIDED_T3
MODELE_ANNALES += ANNALES_LG + ANNALES_T2 + ANNALES_T3
MODELE_GUIDED.update({**GUIDED_LG, **GUIDED_T2, **GUIDED_T3})
# sujets types ×3 (Terminale et Première) : chaque fichier sujets_x3_*.py fournit ANNALES_X et GUIDED_X
import glob as _g, importlib as _imp
for _f in sorted(_g.glob(str(Path(__file__).parent / "sujets_x3_*.py"))):
    _m = _imp.import_module(Path(_f).stem)
    MODELE_ANNALES += _m.ANNALES_X
    MODELE_GUIDED.update(_m.GUIDED_X)
ANNALES = MODELE_ANNALES + ANNALES
GUIDED = {**GUIDED, **MODELE_GUIDED}
from q_plus import EXTRA
from q_plus_college import EXTRA_COLLEGE
from q_plus_lycee import EXTRA_LYCEE
from q_chapitres import CHAPITRE_FORCE, EXTRA_CHAPITRES
from q_programme import QCM_CH
from q_svt_plus import QCM_SVT
from q_tle_plus import QCM_TLE
from q_tle_plus2 import QCM_TLE2
from q_tle_plus3 import QCM_TLE3
from q_tle_plus4 import QCM_TLE4
from q_tle_s import QCM_TLE_S
from q_tle_s2 import QCM_TLE_S2
from q_tle_s3 import QCM_TLE_S3
# volume ×3 de 1re et Tle : chaque fichier q_*_x3*.py apporte un dictionnaire QCM_… {matière: {chapitre: questions}}
import glob as _glob, importlib as _il
_X3 = [v for _f in sorted(_glob.glob(str(Path(__file__).parent / "q_*_x3*.py"))) for _k, v in vars(_il.import_module(Path(_f).stem)).items() if _k.startswith("QCM_")]
X3_CH = {}
for _d in _X3:
    for _sid, _chs in _d.items():
        for _t, _qs in _chs.items():
            X3_CH.setdefault(_sid, {}).setdefault(_t, []).extend(_qs)
for _sid, _chs in [*QCM_SVT.items(), *QCM_TLE.items(), *QCM_TLE2.items(), *QCM_TLE3.items(), *QCM_TLE4.items(), *QCM_TLE_S.items(), *QCM_TLE_S2.items(), *QCM_TLE_S3.items()]:
    for _t, _qs in _chs.items():
        QCM_CH.setdefault(_sid, {}).setdefault(_t, []).extend(_qs)
from fiches import FICHES
from fiches_autres import FICHES_AUTRES
from syntheses import SYNTH
FICHES = {**FICHES, **FICHES_AUTRES}
# une synthèse = liste de chapitres ; les anciennes fiches (titre, points) gardent seulement « l'essentiel »
FICHES = {sid: [{"t": t, "cles": pts} for t, pts in f] for sid, f in FICHES.items()}
FICHES.update(SYNTH)
from catalogue import LIBRARY, LIB_HOST
from catalogue_devoirs import DEVOIRS
from ressources import RESSOURCES
from exercices import EXERCISES
from notions import NOTIONS
from notions_autres import NOTIONS_AUTRES
from programmes import PROGRAMMES
NOTIONS = {**NOTIONS, **NOTIONS_AUTRES}
# notions qui complètent tout le programme, classe par classe (une par chapitre sans notion)
import importlib
for _mod, _var in [("notions_3e", "N3"), ("notions_tle_maths", "NTM"), ("notions_tle_pc", "NTP"), ("notions_tle_autres", "NTA"), ("notions_2nde", "N2"), ("notions_1ere", "N1"), ("notions_g", "NG"), ("notions_6e", "N6"), ("notions_5e", "N5"), ("notions_4e", "N4"), ("notions_lg", "NLG"), ("notions_tle_com", "NTC"), ("notions_tle_com2", "NTC2"), ("notions_x3_tle_maths", "NX3TM"), ("notions_x3_tle_pc", "NX3TP"), ("notions_x3_tle_svt", "NX3TS"), ("notions_x3_tle_philo", "NX3TPH"), ("notions_x3_tle_hg", "NX3THG"), ("notions_x3_tle_fr", "NX3TFR"), ("notions_x3_tle_en", "NX3TEN"), ("notions_x3_tle_ml", "NX3TML"), ("notions_x3_tle_mg", "NX3TMG"), ("notions_x3_tle_es", "NX3TES"), ("notions_x3_1ere_maths", "NX3PM"), ("notions_x3_1ere_pc", "NX3PPC"), ("notions_x3_1ere_svt_hg", "NX3PSH"), ("notions_x3_1ere_lang", "NX3PL"), ("notions_x3_1ere_mlg", "NX3PMLG"), ("notions_x3_3e_sci", "NX33S"), ("notions_x3_3e_svt_fr", "NX33F"), ("notions_x3_3e_hg_lang", "NX33H"), ("notions_x3_6e_sci", "NX36S"), ("notions_x3_6e_let", "NX36L"), ("notions_x3_2nde_sci", "NX3SS"), ("notions_x3_2nde_let", "NX3SL"), ("notions_x3_4e_sci", "NX34S"), ("notions_x3_4e_let", "NX34L"), ("notions_x3_5e_sci", "NX35S"), ("notions_x3_5e_let", "NX35L"), ("notions_meth_6e", "MT6"), ("notions_meth_5e", "MT5")]:
    for _sid, _lst in getattr(importlib.import_module(_mod), _var).items():
        NOTIONS.setdefault(_sid, []).extend(_lst)
# matières ajoutées : maths des séries L et G, espagnol LV2
from matieres_plus import SUBJECTS_PLUS, PROG_PLUS, QCM_PLUS, N_PLUS
PROGRAMMES.update(PROG_PLUS)
for _sid, _chs in QCM_PLUS.items():
    for _t, _qs in _chs.items():
        QCM_CH.setdefault(_sid, {}).setdefault(_t, [])[:0] = _qs
for _sid, _lst in N_PLUS.items():
    NOTIONS.setdefault(_sid, []).extend(_lst)
# notions supplémentaires L et G après la notion principale de chaque chapitre
for _sid in NOTIONS:
    NOTIONS[_sid].sort(key=lambda n: n["id"].startswith(("lg-", "x-")))
# synthèses chapitre par chapitre là où il n'y avait qu'une fiche générale (gardée en fin de synthèse)
from syntheses_auto import auto_synth
from formules import formulaire
for _sid, _chs in auto_synth(NOTIONS, PROGRAMMES).items():
    FICHES[_sid] = _chs + [c for c in FICHES.get(_sid, []) if "p" not in c]
from questions import CLASSES, FAMILIES, FREE, LEVELS, SERIES, SUBJECTS
_i = next(i for i, s in enumerate(SUBJECTS) if "annales" in s[0])
SUBJECTS[_i:_i] = SUBJECTS_PLUS

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "docs" / "data"
HASHES = ROOT / "code_hashes.txt"
SALT = "rev-bac-bfem:"
ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  # sans 0/O ni 1/I

# Réglages de vente (à remplir par Est : numéro Wave et WhatsApp au format 221XXXXXXXXX)
CONFIG = {
    "price_fcfa": 1000,
    "wave_number": "78 272 19 20",
    # numéro Orange Money (même numéro que Wave tant qu'Est n'en donne pas un autre)
    "om_number": "78 272 19 20",
    "whatsapp": "221782721920",
    # classes d'examen : nom de l'examen et date indicative
    "exams": {"3e": ["BFEM", "2027-07-06"], "Tle": ["BAC", "2027-07-01"]},
    # clé publique des notifications (Firebase > Paramètres du projet > Cloud Messaging > Certificats Web Push) ;
    # vide : le bouton « Recevoir les rappels » reste caché
    # infos de la société pour les pages légales (#legal) : à compléter par Est (vide = « à compléter »)
    # accord du parent obligatoire avant de payer (activer seulement après avoir publié les règles Firestore « accords »)
    "accord_parent": False,
    # mentions légales et coordonnées d'Est visibles dans les pages légales : False tant que le RCCM n'est pas régularisé
    "mentions_publiques": False,
    "societe": {"nom": "", "forme": "", "rccm": "", "ninea": "", "adresse": "", "responsable": "", "cdp": ""},
    "vapid": "BKmmvPfiqpxCLAislhc0r7Kr6UmK1CQWqsIi1Yze2uhGQlm7dfxfeFJJzAdPCn0yVpiBEZ3bb7YsWDTD7eozxOY",
}


# Règles Firestore à coller dans la console Firebase (Firestore Database > Règles).
# Elles contiennent le secret des codes : elles sont écrites hors du dépôt, à côté de la liste des codes.
# Un code = 5 caractères au hasard + « - » + 6 caractères de contrôle (début du SHA-256 de secret + partie au hasard).
RULES = """rules_version = '2';
service cloud.firestore {
  match /databases/{db}/documents {
    function validCode(code) {
      let p = code.split('-');
      return p.size() == 2 && p[0].size() == 5
        && hashing.sha256('SECRET' + p[0]).toHexString().lower()[0:6] == p[1].lower();
    }
    match /users/{uid} {
      allow read: if request.auth != null && request.auth.uid == uid;
      // création : date fixée par le serveur et sans premium
      allow create: if request.auth != null && request.auth.uid == uid
        && request.resource.data.created == request.time
        && request.resource.data.premium == false;
      // la date de création ne change jamais ; le premium ne s'obtient qu'avec un code réclamé par cet élève
      allow update: if request.auth != null && request.auth.uid == uid
        && request.resource.data.created == resource.data.created
        && (request.resource.data.premium == resource.data.premium
          || (request.resource.data.premium == true
            && getAfter(/databases/$(db)/documents/claims/$(request.resource.data.code)).data.uid == uid));
    }
    // sessions de groupe : chaque élève connecté écrit seulement sa propre note, le groupe lit le classement
    match /sessions/{code}/scores/{uid} {
      allow read: if request.auth != null && code.size() <= 12;
      allow create, update: if request.auth != null && request.auth.uid == uid && code.size() <= 12
        && request.resource.data.keys().hasOnly(['name', 'note', 'score', 'total', 'level', 'at'])
        && request.resource.data.name is string && request.resource.data.name.size() <= 30
        && request.resource.data.note is number && request.resource.data.note >= 0 && request.resource.data.note <= 20
        && request.resource.data.score is int && request.resource.data.total is int
        && request.resource.data.score >= 0 && request.resource.data.score <= request.resource.data.total && request.resource.data.total <= 50
        && request.resource.data.level is string && request.resource.data.level.size() <= 20
        && request.resource.data.at == request.time;
      allow delete: if false;
    }
    // un code ne peut être réclamé qu'une fois (pas de recréation possible)
    match /claims/{code} {
      allow read, update, delete: if false;
      allow create: if request.auth != null && request.resource.data.uid == request.auth.uid && validCode(code);
    }
  }
}
"""
PRIVATE = Path("/mnt/project-files/revision")
SECRET_FILE = PRIVATE / "secret-codes.txt"


def secret():
    if not SECRET_FILE.exists():
        PRIVATE.mkdir(parents=True, exist_ok=True)
        SECRET_FILE.write_text(secrets.token_hex(16))
    return SECRET_FILE.read_text().strip()


def make_code(sec):
    head = "".join(secrets.choice(ALPHABET) for _ in range(5))
    return head + "-" + hashlib.sha256((sec + head).encode()).hexdigest()[:6].upper()


def code_hash(code):
    return hashlib.sha256((SALT + code.strip().upper().replace(" ", "")).encode()).hexdigest()


def new_codes(n, dest):
    sec = secret()
    codes = [make_code(sec) for _ in range(n)]
    with HASHES.open("a") as f:
        f.writelines(code_hash(c) + "\n" for c in codes)
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("a") as f:
        f.writelines(c + "\n" for c in codes)
    # les règles en ligne ont évolué depuis (paiements, admin, accords) : ne pas écraser le fichier à jour
    if not (PRIVATE / "firestore.rules").exists():
        (PRIVATE / "firestore.rules").write_text(RULES.replace("SECRET", sec))
    print(f"{n} codes ajoutés dans {dest}")


def _norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def chapter_of(sid, text):
    """Indice du chapitre du programme dont les mots-clés apparaissent le plus dans le texte (−1 si aucun)."""
    t, best, top = _norm(text), -1, 0
    for i, (_, kws) in enumerate(PROGRAMMES.get(sid, [])):
        n = sum(len(re.findall(r"(?<![a-z])" + re.escape(_norm(k)), t)) for k in kws)
        if n > top:
            best, top = i, n
    return best


def build():
    questions, subjects = [], []
    for sid, levels, name, items in SUBJECTS:
        items = items + EXTRA.get(sid, []) + EXTRA_COLLEGE.get(sid, []) + EXTRA_LYCEE.get(sid, []) + EXTRA_CHAPITRES.get(sid, [])
        # QCM rangés par chapitre : le chapitre est imposé
        force = {q: t for src in (QCM_CH, X3_CH) for t, qs in src.get(sid, {}).items() for q, *_ in qs}
        # les QCM ×3 viennent en dernier : les identifiants des questions déjà en ligne (et les progrès des élèves) ne bougent pas
        items = items + [x for qs in QCM_CH.get(sid, {}).values() for x in qs] + [x for qs in X3_CH.get(sid, {}).values() for x in qs]
        # pas deux fois la même question dans une matière
        _vus = set(); items = [x for x in items if not (x[0] in _vus or _vus.add(x[0]))]
        fams = {f"{c} {f}" for c in SERIES for f in set(FAMILIES.values())}
        assert set(levels) <= set(LEVELS) | fams, (sid, levels)
        subjects.append({"id": sid, "levels": levels, "name": name, "count": len(items), "free": min(FREE, len(items)), "fiche": sid in FICHES, "notions": len(NOTIONS.get(sid, []))})
        for i, (q, choices, a, ex, *src) in enumerate(items):
            assert len(choices) == 4 and 0 <= a < 4, (sid, q)
            qid = f"{sid}-{i + 1}"
            # ordre des choix mélangé (fixe pour chaque question) pour que la bonne réponse ne soit pas toujours à la même place
            order = list(range(4))
            random.Random(qid).shuffle(order)
            questions.append({"id": qid, "s": sid, "q": q, "c": [choices[j] for j in order], "a": order.index(a), "e": ex, "free": i < FREE, "ch": [t for t, _ in PROGRAMMES[sid]].index(force.get(q) or CHAPITRE_FORCE[q]) if q in force or q in CHAPITRE_FORCE else chapter_of(sid, f"{q} {choices[a]} {ex}"), **({"alt": "tle-maths", "ach": chapter_of("tle-maths", f"{q} {choices[a]} {ex}")} if sid.startswith("tle-annales-maths") else {}), **({"src": src[0]} if src else {})})
    # sujets guidés et exercices corrigés : choix mélangés de la même façon, étape par étape
    def guided(key, parts):
        out = []
        for k, part in enumerate(parts):
            steps = []
            for j, (q, choices, a, ex, pts) in enumerate(part["steps"]):
                assert len(choices) == 4 and 0 <= a < 4, (key, q)
                order = list(range(4))
                random.Random(f"{key}-{k}-{j}").shuffle(order)
                steps.append({"q": q, "c": [choices[i] for i in order], "a": order.index(a), "e": ex, "pts": pts})
            out.append({"title": part["title"], "context": part["context"], "steps": steps})
        return out
    for an in ANNALES:
        if GUIDED.get(an["id"]):
            an["guided"] = guided(an["id"], GUIDED[an["id"]])
    exercises = []
    for ex in EXERCISES:
        assert set(ex["levels"]) <= set(LEVELS) | fams, ex["id"]
        exercises.append({**{k: v for k, v in ex.items() if k != "parts"}, "guided": guided(ex["id"], ex["parts"])})
    # notions de cours : le cours reste dans « notions », l'exercice d'application rejoint les exercices corrigés
    notions = {}
    subj = {s[0]: s for s in SUBJECTS}
    for sid, chapters in NOTIONS.items():
        assert sid in subj, sid
        notions[sid] = []
        for i, ch in enumerate(chapters):
            notions[sid].append({k: v for k, v in ch.items() if k not in ("exo", "programme")} | {"free": i == 0, "pch": [t for t, _ in PROGRAMMES[sid]].index(ch["programme"]) if "programme" in ch else chapter_of(sid, ch["title"] + " " + " ".join(ch["cours"] + ch["enonce"]))})
            exo = ch["exo"]
            exercises.append({"id": "ch-" + ch["id"], "levels": subj[sid][1], "subject": subj[sid][2], "free": i == 0, "chapter": ch["id"],
                              "title": ch["title"], "src": "Exercice d'application du cours",
                              "guided": guided("ch-" + ch["id"], [{"title": ch["title"], "context": exo["context"], "steps": exo["steps"]}])})
    for sid in notions:
        notions[sid].sort(key=lambda n: n["pch"])
    assert set(PROGRAMMES) <= {s[0] for s in SUBJECTS}
    assert set(EXTRA) | set(EXTRA_COLLEGE) | set(EXTRA_LYCEE) | set(EXTRA_CHAPITRES) | set(QCM_CH) <= {s[0] for s in SUBJECTS} and set(FICHES) <= {s[0] for s in SUBJECTS}
    for sid, chs in SYNTH.items():
        assert all("p" not in c or 0 <= c["p"] < len(PROGRAMMES[sid]) for c in chs), sid
    for e in LIBRARY + DEVOIRS:
        assert set(e["levels"]) <= set(LEVELS) | fams, e
    # sources consultées, affichées en texte (sans lien) dans l'appli : #sources et sous chaque cours
    # Ne sont affichés que des documents officiels et publics (examens d'État, ministère, Office du BAC).
    # Les sites privés (archives, cours en ligne) et les devoirs d'établissement ne sont jamais montrés.
    def _off(exam):
        return "Office du Baccalauréat (UCAD) · sujet officiel public" if exam == "BAC" else "Ministère de l'Éducation nationale · sujet officiel public"
    sources = [{"k": "Programme officiel", "lv": LEVELS, "m": "Toutes matières", "t": "Programmes officiels de l'enseignement moyen et secondaire du Sénégal, chapitre par chapitre", "o": "Ministère de l'Éducation nationale"}]
    sources += [{"k": "Examen officiel", "lv": e["levels"], "m": e["subject"], "t": f"{e['exam']} {e['year']} · {e['subject']}" + (f" · séries {e['series']}" if e.get("series") else ""), "o": _off(e["exam"])} for e in LIBRARY if e["exam"] in ("BAC", "BFEM")]
    sources += [{"k": "Document officiel", "lv": lv, "m": m, "t": t, "o": "Office du Baccalauréat (UCAD)" if "officedubac" in u else "Ministère de l'Éducation nationale"} for lv, m, k, t, u in RESSOURCES if "officedubac" in u or "education.sn" in u]
    for a in ANNALES:
        if a.get("sujet") and a["exam"] in ("BAC", "BFEM"):
            sources.append({"k": "Sujet officiel détaillé dans l'appli", "lv": a["levels"], "m": a["subject"], "t": f"{a['exam']} {a['year']} · {a['subject']} · séries {a['series']}", "o": _off(a["exam"])})
    hashes = HASHES.read_text().split() if HASHES.exists() else []
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "questions.json").write_text(json.dumps({"classes": CLASSES, "series": SERIES, "families": FAMILIES, "levels": LEVELS, "subjects": subjects, "questions": questions, "annales": [{k: v for k, v in a.items() if k not in ("sujet", "corrige")} for a in ANNALES], "fiches": FICHES, "exercises": exercises, "notions": notions,  "programmes": {k: [t for t, _ in v] for k, v in PROGRAMMES.items()}, "formules": formulaire(FICHES, notions, PROGRAMMES), "sources": sources}, ensure_ascii=False, separators=(",", ":")))
    (OUT / "config.json").write_text(json.dumps({**CONFIG, "salt": SALT, "codes": hashes}, ensure_ascii=False, separators=(",", ":")))
    print(f"{len(questions)} questions, {len(subjects)} matières, {len(hashes)} codes")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--codes", type=int, default=0)
    p.add_argument("--dest", default="/mnt/project-files/revision/codes-premium.txt")
    args = p.parse_args()
    if args.codes:
        new_codes(args.codes, args.dest)
    build()
