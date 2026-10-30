"""Construit les données de l'appli Révision BAC et BFEM (docs/revision/data/).

python contenu/build.py               -> questions.json et config.json
python contenu/build.py --codes 200   -> ajoute 200 codes premium ; la liste en clair
                                          est écrite hors du dépôt (public), seul le hachage est publié.
"""
import argparse
import hashlib
import json
import random
import secrets
from pathlib import Path

from annales import ANNALES, GUIDED, HOST
from q_plus import EXTRA
from q_plus_college import EXTRA_COLLEGE
from q_plus_lycee import EXTRA_LYCEE
from fiches import FICHES
from catalogue import LIBRARY, LIB_HOST
from questions import CLASSES, FAMILIES, FREE, LEVELS, SERIES, SUBJECTS

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "docs" / "data"
HASHES = ROOT / "code_hashes.txt"
SALT = "rev-bac-bfem:"
ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  # sans 0/O ni 1/I

# Réglages de vente (à remplir par Est : numéro Wave et WhatsApp au format 221XXXXXXXXX)
CONFIG = {
    "price_fcfa": 2000,
    "wave_number": "78 272 19 20",
    "whatsapp": "221782721920",
    # classes d'examen : nom de l'examen et date indicative
    "exams": {"3e": ["BFEM", "2027-07-06"], "Tle": ["BAC", "2027-07-01"]},
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
    (PRIVATE / "firestore.rules").write_text(RULES.replace("SECRET", sec))
    print(f"{n} codes ajoutés dans {dest}")


def build():
    questions, subjects = [], []
    for sid, levels, name, items in SUBJECTS:
        items = items + EXTRA.get(sid, []) + EXTRA_COLLEGE.get(sid, []) + EXTRA_LYCEE.get(sid, [])
        fams = {f"{c} {f}" for c in SERIES for f in set(FAMILIES.values())}
        assert set(levels) <= set(LEVELS) | fams, (sid, levels)
        subjects.append({"id": sid, "levels": levels, "name": name, "count": len(items), "free": min(FREE, len(items)), "fiche": sid in FICHES})
        for i, (q, choices, a, ex, *src) in enumerate(items):
            assert len(choices) == 4 and 0 <= a < 4, (sid, q)
            qid = f"{sid}-{i + 1}"
            # ordre des choix mélangé (fixe pour chaque question) pour que la bonne réponse ne soit pas toujours à la même place
            order = list(range(4))
            random.Random(qid).shuffle(order)
            questions.append({"id": qid, "s": sid, "q": q, "c": [choices[j] for j in order], "a": order.index(a), "e": ex, "free": i < FREE, **({"src": src[0]} if src else {})})
    # sujets guidés : mêmes choix mélangés que les questions, attachés à leur annale
    for an in ANNALES:
        parts = GUIDED.get(an["id"])
        if not parts:
            continue
        an["guided"] = []
        for k, part in enumerate(parts):
            steps = []
            for j, (q, choices, a, ex, pts) in enumerate(part["steps"]):
                assert len(choices) == 4 and 0 <= a < 4, (an["id"], q)
                order = list(range(4))
                random.Random(f'{an["id"]}-{k}-{j}').shuffle(order)
                steps.append({"q": q, "c": [choices[i] for i in order], "a": order.index(a), "e": ex, "pts": pts})
            an["guided"].append({"title": part["title"], "context": part["context"], "steps": steps})
    assert set(EXTRA) | set(EXTRA_COLLEGE) | set(EXTRA_LYCEE) <= {s[0] for s in SUBJECTS} and set(FICHES) <= {s[0] for s in SUBJECTS}
    for e in LIBRARY:
        assert set(e["levels"]) <= set(LEVELS) | fams, e
    hashes = HASHES.read_text().split() if HASHES.exists() else []
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "questions.json").write_text(json.dumps({"classes": CLASSES, "series": SERIES, "families": FAMILIES, "levels": LEVELS, "subjects": subjects, "questions": questions, "annales": ANNALES, "annalesHost": HOST, "library": LIBRARY, "libraryHost": LIB_HOST, "fiches": FICHES}, ensure_ascii=False, separators=(",", ":")))
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
