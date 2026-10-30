# Révision

Appli de téléphone pour réviser de la 6e à la Terminale (séries L et S) au Sénégal : quiz corrigés et expliqués, examens et devoirs blancs chronométrés, erreurs à revoir et progrès. Elle s'installe sur l'écran d'accueil et marche sans connexion.

En ligne : https://kanelimamou-blip.github.io/revision/

## Fichiers

- `contenu/` : les questions (`questions.py` pour la 3e et la Terminale, `q_college.py` de la 6e à la 4e, `q_lycee.py` pour la 2nde et la 1ère) et `build.py`, qui génère `docs/data/`.
- `docs/` : l'appli (HTML/JS), publiée sur GitHub Pages à chaque modification.

## Premium

Les 5 premières questions de chaque matière sont gratuites. Le reste et les examens blancs se débloquent avec un code vendu par Wave (prix, numéro Wave et WhatsApp dans `CONFIG` de `contenu/build.py`).
`python contenu/build.py --codes 100` ajoute des codes : seuls leurs hachages sont publiés (`contenu/code_hashes.txt`), la liste en clair est écrite hors du dépôt.
