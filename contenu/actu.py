"""Flash actu : lit les fils RSS publics de la presse sénégalaise et africaine, garde les titres récents adaptés à
des élèves, les classe par centre d'intérêt et écrit docs/data/actu.json (lancé toutes les 30 min par actu.yml).

On ne garde que le titre, deux lignes de résumé et le nom du journal : l'élève lit le flash dans l'appli, sans lien.
"""
import html
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from xml.etree import ElementTree as ET

OUT = Path(__file__).resolve().parent.parent / "docs" / "data" / "actu.json"

SOURCES = [
    ("APS", "https://aps.sn/feed/", True),
    ("Le Soleil", "https://www.lesoleil.sn/feed/", True),
    ("Le Quotidien", "https://www.lequotidien.sn/feed/", True),
    ("Senenews", "https://www.senenews.com/feed", True),
    ("Seneweb", "https://www.seneweb.com/feed/news", True),
    ("Dakaractu", "https://www.dakaractu.com/xml/syndication.rss", True),
    ("PressAfrik", "https://www.pressafrik.com/xml/syndication.rss", True),
    ("RFI Afrique", "https://www.rfi.fr/fr/afrique/rss", False),
]

# centres d'intérêt proposés à l'élève : mots qui classent un flash, et le lien avec ses cours
THEMES = {
    "sport": ("⚽ Sport", r"football|lions|basket|lutte|\bjo\b|olympi|can 20|coupe du monde|match|champion|athl|sadio|mané|stade|navétane", "En maths : pourcentages, moyennes et statistiques des résultats."),
    "education": ("🎓 Éducation", r"école|élève|enseign|bac\b|bfem|examen|universit|étudiant|bourse|ucad|ministère de l.éducation|concours|scolaire|cfee", "Ton avenir : orientation, examens et bourses."),
    "sciences": ("🔬 Sciences et techno", r"numérique|technolog|intelligence artificielle|\bia\b|internet|satellite|gaindesat|science|recherche|innovation|startup|téléphon|4g|5g|fibre|digital", "En SVT, physique et maths : les sciences derrière l'innovation."),
    "sante": ("🩺 Santé", r"santé|hôpital|médec|vaccin|paludisme|maladie|épidém|nutrition|sida|cancer|dengue|choléra", "En SVT : immunologie, maladies et prévention."),
    "environnement": ("🌍 Environnement", r"climat|environnement|pluie|hivernage|inondation|sécheresse|forêt|reboisement|pollution|plastique|érosion|énergie solaire|eau potable|biodiversité", "En SVT et en géographie : climat, eau et développement durable."),
    "economie": ("💰 Économie", r"économi|croissance|pétrole|gaz|budget|fcfa|inflation|prix|commerce|export|import|banque|emploi|entreprise|investiss|port de dakar|agricult|arachide|pêche", "En économie, HG et maths : croissance, prix, pourcentages."),
    "culture": ("🎭 Culture", r"culture|musique|cinéma|film|livre|littérature|festival|art|théâtre|patrimoine|dak.art|biennale|écrivain|poète|senghor", "En français : auteurs, œuvres et culture africaine."),
    "monde": ("🌐 Afrique et monde", r"cedeao|union africaine|onu|afrique|international|sommet|diplomat|ambassad|uemoa|aes\b|mali|mauritanie|gambie|guinée", "En histoire-géo : coopération, intégration régionale, relations internationales."),
    "politique": ("🏛️ Vie publique", r"président|gouvernement|ministre|assemblée|député|conseil des ministres|loi|élection|maire|sonko|diomaye", "En HG et philo : l'État, la citoyenneté et la démocratie."),
}
# sujets écartés pour une appli d'élèves (faits divers violents, sujets adultes)
BLOQUE = re.compile(r"meurtre|tué|tuée|assassin|viol|cadavre|corps sans vie|égorg|poignard|drogue|chanvre|prostitu|sexe|sexuel|décapit|suicide|braquage|agress|lynch|accident mortel|morts? sur|sang\b|homosex|pornogr|avortement|infanticide|charlatan", re.I)


def texte(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"(The post|L’article|L'article) .*? (appeared first on|est apparu en premier sur) .*$", "", s).strip()
    return s


def resume(s, n=220):
    if len(s) <= n:
        return s
    coupe = s[:n].rsplit(" ", 1)[0]
    return coupe.rstrip(",;:") + "…"


def lire(nom, url, local):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Revision-actu; +https://kanelimamou-blip.github.io/revision/)"})
    data = urllib.request.urlopen(req, timeout=20).read()
    root = ET.fromstring(data)
    out = []
    for it in root.iter("item"):
        titre = texte(it.findtext("title"))
        desc = texte(it.findtext("description"))
        if titre and desc.startswith(titre):
            desc = desc[len(titre):].strip(" -–:")
        try:
            d = parsedate_to_datetime(it.findtext("pubDate")).astimezone(timezone.utc)
        except Exception:
            continue
        cats = " ".join(texte(c.text) for c in it.findall("category"))
        if not titre or BLOQUE.search(titre + " " + desc + " " + cats):
            continue
        tout = f"{titre} {desc} {cats}".lower()
        themes = [k for k, (_, rx, _) in THEMES.items() if re.search(rx, tout)]
        out.append({"t": titre, "r": resume(desc), "s": nom, "d": d.strftime("%Y-%m-%dT%H:%M:%SZ"), "th": themes[:3], "loc": local or "sénégal" in tout or "dakar" in tout})
    return out


def main():
    tous, ok = [], []
    for nom, url, local in SOURCES:
        try:
            items = lire(nom, url, local)
            tous += items
            ok.append(f"{nom} {len(items)}")
        except Exception as e:  # une source en panne ne bloque pas les autres
            ok.append(f"{nom} ERREUR {type(e).__name__}")
    print(" · ".join(ok))
    # doublons (même titre repris par plusieurs journaux) et ordre du plus récent au plus ancien
    vus, flash = set(), []
    for x in sorted(tous, key=lambda x: x["d"], reverse=True):
        cle = re.sub(r"\W+", "", x["t"].lower())[:60]
        if cle in vus:
            continue
        vus.add(cle)
        flash.append(x)
    flash = flash[:80]
    if not flash:
        print("Aucun flash lu : on garde l'ancien fichier.")
        return 0
    themes = {k: [lbl, lien] for k, (lbl, _, lien) in THEMES.items()}
    OUT.write_text(json.dumps({"maj": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "themes": themes, "flash": flash}, ensure_ascii=False, separators=(",", ":")))
    print(f"{len(flash)} flashs écrits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
