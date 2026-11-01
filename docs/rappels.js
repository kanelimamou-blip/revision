"use strict";
// Nouveautés (pastille rouge tant que l'élève n'a pas lu), rappels guidés à la pause de midi et après l'école,
// petites questions à l'élève (réponses visibles dans l'admin), micro et lecture à voix haute dans l'assistant.
(() => {
  // ---------- Nouveautés : ajouter une entrée en tête à chaque changement visible, la pastille se rallume
  const NEWS = [
    ["2026-11-01u", "📚 18 devoirs types en 5e", ["Chaque matière de 5e a 3 devoirs types, un par trimestre : 3 exercices notés sur 20, corrigés étape par étape.", "Rédigés pour l'appli sur le modèle des devoirs de classe (ce ne sont pas des sujets officiels). La 4e suit."]],
    ["2026-11-01t", "📚 18 devoirs types en 6e", ["Chaque matière de 6e a 3 devoirs types, un par trimestre : 3 exercices, notés sur 20, corrigés étape par étape.", "Rédigés pour l'appli sur le modèle des devoirs de classe (ce ne sont pas des sujets officiels). La 5e suit."]],
    ["2026-11-01s", "✅ Plus de 10 000 QCM par classe, synthèses enrichies", ["Le compteur de QCM compte maintenant aussi les questions à nombres nouveaux, qui étaient déjà dans tes quiz : plus de 10 000 QCM différents par classe.", "De la 6e à la 3e, chaque synthèse contient en plus la méthode pas à pas, les pièges fréquents et deux exercices corrigés de plus.", "Les devoirs types arrivent ensuite."]],
    ["2026-11-01r", "✍️ 64 exercices type devoir en 3e", ["64 nouveaux exercices guidés en 3e pour préparer le BFEM, un par chapitre (deux en maths) : PGCD et carrelage, hauteur du baobab avec Thalès, facture Senelec, paludisme, tirailleurs, Grande Muraille verte…", "Rédigés pour l'appli (ce ne sont pas des sujets officiels). Toutes les classes de la 6e à la 3e sont enrichies."]],
    ["2026-11-01q", "✍️ 53 exercices type devoir en 4e", ["53 nouveaux exercices guidés en 4e, un par chapitre (deux en maths), y compris en sciences physiques et en espagnol : échelle contre le mur, trajet Dakar – Touba, commerce triangulaire, résistants…", "Rédigés pour l'appli (ce ne sont pas des sujets officiels). La 3e suit."]],
    ["2026-11-01p", "✍️ 41 exercices type devoir en 5e", ["41 nouveaux exercices guidés en 5e, un par chapitre (deux en maths) : soldes, héritage du troupeau, empires du Ghana, du Mali et songhaï, caravanes…", "Rédigés pour l'appli (ce ne sont pas des sujets officiels). La 4e suit."]],
    ["2026-11-01o", "✍️ 43 exercices type devoir en 6e", ["43 nouveaux exercices guidés en 6e, un par chapitre (deux en maths), avec des situations de la vie courante : marché, champ, voyage, conte…", "Rédigés pour l'appli (ce ne sont pas des sujets officiels). La 5e suit."]],
    ["2026-11-01n", "🧭 Fiches méthode en 3e", ["Chaque chapitre de 3e a maintenant une fiche « Méthode et pièges » orientée BFEM : étapes, erreurs fréquentes, deux exemples corrigés et un exercice guidé.", "Toutes les classes de la 6e à la 3e ont leurs fiches méthode."]],
    ["2026-11-01m", "🧭 Fiches méthode en 4e", ["Chaque chapitre de 4e a maintenant une fiche « Méthode et pièges » : étapes, erreurs fréquentes, deux exemples corrigés et un exercice guidé.", "La 3e suit."]],
    ["2026-11-01l", "🧭 Fiches méthode en 5e", ["Chaque chapitre de 5e a maintenant une fiche « Méthode et pièges » : étapes, erreurs fréquentes, deux exemples corrigés et un exercice guidé.", "La 4e et la 3e suivent."]],
    ["2026-11-01k", "🧭 Fiches méthode en 6e", ["Chaque chapitre de 6e a maintenant une fiche « Méthode et pièges » : les étapes à suivre, les erreurs fréquentes et deux exemples corrigés.", "Chaque fiche a aussi un exercice guidé de 5 questions.", "La 5e, la 4e et la 3e suivent."]],
    ["2026-11-01j", "📚 Cours ×3 en 5e", ["En 5e, chaque chapitre a maintenant 3 cours au lieu d'un : maths, français, SVT, histoire, géographie et anglais.", "Toutes les classes, de la 6e à la Terminale, ont désormais 3 cours par chapitre.", "Ouvre l'onglet Cours pour les voir."]],
    ["2026-11-01i", "📚 Cours ×3 en 4e", ["En 4e, chaque chapitre a maintenant 3 cours au lieu d'un : maths, PC, SVT, français, histoire, géographie, anglais et espagnol.", "Chaque cours a son essentiel, un exemple et un petit exercice guidé.", "Ouvre l'onglet Cours pour les voir."]],
    ["2026-11-01h", "📚 Cours ×3 en 2nde", ["En 2nde, chaque chapitre a maintenant 3 cours au lieu d'un : maths, PC, SVT, français, histoire-géo, anglais et espagnol.", "Chaque cours a son essentiel, un exemple et un petit exercice guidé.", "Ouvre l'onglet Cours pour les voir."]],
    ["2026-11-01g", "📚 Cours ×3 en 6e", ["En 6e, chaque chapitre a maintenant 3 cours au lieu d'un : maths, français, SVT, histoire, géographie et anglais.", "Chaque cours a son essentiel, un exemple et un petit exercice guidé.", "Ouvre l'onglet Cours pour les voir."]],
    ["2026-11-01f", "📚 Cours ×3 en 3e", ["En 3e, chaque chapitre a maintenant 3 cours au lieu d'un : maths, PC, SVT, français, histoire, géographie, anglais et espagnol.", "Chaque cours a son essentiel, un exemple et un petit exercice guidé.", "Ouvre l'onglet Cours pour les voir. La 6e arrive ensuite."]],
    ["2026-11-01e", "📐 Formulaire complet de la 6e à la 1re", ["Le formulaire couvre maintenant toutes les matières et tous les chapitres, de la 6e à la 1re.", "Sciences : formules et valeurs à connaître ; français, histoire-géo, anglais, espagnol : règles et repères à retenir.", "Ouvre-le depuis l'accueil (📐 Formulaire), matière par matière."]],
    ["2026-11-01d", "🎯 Plus de 10 000 questions dans chaque classe", ["Chaque classe, de la 6e à la Terminale, propose maintenant plus de 10 000 questions différentes.", "Maths de 2nde : trigonométrie, pourcentages, statistiques, valeur absolue, droites, cercles et volumes.", "Maths de 5e : proportionnalité, aires, volumes, angles et statistiques.", "Anglais de 5e et de 2nde, histoire-géo de Terminale (calculs sur les puissances et l'intégration régionale)."]],
    ["2026-11-01c", "⚖️ Plus de questions là où le coefficient est fort", ["Les matières à gros coefficient ont maintenant plus de questions que les autres, dans chaque série.", "Terminale L : philosophie (auteurs, citations, œuvres, notions) et français (dates des œuvres) renforcés.", "Première : SVT avec de nouveaux calculs (dorsale, séismes, influx nerveux, glycémie, rein, muscle), histoire-géo, français et anglais enrichis.", "Collège : conjugaison de tous les verbes du 1er et du 2e groupe à tous les temps, homophones et fonctions."]],
    ["2026-11-01b", "📚 Toutes les matières au moins à 500 questions", ["Chaque matière de chaque classe propose maintenant au moins 500 questions différentes.", "Collège : histoire (5e, 4e, 3e), SVT, physique-chimie 4e, géographie 6e et 5e, anglais 6e et français 4e enrichis.", "Espagnol de la 4e à la Terminale : conjugaisons à tous les temps du programme, avec des verbes tirés au hasard.", "Seconde et Première : histoire-géo et français (épopée, registres, versification, théâtre, auteurs) enrichis."]],
    ["2026-11-01a", "📈 Encore plus de questions en Terminale et en Première", ["Terminale : philosophie, histoire-géo et français ont maintenant des sujets sur 20 neufs à chaque essai.", "SVT et physique-chimie de Terminale : nouveaux exercices chiffrés (glycémie, cycle, génétique, satellites, champ magnétique, oscillateurs, alcools, amines, dosages).", "Première : histoire-géo et français avec sujets neufs, plus d'anglais ; espagnol de 3e et de Terminale enrichi.", "Les chapitres qui se répétaient vite proposent 3 à 20 fois plus de questions différentes."]],
    ["2026-10-31r", "🎁 Essai gratuit rallongé : 15 jours", ["L'essai gratuit passe de 10 à 15 jours, toujours avec tout débloqué.", "Si ton essai venait de se terminer, tu retrouves les jours en plus tout de suite."]],
    ["2026-10-31p", "⚖️ Conditions, confidentialité et mot aux parents", ["Les conditions d'utilisation, la politique de confidentialité et un mot pour les parents sont en bas de l'accueil.", "Pour créer un compte, on accepte les conditions ; un élève de moins de 18 ans doit avoir l'accord d'un parent.", "Tes données ne sont jamais revendues ni utilisées pour de la publicité."]],
    ["2026-10-31o", "🎲 Beaucoup plus de questions, et un parcours rien qu'à toi", ["Nouveaux exercices à nombres nouveaux dans presque tous les chapitres, de la 6e à la Terminale : SVT, histoire-géo, français, espagnol, maths L et G, physique-chimie.", "Sujets sur 20 neufs à chaque essai, maintenant aussi en SVT, maths L et G, comptabilité et économie.", "L'appli se souvient de ce que tu as déjà fait et ne te le repropose pas tant qu'il reste du neuf.", "Les questions suivent ton chapitre en cours, ton emploi du temps, tes devoirs et tes points faibles : voir « Ma trajectoire »."]],
    ["2026-10-31n", "🔎 Sources : uniquement officielles et publiques", ["La page Sources ne liste plus que des documents officiels et publics : programmes du ministère, sujets du BAC et du BFEM, documents de l'Office du BAC.", "Aucun document privé ou réservé n'est utilisé dans l'appli."]],
    ["2026-10-31m", "📲 Installer l'appli, expliqué pas à pas", ["Le lien partagé demande d'abord : Android ou iPhone ? Puis il montre les étapes une par une, avec un dessin de l'écran.", "Nouveau : « Comment ça marche » (prix, contenu de ta classe, sources) et la page Sources.", "Sous chaque question et chaque cours, tu vois maintenant d'où il vient : le chapitre du programme officiel, ou le vrai sujet du BAC ou du BFEM."]],
    ["2026-10-31l", "📝 Sujets types : 3 fois plus", ["Terminale : 3 fois plus de sujets types BAC d'entraînement dans chaque matière (philo, français, HG, langues, maths, PC, SVT, éco, compta), notés sur 20 et corrigés étape par étape.", "Première : 14 devoirs types corrigés (français, anglais, maths, PC, SVT).", "Ce sont des sujets d'entraînement sur le modèle de l'épreuve, pas des annales officielles. Va dans Exercices corrigés."]],
    ["2026-10-31k", "🎁 Partage l'appli à un ami", ["Touche 📤 en haut de l'écran ou le bouton vert « Partager l'appli à un ami » sur l'accueil.", "Envoie le lien ou le QR code par WhatsApp : ton ami installe l'appli en quelques secondes."]],
    ["2026-10-31j", "📚 Terminale et Première : tout le contenu ×3", ["Terminale : près de 490 chapitres de cours, chacun avec un exercice noté, et plus de 4 700 QCM corrigés.", "Première : 207 chapitres de cours (3 fois plus) avec exercice noté, et le triple de QCM dans toutes les matières.", "Tout est nouveau, sans doublon, rangé dans les chapitres du programme."]],
    ["2026-10-31i", "🗂️ Accueil rangé par besoin", ["La carte Bonjour en deux : à gauche tout ce qui est corrigé pour ta classe, à droite « Réviser » (préparer un devoir, examen blanc…).", "🏆 Le challenge du jour est à côté de la cloche : un point rouge tant que tu ne l'as pas fait.", "Un gros bouton rouge « 🆘 Je bloque sur un exercice ou un devoir ».", "Les rubriques sont rangées : Devoirs et entraînement, Apprendre le cours, Mon suivi.", "🧰 Mes outils, ton arme secrète, bien en vue : formulaire, fiches flash, ta fiche perso et ta moyenne en un clic.", "📖 Cours rangés par matière : choisis Maths, PC, SVT… puis les chapitres, regroupés comme le programme.", "Terminale : 36 nouvelles notions de philosophie avec exercice noté."]],
    ["2026-10-31h", "🏠 Nouvel accueil, plus simple", ["En haut : bonjour, le compte à rebours, ta série et un gros bouton vers ce qu'il faut faire maintenant.", "Juste en dessous, toutes les rubriques d'un coup d'œil, en petites icônes.", "Les autres blocs (notes, trajectoire, agenda…) restent dans les rubriques ; tu peux les remettre sur l'accueil avec « Organiser mon accueil »."]],
    ["2026-10-31g", "🎤 Dictée et 🆘 aide plus fiables", ["Avec « 🎤 Dicter », tu peux dicter un long énoncé : l'écoute continue phrase après phrase jusqu'à « ⏹️ Arrêter ».", "Si ton exercice n'est pas assez clair, l'appli te propose les chapitres possibles au lieu de deviner."]],
    ["2026-10-31f", "💳 Premium sans code", ["Après ton paiement Wave ou Orange Money, envoie la capture directement dans l'appli (page Premium).", "Dès que le paiement est vérifié, l'appli se débloque toute seule, là où tu étais : plus besoin d'attendre un code.", "Active la notification : ton téléphone te prévient dès la validation, même appli fermée."]],
    ["2026-10-31e", "📒 Mes notes et 🆘 Je bloque sur un exercice", ["« Mes notes » : note tes devoirs et compositions ; l'appli calcule ta moyenne avec les coefficients officiels de ta série (modifiables), prévoit ta fin de trimestre et te donne des pistes d'orientation.", "Ta trajectoire se réajuste à chaque note : les matières où tu gagnes le plus de points passent en tête.", "« Je bloque sur un exercice » : écris, dicte ou photographie l'énoncé, et reçois un indice, puis la méthode, puis un exercice semblable corrigé."]],
    ["2026-10-31d", "🧭 Ma trajectoire et emploi du temps en 2 minutes", ["« 🧭 Ma trajectoire » : ton objectif, ta courbe jusqu'à l'examen comparée à une base de parcours, et ta semaine séance par séance.", "Le plan suit le chapitre que ta classe est en train de voir : tu peux le corriger matière par matière.", "Emploi du temps : saisie guidée (tu choisis la matière, puis tu places toutes ses heures d'un coup).", "Ou importe-le : photo, capture d'écran ou texte collé. Tu vérifies avant d'enregistrer."]],
    ["2026-10-31b", "🧭 Bien démarrer, accueil à ton goût, micro", ["Après le choix de ta classe, un parcours en 7 étapes te dit par où commencer.", "« ⭐ Organiser mon accueil » : range les blocs, masque ce qui ne te sert pas, épingle tes rubriques préférées.", "Dans « Pose ta question », tu peux parler au micro et écouter la réponse.", "Sur chaque notion, le bouton « 🤔 Je ne comprends pas » t'explique le chapitre autrement."]],
    ["2026-10-31a", "📱 Connexion par numéro", ["Tu te connectes avec ton numéro de téléphone et un code de 6 chiffres, sur iPhone comme sur Android.", "Pour le premium, paie avec le numéro de ton compte : c'est ta preuve de paiement."]],
    ["2026-10-30", "📚 Terminale : 5 fois plus de contenu", ["39 sujets du BAC corrigés pas à pas, pour toutes les séries.", "Des dizaines de nouvelles notions de cours avec exercice corrigé.", "Des centaines de nouveaux QCM, à faire aussi par thème pour préparer un devoir."]],
  ];
  const unread = () => NEWS.findIndex((n) => n[0] === S.newsSeen) === -1 ? NEWS.length : NEWS.findIndex((n) => n[0] === S.newsSeen);
  function badge() {
    let a = document.getElementById("news");
    if (!a) {
      a = document.createElement("a"); a.id = "news"; a.href = "#nouveautes"; a.className = "news-btn"; a.setAttribute("aria-label", "Nouveautés");
      document.querySelector(".top-r").prepend(a);
    }
    const n = unread();
    a.innerHTML = `🔔${n ? `<i class="dot">${n}</i>` : ""}`;
    // challenge du jour : icône à côté de la cloche, point rouge tant qu'il n'est pas fait aujourd'hui
    let c = document.getElementById("chal");
    if (!c) { c = document.createElement("a"); c.id = "chal"; c.href = "#challenge"; c.className = "news-btn"; c.setAttribute("aria-label", "Challenge du jour"); a.before(c); }
    const fait = typeof doneToday === "function" && doneToday("challenge");
    c.innerHTML = `🏆${fait ? "" : '<i class="dot pt"></i>'}`;
    c.title = fait ? "Challenge du jour fait ✔" : "Challenge du jour à faire";
    // partager l'appli : icône toujours visible en haut
    if (!document.getElementById("shr")) { const sh = document.createElement("a"); sh.id = "shr"; sh.href = "#partager"; sh.className = "news-btn"; sh.setAttribute("aria-label", "Partager l'appli à un ami"); sh.title = "Partager l'appli à un ami"; sh.textContent = "📤"; c.before(sh); }
  }
  function viewNouveautes() {
    const n = unread();
    $view.innerHTML = `<h1>🔔 Nouveautés</h1>${pushCard()}<p class="muted">Ce qui a changé dans l'appli, du plus récent au plus ancien.</p>
      ${NEWS.map(([id, t, l], i) => `<div class="card"${i < n ? ' style="border:2px solid var(--accent)"' : ""}><p class="small muted">${i < n ? "🔴 Nouveau · " : ""}${new Date(id.slice(0, 10)).toLocaleDateString("fr-FR", { day: "numeric", month: "long" })}</p><h2>${esc(t)}</h2><ul class="steps">${l.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>`).join("")}
      <a class="btn" href="#accueil">Retour à l'accueil</a>`;
    S.newsSeen = NEWS[0][0]; store.save(); badge();
  }

  // ---------- Rappels guidés : pause de midi (13 h – 14 h 30) et après l'école (17 h – 18 h)
  const QUESTIONS = [
    ["Qu'est-ce que tu veux réviser en ce moment ?", ["Une matière où j'ai des difficultés", "Préparer un devoir qui arrive", "Le BAC ou le BFEM", "Juste m'entraîner"]],
    ["Qu'est-ce qui te manque le plus dans l'appli ?", ["Plus de cours expliqués", "Plus d'exercices corrigés", "Des vidéos", "Rien, c'est très bien"]],
    ["Comment tu préfères réviser ?", ["En lisant le cours", "En faisant des QCM", "En faisant des exercices", "En groupe avec des amis"]],
    ["Quelle matière te pose le plus de problèmes ?", ["Mathématiques", "Physique-Chimie ou SVT", "Français ou philosophie", "Langues ou histoire-géo"]],
    ["Combien de temps tu peux réviser par jour ?", ["Moins de 15 minutes", "Environ 30 minutes", "Environ 1 heure", "Plus d'une heure"]],
    ["L'appli t'aide-t-elle à avoir de meilleures notes ?", ["Oui, beaucoup", "Un peu", "Pas encore", "Je viens de commencer"]],
  ];
  function creneau() {
    const d = new Date(), m = d.getHours() * 60 + d.getMinutes();
    return m >= 13 * 60 && m < 14 * 60 + 30 ? "midi" : m >= 17 * 60 && m < 18 * 60 ? "soir" : null;
  }
  globalThis.pauseCard = () => {
    const c = creneau(); if (!c) return "";
    const key = today() + c, day = Math.floor(Date.now() / 864e5), [q, opts] = QUESTIONS[(day * 2 + (c === "soir")) % QUESTIONS.length];
    const asked = (S.avis || []).some((a) => a.k === key);
    const go = c === "midi" ? ["#challenge", "🏆 Le challenge du jour en 5 minutes"] : ["#agenda", "🗓️ Voir ce que je dois réviser pour demain"];
    return `<div class="card prog" id="pause"><h2>${c === "midi" ? "☀️ C'est la pause : 5 minutes pour réviser ?" : "🎒 De retour de l'école ?"}</h2>
      <a class="mission" href="${go[0]}"><span>👉</span><span><b>${go[1]}</b></span></a>
      ${asked ? `<p class="small msg-ok">Merci pour ta réponse ! 🙏</p>` : `<p><b>Petite question :</b> ${esc(q)}</p><div class="grid">${opts.map((o, i) => `<button class="subj tile avis" data-i="${i}" style="min-height:0"><span class="small">${esc(o)}</span></button>`).join("")}</div>`}</div>`;
  };
  document.addEventListener("click", (e) => {
    const b = e.target.closest && e.target.closest("#pause .avis");
    if (!b) return;
    const c = creneau() || "midi", day = Math.floor(Date.now() / 864e5), [q, opts] = QUESTIONS[(day * 2 + (c === "soir")) % QUESTIONS.length];
    const rec = { k: today() + c, q, r: opts[+b.dataset.i], d: today() };
    S.avis = [...(S.avis || []), rec].slice(-30); store.save();
    if (Compte.avis) Compte.avis(rec).catch(() => {});
    const card = document.getElementById("pause"); if (card) card.outerHTML = pauseCard();
  });

  // ---------- Vraies notifications (même appli fermée) : l'élève les active d'un geste
  globalThis.pushCard = () => {
    if (!CFG.vapid || !("Notification" in window) || !("serviceWorker" in navigator) || S.pushOff || !Compte.user) return "";
    if (Notification.permission === "granted" && S.pushOn) return "";
    if (Notification.permission === "denied") return "";
    const ios = /iPhone|iPad/.test(navigator.userAgent), alone = matchMedia("(display-mode: standalone)").matches || navigator.standalone;
    return `<div class="card" id="pushc"><h2>🔔 Recevoir les rappels</h2><p class="small">Un petit message à la pause de midi et après l'école pour réviser 5 minutes. Tu peux les arrêter quand tu veux dans les réglages du téléphone.</p>
      ${ios && !alone ? `<p class="small muted">Sur iPhone, installe d'abord l'appli sur l'écran d'accueil (Partager puis « Sur l'écran d'accueil »), puis ouvre-la depuis son icône.</p>`
        : `<div class="row"><button class="btn" id="pushon" style="flex:1">Activer les rappels</button><button class="btn alt" id="pushno" style="width:auto">Plus tard</button></div>`}<p class="small" id="pushmsg"></p></div>`;
  };
  document.addEventListener("click", async (e) => {
    const t = e.target.closest && e.target.closest("#pushon, #pushno");
    if (!t) return;
    if (t.id === "pushno") { S.pushOff = true; store.save(); document.getElementById("pushc").remove(); return; }
    const m = document.getElementById("pushmsg");
    try {
      if ((await Notification.requestPermission()) !== "granted") { m.textContent = "Notifications refusées. Tu peux les autoriser plus tard dans les réglages du navigateur."; return; }
      await Compte.enablePush(CFG.vapid);
      S.pushOn = true; store.save(); m.className = "small msg-ok"; m.textContent = "C'est activé ! Premier rappel à la prochaine pause. 👍";
    } catch (err) { m.className = "small msg-ko"; m.textContent = "Activation impossible sur ce téléphone pour le moment."; if (Compte.logError) Compte.logError("Notifications : " + (err.code || err.message)); }
  });

  // ---------- Assistant et « Je bloque » : dicter au micro
  // Le texte s'affiche pendant qu'on parle et s'ajoute à ce qui est déjà écrit ; rien n'est envoyé tout seul :
  // l'élève relit et corrige avant d'envoyer. Le bouton n'apparaît que si le navigateur sait vraiment dicter
  // (Chrome Android / ordinateur, en ligne). Après un refus du micro ou 2 échecs de suite, il est masqué.
  const Rec = window.SpeechRecognition || window.webkitSpeechRecognition;
  const iOS = /iP(hone|ad|od)/.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  const micOk = () => !!Rec && !iOS && window.isSecureContext !== false && !(S.micKo >= 2);
  const MIC_ERR = {
    "not-allowed": "Micro refusé. Autorise le micro pour ce site dans les réglages de Chrome, ou écris ton texte.",
    "service-not-allowed": "La dictée n'est pas disponible sur ce téléphone : écris ton texte.",
    "audio-capture": "Aucun micro trouvé : écris ton texte.",
    "network": "La dictée a besoin d'internet : vérifie ta connexion ou écris ton texte.",
    "no-speech": "Je n'ai rien entendu. Touche « 🎤 Dicter » et parle près du téléphone.",
    "language-not-supported": "La dictée en français n'est pas disponible ici : écris ton texte.",
  };
  globalThis.assistVoice = (input, send, place) => {
    const form = document.getElementById("ask");
    if (!form || !micOk()) return;
    const mic = document.createElement("button"); mic.type = "button"; mic.className = "btn alt mic-btn"; mic.style.width = "auto";
    const idle = () => { mic.textContent = "🎤 Dicter"; mic.setAttribute("aria-label", "Dicter au micro"); mic.classList.remove("on"); };
    idle();
    const note = document.createElement("p"); note.className = "small muted mic-note"; note.hidden = true;
    const at = place || form; at.insertBefore(mic, at.lastElementChild);
    form.insertAdjacentElement("afterend", note);
    const tell = (t, ko) => { note.hidden = !t; note.textContent = t || ""; note.className = "small mic-note " + (ko ? "msg-ko" : "muted"); };
    let r = null, base = "", heard = "";
    const fail = (code) => {
      S.micKo = ["service-not-allowed", "audio-capture", "language-not-supported"].includes(code) ? 2 : (S.micKo || 0) + 1;
      store.save();
      tell(MIC_ERR[code] || "La dictée n'a pas marché : écris ton texte.", true);
      if (S.micKo >= 2) mic.remove();
      if (typeof Compte !== "undefined" && Compte.logError && code !== "no-speech") Compte.logError("Dictée : " + code);
    };
    let fini = true, deja = false;
    mic.onclick = () => {
      if (r) { fini = true; r.stop(); return; }
      fini = false; deja = false; ecoute();
    };
    // une écoute par phrase, relancée tant que l'élève parle : il peut dicter un long énoncé avec des pauses
    const ecoute = () => {
      try { r = new Rec(); } catch (e) { r = null; fail("service-not-allowed"); return; }
      r.lang = "fr-FR"; r.interimResults = true; r.continuous = false; r.maxAlternatives = 1;
      base = input.value.trim(); heard = "";
      const show = (t) => { input.value = (base ? base + " " : "") + t; };
      r.onstart = () => { mic.textContent = "⏹️ Arrêter"; mic.setAttribute("aria-label", "Arrêter la dictée"); mic.classList.add("on"); tell("Je t'écoute… parle lentement et distinctement."); };
      r.onresult = (ev) => {
        let fin = "", tmp = "";
        for (let i = 0; i < ev.results.length; i++) { const t = ev.results[i][0].transcript; if (ev.results[i].isFinal) fin += t; else tmp += t; }
        heard = (fin + tmp).trim(); show(heard);
      };
      r.onerror = (ev) => { const c = ev.error || "inconnue"; if (c !== "aborted" && !(c === "no-speech" && deja)) fail(c); };
      r.onend = () => {
        r = null;
        if (heard) deja = true;
        if (heard && !fini) { show(heard); try { ecoute(); return; } catch (e) {} }
        idle(); fini = true;
        if (deja) { S.micKo = 0; store.save(); if (heard) show(heard); tell("Relis le texte dicté et corrige les mots mal compris avant d'envoyer."); input.focus(); }
        else if (note.textContent.startsWith("Je t'écoute")) tell(MIC_ERR["no-speech"], true);
      };
      try { r.start(); } catch (e) { r = null; idle(); fail("service-not-allowed"); }
    };
  };
  globalThis.sayBtn = () => ("speechSynthesis" in window ? `<button class="btn alt small say-ans">🔊 Écouter la réponse</button>` : "");
  document.addEventListener("click", (e) => {
    const b = e.target.closest && e.target.closest(".say-ans");
    if (!b) return;
    if (speechSynthesis.speaking) { speechSynthesis.cancel(); b.textContent = "🔊 Écouter la réponse"; return; }
    const box = b.closest(".bubble");
    const txt = [...box.querySelectorAll("p, li")].filter((el) => !el.closest("details") && !el.closest(".mini")).map((el) => el.innerText).join(". ");
    const u = new SpeechSynthesisUtterance(txt); u.lang = "fr-FR"; u.rate = 0.95; u.onend = () => { b.textContent = "🔊 Écouter la réponse"; };
    speechSynthesis.cancel(); speechSynthesis.speak(u); b.textContent = "⏹️ Arrêter";
  });

  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  ROUTES.nouveautes = viewNouveautes;
  window.addEventListener("hashchange", badge);
  document.addEventListener("DOMContentLoaded", badge);
  if (document.readyState !== "loading") badge();
})();
