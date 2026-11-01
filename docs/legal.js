"use strict";
// Pages légales : conditions d'utilisation, confidentialité (loi sénégalaise 2008-12), mentions légales, mot aux parents.
// Lisibles sans compte (#legal/...). Les infos de la société viennent de CONFIG.societe (contenu/build.py).
(() => {
  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  const CGU_V = (globalThis.CGU_V = "2026-10-31");
  const so = () => ({ ...((typeof CFG !== "undefined" && CFG && CFG.societe) || {}), ...(globalThis.SOCIETE || {}) });
  const PUB = () => !!(typeof CFG !== "undefined" && CFG && CFG.mentions_publiques);
  const val = (k) => esc(so()[k] || "à compléter");
  const contact = () => esc((typeof CFG !== "undefined" && CFG && (CFG.wave_number || CFG.whatsapp)) || "");
  const prix = () => (typeof CFG !== "undefined" && CFG ? fcfa(CFG.price_fcfa) : "1 000 F");
  const essai = () => (typeof TRIAL_DAYS !== "undefined" ? TRIAL_DAYS : 10);

  const PAGES = {
    cgu: ["Conditions d'utilisation", () => `
      <p class="small muted">Version du ${CGU_V}</p>
      <h2>1. L'appli</h2><p>Révision est une appli de révision scolaire pour les élèves du Sénégal, du CE1 à la Terminale. Elle suit les programmes officiels. Elle aide à réviser, mais ne remplace ni les cours ni les professeurs.</p>
      <h2>2. Le compte</h2><p>Le compte se crée avec un prénom, un nom, un numéro de téléphone et un code secret à 6 chiffres. Le code est personnel : ne le donne à personne. Un compte sert à un seul élève.</p>
      <p><b>Élève de moins de 18 ans :</b> un parent ou un tuteur doit être d'accord pour la création du compte et pour le paiement. Avant de payer, l'élève envoie un lien à son parent, qui donne son accord depuis son propre téléphone ; l'accord est enregistré avec son nom, son numéro et la date. En 1re et en Terminale, un élève de 18 ans ou plus peut déclarer sa date de naissance à la place : une fausse déclaration est de sa seule responsabilité.</p>
      <h2>3. Essai et prix</h2><p>L'essai gratuit dure ${essai()} jours, avec tout débloqué. Ensuite, le pack premium coûte <b>${prix()}</b>, payé une seule fois par Wave ou Orange Money, et reste valable jusqu'à l'examen de l'année scolaire en cours. Le prix est affiché avant tout paiement.</p>
      <p>Une école ou une structure peut aussi acheter l'accès pour ses élèves, selon un contrat écrit avec elle.</p>
      <h2>4. Remboursement</h2><p>Si le premium ne s'active pas après ton paiement, et que nous ne pouvons pas régler le problème, ton argent est remboursé. Écris-nous dans les 7 jours qui suivent le paiement.</p>
      <h2>5. Bon usage</h2><p>Il est interdit de partager ton compte ou tes codes, de copier le contenu de l'appli pour le revendre, ou d'essayer de contourner le paiement. En cas d'abus, le compte peut être suspendu.</p>
      <h2>6. Contenu</h2><p>Les cours, les questions et les corrigés sont rédigés par l'équipe Révision à partir des programmes et des sujets officiels publics. Les sujets générés sont des sujets d'entraînement sur le modèle de l'examen, et non des sujets officiels. Malgré nos vérifications, une erreur reste possible : signale-la et nous la corrigeons.</p>
      <h2>7. Disponibilité</h2><p>Nous faisons au mieux pour que l'appli marche tout le temps, aussi hors connexion, sans pouvoir le garantir à 100 %.</p>
      <h2>8. Droit applicable</h2><p>Ces conditions relèvent du droit sénégalais. En cas de désaccord, on cherche d'abord une solution à l'amiable.</p>`],
    confidentialite: ["Confidentialité", () => `
      <p class="small muted">Version du ${CGU_V}. Conformément à la loi n° 2008-12 du 25 janvier 2008 sur la protection des données personnelles.</p>
      <h2>Ce que nous gardons</h2><ul>
        <li>Ton prénom, ton nom et ton numéro de téléphone, pour ton compte.</li>
        <li>Ta classe et tes progrès (réponses, notes, emploi du temps, agenda), pour que ton parcours te suive sur tous tes téléphones.</li>
        <li>Un identifiant au hasard du téléphone, pour l'essai gratuit (un seul essai par téléphone).</li>
        <li>La capture de ton paiement, si tu en envoies une, pour activer le premium.</li>
        <li>L'accord de ton parent (son nom, son numéro, son lien avec toi, la date), ou ta date de naissance si tu déclares avoir 18 ans ou plus.</li>
        <li>Les erreurs techniques de l'appli, pour les corriger.</li></ul>
      <h2>Ce que nous ne faisons pas</h2><ul>
        <li>Pas de publicité, pas de revente, pas de partage de tes données.</li>
        <li>Pas de géolocalisation, pas d'accès à tes contacts ni à tes photos (sauf la photo que tu choisis d'envoyer).</li></ul>
      <h2>Où sont tes données</h2><p>Sur ton téléphone, et dans un service sécurisé de Google (Firebase), en Europe (Belgique). L'appli est servie par GitHub Pages.</p>
      <h2>Combien de temps</h2><p>Tant que ton compte existe. Si tu demandes la suppression, ton compte et tes données sont effacés dans les 30 jours.</p>
      <h2>Tes droits</h2><p>Tu peux demander à voir, corriger ou supprimer tes données, ou t'opposer à leur usage. Écris-nous${PUB() && contact() ? ` sur WhatsApp au <b>${contact()}</b>` : " sur WhatsApp, au numéro indiqué dans la page Premium"}, depuis le numéro de ton compte. Tu peux aussi saisir la Commission de protection des données personnelles (CDP) du Sénégal.</p>
      <h2>Mineurs</h2><p>L'appli est faite pour des élèves, souvent mineurs. Nous ne demandons que le strict nécessaire. Un parent peut, à tout moment, demander l'accès aux données de son enfant ou leur suppression.</p>
      ${PUB() ? `<p><b>Responsable du traitement :</b> ${val("nom")}. Déclaration CDP : ${val("cdp")}.</p>` : ""}`],
    mentions: ["Mentions légales", () => `
      <ul><li><b>Éditeur :</b> ${val("nom")}</li>
      <li><b>Forme :</b> ${val("forme")}</li>
      <li><b>RCCM :</b> ${val("rccm")}</li>
      <li><b>NINEA :</b> ${val("ninea")}</li>
      <li><b>Adresse :</b> ${val("adresse")}</li>
      <li><b>Responsable de la publication :</b> ${val("responsable")}</li>
      <li><b>Contact :</b> ${contact() ? `WhatsApp ${contact()}` : "à compléter"}</li>
      <li><b>Hébergement :</b> GitHub Pages (GitHub Inc., États-Unis) pour l'appli ; Google Firebase (Google, région Europe) pour les comptes.</li>
      <li><b>Déclaration CDP :</b> ${val("cdp")}</li></ul>
      <p>Les textes, questions et corrigés de l'appli appartiennent à l'éditeur. Les programmes et sujets officiels cités appartiennent à leurs auteurs (ministère de l'Éducation nationale, Office du Baccalauréat).</p>`],
    parents: ["Mot aux parents", () => `
      <p>Votre enfant utilise Révision pour réviser ses cours. Voici ce qu'il faut savoir :</p><ul>
        <li>L'essai dure ${essai()} jours, gratuit et sans engagement.</li>
        <li>Rien n'est payé sans votre accord : votre enfant vous envoie un lien, vous le lisez et vous touchez « J'autorise ».</li>
        <li>Ensuite, le pack coûte ${prix()}, une seule fois, jusqu'à l'examen. Aucun prélèvement automatique.</li>
        <li>Pas de publicité, pas de discussion avec des inconnus dans l'appli.</li>
        <li>Seules les données utiles au compte et aux progrès sont gardées, et jamais revendues.</li>
        <li>Vous pouvez demander à tout moment de voir ou de supprimer les données de votre enfant${PUB() && contact() ? ` (WhatsApp ${contact()})` : ""}.</li></ul>`],
  };

  let charge = false;
  function viewLegal(arg) {
    // fiche société remplie par l'admin (une lecture, puis on réaffiche)
    if (!charge && PUB() && globalThis.Compte && Compte.getSociete) { charge = true; Compte.getSociete().then((s) => { if (s) { globalThis.SOCIETE = s; if (location.hash.startsWith("#legal")) viewLegal(location.hash.split("/")[1]); } }).catch(() => {}); }
    const k = PAGES[arg] && (arg !== "mentions" || PUB()) ? arg : null;
    const nav = `<div class="row" style="flex-wrap:wrap;gap:6px">${Object.entries(PAGES).filter(([id]) => id !== "mentions" || PUB()).map(([id, [t]]) => `<a class="btn ${id === k ? "" : "alt "}small" href="#legal/${id}">${t}</a>`).join("")}</div>`;
    const retour = `<a class="btn alt" href="#accueil">Retour à l'appli</a>`;
    $view.innerHTML = k
      ? `<div class="card"><h1>${PAGES[k][0]}</h1>${PAGES[k][1]()}</div><div class="card small">${nav}</div>${retour}`
      : `<div class="card"><h1>Informations légales</h1><p class="muted">Tout ce qui encadre l'appli : tes droits, tes données, le prix.</p>${nav}</div>${retour}`;
    window.scrollTo(0, 0);
  }
  globalThis.viewLegal = viewLegal;
  ROUTES.legal = viewLegal;
  // lien en bas de chaque page
  globalThis.legalFooter = () => `<p class="small muted" style="text-align:center;margin-top:12px"><a href="#legal/cgu">Conditions</a> · <a href="#legal/confidentialite">Confidentialité</a>${PUB() ? ' · <a href="#legal/mentions">Mentions légales</a>' : ""} · <a href="#legal/parents">Parents</a></p>`;
})();
