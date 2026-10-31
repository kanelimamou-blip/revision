// Tuto d'installation guidé : on demande d'abord Android ou iPhone, puis on montre les étapes une par une
// (fil conducteur) ou toutes d'un coup. Ouvert par le lien partagé (…/revision/?qr ou #installer), avant même la connexion.
const INST = { os: null, k: 0, tout: false };

const INST_UA = navigator.userAgent;
const instDetect = () => (/iphone|ipad|ipod/i.test(INST_UA) ? "ios" : /android/i.test(INST_UA) ? "android" : null);
const instBrowser = () => {
  if (/FBAN|FBAV|Instagram|WhatsApp|Line\//i.test(INST_UA)) return "inapp";
  if (/CriOS/i.test(INST_UA)) return "chrome-ios";
  if (/SamsungBrowser/i.test(INST_UA)) return "samsung";
  return "";
};

// petits écrans de téléphone dessinés, avec le bouton à toucher qui clignote
const instIco = {
  share: `<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v12M7 8l5-5 5 5"/><path d="M5 12v8h14v-8"/></svg>`,
  dots: `<svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>`,
  plus: `<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="4"/><path d="M12 8v8M8 12h8"/></svg>`,
};
function instEcran(kind) {
  const appIcon = `<span class="ins-app"><img src="icons/icon-192.png" alt=""><small>Révision</small></span>`;
  const screens = {
    "ios-safari": `<div class="ins-url">kanelimamou-blip.github.io</div><div class="ins-body"><b>Révision</b><span>Ouvre cette page dans <b>Safari</b> 🧭</span></div><div class="ins-bar"><span>‹</span><span>›</span><span class="ins-hl">${instIco.share}</span><span>▢</span><span>⧉</span></div>`,
    "ios-share": `<div class="ins-url">kanelimamou-blip.github.io</div><div class="ins-body"><b>Révision</b></div><div class="ins-bar"><span>‹</span><span>›</span><span class="ins-hl">${instIco.share}</span><span>▢</span><span>⧉</span></div>`,
    "ios-menu": `<div class="ins-sheet"><div class="ins-row">Copier</div><div class="ins-row">Ajouter aux favoris</div><div class="ins-row ins-hl-row">Sur l'écran d'accueil <span>${instIco.plus}</span></div><div class="ins-row">Imprimer</div></div>`,
    "ios-add": `<div class="ins-top"><span>Annuler</span><b>Ajouter à l'écran</b><span class="ins-hl-txt">Ajouter</span></div><div class="ins-body">${appIcon}<span>Révision</span></div>`,
    "home": `<div class="ins-home">${["📷", "💬", "🎵", "📞", "⚙️"].map((e) => `<span class="ins-app"><i>${e}</i><small>&nbsp;</small></span>`).join("")}<span class="ins-app ins-hl-app"><img src="icons/icon-192.png" alt=""><small>Révision</small></span></div>`,
    "and-chrome": `<div class="ins-url">kanelimamou-blip.github.io <span class="ins-hl">${instIco.dots}</span></div><div class="ins-body"><b>Révision</b><span>Ouvre cette page dans <b>Chrome</b></span></div>`,
    "and-menu": `<div class="ins-url">kanelimamou-blip.github.io <span>${instIco.dots}</span></div><div class="ins-sheet ins-sheet-top"><div class="ins-row">Nouvel onglet</div><div class="ins-row">Favoris</div><div class="ins-row ins-hl-row">Installer l'application <span>📲</span></div><div class="ins-row">Partager…</div></div>`,
    "and-ok": `<div class="ins-dialog"><b>Installer l'application ?</b>${appIcon}<div class="ins-dlg-btns"><span>Annuler</span><span class="ins-hl-txt">Installer</span></div></div>`,
  };
  return `<div class="ins-phone" aria-hidden="true">${screens[kind] || ""}</div>`;
}

function instEtapes(os) {
  const br = instBrowser();
  if (os === "ios") return [
    { t: "Ouvre le lien dans Safari", ecran: "ios-safari", p: br === "inapp"
      ? "La page est ouverte dans WhatsApp (ou une autre appli). Touche <b>⋯</b> ou l'icône de boussole en bas, puis <b>« Ouvrir dans Safari »</b>."
      : br === "chrome-ios" ? "Tu es dans Chrome : ça marche aussi, avec le bouton Partager en haut à droite. Mais le plus simple reste <b>Safari</b> (la boussole bleue)."
      : "Tu es au bon endroit si la barre d'adresse est en bas ou en haut de Safari. Sinon, copie le lien et colle-le dans <b>Safari</b>.", copier: true },
    { t: "Touche le bouton Partager", ecran: "ios-share", p: "C'est le carré avec une flèche vers le haut, en bas de l'écran (en haut sur iPad)." },
    { t: "Choisis « Sur l'écran d'accueil »", ecran: "ios-menu", p: "Fais glisser la liste vers le haut si tu ne le vois pas tout de suite." },
    { t: "Touche « Ajouter »", ecran: "ios-add", p: "En haut à droite. Le nom « Révision » est déjà écrit." },
    { t: "Ouvre l'appli depuis ton écran", ecran: "home", p: "L'icône <b>Révision</b> est sur ton écran d'accueil. Elle s'ouvre en plein écran, comme une vraie appli. Crée ton compte avec ton numéro : <b>10 jours gratuits</b>." },
  ];
  return [
    { t: "Ouvre le lien dans Chrome", ecran: "and-chrome", p: br === "inapp"
      ? "La page est ouverte dans WhatsApp. Touche les <b>3 points ⋮</b> en haut à droite, puis <b>« Ouvrir dans Chrome »</b>."
      : br === "samsung" ? "Tu es dans Samsung Internet : ça marche aussi. Touche le menu <b>≡</b> en bas, puis <b>« Ajouter page à » → « Écran d'accueil »</b>."
      : "Si la page est déjà ouverte dans Chrome, passe à l'étape suivante.", copier: true },
    { t: "Installe l'appli", ecran: "and-menu", p: "Touche le bouton « Installer maintenant » ci-dessous s'il apparaît. Sinon, touche les <b>3 points ⋮</b> en haut à droite, puis <b>« Installer l'application »</b> (ou « Ajouter à l'écran d'accueil »).", installer: true },
    { t: "Confirme avec « Installer »", ecran: "and-ok", p: "Une petite fenêtre s'ouvre : touche <b>Installer</b>. Quelques secondes suffisent." },
    { t: "Ouvre l'appli depuis ton écran", ecran: "home", p: "L'icône <b>Révision</b> est sur ton écran d'accueil (ou dans la liste de tes applis). Elle s'ouvre en plein écran, comme une vraie appli. Crée ton compte avec ton numéro : <b>10 jours gratuits</b>." },
  ];
}

function viewInstaller() {
  document.body.classList.add("ins-mode");
  const lien = location.href.split("#")[0].split("?")[0] + "?qr";
  if (typeof standalone !== "undefined" && standalone) {
    $view.innerHTML = `<div class="card" style="text-align:center"><h1>✅ L'appli est installée</h1><p>Tu l'utilises déjà comme une vraie appli.</p><a class="btn" href="#accueil">Continuer</a></div>`;
    return;
  }
  if (!INST.os) {
    const d = instDetect();
    $view.innerHTML = `<div class="card ins-intro"><img src="icons/icon-192.png" alt="" class="ins-logo"><h1>Installe Révision sur ton téléphone</h1>
      <p>Gratuit, en 1 minute, sans Play Store ni App Store. L'appli s'ouvre ensuite en plein écran, comme une vraie appli.</p></div>
      <h2 style="text-align:center">Tu as quel téléphone ?</h2>
      <div class="ins-choix">
        <button class="ins-os${d === "android" ? " ins-devine" : ""}" data-os="android"><span>🤖</span><b>Android</b><small>Samsung, Tecno, Infinix, Itel, Xiaomi…</small>${d === "android" ? "<em>C'est ton téléphone</em>" : ""}</button>
        <button class="ins-os${d === "ios" ? " ins-devine" : ""}" data-os="ios"><span>🍎</span><b>iPhone</b><small>ou iPad</small>${d === "ios" ? "<em>C'est ton téléphone</em>" : ""}</button>
      </div>
      <p class="small muted" style="text-align:center">Déjà installée ? <a href="#accueil">Ouvrir l'appli</a></p>`;
    $view.querySelectorAll(".ins-os").forEach((b) => b.onclick = () => { INST.os = b.dataset.os; INST.k = 0; INST.tout = false; viewInstaller(); window.scrollTo(0, 0); });
    return;
  }
  const et = instEtapes(INST.os), nom = INST.os === "ios" ? "iPhone" : "Android";
  const bloc = (e, i) => `<div class="card ins-etape"><p class="tag-src">Étape ${i + 1} sur ${et.length}</p><h2>${esc(e.t)}</h2>${instEcran(e.ecran)}<p>${e.p}</p>
    ${e.copier ? `<button class="btn alt small ins-copier">📋 Copier le lien</button>` : ""}
    ${e.installer && typeof deferred !== "undefined" && deferred ? `<button class="btn ins-go">📲 Installer maintenant</button>` : ""}</div>`;
  const haut = `<div class="row" style="justify-content:space-between;align-items:center"><button class="btn-ghost" id="ins-os">‹ Changer (${nom})</button><button class="btn-ghost" id="ins-mode">${INST.tout ? "Étape par étape" : "Voir tout d'un coup"}</button></div>`;
  if (INST.tout) {
    $view.innerHTML = `${haut}<h1>Installer sur ${nom}</h1>${et.map(bloc).join("")}<a class="btn" href="#accueil">J'ai fini, ouvrir l'appli</a>`;
  } else {
    const k = Math.min(INST.k, et.length - 1);
    $view.innerHTML = `${haut}<div class="ins-points">${et.map((_, i) => `<i class="${i < k ? "fait" : i === k ? "ici" : ""}"></i>`).join("")}</div>${bloc(et[k], k)}
      <div class="btns">${k > 0 ? `<button class="btn alt" id="ins-prec">‹ Précédent</button>` : ""}${k + 1 < et.length ? `<button class="btn" id="ins-suiv">C'est fait, étape suivante ›</button>` : `<a class="btn" href="#accueil">🎉 C'est installé</a>`}</div>`;
    const s = document.getElementById("ins-suiv"), p = document.getElementById("ins-prec");
    if (s) s.onclick = () => { INST.k = k + 1; viewInstaller(); window.scrollTo(0, 0); };
    if (p) p.onclick = () => { INST.k = k - 1; viewInstaller(); window.scrollTo(0, 0); };
  }
  document.getElementById("ins-os").onclick = () => { INST.os = null; viewInstaller(); };
  document.getElementById("ins-mode").onclick = () => { INST.tout = !INST.tout; viewInstaller(); window.scrollTo(0, 0); };
  $view.querySelectorAll(".ins-copier").forEach((b) => b.onclick = () => navigator.clipboard?.writeText(lien).then(() => { b.textContent = "Lien copié ✓ : colle-le dans le navigateur"; }).catch(() => { b.textContent = lien; }));
  $view.querySelectorAll(".ins-go").forEach((b) => b.onclick = async () => {
    if (!deferred) return;
    deferred.prompt();
    const r = await deferred.userChoice.catch(() => null);
    deferred = null;
    if (r && r.outcome === "accepted") { INST.k = et.length - 1; INST.tout = false; viewInstaller(); }
  });
}

// le bouton « Installer maintenant » apparaît dès que Chrome le permet
window.addEventListener("beforeinstallprompt", () => setTimeout(() => { if (location.hash.startsWith("#installer")) viewInstaller(); }, 0));
// lien partagé (…?qr) : on arrive directement sur le tuto, sauf si l'appli est déjà installée
if (/[?&]qr\b/.test(location.search) && !(matchMedia("(display-mode: standalone)").matches || navigator.standalone) && !location.hash) history.replaceState(null, "", location.pathname + location.search + "#installer");
if (location.hash.startsWith("#installer")) viewInstaller();

// ---------- « Comment ça marche » : très court, montré une fois après le choix de la classe, puis depuis Premium et Partager
function viewComment() {
  const lv = S.level, subs = subjectsOf(lv), ids = new Set(subs.map((s) => s.id));
  const nq = DATA.questions.filter((q) => ids.has(q.s)).length;
  const nn = subs.reduce((a, s) => a + ((DATA.notions || {})[s.id] || []).length, 0);
  const ns = annalesOf(lv).length + exercisesOf(lv).length;
  const nf = subs.reduce((a, s) => a + ((DATA.formules || {})[s.id] || []).reduce((b, c) => b + c.f.length, 0), 0);
  const nb = (x) => x.toLocaleString("fr-FR");
  const prix = typeof fcfa === "function" ? fcfa(CFG.price_fcfa) : "1 000 FCFA";
  $view.innerHTML = `<h1>💡 Comment ça marche</h1>
    <div class="card"><h2>💸 Combien ça coûte</h2><ul class="steps">
      <li><b>${TRIAL_DAYS} jours gratuits</b>, tout est débloqué.</li>
      <li>Ensuite <b>${prix}, une seule fois</b>, valable jusqu'à l'examen. Pas d'abonnement caché.</li>
      <li>Paiement par Wave ou Orange Money depuis ton numéro : l'appli se débloque toute seule.</li></ul></div>
    <div class="card"><h2>📚 Ce qu'il y a pour ta classe (${esc(lv)})</h2><div class="dispo" style="grid-template-columns:1fr 1fr">
      <div class="dispo-i"><b>${nb(nq)}</b><span>QCM corrigés</span></div>
      <div class="dispo-i"><b>${nb(nn)}</b><span>chapitres de cours</span></div>
      <div class="dispo-i"><b>${nb(ns)}</b><span>sujets et exercices notés</span></div>
      <div class="dispo-i"><b>${nb(nf)}</b><span>formules</span></div></div>
      <p class="small muted">Tout le programme officiel, matière par matière, chapitre par chapitre.</p></div>
    <div class="card"><h2>🧭 Comment réviser</h2><ul class="steps">
      <li><b>Cours</b> du chapitre, en court.</li><li><b>QCM</b> : chaque réponse est expliquée.</li>
      <li><b>Exercice</b> puis <b>sujet noté sur 20</b>, corrigé étape par étape.</li>
      <li>Bloqué ? <b>🆘 Je bloque</b> : indice, méthode, puis exercice semblable corrigé.</li></ul></div>
    <div class="card"><h2>🔎 D'où vient le contenu</h2><ul class="steps">
      <li>Le <b>programme officiel</b> du Sénégal, chapitre par chapitre.</li>
      <li>Les <b>vrais sujets du BAC et du BFEM</b> : la source est écrite sous chaque question qui en vient.</li>
      <li>Les autres questions et sujets types sont rédigés par l'équipe sur le modèle des examens, et indiqués comme tels.</li>
      <li>Uniquement des <b>documents officiels et publics</b> : aucun document privé ou réservé.</li></ul>
      <a class="small" href="#sources">Voir toutes les sources ›</a></div>
    <div class="btns"><a class="btn" href="${S.parcoursVu && location.hash === "#comment/debut" ? "#bienvenue" : "#accueil"}">C'est parti !</a></div>`;
}
