# Synthèses de cours détaillées, chapitre par chapitre selon le programme officiel sénégalais.
# Format : identifiant de matière -> liste de chapitres
#   t        titre du chapitre
#   p        indice du chapitre correspondant dans PROGRAMMES[matière] (pour l'entraînement ciblé)
#   cles     définitions, propriétés et formules à connaître
#   methodes [(ce qu'on demande, [étapes de la méthode])]
#   pieges   erreurs fréquentes relevées dans les copies
#   exemple  (énoncé, [lignes du corrigé])
#   exam     ce qui tombe à l'examen sur ce chapitre

SYNTH = {}

SYNTH["tle-maths"] = [
  {"t": "Limites de fonctions", "p": 0,
   "cles": [
     "Limites de référence : lim (x→+∞) xⁿ = +∞ ; lim (x→+∞) 1/xⁿ = 0 ; lim (x→0⁺) 1/x = +∞ ; lim (x→0⁻) 1/x = −∞ ; lim (x→+∞) √x = +∞.",
     "Formes indéterminées : « ∞ − ∞ », « 0 × ∞ », « ∞/∞ », « 0/0 ». Toutes les autres opérations se calculent directement.",
     "Polynôme en ±∞ : il a la même limite que son terme de plus haut degré. Fraction rationnelle en ±∞ : même limite que le quotient des termes de plus haut degré.",
     "Théorème des gendarmes : si g(x) ≤ f(x) ≤ h(x) et lim g = lim h = L, alors lim f = L.",
     "Comparaison : si f(x) ≥ g(x) et lim g = +∞, alors lim f = +∞.",
     "Limite d'une composée : si lim (x→a) u(x) = b et lim (X→b) v(X) = c, alors lim (x→a) v(u(x)) = c.",
     "Asymptotes : lim (x→a) f(x) = ±∞ donne l'asymptote verticale x = a ; lim (x→±∞) f(x) = b donne l'asymptote horizontale y = b ; lim (x→±∞) [f(x) − (ax + b)] = 0 donne l'asymptote oblique y = ax + b.",
   ],
   "methodes": [
     ("Lever une forme « ∞/∞ » ou « ∞ − ∞ » en l'infini", [
       "Mettre en facteur le terme de plus haut degré au numérateur et au dénominateur.",
       "Simplifier, puis utiliser lim 1/xⁿ = 0.",
     ]),
     ("Lever une forme « 0/0 » en un réel a", [
       "Factoriser numérateur et dénominateur par (x − a), puis simplifier.",
       "Avec des racines carrées : multiplier par l'expression conjuguée.",
       "Sinon, reconnaître un taux d'accroissement : lim (x→a) (f(x) − f(a))/(x − a) = f′(a).",
     ]),
     ("Montrer que y = ax + b est asymptote oblique", [
       "Calculer f(x) − (ax + b) et montrer que sa limite en ±∞ vaut 0.",
       "Le signe de f(x) − (ax + b) donne la position de la courbe par rapport à l'asymptote.",
     ]),
   ],
   "pieges": [
     "Écrire « +∞ − ∞ = 0 » ou « ∞/∞ = 1 » : ce sont des formes indéterminées, on ne conclut pas.",
     "Oublier de distinguer limite à gauche et à droite en un point où le dénominateur s'annule : le signe du dénominateur change.",
     "Utiliser la règle du terme de plus haut degré en un réel a : elle ne vaut qu'en ±∞.",
   ],
   "exemple": ("Calculer la limite en +∞ de f(x) = (2x² − 3x + 1)/(x² + 5), puis la limite en 1 de g(x) = (x² − 1)/(x − 1).", [
     "En +∞ : forme ∞/∞. On factorise : f(x) = x²(2 − 3/x + 1/x²) / [x²(1 + 5/x²)] = (2 − 3/x + 1/x²)/(1 + 5/x²).",
     "3/x, 1/x² et 5/x² tendent vers 0, donc lim f = 2/1 = 2. La droite y = 2 est asymptote horizontale.",
     "En 1 : forme 0/0. x² − 1 = (x − 1)(x + 1), donc g(x) = x + 1 pour x ≠ 1.",
     "lim (x→1) g(x) = 2.",
   ]),
   "exam": "Au BAC, l'étude de fonction commence presque toujours par les limites aux bornes et les asymptotes (1 à 2 points). Justifie chaque forme indéterminée levée.",
  },
  {"t": "Continuité et théorème des valeurs intermédiaires", "p": 0,
   "cles": [
     "f est continue en a si lim (x→a) f(x) = f(a). Les polynômes, fractions rationnelles, racines, ln, exp, sin, cos sont continues sur leur ensemble de définition.",
     "Sommes, produits, quotients (dénominateur non nul) et composées de fonctions continues sont continues.",
     "Théorème des valeurs intermédiaires (TVI) : si f est continue sur [a ; b], pour tout k compris entre f(a) et f(b), l'équation f(x) = k a au moins une solution dans [a ; b].",
     "Corollaire (bijection) : si f est continue et strictement monotone sur [a ; b], l'équation f(x) = k a une solution unique pour tout k entre f(a) et f(b).",
     "Une fonction continue strictement monotone sur un intervalle I réalise une bijection de I sur f(I) ; sa réciproque f⁻¹ a le même sens de variation et sa courbe est symétrique de celle de f par rapport à la droite y = x.",
     "Prolongement par continuité : si f n'est pas définie en a mais lim (x→a) f(x) = L (réel), on pose f(a) = L.",
   ],
   "methodes": [
     ("Montrer que f(x) = 0 a une unique solution α dans [a ; b]", [
       "Dire que f est continue sur [a ; b] (citer pourquoi).",
       "Dire que f est strictement monotone sur [a ; b] (s'appuyer sur le tableau de variations).",
       "Montrer que f(a) et f(b) sont de signes contraires (f(a) × f(b) < 0).",
       "Conclure par le corollaire du TVI.",
     ]),
     ("Encadrer α à 10⁻² près", [
       "Calculer f à pas de 0,1 puis de 0,01 (calculatrice) et repérer le changement de signe.",
       "Écrire l'encadrement : par exemple 1,32 < α < 1,33.",
     ]),
   ],
   "pieges": [
     "Oublier la stricte monotonie : sans elle, on prouve l'existence mais pas l'unicité.",
     "Confondre f(I) avec [f(a) ; f(b)] quand f est décroissante : f(I) = [f(b) ; f(a)].",
   ],
   "exemple": ("Montrer que x³ + x − 1 = 0 admet une unique solution α dans [0 ; 1] et en donner un encadrement d'amplitude 0,1.", [
     "f(x) = x³ + x − 1 est un polynôme, donc continue sur [0 ; 1].",
     "f′(x) = 3x² + 1 > 0, donc f est strictement croissante sur [0 ; 1].",
     "f(0) = −1 < 0 et f(1) = 1 > 0. D'après le corollaire du TVI, α existe et est unique.",
     "f(0,6) = −0,184 < 0 et f(0,7) = 0,043 > 0, donc 0,6 < α < 0,7.",
   ]),
   "exam": "Question classique de l'étude de fonction : « Montrer que l'équation f(x) = 0 admet une solution unique α ; donner un encadrement de α ». Puis α sert à étudier le signe d'une fonction auxiliaire.",
  },
  {"t": "Dérivabilité et calcul de dérivées", "p": 1,
   "cles": [
     "f est dérivable en a si le taux (f(a + h) − f(a))/h a une limite finie quand h → 0 ; cette limite est f′(a).",
     "Tangente au point d'abscisse a : y = f′(a)(x − a) + f(a).",
     "Si la limite du taux est infinie, la courbe a une tangente verticale ; si les limites à gauche et à droite diffèrent, on a un point anguleux (deux demi-tangentes).",
     "Dérivées usuelles : (xⁿ)′ = n xⁿ⁻¹ ; (1/x)′ = −1/x² ; (√x)′ = 1/(2√x) ; (ln x)′ = 1/x ; (eˣ)′ = eˣ ; (sin x)′ = cos x ; (cos x)′ = −sin x.",
     "Opérations : (uv)′ = u′v + uv′ ; (u/v)′ = (u′v − uv′)/v² ; (uⁿ)′ = n u′ uⁿ⁻¹ ; (√u)′ = u′/(2√u) ; (ln u)′ = u′/u ; (eᵘ)′ = u′eᵘ ; (v∘u)′ = u′ × v′∘u.",
     "Dérivée de la réciproque : (f⁻¹)′(y) = 1 / f′(f⁻¹(y)) si f′(f⁻¹(y)) ≠ 0.",
     "Inégalité des accroissements finis : si m ≤ f′(x) ≤ M sur [a ; b], alors m(b − a) ≤ f(b) − f(a) ≤ M(b − a). Si |f′| ≤ M, alors |f(b) − f(a)| ≤ M|b − a|.",
   ],
   "methodes": [
     ("Étudier la dérivabilité en un point « à problème » (racine, valeur absolue)", [
       "Écrire le taux d'accroissement (f(x) − f(a))/(x − a).",
       "Calculer sa limite à gauche et à droite.",
       "Conclure : limite finie et égale des deux côtés → dérivable ; limites finies différentes → point anguleux ; limite infinie → tangente verticale.",
     ]),
     ("Utiliser l'inégalité des accroissements finis (suites récurrentes)", [
       "Majorer |f′(x)| par une constante k < 1 sur l'intervalle I stable.",
       "En déduire |u(n+1) − α| ≤ k|u(n) − α|, puis par récurrence |u(n) − α| ≤ kⁿ|u(0) − α|.",
       "Comme 0 < k < 1, kⁿ → 0 donc u(n) → α.",
     ]),
   ],
   "pieges": [
     "Oublier la dérivée intérieure : (e²ˣ)′ = 2e²ˣ et non e²ˣ ; (ln(x² + 1))′ = 2x/(x² + 1).",
     "Inverser l'ordre dans (u/v)′ : c'est u′v − uv′ au numérateur.",
     "Croire que continue entraîne dérivable : √x est continue en 0 mais pas dérivable.",
   ],
   "exemple": ("Soit f(x) = x√x sur [0 ; +∞[. f est-elle dérivable en 0 ? Calculer f′(x) pour x > 0.", [
     "Taux en 0 : (f(x) − f(0))/x = x√x / x = √x.",
     "lim (x→0⁺) √x = 0 : limite finie, donc f est dérivable à droite en 0 et f′(0) = 0 (tangente horizontale).",
     "Pour x > 0 : f′(x) = 1 × √x + x × 1/(2√x) = √x + √x/2 = (3/2)√x.",
   ]),
   "exam": "Tombe dans chaque problème : calcul de f′, équation de tangente, et souvent l'étude de la dérivabilité en une borne. L'inégalité des accroissements finis revient dans les suites u(n+1) = f(u(n)) (série S1 surtout).",
  },
  {"t": "Étude complète d'une fonction", "p": 1,
   "cles": [
     "Plan type : ensemble de définition → limites et asymptotes → dérivée et son signe → tableau de variations → points particuliers (tangentes, intersections avec les axes) → courbe.",
     "f′ > 0 sur un intervalle → f strictement croissante ; f′ < 0 → strictement décroissante ; f′ s'annule en changeant de signe → extremum local.",
     "Parité : f paire si f(−x) = f(x) (courbe symétrique par rapport à (Oy)) ; impaire si f(−x) = −f(x) (symétrique par rapport à O).",
     "Centre de symétrie Ω(a ; b) : f(2a − x) + f(x) = 2b. Axe de symétrie x = a : f(2a − x) = f(x).",
     "Point d'inflexion : la dérivée seconde f″ s'annule en changeant de signe ; la courbe traverse sa tangente.",
     "Position relative de deux courbes Cf et Cg : étudier le signe de f(x) − g(x).",
     "Fonction périodique de période T : f(x + T) = f(x) ; on l'étudie sur un intervalle de longueur T.",
   ],
   "methodes": [
     ("Étudier le signe de f′ quand on ne sait pas résoudre f′(x) = 0", [
       "Poser une fonction auxiliaire g (souvent le numérateur de f′).",
       "Étudier les variations de g, puis utiliser le TVI pour trouver α où g s'annule.",
       "En déduire le signe de g, donc de f′, puis exprimer f(α) en utilisant g(α) = 0.",
     ]),
     ("Tracer la courbe proprement", [
       "Placer d'abord les asymptotes en pointillés et les tangentes horizontales.",
       "Placer les points du tableau de variations et quelques points calculés.",
       "Respecter les positions par rapport aux asymptotes.",
     ]),
   ],
   "pieges": [
     "Tableau de variations sans les limites aux bornes ni les valeurs des extrema.",
     "Confondre le signe de f et le signe de f′.",
     "Oublier de vérifier que 2a − x est dans l'ensemble de définition pour une symétrie.",
   ],
   "exemple": ("f(x) = x + 1 + 4/(x − 1) sur ℝ \\ {1}. Étudier les variations et les asymptotes.", [
     "Limites : en ±∞, 4/(x − 1) → 0 donc f → ±∞ ; en 1⁺, f → +∞ ; en 1⁻, f → −∞ : asymptote verticale x = 1.",
     "f(x) − (x + 1) = 4/(x − 1) → 0 en ±∞ : y = x + 1 est asymptote oblique. Courbe au-dessus pour x > 1, en dessous pour x < 1.",
     "f′(x) = 1 − 4/(x − 1)² = [(x − 1)² − 4]/(x − 1)² = (x − 3)(x + 1)/(x − 1)².",
     "f′ > 0 sur ]−∞ ; −1[ et ]3 ; +∞[, f′ < 0 sur ]−1 ; 1[ et ]1 ; 3[. Maximum local f(−1) = −2, minimum local f(3) = 6.",
     "Centre de symétrie : f(2 − x) + f(x) = 4, donc Ω(1 ; 2) est centre de symétrie.",
   ]),
   "exam": "C'est le problème du BAC (8 à 10 points sur 20). Il enchaîne souvent : fonction auxiliaire g, étude de f, courbe, puis calcul d'aire avec une intégrale et parfois une suite.",
  },
  {"t": "Fonction logarithme népérien", "p": 2,
   "cles": [
     "ln est définie sur ]0 ; +∞[, ln 1 = 0, ln e = 1, (ln x)′ = 1/x : ln est strictement croissante.",
     "ln(ab) = ln a + ln b ; ln(a/b) = ln a − ln b ; ln(1/a) = −ln a ; ln(aⁿ) = n ln a ; ln √a = (1/2) ln a.",
     "ln a = ln b ⟺ a = b ; ln a < ln b ⟺ a < b (a, b > 0). ln x < 0 sur ]0 ; 1[, ln x > 0 sur ]1 ; +∞[.",
     "Limites : lim (x→+∞) ln x = +∞ ; lim (x→0⁺) ln x = −∞ ; lim (x→+∞) (ln x)/x = 0 ; lim (x→0⁺) x ln x = 0 ; lim (x→0) ln(1 + x)/x = 1.",
     "ln u est définie quand u(x) > 0 ; (ln u)′ = u′/u. ln|u| a aussi pour dérivée u′/u (u ≠ 0).",
     "Logarithme décimal : log x = ln x / ln 10, log 10ⁿ = n (utilisé pour le pH en chimie).",
   ],
   "methodes": [
     ("Résoudre une équation avec ln", [
       "Écrire les conditions d'existence (chaque argument > 0) et en déduire l'ensemble de résolution.",
       "Regrouper en un seul ln de chaque côté avec les propriétés algébriques.",
       "Utiliser ln A = ln B ⟺ A = B, résoudre, puis garder seulement les solutions qui vérifient les conditions.",
     ]),
     ("Résoudre une équation du type a(ln x)² + b ln x + c = 0", [
       "Poser X = ln x et résoudre aX² + bX + c = 0.",
       "Revenir à x = e^X pour chaque solution.",
     ]),
   ],
   "pieges": [
     "Écrire ln(a + b) = ln a + ln b : c'est faux.",
     "Oublier les conditions d'existence : ln(x − 2) + ln(x + 1) n'existe que pour x > 2.",
     "Diviser par ln x sans vérifier qu'il n'est pas nul.",
   ],
   "exemple": ("Résoudre ln(x − 1) + ln(x + 1) = ln 3.", [
     "Conditions : x − 1 > 0 et x + 1 > 0, donc x > 1.",
     "ln[(x − 1)(x + 1)] = ln 3 ⟺ x² − 1 = 3 ⟺ x² = 4 ⟺ x = 2 ou x = −2.",
     "Seul x = 2 vérifie x > 1. S = {2}.",
   ]),
   "exam": "Fonctions du type f(x) = x − ln x, (ln x)/x, x ln x − x… Les limites par croissances comparées et les équations avec conditions d'existence reviennent chaque année.",
  },
  {"t": "Fonction exponentielle et fonctions puissances", "p": 2,
   "cles": [
     "exp est la réciproque de ln : y = eˣ ⟺ x = ln y (y > 0). eˣ > 0 pour tout réel x, e⁰ = 1, e¹ = e ≈ 2,718.",
     "eᵃ⁺ᵇ = eᵃ eᵇ ; eᵃ⁻ᵇ = eᵃ/eᵇ ; e⁻ᵃ = 1/eᵃ ; (eᵃ)ⁿ = eⁿᵃ ; ln(eˣ) = x ; e^(ln x) = x pour x > 0.",
     "(eˣ)′ = eˣ, (eᵘ)′ = u′eᵘ : exp est strictement croissante sur ℝ.",
     "Limites : lim (x→+∞) eˣ = +∞ ; lim (x→−∞) eˣ = 0 ; lim (x→+∞) eˣ/x = +∞ ; lim (x→−∞) x eˣ = 0 ; lim (x→0) (eˣ − 1)/x = 1.",
     "Croissances comparées : en +∞, eˣ l'emporte sur toute puissance de x, qui l'emporte sur ln x.",
     "Puissance réelle : pour a > 0, aˣ = e^(x ln a). Si a > 1, x ↦ aˣ croît ; si 0 < a < 1, elle décroît.",
   ],
   "methodes": [
     ("Résoudre une équation ou inéquation avec exp", [
       "Isoler eᵘ, puis appliquer ln (eᵘ = k ⟺ u = ln k si k > 0 ; aucune solution si k ≤ 0).",
       "Pour ae²ˣ + beˣ + c = 0, poser X = eˣ (X > 0) et résoudre l'équation du second degré.",
     ]),
     ("Lever une indétermination avec exp", [
       "Mettre eˣ (ou x) en facteur et utiliser les croissances comparées.",
       "Exemple : x − eˣ = eˣ(x/eˣ − 1) → −∞ en +∞.",
     ]),
   ],
   "pieges": [
     "Écrire eᵃ⁺ᵇ = eᵃ + eᵇ.",
     "Garder une solution X ≤ 0 après avoir posé X = eˣ.",
     "Oublier que eˣ ne s'annule jamais : le signe de (x − 1)eˣ est celui de x − 1.",
   ],
   "exemple": ("Résoudre e²ˣ − 3eˣ + 2 = 0.", [
     "On pose X = eˣ > 0 : X² − 3X + 2 = 0, Δ = 9 − 8 = 1.",
     "X = 1 ou X = 2, toutes deux positives.",
     "eˣ = 1 ⟺ x = 0 ; eˣ = 2 ⟺ x = ln 2. S = {0 ; ln 2}.",
   ]),
   "exam": "Fonctions du type f(x) = (x + 1)e⁻ˣ, x − 1 + e⁻ˣ… avec asymptote oblique, calcul d'aire par intégration par parties. Les équations par changement de variable X = eˣ sont fréquentes.",
  },
  {"t": "Suites numériques", "p": 3,
   "cles": [
     "Suite arithmétique : u(n+1) = u(n) + r ; u(n) = u(0) + nr ; somme de termes consécutifs = nombre de termes × (premier + dernier)/2.",
     "Suite géométrique : u(n+1) = q u(n) ; u(n) = u(0) qⁿ ; somme = premier terme × (1 − q^(nombre de termes))/(1 − q) si q ≠ 1.",
     "Limite de qⁿ : 0 si −1 < q < 1 ; +∞ si q > 1 ; vaut 1 si q = 1 ; pas de limite si q ≤ −1.",
     "Sens de variation : étudier le signe de u(n+1) − u(n), ou comparer u(n+1)/u(n) à 1 si u(n) > 0.",
     "Toute suite croissante et majorée converge ; toute suite décroissante et minorée converge.",
     "Suites adjacentes : (u) croissante, (v) décroissante et lim (v − u) = 0 : elles convergent vers la même limite.",
     "Si u(n+1) = f(u(n)) avec f continue et u(n) → L, alors L = f(L) (point fixe).",
   ],
   "methodes": [
     ("Démontrer par récurrence", [
       "Initialisation : vérifier la propriété pour le premier rang.",
       "Hérédité : supposer la propriété vraie au rang n et montrer qu'elle est vraie au rang n + 1.",
       "Conclure : la propriété est vraie pour tout n.",
     ]),
     ("Étudier une suite u(n+1) = a u(n) + b avec une suite auxiliaire", [
       "Montrer que v(n) = u(n) − α (α donné) est géométrique : calculer v(n+1) et l'écrire q v(n).",
       "Exprimer v(n), puis u(n) = v(n) + α.",
       "En déduire la limite de u(n).",
     ]),
   ],
   "pieges": [
     "Dans l'hérédité, utiliser ce qu'on veut démontrer au lieu de l'hypothèse de récurrence.",
     "Se tromper dans le nombre de termes : de u(0) à u(n), il y a n + 1 termes.",
     "Conclure « croissante donc tend vers +∞ » : une suite croissante peut converger.",
   ],
   "exemple": ("u(0) = 2 et u(n+1) = 0,5 u(n) + 3. On pose v(n) = u(n) − 6. Montrer que v est géométrique et trouver lim u(n).", [
     "v(n+1) = u(n+1) − 6 = 0,5 u(n) − 3 = 0,5 (u(n) − 6) = 0,5 v(n) : géométrique de raison 0,5.",
     "v(0) = 2 − 6 = −4, donc v(n) = −4 × 0,5ⁿ et u(n) = 6 − 4 × 0,5ⁿ.",
     "Comme 0 < 0,5 < 1, 0,5ⁿ → 0, donc lim u(n) = 6.",
   ]),
   "exam": "Un exercice de 4 à 5 points ou la dernière partie du problème : récurrence, suite auxiliaire géométrique, somme de termes, limite. En S1, suites définies par une intégrale ou par u(n+1) = f(u(n)) avec accroissements finis.",
  },
  {"t": "Primitives", "p": 4,
   "cles": [
     "F est une primitive de f sur I si F′ = f sur I. Deux primitives diffèrent d'une constante. Il existe une unique primitive prenant une valeur donnée en un point.",
     "Primitives usuelles : xⁿ → xⁿ⁺¹/(n + 1) (n ≠ −1) ; 1/x → ln|x| ; 1/x² → −1/x ; 1/√x → 2√x ; eˣ → eˣ ; cos x → sin x ; sin x → −cos x.",
     "Formes composées : u′uⁿ → uⁿ⁺¹/(n + 1) ; u′/u → ln|u| ; u′/u² → −1/u ; u′/√u → 2√u ; u′eᵘ → eᵘ ; u′cos u → sin u ; u′ sin u → −cos u.",
     "cos(ax + b) → (1/a) sin(ax + b) ; e^(ax + b) → (1/a) e^(ax + b).",
   ],
   "methodes": [
     ("Trouver une primitive d'une forme composée", [
       "Repérer u et vérifier si u′ apparaît (à une constante près).",
       "Ajuster le coefficient : x/(x² + 1) = (1/2) × 2x/(x² + 1) → (1/2) ln(x² + 1).",
     ]),
     ("Primitive d'une fraction rationnelle", [
       "Décomposer : trouver a, b, c tels que f(x) = ax + b + c/(x − 1) par identification.",
       "Puis primitiver chaque terme.",
     ]),
     ("Linéariser pour primitiver cos² ou sin²", [
       "cos² x = (1 + cos 2x)/2 et sin² x = (1 − cos 2x)/2.",
       "Primitive de cos² x : x/2 + (sin 2x)/4.",
     ]),
   ],
   "pieges": [
     "Oublier le facteur 1/a pour e^(ax) ou cos(ax).",
     "Primitive de 1/x² donnée comme ln(x²).",
   ],
   "exemple": ("Trouver la primitive F de f(x) = 2x e^(x²) sur ℝ telle que F(0) = 3.", [
     "f = u′eᵘ avec u = x², donc F(x) = e^(x²) + C.",
     "F(0) = 1 + C = 3, donc C = 2 et F(x) = e^(x²) + 2.",
   ]),
   "exam": "Sert surtout dans les calculs d'intégrales et d'aires. Une question « vérifier que F est une primitive de f » se règle simplement en dérivant F.",
  },
  {"t": "Calcul intégral et aires", "p": 4,
   "cles": [
     "∫ₐᵇ f(x) dx = F(b) − F(a), où F est une primitive de f.",
     "Relation de Chasles : ∫ₐᶜ f = ∫ₐᵇ f + ∫ᵇᶜ f. Linéarité : ∫ (αf + βg) = α∫f + β∫g.",
     "Positivité : si f ≥ 0 sur [a ; b] (a ≤ b), alors ∫ₐᵇ f ≥ 0. Si f ≤ g, ∫f ≤ ∫g.",
     "Valeur moyenne de f sur [a ; b] : μ = (1/(b − a)) ∫ₐᵇ f(x) dx.",
     "Intégration par parties : ∫ₐᵇ u v′ = [uv]ₐᵇ − ∫ₐᵇ u′v.",
     "Aire entre Cf et l'axe (Ox) pour f ≥ 0 : A = ∫ₐᵇ f(x) dx unités d'aire (u.a.). Entre deux courbes, f ≥ g : A = ∫ₐᵇ (f − g).",
     "Conversion : 1 u.a. = ‖i‖ × ‖j‖ ; avec des unités de 2 cm sur chaque axe, 1 u.a. = 4 cm².",
     "Volume d'un solide de révolution autour de (Ox) : V = π ∫ₐᵇ f(x)² dx.",
   ],
   "methodes": [
     ("Choisir u et v′ dans une intégration par parties", [
       "Prendre pour u ce qui se simplifie en dérivant (polynôme, ln x).",
       "Prendre pour v′ ce qui se primitive facilement (eˣ, cos x, polynôme quand l'autre facteur est ln x).",
       "Exemple : ∫ x eˣ → u = x, v′ = eˣ ; ∫ ln x → u = ln x, v′ = 1.",
     ]),
     ("Calculer une aire en cm²", [
       "Étudier le signe de f (ou de f − g) sur l'intervalle.",
       "Calculer l'intégrale (en découpant si le signe change).",
       "Multiplier par l'aire d'une unité en cm².",
     ]),
   ],
   "pieges": [
     "Donner une aire négative : si f ≤ 0, l'aire vaut −∫f.",
     "Oublier de convertir les u.a. en cm².",
     "Oublier le crochet [uv]ₐᵇ dans l'intégration par parties.",
   ],
   "exemple": ("Calculer I = ∫₀¹ x eˣ dx.", [
     "On pose u = x, v′ = eˣ, donc u′ = 1, v = eˣ.",
     "I = [x eˣ]₀¹ − ∫₀¹ eˣ dx = e − [eˣ]₀¹ = e − (e − 1) = 1.",
   ]),
   "exam": "Dernière partie du problème : aire du domaine entre la courbe, l'asymptote et deux droites, souvent avec une intégration par parties, puis limite quand une borne tend vers l'infini.",
  },
  {"t": "Équations différentielles", "p": 5,
   "cles": [
     "y′ = ay (a réel) : solutions y(x) = C e^(ax), C réel.",
     "y′ = ay + b (a ≠ 0) : solutions y(x) = C e^(ax) − b/a. La solution constante est −b/a.",
     "y″ + ω² y = 0 (ω > 0) : solutions y(x) = A cos(ωx) + B sin(ωx), ou y(x) = R cos(ωx + φ). C'est l'équation des oscillations en physique.",
     "y″ + a y′ + b y = 0 : équation caractéristique r² + a r + b = 0, de discriminant Δ.",
     "Δ > 0 (racines r₁, r₂) : y = A e^(r₁x) + B e^(r₂x). Δ = 0 (racine double r) : y = (Ax + B) e^(rx). Δ < 0 (racines α ± iβ) : y = e^(αx)(A cos βx + B sin βx).",
     "Avec second membre : solution générale = solution particulière + solution générale de l'équation sans second membre.",
   ],
   "methodes": [
     ("Trouver la solution qui vérifie des conditions initiales", [
       "Écrire la solution générale avec ses constantes.",
       "Traduire chaque condition (y(0) = …, y′(0) = …) en équation.",
       "Résoudre le système pour trouver les constantes.",
     ]),
     ("Équation avec second membre (E) : y″ + ay′ + by = g(x)", [
       "Vérifier (ou chercher) une solution particulière p de même forme que g.",
       "Montrer que y est solution de (E) ⟺ y − p est solution de l'équation sans second membre.",
       "Conclure : y = p + solution générale homogène.",
     ]),
   ],
   "pieges": [
     "Oublier qu'il y a deux constantes pour une équation d'ordre 2.",
     "Erreur de signe dans l'équation caractéristique (r² + ar + b, pas r² − ar + b).",
   ],
   "exemple": ("Résoudre y″ − 3y′ + 2y = 0 avec y(0) = 1 et y′(0) = 0.", [
     "Équation caractéristique r² − 3r + 2 = 0 : r = 1 ou r = 2.",
     "y = A eˣ + B e²ˣ et y′ = A eˣ + 2B e²ˣ.",
     "y(0) = A + B = 1 et y′(0) = A + 2B = 0, donc B = −1 et A = 2.",
     "y(x) = 2eˣ − e²ˣ.",
   ]),
   "exam": "Souvent un exercice court (3 points) ou le début du problème : trouver une solution particulière puis la fonction f qui sera étudiée. Lien direct avec les circuits RC, RL et LC en physique.",
  },
  {"t": "Nombres complexes : forme algébrique et équations", "p": 6,
   "cles": [
     "z = a + ib, i² = −1. Re(z) = a, Im(z) = b. Conjugué : z̄ = a − ib ; z z̄ = a² + b².",
     "Module |z| = √(a² + b²) ; |zz′| = |z||z′| ; |z/z′| = |z|/|z′|.",
     "Pour mettre un quotient sous forme algébrique, on multiplie par le conjugué du dénominateur.",
     "z réel ⟺ z = z̄ ; z imaginaire pur ⟺ z̄ = −z.",
     "Équation az² + bz + c = 0 (coefficients réels), Δ = b² − 4ac. Si Δ < 0 : z = (−b ± i√(−Δ))/(2a), deux solutions conjuguées.",
     "Racines carrées de Δ complexe : chercher δ = x + iy avec x² − y² = Re(Δ), 2xy = Im(Δ) et x² + y² = |Δ|.",
     "Polynôme P de degré 3 : si P(z₀) = 0, P(z) = (z − z₀)Q(z) avec Q de degré 2 (identification ou division).",
   ],
   "methodes": [
     ("Résoudre une équation de degré 3", [
       "Vérifier que la racine donnée (souvent réelle ou imaginaire pure) annule P.",
       "Factoriser P(z) = (z − z₀)(az² + bz + c) par identification des coefficients.",
       "Résoudre l'équation du second degré.",
     ]),
     ("Trouver l'ensemble des points M(z) vérifiant une condition", [
       "Poser z = x + iy et traduire la condition en équation en x et y.",
       "Reconnaître une droite, un cercle (x − a)² + (y − b)² = r², ou utiliser |z − zA| = |z − zB| (médiatrice).",
     ]),
   ],
   "pieges": [
     "Écrire |a + ib| = a + b.",
     "Oublier que (a + ib)² = a² − b² + 2iab.",
   ],
   "exemple": ("Résoudre z² − 2z + 5 = 0.", [
     "Δ = 4 − 20 = −16 = (4i)².",
     "z₁ = (2 − 4i)/2 = 1 − 2i et z₂ = 1 + 2i.",
   ]),
   "exam": "L'exercice de complexes (4 à 5 points) commence presque toujours par la résolution d'une équation de degré 2 ou 3, puis place les points solutions et étudie le triangle ou le quadrilatère formé.",
  },
  {"t": "Nombres complexes : forme trigonométrique, exponentielle et géométrie", "p": 6,
   "cles": [
     "z = r(cos θ + i sin θ) = r e^(iθ), avec r = |z| et θ = arg z (à 2π près).",
     "arg(zz′) = arg z + arg z′ ; arg(z/z′) = arg z − arg z′ ; arg(zⁿ) = n arg z. Formule de Moivre : (cos θ + i sin θ)ⁿ = cos nθ + i sin nθ.",
     "Formules d'Euler : cos θ = (e^(iθ) + e^(−iθ))/2 ; sin θ = (e^(iθ) − e^(−iθ))/(2i).",
     "Distance : AB = |zB − zA|. Angle : (u⃗, v⃗) = arg(z_v / z_u) ; (AB⃗, AC⃗) = arg((zC − zA)/(zB − zA)).",
     "A, B, C alignés ⟺ (zC − zA)/(zB − zA) réel. (AB) ⟂ (AC) ⟺ ce quotient est imaginaire pur.",
     "Si (zC − zA)/(zB − zA) = e^(±iπ/3) : ABC est équilatéral. Si c'est ±i : ABC est rectangle isocèle en A.",
     "Racines n-ièmes de l'unité : zₖ = e^(2ikπ/n), k = 0, …, n − 1 ; elles forment un polygone régulier et leur somme est nulle (n ≥ 2).",
   ],
   "methodes": [
     ("Passer de la forme algébrique à la forme exponentielle", [
       "Calculer r = |z|.",
       "Trouver θ tel que cos θ = a/r et sin θ = b/r (valeurs remarquables).",
       "Écrire z = r e^(iθ).",
     ]),
     ("Déterminer la nature d'un triangle ABC", [
       "Calculer q = (zC − zA)/(zB − zA) sous forme exponentielle.",
       "|q| donne le rapport AC/AB ; arg q donne l'angle en A.",
       "|q| = 1 et arg q = ±π/2 → rectangle isocèle en A ; |q| = 1 et arg q = ±π/3 → équilatéral.",
     ]),
   ],
   "pieges": [
     "Prendre θ avec tan θ = b/a sans vérifier le quadrant (cos et sin doivent avoir les bons signes).",
     "Oublier « à 2π près » pour un argument.",
   ],
   "exemple": ("Écrire z = 1 + i√3 sous forme exponentielle et calculer z⁶.", [
     "|z| = √(1 + 3) = 2 ; cos θ = 1/2 et sin θ = √3/2, donc θ = π/3.",
     "z = 2e^(iπ/3), donc z⁶ = 2⁶ e^(i6π/3) = 64 e^(2iπ) = 64.",
   ]),
   "exam": "Questions types : écrire sous forme exponentielle, calculer une puissance, prouver la nature d'un triangle, déterminer un ensemble de points. En S1, linéarisation et calcul de cos(π/12) par deux méthodes.",
  },
  {"t": "Transformations du plan : similitudes", "p": 6,
   "cles": [
     "Translation de vecteur u⃗(b) : z′ = z + b. Homothétie de centre Ω(ω) et de rapport k réel : z′ − ω = k(z − ω).",
     "Rotation de centre Ω(ω) et d'angle θ : z′ − ω = e^(iθ)(z − ω).",
     "Similitude directe : z′ = az + b, a complexe non nul. Si a = 1, c'est une translation ; sinon centre ω = b/(1 − a), rapport k = |a|, angle θ = arg a.",
     "Forme réduite : s = h ∘ r = r ∘ h (homothétie de rapport k et rotation d'angle θ, même centre).",
     "Une similitude directe conserve les angles orientés et multiplie les distances par k, les aires par k².",
     "Il existe une unique similitude directe qui envoie A sur A′ et B sur B′ (A ≠ B, A′ ≠ B′).",
     "Similitude indirecte (S1) : z′ = a z̄ + b.",
   ],
   "methodes": [
     ("Déterminer les éléments caractéristiques de z′ = az + b", [
       "Centre : résoudre ω = aω + b, d'où ω = b/(1 − a).",
       "Rapport : k = |a|. Angle : θ = arg a.",
     ]),
     ("Trouver l'écriture complexe de la similitude envoyant A sur A′ et B sur B′", [
       "Écrire zA′ = a zA + b et zB′ = a zB + b.",
       "Soustraire : a = (zA′ − zB′)/(zA − zB), puis b = zA′ − a zA.",
     ]),
   ],
   "pieges": [
     "Confondre rapport (|a|) et a lui-même quand a est complexe.",
     "Oublier qu'une homothétie de rapport négatif est aussi une rotation d'angle π composée avec une homothétie de rapport |k|.",
   ],
   "exemple": ("Donner la nature et les éléments de s : z′ = (1 + i) z + 1.", [
     "a = 1 + i ≠ 1 : similitude directe.",
     "k = |1 + i| = √2 ; θ = arg(1 + i) = π/4.",
     "ω = 1/(1 − 1 − i) = 1/(−i) = i. Centre Ω(i), rapport √2, angle π/4.",
   ]),
   "exam": "Surtout en S1 et S3 : exercice de géométrie avec similitudes, suites de points M(n+1) = s(M(n)) et distances qui forment une suite géométrique.",
  },
  {"t": "Dénombrement", "p": 7,
   "cles": [
     "Principe multiplicatif : si un choix se fait en p étapes avec n₁, n₂, …, n_p possibilités, il y a n₁ × n₂ × … × n_p résultats.",
     "p-listes (tirages successifs avec remise, ordre compte) : nᵖ.",
     "Arrangements (successifs sans remise, ordre compte) : Aₙᵖ = n!/(n − p)!.",
     "Permutations de n objets : n!. Avec des objets répétés : n!/(n₁! n₂! …).",
     "Combinaisons (simultanés, ordre ne compte pas) : Cₙᵖ = n!/(p!(n − p)!).",
     "Propriétés : Cₙᵖ = Cₙⁿ⁻ᵖ ; Cₙᵖ + Cₙᵖ⁺¹ = Cₙ₊₁ᵖ⁺¹ (triangle de Pascal). Binôme : (a + b)ⁿ = Σ Cₙᵏ aᵏ bⁿ⁻ᵏ.",
   ],
   "methodes": [
     ("Choisir la bonne formule", [
       "L'ordre compte-t-il ? Non → combinaisons (tirage simultané).",
       "Oui : y a-t-il remise ? Oui → nᵖ ; non → arrangements.",
     ]),
     ("Compter « au moins un »", [
       "Passer par le contraire : nombre total − nombre de cas « aucun ».",
     ]),
   ],
   "pieges": [
     "Utiliser Aₙᵖ pour un tirage simultané.",
     "Additionner au lieu de multiplier pour des étapes successives (ou l'inverse pour des cas disjoints : « ou » → on additionne).",
   ],
   "exemple": ("Une urne contient 5 boules rouges et 3 vertes. On tire simultanément 3 boules. Combien de tirages contiennent exactement 2 rouges ?", [
     "Nombre total : C₈³ = 56.",
     "2 rouges parmi 5 et 1 verte parmi 3 : C₅² × C₃¹ = 10 × 3 = 30 tirages.",
   ]),
   "exam": "Base de tout l'exercice de probabilités : bien identifier le type de tirage dès la première question.",
  },
  {"t": "Probabilités et variables aléatoires", "p": 7,
   "cles": [
     "Équiprobabilité : P(A) = nombre de cas favorables / nombre de cas possibles. P(Ā) = 1 − P(A).",
     "P(A ∪ B) = P(A) + P(B) − P(A ∩ B).",
     "Probabilité conditionnelle : P_B(A) = P(A ∩ B)/P(B), donc P(A ∩ B) = P(B) × P_B(A).",
     "Formule des probabilités totales : si B₁, …, Bₙ partitionnent l'univers, P(A) = Σ P(Bᵢ) P_Bᵢ(A). L'arbre pondéré la traduit.",
     "A et B indépendants ⟺ P(A ∩ B) = P(A) × P(B).",
     "Variable aléatoire X : loi = tableau des valeurs xᵢ et des probabilités pᵢ (Σ pᵢ = 1). E(X) = Σ xᵢpᵢ ; V(X) = Σ xᵢ²pᵢ − E(X)² ; σ(X) = √V(X).",
     "Fonction de répartition : F(x) = P(X ≤ x), fonction en escalier croissante de 0 à 1.",
     "Loi binomiale B(n ; p) : n épreuves identiques indépendantes à deux issues. P(X = k) = Cₙᵏ pᵏ (1 − p)ⁿ⁻ᵏ ; E(X) = np ; V(X) = np(1 − p).",
   ],
   "methodes": [
     ("Utiliser un arbre pondéré", [
       "Sur chaque branche, écrire la probabilité conditionnelle ; la somme des branches issues d'un nœud vaut 1.",
       "Probabilité d'un chemin = produit des probabilités le long du chemin.",
       "Probabilité d'un événement = somme des chemins qui y mènent.",
     ]),
     ("Reconnaître une loi binomiale", [
       "Justifier : même épreuve répétée n fois, de façon indépendante, avec deux issues (succès de probabilité p).",
       "Alors X = nombre de succès suit B(n ; p).",
     ]),
   ],
   "pieges": [
     "Confondre P_B(A) et P(A ∩ B).",
     "Oublier de vérifier que la somme des probabilités de la loi vaut 1.",
     "Confondre incompatibles (A ∩ B = ∅) et indépendants.",
   ],
   "exemple": ("On lance 4 fois une pièce équilibrée. X = nombre de « pile ». Calculer P(X = 2) et E(X).", [
     "4 épreuves identiques et indépendantes, succès « pile » de probabilité 1/2 : X suit B(4 ; 1/2).",
     "P(X = 2) = C₄² (1/2)² (1/2)² = 6/16 = 3/8.",
     "E(X) = 4 × 1/2 = 2.",
   ]),
   "exam": "Un exercice par sujet (4 à 5 points) : tirages dans une urne, loi de X, espérance, puis répétition de l'expérience avec la loi binomiale et « au moins une fois » : 1 − (1 − p)ⁿ.",
  },
  {"t": "Statistiques à deux variables", "p": 7,
   "cles": [
     "Nuage de points Mᵢ(xᵢ ; yᵢ) ; point moyen G(x̄ ; ȳ).",
     "Variance : V(x) = (1/n) Σ xᵢ² − x̄². Covariance : cov(x, y) = (1/n) Σ xᵢyᵢ − x̄ȳ.",
     "Coefficient de corrélation linéaire : r = cov(x, y)/(σx σy), compris entre −1 et 1. Si |r| ≥ 0,87 environ, l'ajustement affine est justifié.",
     "Droite de régression de y en x : y = ax + b avec a = cov(x, y)/V(x) et b = ȳ − a x̄ (elle passe par G).",
     "Droite de régression de x en y : x = a′y + b′ avec a′ = cov(x, y)/V(y).",
     "Méthode de Mayer : partager le nuage en deux groupes, la droite passe par les deux points moyens G₁ et G₂.",
   ],
   "methodes": [
     ("Faire un ajustement et une prévision", [
       "Calculer x̄, ȳ, V(x), cov(x, y) avec un tableau (colonnes xᵢ², xᵢyᵢ).",
       "Calculer r et conclure sur la pertinence de l'ajustement.",
       "Donner l'équation de la droite, puis remplacer x par la valeur demandée.",
     ]),
   ],
   "pieges": [
     "Oublier de retrancher x̄² ou x̄ȳ dans la variance ou la covariance.",
     "Confondre droite de y en x et droite de x en y.",
   ],
   "exemple": ("Pour x : 1, 2, 3, 4 et y : 3, 5, 6, 8, trouver la droite de régression de y en x.", [
     "x̄ = 2,5 ; ȳ = 5,5. Σxᵢ² = 30, donc V(x) = 30/4 − 6,25 = 1,25.",
     "Σxᵢyᵢ = 3 + 10 + 18 + 32 = 63, cov = 63/4 − 13,75 = 2.",
     "a = 2/1,25 = 1,6 ; b = 5,5 − 1,6 × 2,5 = 1,5. Droite : y = 1,6x + 1,5.",
   ]),
   "exam": "Surtout en série S2 et L : un exercice de 4 à 5 points avec tableau, nuage, coefficient de corrélation, droite de régression et estimation.",
  },
  {"t": "Arithmétique", "p": 8,
   "cles": [
     "Division euclidienne : a = bq + r avec 0 ≤ r < |b|.",
     "Congruences : a ≡ b [n] ⟺ n divise a − b. Elles se conservent par somme, produit et puissance.",
     "PGCD : algorithme d'Euclide (le dernier reste non nul). a et b premiers entre eux ⟺ PGCD(a, b) = 1.",
     "Théorème de Bézout : a et b premiers entre eux ⟺ il existe u, v entiers tels que au + bv = 1.",
     "Théorème de Gauss : si a divise bc et a est premier avec b, alors a divise c.",
     "Petit théorème de Fermat : si p est premier et ne divise pas a, alors aᵖ⁻¹ ≡ 1 [p].",
     "PGCD(a, b) × PPCM(a, b) = |ab|. Tout entier ≥ 2 se décompose de façon unique en produit de nombres premiers.",
   ],
   "methodes": [
     ("Résoudre ax + by = c dans ℤ²", [
       "Vérifier que PGCD(a, b) divise c (sinon pas de solution) et simplifier.",
       "Trouver une solution particulière (x₀ ; y₀) (Euclide remonté ou à vue).",
       "Soustraire : a(x − x₀) = −b(y − y₀), puis Gauss donne x = x₀ + bk et y = y₀ − ak (k ∈ ℤ, a et b premiers entre eux).",
     ]),
     ("Trouver le reste de aⁿ modulo m", [
       "Calculer les premières puissances de a modulo m jusqu'à retrouver 1 (période).",
       "Écrire n = période × q + r et conclure aⁿ ≡ aʳ [m].",
     ]),
   ],
   "pieges": [
     "Diviser les deux membres d'une congruence sans précaution : ce n'est pas permis en général.",
     "Oublier la vérification de Gauss (premiers entre eux) avant de conclure.",
   ],
   "exemple": ("Quel est le reste de 2²⁰²⁶ dans la division par 7 ?", [
     "2¹ ≡ 2, 2² ≡ 4, 2³ = 8 ≡ 1 [7] : période 3.",
     "2026 = 3 × 675 + 1, donc 2²⁰²⁶ = (2³)⁶⁷⁵ × 2 ≡ 1 × 2 = 2 [7].",
     "Le reste est 2.",
   ]),
   "exam": "Séries S1 et S3 uniquement : un exercice de 4 à 5 points (équations diophantiennes, congruences, codage).",
  },
  {"t": "Géométrie dans l'espace", "p": 9,
   "cles": [
     "Produit scalaire : u⃗ · v⃗ = xx′ + yy′ + zz′ ; ‖u⃗‖ = √(x² + y² + z²) ; u⃗ ⟂ v⃗ ⟺ u⃗ · v⃗ = 0.",
     "Représentation paramétrique d'une droite passant par A et dirigée par u⃗ : x = xA + ta, y = yA + tb, z = zA + tc (t réel).",
     "Équation cartésienne d'un plan de vecteur normal n⃗(a ; b ; c) : ax + by + cz + d = 0.",
     "Distance d'un point M au plan P : d = |axM + byM + czM + d| / √(a² + b² + c²).",
     "Produit vectoriel (S1) : u⃗ ∧ v⃗ est orthogonal à u⃗ et v⃗ ; ‖u⃗ ∧ v⃗‖ = aire du parallélogramme ; il sert à trouver un vecteur normal.",
     "Sphère de centre Ω et de rayon R : (x − a)² + (y − b)² + (z − c)² = R². Elle coupe un plan si la distance du centre au plan est inférieure à R.",
     "Volume d'un tétraèdre : V = (1/3) × aire de la base × hauteur.",
   ],
   "methodes": [
     ("Trouver l'équation du plan (ABC)", [
       "Vérifier que A, B, C ne sont pas alignés (AB⃗ et AC⃗ non colinéaires).",
       "Trouver n⃗ orthogonal à AB⃗ et AC⃗ (système ou produit vectoriel).",
       "Écrire ax + by + cz + d = 0 et trouver d avec les coordonnées de A.",
     ]),
     ("Intersection d'une droite et d'un plan", [
       "Remplacer x, y, z de la représentation paramétrique dans l'équation du plan.",
       "Résoudre en t, puis calculer les coordonnées du point.",
     ]),
   ],
   "pieges": [
     "Prendre un vecteur directeur au lieu d'un vecteur normal pour l'équation du plan.",
     "Oublier la valeur absolue dans la formule de distance.",
   ],
   "exemple": ("Distance de A(1 ; 2 ; 3) au plan P : 2x − y + 2z − 1 = 0.", [
     "d = |2 × 1 − 2 + 2 × 3 − 1| / √(4 + 1 + 4) = |5| / 3 = 5/3.",
   ]),
   "exam": "Séries S1 et S3 surtout : exercice de 4 points (plan, droite, sphère, volume de tétraèdre). En S2, la géométrie passe surtout par les complexes.",
  },
]
