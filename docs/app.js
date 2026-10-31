"use strict";
// Révision BAC et BFEM : quiz, examen blanc, erreurs à revoir, progrès, accès premium par code
const $view = document.getElementById("view");
const LETTERS = "ABCD";
const QUIZ_LEN = 20, EXAM_LEN = 30, EXAM_MIN = 30;
let DATA = null, CFG = null, timer = null;

const store = {
  load() { try { return JSON.parse(localStorage.getItem("rev") || "{}"); } catch { return {}; } },
  save() { try { localStorage.setItem("rev", JSON.stringify(S)); } catch {} Compte.save(S); },
};
const S = Object.assign({ level: null, premium: false, stats: {}, sessions: [], days: [] }, store.load());

// la flèche de vecteur combinante (F⃗) manque dans beaucoup de polices de téléphone : on la dessine en CSS
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])).replace(/([A-Za-zℓ]{1,2}?)\u20d7/g, '<span class="vec">$1</span>');
const today = () => new Date().toISOString().slice(0, 10);
const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const fcfa = (n) => n.toLocaleString("fr-FR") + " FCFA";
// « Tle S2 » appartient aussi à la famille « Tle S » (matières communes à toutes les séries S)
const family = (level) => { const [c, sr] = String(level).split(" "); return sr ? `${c} ${DATA.families[sr] || sr}` : c; };
const matches = (levels, level) => levels.includes(level) || levels.includes(family(level));
const subjectsOf = (level) => DATA.subjects.filter((s) => matches(s.levels, level));
const inLevel = (q) => subjectsOf(S.level).some((s) => s.id === q.s);
const examOf = () => CFG.exams[String(S.level).split(" ")[0]] || null;
const blancName = () => (examOf() ? "Examen blanc" : "Devoir blanc");
// Essai gratuit : tout est débloqué pendant TRIAL_DAYS jours à partir de la première ouverture
const TRIAL_DAYS = 10;
if (!S.trialStart) { S.trialStart = today(); store.save(); }
const trialLeft = () => Math.max(0, TRIAL_DAYS - Math.floor((new Date(today()) - new Date(S.trialStart)) / 864e5));
const isIOS = /iphone|ipad|ipod/i.test(navigator.userAgent);
const standalone = matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;
const isPremium = () => S.premium || trialLeft() > 0;
const open = (q) => isPremium() || q.free;
const qsOf = (sid) => DATA.questions.filter((q) => q.s === sid);
// Tirage sans répétition : d'abord les questions jamais vues, puis celles ratées, puis les plus anciennes ;
// l'ordre des réponses est mélangé à chaque fois pour qu'on ne retienne pas « c'est la B ».
function pickFresh(pool, n) {
  const now = Date.now(), score = (q) => { const st = S.stats[q.id]; if (!st) return Math.random();
    const ageDays = (now - (st.t || 0)) / 864e5; return (st.last === false ? 2 : 4) + (st.ok + st.ko) - Math.min(ageDays, 30) / 10 + Math.random(); };
  return pool.map((q) => [score(q), q]).sort((a, b) => a[0] - b[0]).slice(0, n).map(([, q]) => remix(q));
}
function remix(q) {
  const order = shuffle([0, 1, 2, 3]);
  return { ...q, c: order.map((i) => q.c[i]), a: order.indexOf(q.a) };
}
// Questions de la base + questions générées (nombres nouveaux à chaque fois) pour les abonnés et pendant l'essai
function mixQuestions(sid, pool, n, chapters = null) {
  const g = isPremium() && typeof genQuestions === "function" ? genQuestions(sid, Math.round(n * 0.4), chapters) : [];
  return shuffle([...pickFresh(pool, n - g.length), ...g]);
}
const subjName = (sid) => (DATA.subjects.find((s) => s.id === sid) || {}).name || "";

function mastery(sid) {
  const qs = qsOf(sid), done = qs.filter((q) => S.stats[q.id] && S.stats[q.id].last).length;
  return Math.round((100 * done) / qs.length);
}
function record(q, ok) {
  const st = S.stats[q.id] || { ok: 0, ko: 0 };
  if (q.gen) { const d = (S.daily = S.daily || {})[today()] || { n: 0, ok: 0 }; d.n++; d.ok += ok; S.daily[today()] = d; store.save(); return; }
  st[ok ? "ok" : "ko"]++; st.last = ok; st.t = Date.now(); S.stats[q.id] = st;
  if (!S.days.includes(today())) S.days.push(today());
  const d = (S.daily = S.daily || {})[today()] || { n: 0, ok: 0 }; d.n++; d.ok += ok; S.daily[today()] = d;
  store.save();
}
// Missions du jour (programme des 10 jours d'essai, puis programme quotidien)
const doneToday = (tag) => ((S.done || {})[today()] || []).includes(tag);
function markDone(tag) { S.done = S.done || {}; const t = S.done[today()] || []; if (!t.includes(tag)) { t.push(tag); S.done[today()] = t; store.save(); } }
function streak() {
  let n = 0; const d = new Date();
  if (!S.days.includes(today())) d.setDate(d.getDate() - 1);
  while (S.days.includes(d.toISOString().slice(0, 10))) { n++; d.setDate(d.getDate() - 1); }
  return n;
}

// ---------- Choix de la classe puis de la série
function viewLevel() {
  const cls = location.hash.split("/")[1] ? decodeURIComponent(location.hash.split("/")[1]) : null;
  const series = cls && DATA.series[cls];
  const pick = (l, sub) => `<button class="subj lvl" data-l="${esc(l)}"${l === S.level ? ' aria-pressed="true"' : ""}><b>${esc(l)}</b><span class="small muted">${sub}</span></button>`;
  const info = (l) => { const ex = CFG.exams[l.split(" ")[0]]; return ex ? "Année du " + ex[0] : subjectsOf(l).length + " matières"; };
  $view.innerHTML = series
    ? `<h1>Quelle série en ${esc(cls)} ?</h1><div class="grid">${series.map((sr) => pick(`${cls} ${sr}`, `${subjectsOf(`${cls} ${sr}`).length} matières`)).join("")}</div>
       <a class="btn alt" href="#classe">Retour aux classes</a>`
    : `<h1>Tu es en quelle classe ?</h1>
       <p class="muted">Tu pourras changer plus tard en touchant ta classe en haut de l'écran.</p>
       <div class="grid">${DATA.classes.map((c) => DATA.series[c]
         ? `<a class="subj lvl" href="#classe/${encodeURIComponent(c)}" style="text-decoration:none;color:inherit"${String(S.level).startsWith(c + " ") ? ' aria-pressed="true"' : ""}><b>${esc(c)}</b><span class="small muted">${CFG.exams[c] ? "Année du " + CFG.exams[c][0] + " · " : ""}séries ${DATA.series[c].join(", ")}</span></a>`
         : pick(c, info(c))).join("")}</div>`;
  $view.querySelectorAll("[data-l]").forEach((b) => b.onclick = () => { const first = !S.level && !S.parcoursVu; S.level = b.dataset.l; S.parcoursVu = true; store.save(); go(first ? "bienvenue" : "accueil"); });
}

// ---------- Accueil
const notionsOf = (level) => subjectsOf(level).flatMap((s) => ((DATA.notions || {})[s.id] || []).map((c) => ({ ...c, sid: s.id, sname: s.name })));
const exercisesOf = (level) => (DATA.exercises || []).filter((e) => matches(e.levels, level));
// Exercices et sujets types fabriqués à la demande (exos_gen.js) : nombres nouveaux à chaque essai
const genExosOf = (level) => (typeof EXGEN === "undefined" ? [] : subjectsOf(level).flatMap((s) => (EXGEN[s.id] || []).map((t, k) => ({ id: `gx-${s.id}-${k}`, subject: s.name, title: t.t }))));
const genSujetsOf = (level) => (typeof EXGEN === "undefined" ? [] : subjectsOf(level).filter((s) => (EXGEN[s.id] || []).length >= 3).map((s) => ({ id: `gs-${s.id}`, subject: s.name })));
// Rubriques de l'accueil : [clé, lien, icône, titre, sous-titre] ; l'élève peut en épingler et en masquer
function rubriqueList() {
  const nAnn = annalesOf(S.level).length, nGs = genSujetsOf(S.level).length, nGx = genExosOf(S.level).length, nEx = exercisesOf(S.level).length + annalesOf(S.level).filter((a) => a.guided).length + nGx;
  const exam = examOf() ? examOf()[0] : "BAC", nNot = notionsOf(S.level).length;
  return [
    nAnn || nGs ? ["annales", "#annales", "📚", examOf() ? `Sujets du ${exam}` : "Devoirs types", `${nAnn ? `${nAnn} sujet${nAnn > 1 ? "s" : ""} rédigé${nAnn > 1 ? "s" : ""}` : ""}${nAnn && nGs ? " + " : ""}${nGs ? "un sujet neuf à chaque essai" : ""}, corrigés pas à pas`] : null,
    ["aide", "#aide", "🆘", "Je bloque sur un exercice", "Écris, dicte ou photographie l'énoncé : indice, méthode, exercice corrigé"],
    ["devoir", "#devoir", "🎯", "Préparer un devoir", "Choisis la matière et les chapitres du programme"],
    ["qcm", "#qcm-list", "✅", "QCM corrigés", "Par matière ou par thème, chaque choix expliqué"],
    ["exercices", "#exercices", "✏️", "Exercices corrigés", nEx ? `${nEx} exercices pas à pas${nGx ? ", nombres nouveaux à chaque essai" : ""}` : "Bientôt pour ta classe"],
    nNot ? ["notions", "#notions", "📖", "Notions de cours", `${nNot} chapitres : cours, exemples, exercice corrigé`] : null,
    ["fiches", "#fiches", "📝", "Synthèses de cours", "L'essentiel à retenir"],
    ["notes", "#notes", "📒", "Mes notes", "Moyenne, prévision, coefficients officiels, orientation"],
    ["trajectoire", "#trajectoire", "🧭", "Ma trajectoire", "Ton suivi jusqu'à l'examen et ta semaine séance par séance"],
    ["agenda", "#agenda", "🗓️", "Mon agenda", "Emploi du temps (photo ou saisie guidée), devoirs, rappels du soir"],
    ["assistant", "#assistant", "💬", "Pose ta question", "Une notion pas claire ? Je réponds avec le cours"],
    ["apprendre", "#apprendre", "🚀", "Mieux apprendre", "Plan de révision, diagnostic, jour J, dictées, cartes mentales"],
    ["outils", "#outils", "🧰", "Mes outils", "Fiches flash, formulaire, moyenne, minuteur, journal"],
    ["challenge", "#challenge", "🏆", "Challenge du jour", "Toutes les matières, résultats en graphique"],
    ["duo", "#duo", "👥", "Session de groupe", "De 2 à 10 élèves, classement en direct"],
    ["examen", "#examen", "⏱️", blancName(), `${EXAM_LEN} questions en ${EXAM_MIN} min${isPremium() ? "" : " 🔒"}`],
    ["vie", "#vie", "🌍", "Les cours dans la vie", "Marché, factures Senelec et eau, solaire, route"],
  ].filter(Boolean);
}
// préférences d'accueil, complétées sur place (même objet partout, pour que chaque clic soit bien enregistré)
function homePrefs() {
  const h = S.home || (S.home = {});
  for (const [k, v] of Object.entries({ order: [], hidden: [], pins: [], hiddenRub: [], allRub: false })) if (!(k in h)) h[k] = Array.isArray(v) ? [] : v;
  // accueil allégé (une fois pour tous) : bonjour et rubriques en haut, les blocs secondaires masqués
  // (ils restent dans les rubriques et peuvent être réaffichés dans « Organiser mon accueil »)
  if (!h.v2) {
    h.v2 = true; h.order = []; h.allRub = false;
    h.hidden = [...new Set([...h.hidden.filter((k) => k !== "rubriques" && k !== "compteur"), ...HOME_HIDDEN])];
  }
  return h;
}
const RUB_COURT = { annales: null, aide: "Je bloque", devoir: "Préparer un devoir", qcm: "QCM", exercices: "Exercices", notions: "Cours", fiches: "Synthèses", notes: "Mes notes", trajectoire: "Ma trajectoire",
  agenda: "Agenda", assistant: "Poser une question", apprendre: "Mieux apprendre", outils: "Tous mes outils", challenge: "Challenge", duo: "En groupe", examen: null, vie: "Dans la vie" };
// rubriques rangées par besoin (demande d'Est) : bloqué → devoirs → cours → outils → suivi
const RUB_GROUPES = [
  ["📝", "Devoirs et entraînement", ["annales", "devoir", "exercices", "qcm", "examen", "challenge", "duo"]],
  ["📖", "Apprendre le cours", ["notions", "fiches", "assistant", "apprendre", "vie"]],
  ["📊", "Mon suivi", ["notes", "trajectoire", "agenda"]],
];
const OUTILS_ACCUEIL = [["formules", "📐", "Formulaire"], ["flash", "🃏", "Fiches flash"], ["journal", "📓", "Ma fiche"], ["moyenne", "🧮", "Moyenne"]];
function rubriques() {
  const h = homePrefs(), tile = ([k, href, icon, title], pin) => `<a class="subj tile" href="${href}"><span class="ico">${icon}</span><b>${pin ? "⭐ " : ""}${esc(RUB_COURT[k] || title)}</b></a>`;
  const list = rubriqueList().filter((r) => !h.hiddenRub.includes(r[0])), get = (k) => list.find((r) => r[0] === k);
  const titre = (i, t) => `<h3 class="rubh">${i} ${t}</h3>`, grille = (rs) => rs.length ? `<div class="grid rub">${rs.map((r) => tile(r, false)).join("")}</div>` : "";
  let out = "";
  const pinned = h.pins.map(get).filter(Boolean);
  if (pinned.length) out += titre("⭐", "Mes favoris") + grille(pinned);
  if (get("aide")) out += `<a class="sosbig" href="#aide"><span class="ico">🆘</span><span><b>Je bloque sur un exercice ou un devoir</b><small>Écris, dicte ou prends en photo l'énoncé : indice, méthode puis corrigé</small></span></a>`;
  const vus = new Set(["aide", "outils", ...h.pins]);
  for (const [i, t, ks] of RUB_GROUPES) {
    const rs = ks.filter((k) => !vus.has(k)).map(get).filter(Boolean);
    ks.forEach((k) => vus.add(k));
    out += rs.length ? titre(i, t) + grille(rs) : "";
    // les outils juste après les devoirs, bien visibles : on s'en sert pendant les exercices
    if (ks[0] === "annales" && get("outils")) out += `<div class="outilsbox"><div class="row" style="justify-content:space-between;align-items:center"><b>🧰 Mes outils : ton arme secrète</b><a href="#outils" class="small">Tout voir ›</a></div>
      <p class="small" style="margin:4px 2px 8px">Formules et fiches de chaque matière, ta propre fiche, ta moyenne : avec ces outils tu révises plus vite et tu sais toujours où tu en es.</p>
      <div class="grid rub">${OUTILS_ACCUEIL.map(([id, ic, t]) => `<a class="subj tile" href="#outils/${id}"><span class="ico">${ic}</span><b>${t}</b></a>`).join("")}</div></div>`;
  }
  const reste = list.filter((r) => !vus.has(r[0]));
  if (reste.length) out += titre("➕", "Autres") + grille(reste);
  return out;
}

// ---------- Parcours de départ : les premières étapes conseillées selon la classe, cochées automatiquement
function everDone(tag) { return Object.values(S.done || {}).some((t) => t.includes(tag)); }
function parcoursSteps() {
  const ex = examOf(), nAnn = annalesOf(S.level).length + genSujetsOf(S.level).length;
  return [
    ["🩺", "Fais ton diagnostic", "15 min pour savoir par où commencer, matière par matière", "#diagnostic", !!S.diag],
    ["🗓️", "Note ton emploi du temps", "L'appli te rappellera chaque soir quoi réviser pour le lendemain", "#agenda", Object.keys(S.edt || {}).length > 0],
    ["📖", "Lis ta première notion de cours", "Cours, à retenir, exemple, puis un exercice corrigé", "#notions", everDone("fiche")],
    ["✅", "Fais un QCM sur un chapitre", "Par thème, comme pour préparer un devoir", "#qcm-list", everDone("qcm")],
    ["✏️", "Fais un exercice corrigé pas à pas", "Avec support ou tout seul, à toi de choisir", "#exercices", everDone("exo")],
    ex && nAnn ? ["📚", `Essaie un sujet du ${ex[0]}`, "Un vrai sujet complet, corrigé étape par étape, noté sur 20", "#annales", everDone("sujet")]
      : ["🏆", "Fais le challenge du jour", "Toutes tes matières en 10 questions", "#challenge", everDone("challenge")],
    ["⭐", "Organise ton accueil", "Épingle tes rubriques préférées, range ou masque les blocs", "#accueil/organiser", !!S.homeSet],
  ];
}
function parcoursCard() {
  const st = parcoursSteps(), n = st.filter((x) => x[4]).length;
  if (S.parcoursFini || n === st.length) return "";
  const next = st.find((x) => !x[4]);
  return `<div class="card prog"><div class="row"><h2>🧭 Bien démarrer en ${esc(S.level)}</h2><b>${n}/${st.length}</b></div>
    <span class="bar"><i style="width:${Math.round((100 * n) / st.length)}%"></i></span>
    <a class="mission" href="${next[3]}"><span>${next[0]}</span><span><b>Étape suivante : ${esc(next[1])}</b><br><span class="small muted">${esc(next[2])}</span></span></a>
    <a class="small" href="#bienvenue">Voir tout le parcours ›</a></div>`;
}
function viewBienvenue() {
  const st = parcoursSteps(), n = st.filter((x) => x[4]).length, ex = examOf();
  $view.innerHTML = `<h1>🧭 Ton parcours en ${esc(S.level)}</h1>
    <p class="muted">${ex ? `Objectif ${ex[0]} : voici l'ordre conseillé pour bien démarrer.` : "Voici l'ordre conseillé pour bien démarrer."} Chaque étape se coche toute seule quand tu l'as faite. Tu peux aussi les faire dans l'ordre que tu veux.</p>
    <div class="card prog"><div class="row"><b>${n} étape${n > 1 ? "s" : ""} sur ${st.length}</b></div><span class="bar"><i style="width:${Math.round((100 * n) / st.length)}%"></i></span>
    ${st.map(([ico, t, sub, href, ok], i) => `<a class="mission${ok ? " done" : ""}" href="${href}"><span>${ok ? "✅" : ico}</span><span><b>${i + 1}. ${esc(t)}</b><br><span class="small muted">${esc(sub)}</span></span></a>`).join("")}</div>
    <div class="card"><h2>Ensuite, chaque jour</h2><ul class="steps"><li>Fais tes <b>3 missions du jour</b> sur l'accueil (environ 20 minutes).</li><li>Le soir, regarde ton <b>agenda</b> : il te dit quoi réviser pour le lendemain.</li><li>Avant un devoir, va dans <b>Préparer un devoir</b> et choisis les chapitres.</li><li>Une fois par semaine, refais tes <b>erreurs</b>.</li></ul></div>
    <div class="btns"><a class="btn" href="#accueil">Aller à l'accueil</a>${n < st.length ? `<button class="btn alt" id="pfin">Masquer ce parcours</button>` : ""}</div>`;
  const f = document.getElementById("pfin");
  if (f) f.onclick = () => { S.parcoursFini = true; store.save(); go("accueil"); };
}

// ---------- Organiser l'accueil : l'élève range les blocs, masque ce qui ne lui sert pas et épingle ses rubriques
const HOME_BLOCKS = [["compteur", "👋 Bonjour, compte à rebours et série"], ["rubriques", "🗂️ Rubriques"], ["parcours", "🧭 Bien démarrer"], ["trajectoire", "📈 Ma trajectoire"], ["notes", "📒 Mes notes"], ["programme", "✅ Missions du jour"], ["matieres", "📘 QCM par matière"], ["agenda", "🗓️ Mon agenda"], ["profil", "🦁 Mon niveau et mes XP"], ["plan", "📅 Mon plan de révision"], ["daily", "❓ Question du jour"], ["citation", "💬 Citation du jour"], ["actions", "⏱️ Examen blanc et partage"]];
const HOME_HIDDEN = ["trajectoire", "notes", "matieres", "agenda", "profil", "plan", "citation", "actions"];
function homeOrder() { const h = homePrefs(), keys = HOME_BLOCKS.map((b) => b[0]); return [...h.order.filter((k) => keys.includes(k)), ...keys.filter((k) => !h.order.includes(k))]; }
function viewOrganiser() {
  const h = homePrefs(), order = homeOrder(), rub = rubriqueList();
  const name = (k) => HOME_BLOCKS.find((b) => b[0] === k)[1];
  $view.innerHTML = `<h1>⭐ Organiser mon accueil</h1>
    <p class="muted">Range les blocs dans l'ordre qui te convient, masque ceux qui ne te servent pas, et épingle tes rubriques préférées en haut.</p>
    <div class="card"><h2>Les blocs de l'accueil</h2>${order.map((k, i) => `<div class="row small" style="padding:6px 0;border-bottom:1px solid var(--line);gap:6px">
      <span style="flex:1${h.hidden.includes(k) ? ";opacity:.45" : ""}">${name(k)}</span>
      <button class="btn alt small" data-up="${i}" aria-label="Monter"${i ? "" : " disabled"}>↑</button><button class="btn alt small" data-down="${i}" aria-label="Descendre"${i < order.length - 1 ? "" : " disabled"}>↓</button>
      <button class="btn${h.hidden.includes(k) ? "" : " alt"} small" data-hide="${k}">${h.hidden.includes(k) ? "Afficher" : "Masquer"}</button></div>`).join("")}</div>
    <div class="card"><h2>Les rubriques</h2><p class="small muted">⭐ = épinglée en haut de l'accueil.</p>${rub.map(([k, , ico, t]) => `<div class="row small" style="padding:6px 0;border-bottom:1px solid var(--line);gap:6px">
      <span style="flex:1${h.hiddenRub.includes(k) ? ";opacity:.45" : ""}">${ico} ${esc(t)}</span>
      <button class="btn${h.pins.includes(k) ? "" : " alt"} small" data-pin="${k}">${h.pins.includes(k) ? "⭐ Épinglée" : "☆ Épingler"}</button>
      <button class="btn${h.hiddenRub.includes(k) ? "" : " alt"} small" data-hrub="${k}">${h.hiddenRub.includes(k) ? "Afficher" : "Masquer"}</button></div>`).join("")}</div>
    <div class="btns"><a class="btn" href="#accueil">Voir mon accueil</a><button class="btn alt" id="reset">Revenir à la disposition de départ</button></div>`;
  const save = () => { S.homeSet = true; store.save(); viewOrganiser(); };
  const toggle = (arr, k) => { const i = arr.indexOf(k); i < 0 ? arr.push(k) : arr.splice(i, 1); };
  const move = (i, d) => { const o = homeOrder(); [o[i], o[i + d]] = [o[i + d], o[i]]; h.order = o; save(); };
  $view.querySelectorAll("[data-up]").forEach((b) => b.onclick = () => move(+b.dataset.up, -1));
  $view.querySelectorAll("[data-down]").forEach((b) => b.onclick = () => move(+b.dataset.down, 1));
  $view.querySelectorAll("[data-hide]").forEach((b) => b.onclick = () => { toggle(h.hidden, b.dataset.hide); save(); });
  $view.querySelectorAll("[data-pin]").forEach((b) => b.onclick = () => { toggle(h.pins, b.dataset.pin); h.hiddenRub = h.hiddenRub.filter((x) => x !== b.dataset.pin); save(); });
  $view.querySelectorAll("[data-hrub]").forEach((b) => b.onclick = () => { toggle(h.hiddenRub, b.dataset.hrub); h.pins = h.pins.filter((x) => x !== b.dataset.hrub); save(); });
  document.getElementById("reset").onclick = () => { S.home = null; save(); };
}
// Vidéo de présentation (45 s), proposée sur l'accueil pendant les premiers jours
function tutoCard() {
  if (S.premium || S.tutoVu || S.eco) return "";
  return `<div class="card tuto"><div class="row"><h2>▶️ Découvre l'appli en 45 secondes</h2><button class="btn alt small" id="tuto-x" aria-label="Fermer">✕</button></div>
    <video src="tuto.mp4" controls playsinline preload="none" poster="apercu.png"></video></div>`;
}
function programme() {
  const n = Math.min(TRIAL_DAYS, Math.floor((new Date(today()) - new Date(S.trialStart)) / 864e5) + 1);
  const weakest = subjectsOf(S.level).filter((s) => !/annales/.test(s.id)).sort((a, b) => mastery(a.id) - mastery(b.id))[0];
  const third = n % 3 === 1 ? ["exo", "#exercices", "Fais un exercice corrigé"] : n % 3 === 2 ? (() => { const ch = (DATA.notions || {})[weakest && weakest.id] || [];
    return ch.length ? ["fiche", `#notion/${ch[Math.floor(n / 3) % ch.length].id}`, `Apprends un chapitre de ${weakest.name} : ${ch[Math.floor(n / 3) % ch.length].title}`] : ["fiche", weakest ? `#fiche/${weakest.id}` : "#fiches", "Lis une synthèse de cours"]; })() : ["duo", "#duo", "Fais une session de groupe avec tes camarades"];
  const missions = [["challenge", "#challenge", "Fais le challenge du jour (toutes matières)"],
    ["qcm", weakest ? `#quiz/${weakest.id}` : "#qcm-list", `QCM dans ta matière la plus faible${weakest ? " : " + weakest.name : ""}`], third];
  programme.missions = missions;
  const done = missions.filter(([t]) => doneToday(t)).length;
  const trial = !S.premium && n <= TRIAL_DAYS;
  return `<div class="card prog"><div class="row"><h2>${trial ? `Mon programme : jour ${n} / ${TRIAL_DAYS}` : "Mes missions du jour"}</h2><b>${done}/3</b></div>
    ${missions.map(([t, href, label]) => `<a class="mission${doneToday(t) ? " done" : ""}" href="${href}"><span>${doneToday(t) ? "✅" : "⬜"}</span><span>${esc(label)}</span></a>`).join("")}
    ${done === 3 ? `<p class="msg-ok small">Bravo, journée réussie ! Reviens demain pour garder ta série 🔥</p>` : `<p class="small muted">3 missions par jour, environ 20 minutes.</p>`}</div>`;
}
// le bouton principal de l'accueil : la prochaine mission du jour pas encore faite
// tout ce que l'appli contient pour la classe, d'un coup d'œil (chaque chiffre ouvre la rubrique)
function dispo() {
  const L = S.level, ann = annalesOf(L).length + genSujetsOf(L).length, ex = exercisesOf(L).length + annalesOf(L).filter((a) => a.guided).length + genExosOf(L).length;
  const qcm = subjectsOf(L).reduce((n, s) => n + s.count, 0), cours = notionsOf(L).length, fi = subjectsOf(L).reduce((n, s) => n + ((DATA.fiches || {})[s.id] || []).length, 0);
  const c = (n, ico, t, href) => n ? `<a href="${href}" class="dispo-i"><b>${ico} ${n.toLocaleString("fr-FR")}</b><span>${t}</span></a>` : "";
  return `<p class="small" style="margin:10px 0 6px"><b>Tout est corrigé pas à pas :</b></p><div class="dispo">${c(ann, "📚", examOf() ? `sujets du ${examOf()[0]}` : "devoirs types", "#annales")}${c(ex, "✏️", "exercices", "#exercices")}${c(qcm, "✅", "QCM", "#qcm-list")}${c(cours, "📖", "cours", "#notions")}${c(fi, "📝", "synthèses", "#fiches")}</div>`;
}
function suite() {
  if (!programme.missions) programme();
  const m = (programme.missions || []).find(([t]) => !doneToday(t));
  return m ? [m[1], m[2]] : ["#challenge", "Le challenge du jour"];
}
function viewHome() {
  const ex = examOf();
  const days = ex ? Math.max(0, Math.ceil((new Date(ex[1]) - new Date(today())) / 864e5)) : 0;
  const answered = Object.values(S.stats).reduce((n, s) => n + s.ok + s.ko, 0);
  const free = DATA.questions.filter((q) => q.free && inLevel(q));
  const daily = free[Math.floor(new Date(today()).getTime() / 864e5) % free.length];
  const subs = subjectsOf(S.level).map((s) => `
    <a class="subj" href="#quiz/${s.id}" style="text-decoration:none;color:inherit">
      <b>${esc(s.name)}</b>
      <span class="small muted">${s.count} questions${(GEN[s.id] || []).length ? " + ∞ à nombres nouveaux" : ""}${isPremium() ? "" : ` · <span class="lock">🔒</span>`}</span>
      <span class="bar"><i style="width:${mastery(s.id)}%"></i></span>
    </a>`).join("");
  const blocks = {
    compteur: () => {
      const nom = myName(), next = suite();
      return `<div class="card hello"><h2>${nom ? `Bonjour ${esc(nom)} 👋` : "Bonjour 👋"}</h2>
        <p class="small muted">${ex ? `<b>J−${days}</b> avant le ${ex[0]}` : `<b>${answered}</b> réponses données`} · Série : <b>${streak()} 🔥</b></p>
        ${dispo()}</div>`;
    },
    parcours: parcoursCard,
    trajectoire: () => (typeof trajCard === "function" ? trajCard() : ""),
    notes: () => (typeof notesCard === "function" ? notesCard() : ""),
    programme: () => tutoCard() + programme(),
    rubriques: () => `<div class="rubwrap">${rubriques()}</div>`,
    matieres: () => `<h2 id="qcm">QCM corrigés : choisis une matière</h2><div class="grid">${subs}</div>`,
    agenda: () => agendaCard(),
    profil: () => (typeof profilCard === "function" ? profilCard() : ""),
    plan: () => (typeof planCard === "function" ? planCard() : ""),
    daily: () => daily ? `<div class="card" id="daily"><h2><span class="hi">Question du jour</span></h2><p class="small muted">${esc(subjName(daily.s))}</p>${questionBlock(daily)}</div>` : "",
    citation: () => (typeof citationCard === "function" ? citationCard() : ""),
    actions: () => `<div class="btns"><a class="btn hi-btn" href="#examen">${blancName()} : ${EXAM_LEN} questions en ${EXAM_MIN} min${isPremium() ? "" : " 🔒"}</a>
      <a class="btn alt" href="#partager">Partager l'appli à un camarade (lien ou QR code)</a></div>`,
  };
  const h = homePrefs();
  $view.innerHTML = `
    ${Compte.isAdmin && Compte.isAdmin() ? `<a class="btn" href="#admin/activite">🛠️ Espace admin : inscrits, connexions, erreurs</a>` : ""}
    ${isIOS && !standalone ? `<div class="card small"><b>Installer sur iPhone :</b> ouvre ce lien dans Safari, appuie sur Partager (carré avec une flèche) puis sur « Sur l'écran d'accueil ».</div>` : ""}
    ${!S.premium && trialLeft() > 0 ? `<a class="trial" href="#premium">🎁 Essai gratuit : tout est débloqué encore <b>${trialLeft()} jour${trialLeft() > 1 ? "s" : ""}</b></a>` : ""}
    ${!isPremium() ? `<a class="trial" href="#premium">🔒 Ton essai gratuit de ${TRIAL_DAYS} jours est terminé. Abonne-toi pour tout retrouver, avec tes progrès.</a>` : ""}
    ${homeOrder().filter((k) => !h.hidden.includes(k)).map((k) => blocks[k]() + (k === "rubriques" ? (typeof pauseCard === "function" ? pauseCard() : "") : "")).join("")}
    ${typeof pushCard === "function" ? pushCard() : ""}
    <a class="btn alt" href="#accueil/organiser">⭐ Organiser mon accueil</a>`;
  if (daily && $view.querySelector("#daily"))   bindQuestion($view.querySelector("#daily"), daily, () => {});
  const tx = $view.querySelector("#tuto-x");
  if (tx) tx.onclick = () => { S.tutoVu = true; store.save(); tx.closest(".tuto").remove(); };
}

const srcLine = (q) => (q.src ? `<p class="src">📄 Source : ${esc(q.src)}</p>` : "");
function questionBlock(q) {
  return `${q.src ? `<p class="tag-src">${esc(q.src)}</p>` : ""}<p class="q">${esc(q.q)}</p><div class="choices">${q.c.map((c, i) =>
    `<button class="choice" data-i="${i}"><span class="l">${LETTERS[i]}</span><span>${esc(c)}</span></button>`).join("")}</div>
    <div class="expl" hidden></div>`;
}
function bindQuestion(root, q, done, showExpl = true) {
  root.querySelectorAll(".choice").forEach((b) => b.onclick = () => {
    const i = +b.dataset.i, ok = i === q.a;
    root.querySelectorAll(".choice").forEach((x) => { x.disabled = true; if (+x.dataset.i === q.a && showExpl) x.classList.add("ok"); });
    if (showExpl) {
      if (!ok) b.classList.add("ko");
      const ex = root.querySelector(".expl");
      ex.innerHTML = ok ? `<b class="msg-ok">Bonne réponse !</b> ${esc(q.e)}${srcLine(q)}`
        : `<b class="msg-ko">Pas tout à fait.</b><br>Tu as répondu : <s>${esc(q.c[i])}</s><br>La bonne réponse est <b>${LETTERS[q.a]} : ${esc(q.c[q.a])}</b>
          <p><b>Pourquoi :</b> ${esc(q.e)}</p><p class="small muted">Cette question est gardée dans « Mes erreurs » pour la refaire plus tard.</p>${srcLine(q)}`;
      ex.hidden = false;
    } else b.classList.add("ok");
    record(q, ok); done(ok, i);
  });
}

// ---------- Quiz par matière, erreurs, examen blanc
function runQuiz(title, qs, back, { exam = false, duo = null, solo = false, onEnd = null } = {}) {
  const hide = exam || solo;
  clearInterval(timer);
  if (!qs.length) { $view.innerHTML = `<div class="card"><h2>${esc(title)}</h2><p class="muted">Aucune question ici pour l'instant.</p><a class="btn" href="${back}">Retour</a></div>`; return; }
  let k = 0, score = 0; const answers = [];
  const end = Date.now() + EXAM_MIN * 60e3;
  if (exam) timer = setInterval(() => {
    const left = Math.max(0, end - Date.now()), el = document.getElementById("timer");
    if (el) el.textContent = `${Math.floor(left / 60e3)}:${String(Math.floor(left / 1e3) % 60).padStart(2, "0")}`;
    if (!left) finish();
  }, 500);
  function step() {
    const q = qs[k];
    $view.innerHTML = `<div class="progress"><span>${esc(title)}</span><span>${exam ? `<span class="timer" id="timer"></span> · ` : ""}${k + 1} / ${qs.length}</span></div>
      <div class="bar"><i style="width:${(100 * k) / qs.length}%"></i></div>
      <div class="card" id="qc">${hide ? `<p class="small muted">${esc(subjName(q.s))}</p>` : ""}${questionBlock(q)}</div>
      <button class="btn" id="next" hidden>${k + 1 < qs.length ? "Question suivante" : "Voir mon score"}</button>`;
    const next = document.getElementById("next");
    bindQuestion(document.getElementById("qc"), q, (ok, i) => {
      score += ok; answers.push({ q, i, ok });
      if (hide) { k + 1 < qs.length ? (k++, step()) : finish(); } else next.hidden = false;
    }, !hide);
    next.onclick = () => (k + 1 < qs.length ? (k++, step()) : finish());
    window.scrollTo(0, 0);
  }
  function finish() {
    clearInterval(timer);
    const total = hide ? qs.length : answers.length, note = Math.round((20 * score) / total * 10) / 10;
    S.sessions.push({ t: title, score, total, d: today() }); store.save();
    const mot = note >= 16 ? "Excellent, continue comme ça !" : note >= 12 ? "Bien joué, encore un effort." : note >= 10 ? "C'est juste, revois tes erreurs." : "Courage, revois les corrections et recommence.";
    const fixes = hide ? `<h2>Corrigé ligne par ligne</h2><div class="list">${qs.map((q) => { const a = answers.find((x) => x.q === q);
      return `<div class="card"><p class="small muted">${esc(subjName(q.s))}</p><p><b>${esc(q.q)}</b></p>
        <p class="${a && a.ok ? "msg-ok" : "msg-ko"}">${a ? (a.ok ? "✓ " : "✗ Ta réponse : " + esc(q.c[a.i]) + " · ") : "Sans réponse · "}Bonne réponse : ${esc(q.c[q.a])}</p>
        <p class="small muted">${esc(q.e)}</p>${srcLine(q)}</div>`; }).join("")}</div>` : "";
    $view.innerHTML = `<div class="card" style="text-align:center"><p class="muted">${esc(title)}</p><p class="score">${note} / 20</p>
      <p>${score} bonne${score > 1 ? "s" : ""} réponse${score > 1 ? "s" : ""} sur ${total}</p><p><b>${mot}</b></p></div>
      ${!isPremium() ? `<div class="card"><p>Il y a encore beaucoup de questions dans cette matière, avec l'examen blanc chronométré.</p><a class="btn hi-btn" href="#premium">Débloquer tout pour ${fcfa(CFG.price_fcfa)}</a></div>` : ""}
      ${duo ? `<div class="card"><h2>Classement du groupe ${esc(duo)}</h2><div id="board"><p class="small muted">Chargement du classement…</p></div></div>
        <a class="btn hi-btn" href="https://wa.me/?text=${encodeURIComponent(`Session de groupe ${duo} (${S.level}) : j'ai eu ${note}/20 (${score}/${total}). À toi ! ${duoLink(duo)}`)}" target="_blank" rel="noopener">Envoyer ma note au groupe sur WhatsApp</a>` : ""}
      ${onEnd ? onEnd(score, total, answers) : ""}
      <div class="btns"><button class="btn" id="again">Recommencer</button><a class="btn alt" href="${back}">Retour</a></div>${fixes}`;
    document.getElementById("again").onclick = () => render();
    if (duo) groupBoard(duo, { name: myName(), note, score, total, level: S.level });
    window.scrollTo(0, 0);
  }
  step();
}

// Avant chaque QCM ou exercice, l'élève choisit : avec support (corrigé après chaque réponse) ou tout seul (corrigé à la fin)
function chooseMode(title, sub, start) {
  $view.innerHTML = `<div class="card"><h1>${esc(title)}</h1><p class="muted">${esc(sub)}</p>
    <h2>Comment veux-tu travailler ?</h2>
    <button class="btn" id="m-help">🧑‍🏫 Avec support<br><span class="small">Corrigé et explication après chaque réponse</span></button>
    <button class="btn alt" id="m-solo">💪 Tout seul<br><span class="small">Tu réponds à tout, corrigé ligne par ligne à la fin</span></button></div>`;
  document.getElementById("m-help").onclick = () => start(false);
  document.getElementById("m-solo").onclick = () => start(true);
}
function viewQuiz(arg = "") {
  const [sid, theme] = arg.split("/"), s = DATA.subjects.find((x) => x.id === sid);
  if (!s) return go("accueil");
  const titres = (DATA.programmes || {})[sid] || [];
  // QCM par thème : un chapitre du programme, pour préparer un devoir
  if (theme === "themes") {
    const n = (i) => qsOf(sid).filter((q) => q.ch === i).length;
    $view.innerHTML = `<h1>${esc(s.name)} : QCM par thème</h1><p class="muted">Choisis le chapitre de ton prochain devoir : les questions portent uniquement sur ce chapitre.</p>
      ${titres.map((t, i) => n(i) ? `<a class="card lib-card" href="#quiz/${sid}/${i}"><b>${i + 1}. ${esc(t)}</b><span class="small muted">${n(i)} questions${(GEN[sid] || []).some(([c]) => c === t || c === i) ? " + ∞ à nombres nouveaux" : ""}${isPremium() ? "" : " 🔒"}</span></a>` : "").join("")}
      <a class="btn alt" href="#quiz/${sid}">Toutes les questions de ${esc(s.name)}</a><a class="btn alt" href="#qcm-list">Retour aux matières</a>`;
    return;
  }
  const ch = theme !== undefined && theme !== "" ? Number(theme) : null;
  if (ch !== null) {
    const qs = mixQuestions(sid, qsOf(sid).filter((q) => q.ch === ch && open(q)), QUIZ_LEN, [ch, titres[ch]]);
    return chooseMode(`QCM · ${titres[ch] || s.name}`, `${qs.length} questions sur ce chapitre`, (solo) => { markDone("qcm"); runQuiz(`${S.level} · ${titres[ch] || s.name}`, qs, `#quiz/${sid}/themes`, { solo }); });
  }
  const qs = mixQuestions(sid, qsOf(sid).filter(open), QUIZ_LEN);
  chooseMode(`QCM · ${s.name}`, `${qs.length} questions de ${S.level}`, (solo) => { markDone("qcm"); runQuiz(`${S.level} · ${s.name}`, qs, "#qcm-list", { solo }); });
}
function viewExam() {
  if (!isPremium()) return viewPremium(`${examOf() ? "L'examen blanc" : "Le devoir blanc"} fait partie du pack premium.`);
  const qs = pickFresh(DATA.questions.filter(inLevel), EXAM_LEN);
  runQuiz(`${blancName()} ${S.level}`, qs, "#accueil", { exam: true });
}
function viewErrors() {
  const wrong = DATA.questions.filter((q) => open(q) && inLevel(q) && S.stats[q.id] && S.stats[q.id].last === false);
  if (location.hash === "#erreurs/go") return runQuiz(`Mes erreurs ${S.level}`, shuffle(wrong).slice(0, QUIZ_LEN), "#erreurs");
  const by = {}; wrong.forEach((q) => (by[q.s] = (by[q.s] || 0) + 1));
  $view.innerHTML = `<h1>Mes erreurs</h1>
    <p class="muted">Les questions de ${S.level} que tu as ratées la dernière fois. Quand tu les réussis, elles disparaissent de la liste.</p>
    ${wrong.length ? `<div class="card">${Object.entries(by).map(([sid, n]) => `<div class="row"><span>${esc(subjName(sid))}</span><b>${n}</b></div>`).join("")}</div>
      <a class="btn" href="#erreurs/go">Revoir ${Math.min(wrong.length, QUIZ_LEN)} erreur${wrong.length > 1 ? "s" : ""}</a>`
    : `<div class="card"><p>Aucune erreur à revoir. Fais un quiz depuis l'accueil.</p><a class="btn" href="#accueil">Choisir une matière</a></div>`}`;
}

// ---------- Annales : sujets officiels repris dans l'appli et corrigés étape par étape (les références sont gardées dans contenu/)
const annalesOf = (level) => (DATA.annales || []).filter((a) => a.guided && matches(a.levels, level));

// ---------- Synthèses de cours : l'essentiel à retenir, gratuit, avant les quiz
function viewFiches() {
  const subs = subjectsOf(S.level).filter((s) => s.fiche);
  $view.innerHTML = `<h1>Synthèses de cours</h1><p class="muted">L'essentiel du programme de ${esc(S.level)} à retenir, matière par matière. Lis la fiche, puis entraîne-toi avec le quiz.</p>
    <div class="grid">${subs.map((s) => `<a class="subj" href="#fiche/${s.id}" style="text-decoration:none;color:inherit"><b>${esc(s.name)}</b><span class="small muted">${DATA.fiches[s.id].length} chapitres</span></a>`).join("")}</div>
    ${subs.length ? "" : `<div class="card"><p>Les synthèses de ta classe arrivent bientôt.</p></div>`}`;
}
function viewFiche(arg) {
  const [sid, k] = arg.split("~"), s = DATA.subjects.find((x) => x.id === sid), f = DATA.fiches && DATA.fiches[sid];
  if (!s || !f) return go("fiches");
  markDone("fiche");
  if (k === undefined) {
    $view.innerHTML = `<p class="tag-src">Synthèse de cours · ${esc(S.level)}</p><h1>${esc(s.name)}</h1>
      <p class="muted">${f.length} chapitres. Chaque chapitre : l'essentiel à savoir${f.some((c) => c.methodes) ? ", les méthodes pas à pas, les pièges, un exemple corrigé et ce qui tombe à l'examen" : ""}.</p>
      <div class="card">${f.map((c, i) => `<a class="row lib" href="#fiche/${sid}~${i}"><span>${i + 1}. ${esc(c.t)}</span><span class="small muted">lire ›</span></a>`).join("")}</div>
      <a class="btn" href="#quiz/${s.id}">M'entraîner sur ${esc(s.name)}</a>
      <a class="btn alt" href="#fiches">Autres synthèses</a>`;
    return;
  }
  const i = +k, c = f[i];
  if (!c) return go("fiche/" + sid);
  const nots = ((DATA.notions || {})[sid] || []).filter((n) => c.p !== undefined && n.pch === c.p);
  const prog = (DATA.programmes || {})[sid];
  $view.innerHTML = `<p class="tag-src">${esc(s.name)} · chapitre ${i + 1} / ${f.length}</p><h1>${esc(c.t)}</h1>
    <div class="btns">${typeof audioBtn === "function" ? audioBtn() : ""}<a class="btn alt" href="#carte/${sid}~${i}">🧠 Carte mentale</a></div>
    <div class="card notion-key"><h2>📌 L'essentiel</h2><ul class="steps">${c.cles.map((p) => `<li>${esc(p)}</li>`).join("")}</ul></div>
    ${(c.methodes || []).map(([t, st]) => `<div class="card"><h2>🛠️ Méthode : ${esc(t)}</h2><ol class="steps">${st.map((l) => `<li>${esc(l)}</li>`).join("")}</ol></div>`).join("")}
    ${c.pieges ? `<div class="card"><h2>⚠️ Pièges à éviter</h2><ul class="steps">${c.pieges.map((p) => `<li>${esc(p)}</li>`).join("")}</ul></div>` : ""}
    ${[...(c.exemple ? [c.exemple] : []), ...(c.exemples || [])].map(([q, lines], j, all) => `<div class="card"><h2>💡 Exercice corrigé${all.length > 1 ? " " + (j + 1) : ""}</h2><p><b>${esc(q)}</b></p><details><summary class="small">Voir le corrigé</summary><ol class="steps">${lines.map((l) => `<li>${esc(l)}</li>`).join("")}</ol></details></div>`).join("")}
    ${c.exam ? `<div class="card"><h2>🎯 À l'examen</h2><p>${esc(c.exam)}</p></div>` : ""}
    ${typeof pourquoiCard === "function" ? pourquoiCard(c.t, sid) : ""}
    ${prog && c.p !== undefined ? `<button class="btn hi-btn" id="train">✏️ M'entraîner sur ce chapitre</button>` : `<a class="btn hi-btn" href="#quiz/${s.id}">✏️ M'entraîner sur ${esc(s.name)}</a>`}
    ${nots.map((n) => `<a class="btn alt" href="#notion/${n.id}">📖 Cours détaillé : ${esc(n.title)}${isPremium() || n.free ? "" : " 🔒"}</a>`).join("")}
    ${f[i + 1] ? `<a class="btn alt" href="#fiche/${sid}~${i + 1}">Chapitre suivant : ${esc(f[i + 1].t)}</a>` : ""}
    <a class="btn alt" href="#fiche/${sid}">Tous les chapitres</a>`;
  const b = document.getElementById("train");
  if (b) b.onclick = () => { S.devoir = { ...(S.devoir || {}), [sid]: [c.p] }; store.save(); go("devoir/" + sid); };
  window.scrollTo(0, 0);
}
// ---------- Notions de cours : chapitre détaillé (cours, énoncé, exemples, illustration) + exercice corrigé
// icône d'une matière d'après son identifiant (pour les tuiles par matière)
const matIco = (sid) => [[/maths/, "📐"], [/pc|physique/, "⚗️"], [/svt/, "🌿"], [/philo/, "🤔"], [/hg|histoire|geo/, "🌍"], [/fr/, "📚"], [/an|en$/, "🇬🇧"], [/es/, "🇪🇸"], [/eco|ses/, "💹"], [/compta/, "🧾"], [/ar/, "🕌"], [/ec|civi/, "⚖️"]].find(([r]) => r.test(sid.replace(/^[^-]+-/, "")))?.[1] || "📘";
// Cours : d'abord une tuile par matière, puis les chapitres de la matière, rangés par chapitre du programme (demande d'Est)
function viewNotions(sid) {
  const all = notionsOf(S.level), subs = [...new Set(all.map((c) => c.sid))];
  const cur = subs.includes(sid) ? sid : subs.length === 1 ? subs[0] : null;
  if (!all.length) { $view.innerHTML = `<h1>Cours</h1><div class="card"><p>Les chapitres détaillés de ta classe arrivent. En attendant, lis les synthèses.</p><a class="btn" href="#fiches">Synthèses de cours</a></div>`; return; }
  if (!cur) {
    $view.innerHTML = `<h1>📖 Cours</h1><p class="muted">Choisis ta matière. Chaque chapitre : le cours expliqué, l'essentiel à retenir, des exemples, puis un exercice corrigé.</p>
      <div class="grid rub">${subs.map((s) => { const ch = all.filter((c) => c.sid === s);
        return `<a class="subj tile" href="#notions/${s}"><span class="ico">${matIco(s)}</span><b>${esc(ch[0].sname)}</b><span class="small muted">${ch.length} chapitres</span></a>`; }).join("")}</div>`;
    return;
  }
  const ch = all.filter((c) => c.sid === cur), prog = (DATA.programmes || {})[cur] || [];
  const carte = (c) => `<a class="card lib-card" href="#notion/${c.id}"><b>${esc(c.title)}${isPremium() || c.free ? "" : " 🔒"}</b><span class="small muted">Cours · ${c.exemples.length} exemple${c.exemples.length > 1 ? "s" : ""} · exercice corrigé</span></a>`;
  // regroupement par chapitre du programme quand il est connu
  const groupes = [];
  ch.forEach((c) => { const t = prog[c.pch] || "Autres chapitres"; let g = groupes.find((x) => x.t === t); if (!g) groupes.push(g = { t, p: c.pch ?? 99, l: [] }); g.l.push(c); });
  groupes.sort((x, y) => x.p - y.p);
  const onglets = subs.length > 1 ? `<div class="row onglets">${subs.map((s) => `<a class="btn alt small${s === cur ? " on" : ""}" href="#notions/${s}">${matIco(s)} ${esc(all.find((c) => c.sid === s).sname)}</a>`).join("")}</div>` : "";
  $view.innerHTML = `<h1>${matIco(cur)} ${esc(ch[0].sname)}</h1>${onglets}<p class="muted">${ch.length} chapitres de cours, rangés comme le programme.</p>
    ${groupes.map((g, i) => `<details class="card"${i === 0 ? " open" : ""}><summary><b>${groupes.length > 1 && !/^[A-Z]{1,3}\d/.test(g.t) ? `${i + 1}. ` : ""}${esc(g.t)}</b> <span class="small muted">· ${g.l.length}</span></summary>${g.l.map(carte).join("")}</details>`).join("")}
    ${subs.length > 1 ? `<a class="btn alt" href="#notions">Toutes les matières</a>` : ""}`;
}
function viewNotion(id) {
  const all = Object.entries(DATA.notions || {}).flatMap(([sid, ch]) => ch.map((c, i) => ({ ...c, sid, i, n: ch.length })));
  const c = all.find((x) => x.id === id);
  if (!c) return go("notions");
  if (!isPremium() && !c.free) return viewPremium("Tous les chapitres détaillés font partie du pack premium. Le premier chapitre de chaque matière est gratuit.");
  markDone("fiche");
  const s = DATA.subjects.find((x) => x.id === c.sid), next = all.find((x) => x.sid === c.sid && x.i === c.i + 1);
  $view.innerHTML = `<p class="tag-src">${esc(s ? s.name : "")} · chapitre ${c.i + 1} / ${c.n}</p><h1>${esc(c.title)}</h1>${typeof audioBtn === "function" ? audioBtn() : ""}
    <div class="card"><h2>📘 Le cours</h2>${c.cours.map((p) => `<p>${esc(p)}</p>`).join("")}</div>
    ${c.svg ? `<div class="card notion-fig">${c.svg}</div>` : ""}
    <div class="card notion-key"><h2>📌 À retenir</h2><ul class="steps">${c.enonce.map((p) => `<li>${esc(p)}</li>`).join("")}</ul></div>
    ${c.exemples.map(([t, lines]) => `<div class="card"><h2>💡 Exemple : ${esc(t)}</h2><ol class="steps">${lines.map((l) => `<li>${esc(l)}</li>`).join("")}</ol></div>`).join("")}
    <a class="btn hi-btn" href="#sujet/ch-${c.id}">✏️ Exercice corrigé sur ce chapitre</a>
    <a class="btn alt" href="#assistant/${encodeURIComponent(c.title)}">🤔 Je ne comprends pas : explique-moi autrement</a>
    ${next ? `<a class="btn alt" href="#notion/${next.id}">Chapitre suivant : ${esc(next.title)}${isPremium() || next.free ? "" : " 🔒"}</a>` : ""}
    <a class="btn alt" href="#notions/${c.sid}">Tous les chapitres de ${esc(s ? s.name : "la matière")}</a>`;
  window.scrollTo(0, 0);
}
// ---------- Préparer un devoir : l'élève choisit la matière puis les chapitres du programme sur lesquels il sera interrogé
function viewDevoir(arg) {
  const progs = DATA.programmes || {};
  const subs = subjectsOf(S.level).filter((s) => progs[s.id] && !/annales/.test(s.id));
  const s = subs.find((x) => x.id === arg);
  if (!s) {
    $view.innerHTML = `<h1>Préparer un devoir</h1><p class="muted">Tu as un devoir ou un contrôle bientôt ? Choisis la matière, puis coche les chapitres au programme : l'appli te prépare un entraînement corrigé sur ces chapitres seulement.</p>
      <div class="grid">${subs.map((x) => `<a class="subj" href="#devoir/${x.id}" style="text-decoration:none;color:inherit"><b>${esc(x.name)}</b><span class="small muted">${progs[x.id].length} chapitres</span></a>`).join("")}</div>`;
    return;
  }
  // les questions tirées des annales du BAC comptent aussi dans les chapitres de la matière
  const lv = subjectsOf(S.level).map((x) => x.id), extra = DATA.questions.filter((q) => q.alt === s.id && lv.includes(q.s)).map((q) => ({ ...q, ch: q.ach }));
  const chs = progs[s.id], all = [...qsOf(s.id), ...extra], nots = ((DATA.notions || {})[s.id] || []);
  const count = (i) => all.filter((q) => q.ch === i).length;
  const saved = (S.devoir || {})[s.id] || [];
  $view.innerHTML = `<p class="tag-src">Préparer un devoir · ${esc(S.level)}</p><h1>${esc(s.name)}</h1>
    <p class="muted">Coche les chapitres de ton devoir. Tu peux en choisir un seul ou plusieurs.${(GEN[s.id] || []).length ? " « + ∞ » : des exercices nouveaux sont fabriqués à chaque fois sur ce chapitre." : ""}</p>
    <div class="card"><label class="row small"><span><input type="checkbox" id="all"> <b>Tout le programme</b></span></label>
      ${chs.map((t, i) => `<label class="row chk"><span><input type="checkbox" class="ch" value="${i}"${saved.includes(i) ? " checked" : ""}> ${i + 1}. ${esc(t)}</span><span class="small muted">${count(i)} q.${(GEN[s.id] || []).some(([c]) => c === t) ? " + ∞" : ""}</span></label>`).join("")}</div>
    <div class="card"><h2>Nombre de questions</h2><div class="row">${[10, 20, 30].map((n) => `<button class="btn alt small nb${n === 20 ? " on" : ""}" data-n="${n}" style="flex:1">${n}</button>`).join("")}</div></div>
    <div id="revoir"></div>
    <p id="dmsg" class="small msg-ko"></p>
    <button class="btn hi-btn" id="go">Commencer l'entraînement</button>`;
  let n = 20;
  const boxes = [...$view.querySelectorAll(".ch")], picked = () => boxes.filter((b) => b.checked).map((b) => +b.value);
  function refresh() {
    const sel = picked();
    document.getElementById("all").checked = sel.length === chs.length;
    S.devoir = { ...(S.devoir || {}), [s.id]: sel }; store.save();
    const rel = nots.filter((c) => sel.includes(c.pch));
    document.getElementById("revoir").innerHTML = rel.length ? `<div class="card"><h2>📖 À revoir avant</h2>${rel.map((c) => `<a class="row lib" href="#notion/${c.id}"><span>${esc(c.title)}</span><span class="small muted">cours + exercice${isPremium() || c.free ? "" : " 🔒"}</span></a>`).join("")}</div>` : "";
  }
  boxes.forEach((b) => b.onchange = refresh);
  document.getElementById("all").onchange = (e) => { boxes.forEach((b) => b.checked = e.target.checked); refresh(); };
  $view.querySelectorAll(".nb").forEach((b) => b.onclick = () => { n = +b.dataset.n; $view.querySelectorAll(".nb").forEach((x) => x.classList.toggle("on", x === b)); });
  refresh();
  document.getElementById("go").onclick = () => {
    const sel = picked(), pool = all.filter((q) => sel.includes(q.ch) && open(q));
    const m = document.getElementById("dmsg");
    if (!sel.length) { m.textContent = "Coche au moins un chapitre."; return; }
    if (!pool.length && !(isPremium() && (GEN[s.id] || []).some(([c]) => sel.map((i) => chs[i]).includes(c)))) { m.textContent = isPremium() ? "Pas encore de questions sur ces chapitres. Choisis-en d'autres." : "Ces chapitres sont dans le pack premium."; return; }
    const qs = mixQuestions(s.id, pool, n, sel.map((i) => chs[i]));
    const title = `Devoir de ${s.name}`, sub = `${qs.length} questions sur : ${sel.map((i) => chs[i]).join(", ")}.`;
    chooseMode(title, sub, (solo) => { markDone("qcm"); runQuiz(title, qs, `#devoir/${s.id}`, { solo }); });
  };
}
function viewAnnales() {
  const list = annalesOf(S.level);
  $view.innerHTML = `${examOf() ? `<h1>Sujets du ${esc(examOf()[0])}</h1>
    <p class="muted">Des sujets complets du ${esc(examOf()[0])}, avec la structure, le barème et les notions des épreuves officielles. Tu les traites étape par étape et chaque réponse est corrigée.</p>` : `<h1>Devoirs et compositions</h1>
    <p class="muted">Ta classe n'a pas d'examen national : voici des devoirs types de ${esc(S.level)} pour t'entraîner, corrigés étape par étape.</p>`}
    ${list.length ? list.map((a) => `<div class="card">
      <div class="row"><h2>${a.modele ? `Sujet ${esc(a.exam)} ${esc(a.year)}` : `${esc(a.exam)} ${a.year}`}</h2><span class="tag">${esc(a.subject)}</span></div>
      ${a.modele ? `<p class="small muted">Sur le modèle de l'épreuve officielle</p>` : ""}<p class="small muted">${a.series ? "Séries " + esc(a.series) : esc(a.levels.join(", "))}${a.duration ? " · " + esc(a.duration) : ""}${a.coef ? " · coefficient " + a.coef : ""}</p>
      ${a.parts ? `<ul class="steps small">${a.parts.map((p) => `<li>${esc(p)}</li>`).join("")}</ul>` : ""}
      ${a.guided ? `<a class="btn hi-btn" href="#sujet/${a.id}">Faire ce sujet en mode guidé, corrigé à chaque étape${isPremium() ? "" : " 🔒"}</a>` : ""}</div>`).join("")
    : ""}
    ${genSujetsOf(S.level).length ? `<h2>${examOf() ? "Sujets types" : "Devoirs types"} à nombres nouveaux</h2><p class="small muted">4 exercices de chapitres différents, notés sur 20. Un sujet différent à chaque essai.</p>
      ${genSujetsOf(S.level).map((g) => `<a class="card lib-card" href="#sujet/${g.id}"><b>${esc(g.subject)} : nouveau sujet</b><span class="small muted">${examOf() ? `Sur le modèle du ${esc(examOf()[0])}` : "Devoir de 2 h"} · noté sur 20${isPremium() ? "" : " 🔒"}</span></a>`).join("")}` : ""}
    ${list.length || genSujetsOf(S.level).length ? "" : `<div class="card"><p>Pas encore d'annales pour ta série. Elles arrivent au fur et à mesure.</p></div>`}`;
}

// ---------- Exercices corrigés : sujets guidés et exercices pas à pas de la classe
function viewExercices() {
  const ann = annalesOf(S.level).filter((a) => a.guided), exs = exercisesOf(S.level);
  const card = (href, title, sub, lock) => `<a class="card lib-card" href="${href}"><b>${esc(title)}</b><span class="small muted">${esc(sub)}${lock ? " 🔒" : ""}</span></a>`;
  $view.innerHTML = `<h1>Exercices corrigés</h1><p class="muted">Tu réponds étape par étape ; après chaque réponse, le corrigé s'affiche avec les points gagnés.</p>
    ${ann.length ? `<h2>Sujets complets du ${esc(examOf() ? examOf()[0] : "BAC")}</h2>${ann.map((a) => card(`#sujet/${a.id}`, `${a.exam} ${a.year} · ${a.subject}`, `${a.series ? `Séries ${a.series} · ` : ""}${a.modele ? "sur le modèle officiel · " : ""}sujet entier noté sur 20`, !isPremium())).join("")}` : ""}
    ${exs.length ? `<h2>Exercices</h2>${exs.map((e) => card(`#sujet/${e.id}`, `${e.subject} · ${e.title}`, `${e.src} · ${e.guided.reduce((n, p) => n + p.steps.length, 0)} étapes${e.free ? " · gratuit" : ""}`, !isPremium() && !e.free)).join("")}` : ""}
    ${genExosOf(S.level).length ? `<h2>Exercices à nombres nouveaux</h2><p class="small muted">Les nombres changent à chaque essai : refais-les autant que tu veux.</p>${genExosOf(S.level).map((e) => card(`#sujet/${e.id}`, `${e.subject} · ${e.title}`, "Énoncé suivi · noté sur 5 · ∞", !isPremium())).join("")}` : ""}
    ${ann.length + exs.length + genExosOf(S.level).length ? "" : `<div class="card"><p>Les exercices corrigés de ta classe arrivent. En attendant, fais les QCM corrigés.</p><a class="btn" href="#qcm-list">QCM corrigés</a></div>`}`;
}
function viewQcmList() {
  $view.innerHTML = `<h1>QCM corrigés</h1><p class="muted">Pour chaque question, tu vois si ton choix est juste, la bonne réponse et l'explication. Les erreurs sont gardées pour les revoir.</p>
    <div class="grid">${subjectsOf(S.level).map((s) => `<a class="subj" href="#quiz/${s.id}" style="text-decoration:none;color:inherit"><b>${esc(s.name)}</b>
      <span class="small muted">${isPremium() ? s.count : s.free} questions${isPremium() && (GEN[s.id] || []).length ? " + ∞" : ""}</span><span class="bar"><i style="width:${mastery(s.id)}%"></i></span></a>`).join("")}</div>
    <h2>🎯 Par thème, pour préparer un devoir</h2><p class="small muted">Choisis la matière, puis le chapitre de ton devoir.</p>
    <div class="row onglets">${subjectsOf(S.level).filter((s) => ((DATA.programmes || {})[s.id] || []).length).map((s) => `<a class="btn alt small" href="#quiz/${s.id}/themes">${esc(s.name)}</a>`).join("")}</div>
    <a class="btn alt" href="#erreurs">Revoir mes erreurs</a>`;
}

// ---------- Session de groupe : de 2 à 10 camarades de la même classe reçoivent les mêmes questions dans le même ordre
const DUO_LEN = 10;
function seeded(str) { let h = 1779033703; for (const c of str) h = Math.imul(h ^ c.charCodeAt(0), 3432918353), (h = (h << 13) | (h >>> 19)); return () => { h = Math.imul(h ^ (h >>> 16), 2246822507); h = Math.imul(h ^ (h >>> 13), 3266489909); return ((h ^= h >>> 16) >>> 0) / 4294967296; }; }
function duoQuestions(code, level) {
  const rnd = seeded(code + "|" + level), pool = DATA.questions.filter((q) => subjectsOf(level).some((s) => s.id === q.s));
  const a = pool.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a.slice(0, DUO_LEN);
}
const GROUP_MAX = 10;
const myName = () => (S.pseudo || (Compte.user && Compte.user.displayName) || "").split(" ")[0].slice(0, 30);
function groupBoard(code, rec) {
  const el = () => document.getElementById("board");
  if (!Compte.user) { if (el()) el().innerHTML = `<p class="small muted">Connecte-toi pour apparaître dans le classement du groupe.</p>`; return; }
  const off = (msg) => { if (el()) el().innerHTML = `<p class="small muted">${msg} Envoyez-vous vos notes sur WhatsApp.</p>`; };
  Compte.postScore(code, { ...rec, name: rec.name || "Élève" }).catch(() => off("Le classement en direct n'est pas disponible pour le moment."));
  const stop = Compte.listenScores(code, (rows) => {
    if (!el()) return stop();
    rows.sort((a, b) => b.note - a.note || (a.at && b.at ? a.at.toMillis() - b.at.toMillis() : 0));
    const top = rows.slice(0, GROUP_MAX);
    el().innerHTML = `${barChart(top.map((r, i) => [`${["🥇", "🥈", "🥉"][i] || i + 1 + "."} ${r.name}${r.me ? " (toi)" : ""}`, r.note * 5, pts(r.note) + "/20"]))}
      <p class="small muted">${rows.length} élève${rows.length > 1 ? "s ont" : " a"} fini. Le classement se met à jour tout seul quand les autres terminent.</p>`;
  }, () => off("Le classement en direct n'est pas disponible pour le moment."));
}
const duoLink = (code) => `${location.href.split("#")[0]}#duo/${code}~${encodeURIComponent(S.level)}`;
function viewDuo(arg) {
  if (arg) {
    const [code, lv] = decodeURIComponent(arg).split("~");
    if (lv && lv !== S.level && DATA.levels.includes(lv)) { S.level = lv; store.save(); }
    markDone("duo");
    return runQuiz(`Session de groupe · ${code}`, duoQuestions(code, S.level), "#duo", { duo: code });
  }
  $view.innerHTML = `<h1>Session de groupe</h1>
    <p class="muted">De 2 à ${GROUP_MAX} camarades de ${esc(S.level)} répondent aux mêmes ${DUO_LEN} questions, dans le même ordre, chacun sur son téléphone. À la fin, le classement du groupe s'affiche en direct, puis vous revoyez ensemble les corrections.</p>
    <div class="card"><h2>Ton prénom dans le classement</h2><input class="field" id="pseudo" maxlength="30" value="${esc(myName())}" placeholder="Ton prénom"></div>
    <div class="card"><h2>Créer une session</h2><p class="small muted">Tu reçois un code et un lien à envoyer au groupe WhatsApp de ta classe.</p><button class="btn" id="new">Créer une session</button><div id="made"></div></div>
    <div class="card"><h2>Rejoindre une session</h2><p class="small muted">Entre le code reçu. Vous devez être dans la même classe et la même série.</p>
      <input class="field" id="code" maxlength="5" placeholder="Code (ex. K7P2Q)" autocapitalize="characters"><button class="btn alt" id="join">Rejoindre</button></div>`;
  document.getElementById("pseudo").onchange = (e) => { S.pseudo = e.target.value.trim().slice(0, 30); store.save(); };
  document.getElementById("new").onclick = () => {
    const code = Array.from(crypto.getRandomValues(new Uint8Array(5)), (x) => "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"[x % 32]).join("");
    const text = `Session de groupe sur Révision (${S.level}) : on répond tous aux mêmes ${DUO_LEN} questions, classement en direct. Code ${code}. Ouvre ce lien : ${duoLink(code)}`;
    document.getElementById("made").innerHTML = `<p>Code de la session : <b class="count">${code}</b></p>
      <a class="btn alt" href="https://wa.me/?text=${encodeURIComponent(text)}" target="_blank" rel="noopener">Envoyer le lien au groupe sur WhatsApp</a>
      <a class="btn" href="#duo/${code}~${encodeURIComponent(S.level)}">Commencer la session</a>`;
  };
  document.getElementById("join").onclick = () => {
    const code = document.getElementById("code").value.trim().toUpperCase();
    if (code.length >= 4) go(`duo/${code}~${encodeURIComponent(S.level)}`);
  };
}

// ---------- Challenge du jour : 20 questions qui mélangent tout le programme, résultats en graphique
const CHAL_LEN = 20;
function challengeQuestions(level, day) {
  const rnd = seeded("challenge|" + level + "|" + day), subs = subjectsOf(level);
  const pools = subs.map((s) => { const a = qsOf(s.id); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; });
  const out = []; for (let r = 0; out.length < CHAL_LEN && r < 50; r++) pools.forEach((p) => { if (p[r] && out.length < CHAL_LEN) out.push(p[r]); });
  return out;
}
function barChart(rows) {
  return `<div class="chart">${rows.map(([label, val, sub]) => `<div class="crow"><span class="clab">${esc(label)}</span>
    <span class="ctrack"><i style="width:${Math.max(2, val)}%;background:${val >= 70 ? "var(--ok)" : val >= 50 ? "var(--hi)" : "var(--ko)"}"></i></span><b>${sub}</b></div>`).join("")}</div>`;
}
function viewChallenge() {
  const day = today(), qs = challengeQuestions(S.level, day), prev = (S.challenges || {})[day];
  const hist = Object.entries(S.challenges || {}).sort().slice(-10);
  $view.innerHTML = `<h1>Challenge du jour</h1>
    <p class="muted">${CHAL_LEN} questions qui mélangent toutes les matières de ${esc(S.level)}. Toute ta classe a le même challenge aujourd'hui : compare ta note avec tes camarades.</p>
    ${prev ? `<div class="card"><p>Déjà fait aujourd'hui : <b>${pts(prev.note)} / 20</b>. Tu peux le refaire pour t'entraîner, ta première note reste enregistrée.</p></div>` : ""}
    <button class="btn hi-btn" id="go">Lancer le challenge</button>
    ${hist.length ? `<div class="card"><h2>Mes derniers challenges</h2>${barChart(hist.map(([d, c]) => [d.slice(5).split("-").reverse().join("/"), c.note * 5, pts(c.note) + "/20"]))}</div>` : ""}`;
  document.getElementById("go").onclick = () => runQuiz(`Challenge du ${day.slice(5).split("-").reverse().join("/")}`, qs, "#challenge", { solo: true, onEnd: (score, total, answers) => {
    const by = {}; answers.forEach((a) => { const b = (by[a.q.s] = by[a.q.s] || { ok: 0, n: 0 }); b.n++; b.ok += a.ok; });
    const note = Math.round((20 * score) / total * 10) / 10;
    if (!prev) { S.challenges = S.challenges || {}; S.challenges[day] = { note, by }; store.save(); }
    markDone("challenge");
    const weak = Object.entries(by).sort((a, b) => a[1].ok / a[1].n - b[1].ok / b[1].n)[0];
    const text = `Challenge du jour Révision (${S.level}) : j'ai eu ${note}/20. Fais mieux ! ${location.href.split("#")[0]}`;
    return `<div class="card"><h2>Tes résultats par matière</h2>${barChart(Object.entries(by).map(([sid, b]) => [subjName(sid), Math.round((100 * b.ok) / b.n), `${b.ok}/${b.n}`]))}
      ${weak ? `<p class="small">À travailler en priorité : <b>${esc(subjName(weak[0]))}</b>.</p><a class="btn alt" href="#fiche/${weak[0]}">Revoir la synthèse</a>` : ""}</div>
      <a class="btn hi-btn" href="https://wa.me/?text=${encodeURIComponent(text)}" target="_blank" rel="noopener">Défier mes camarades sur WhatsApp</a>`;
  } });
}

// ---------- Sujet guidé : un vrai sujet, étape par étape, corrigé tout de suite
const pts = (x) => String(Math.round(x * 100) / 100).replace(".", ",");
function viewGuided(id) {
  const gid = String(id), cut = gid.lastIndexOf("-");
  const an = [...(DATA.annales || []), ...(DATA.exercises || [])].find((x) => x.id === id && x.guided)
    || (typeof genExercise === "function" && gid.startsWith("gx-") ? genExercise(gid.slice(3, cut), +gid.slice(cut + 1)) : null)
    || (typeof genSujet === "function" && gid.startsWith("gs-") ? genSujet(gid.slice(3)) : null);
  if (!an) return go("exercices");
  if (!isPremium() && !an.free) return viewPremium("Les sujets guidés et les exercices corrigés font partie du pack premium.");
  const head = an.title ? `${an.subject} · ${an.title}` : `${an.exam} ${an.year} · ${an.subject}`;
  const steps = an.guided.flatMap((p, pi) => p.steps.map((st) => ({ ...st, pi })));
  const max = steps.reduce((n, st) => n + st.pts, 0);
  let k = -1, got = 0, solo = false;
  const byPart = an.guided.map(() => 0), picks = [];
  function intro() {
    $view.innerHTML = `<div class="card"><p class="tag-src">${an.title ? "Exercice corrigé" : "Sujet guidé"}</p><h1>${esc(head)}</h1>
      ${an.src ? `<p class="src">📄 ${esc(an.src)}</p>` : `<p class="muted">${an.modele ? "Sur le modèle de l'épreuve officielle · " : ""}${an.series ? "Séries " + esc(an.series) : esc(an.levels.join(", "))}${an.duration ? " · " + esc(an.duration) : ""}${an.coef ? " · coefficient " + an.coef : ""}</p>`}
      <p>Tu réponds étape par étape. Choisis si tu veux le corrigé après chaque réponse ou seulement à la fin.</p>
      <p class="small muted">${steps.length} étapes, ${pts(max)} points.${an.gen ? " Les nombres changent à chaque essai : tu peux le refaire autant de fois que tu veux." : an.title ? "" : " Les tableaux et les tracés de courbes ne sont pas notés ici."}</p>
      <button class="btn" id="go">🧑‍🏫 Avec support<br><span class="small">Corrigé et points après chaque réponse</span></button>
      <button class="btn alt" id="solo">💪 Tout seul<br><span class="small">Tu fais tout l'exercice, corrigé ligne par ligne à la fin</span></button></div>`;
    document.getElementById("go").onclick = () => { solo = false; k = 0; markDone(an.title ? "exo" : "sujet"); step(); };
    document.getElementById("solo").onclick = () => { solo = true; k = 0; markDone(an.title ? "exo" : "sujet"); step(); };
  }
  function step() {
    const st = steps[k], part = an.guided[st.pi];
    $view.innerHTML = `<div class="progress"><span>${esc(an.title || an.exam + " " + an.year)} · étape ${k + 1} / ${steps.length}</span><span>${solo ? "💪 Tout seul" : `<b>${pts(got)}</b> / ${pts(max)} pts`}</span></div>
      <div class="bar"><i style="width:${(100 * k) / steps.length}%"></i></div>
      <div class="card"><h2>${esc(part.title)}</h2><p class="small">${esc(part.context)}</p></div>
      <div class="card" id="qc"><p class="tag-src">${pts(st.pts)} point${st.pts > 1 ? "s" : ""}</p>${questionBlock(st)}</div>
      <button class="btn" id="next" hidden>${k + 1 < steps.length ? "Étape suivante" : "Voir ma note"}</button>`;
    const qc = document.getElementById("qc");
    qc.querySelectorAll(".choice").forEach((b) => b.onclick = () => {
      const ok = +b.dataset.i === st.a;
      picks[k] = +b.dataset.i;
      if (ok) { got += st.pts; byPart[st.pi] += st.pts; }
      if (solo) return k + 1 < steps.length ? (k++, step()) : finish();
      qc.querySelectorAll(".choice").forEach((x) => { x.disabled = true; if (+x.dataset.i === st.a) x.classList.add("ok"); });
      if (!ok) b.classList.add("ko");
      const ex = qc.querySelector(".expl");
      ex.innerHTML = ok ? `<b class="msg-ok">Juste : +${pts(st.pts)} pt</b><br><b>Corrigé :</b> ${esc(st.e)}`
        : `<b class="msg-ko">Faux : 0 pt</b><br>Tu as répondu : <s>${esc(st.c[+b.dataset.i])}</s><br>La bonne réponse est <b>${LETTERS[st.a]} : ${esc(st.c[st.a])}</b><p><b>Corrigé :</b> ${esc(st.e)}</p>`;
      ex.hidden = false;
      document.getElementById("next").hidden = false;
      if (!S.days.includes(today())) { S.days.push(today()); store.save(); }
    });
    document.getElementById("next").onclick = () => (k + 1 < steps.length ? (k++, step()) : finish());
    window.scrollTo(0, 0);
  }
  function finish() {
    const note = Math.round((20 * got) / max * 10) / 10;
    S.sessions.push({ t: an.title ? `Exercice : ${an.title}` : `Sujet guidé ${an.exam} ${an.year}`, score: got, total: max, d: today() }); store.save();
    $view.innerHTML = `<div class="card" style="text-align:center"><p class="muted">${esc(head)}</p>
      <p class="score">${pts(note)} / 20</p><p>${pts(got)} points sur ${pts(max)} notés</p></div>
      <div class="card">${an.guided.map((p, i) => `<div class="row small"><span>${esc(p.title)}</span><b>${pts(byPart[i])} / ${pts(p.steps.reduce((n, x) => n + x.pts, 0))}</b></div>`).join("")}</div>
      <div class="btns">
      <button class="btn" id="again">${an.gen ? "Nouveaux nombres" : "Recommencer"}</button>${an.chapter ? `<a class="btn alt" href="#notion/${an.chapter}">Revoir le cours</a>` : ""}<a class="btn alt" href="#exercices">Autres exercices</a></div>
      ${solo ? `<h2>Corrigé ligne par ligne</h2>${steps.map((st, i) => { const ok = picks[i] === st.a;
        return `<div class="card"><p class="small muted">${esc(an.guided[st.pi].title)} · ${pts(st.pts)} pt</p><p><b>${esc(st.q)}</b></p>
          <p class="${ok ? "msg-ok" : "msg-ko"}">${ok ? "✓ Juste" : "✗ Ta réponse : " + esc(st.c[picks[i]])} · Bonne réponse : ${esc(st.c[st.a])}</p><p class="small">${esc(st.e)}</p></div>`; }).join("")}` : ""}`;
    document.getElementById("again").onclick = () => (an.gen ? viewGuided(id) : (got = 0, byPart.fill(0), picks.length = 0, intro()));
    window.scrollTo(0, 0);
  }
  intro();
}

// ---------- Progrès
function daysChart() {
  const days = [...Array(10)].map((_, i) => { const d = new Date(); d.setDate(d.getDate() - 9 + i); return d.toISOString().slice(0, 10); });
  const data = days.map((d) => (S.daily || {})[d] || { n: 0, ok: 0 }), top = Math.max(10, ...data.map((x) => x.n));
  return `<div class="days">${days.map((d, i) => `<div class="day"><span class="dbar"><i style="height:${(100 * data[i].n) / top}%"></i><i class="okp" style="height:${(100 * data[i].ok) / top}%"></i></span>
    <span class="small muted">${d.slice(8)}</span><span class="small"><b>${data[i].n || ""}</b></span></div>`).join("")}</div>
    <p class="small muted">Barre claire : questions répondues ; barre verte : bonnes réponses.</p>`;
}
function viewProgress() {
  const answered = Object.values(S.stats).reduce((n, s) => n + s.ok + s.ko, 0);
  const good = Object.values(S.stats).reduce((n, s) => n + s.ok, 0);
  const rows = subjectsOf(S.level).map((s) => `<div><div class="row small"><span>${esc(s.name)}</span><b>${mastery(s.id)} %</b></div><div class="bar"><i style="width:${mastery(s.id)}%"></i></div></div>`).join("");
  const last = S.sessions.slice(-8).reverse().map((x) => `<div class="row small"><span>${esc(x.t)}<br><span class="muted">${x.d}</span></span><b>${Math.round((200 * x.score) / x.total) / 10} / 20</b></div>`).join("");
  $view.innerHTML = `<h1>Mes progrès</h1>
    <div class="card"><div class="row"><div><p class="small muted">Réponses</p><p class="count">${answered}</p></div>
      <div><p class="small muted">Réussite</p><p class="count">${answered ? Math.round((100 * good) / answered) : 0} %</p></div>
      <div><p class="small muted">Série</p><p class="count">${streak()} 🔥</p></div></div></div>
    <div class="card"><h2>Mes 10 derniers jours</h2>${daysChart()}</div>
    <div class="card"><h2>Matières maîtrisées en ${S.level}</h2>${rows}<p class="small muted">Part des questions réussies la dernière fois.</p></div>
    <div class="card"><h2>Derniers quiz</h2>${last || '<p class="muted">Pas encore de quiz.</p>'}</div>
    ${Compte.user ? `<div class="card"><p class="small muted">Connecté avec ${esc(Compte.user.email || Compte.user.displayName || "Google")}</p><button class="btn alt" id="logout">Se déconnecter</button></div>` : ""}`;
  const lo = document.getElementById("logout");
  if (lo) lo.onclick = () => Compte.signOut().then(() => { localStorage.removeItem("rev"); location.reload(); });
}

// ---------- Premium : paiement Wave puis code reçu par WhatsApp
async function sha256(s) {
  const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(b)].map((x) => x.toString(16).padStart(2, "0")).join("");
}
function viewPremium(reason = "", pay = "wave") {
  const total = DATA.questions.length, wa = CFG.whatsapp, wave = CFG.wave_number, om = CFG.om_number;
  if (!wave) pay = "om";
  // numéro du compte, affiché « 77 123 45 67 » : c'est avec lui que l'élève doit payer
  const tel = (S.phone || "").replace(/^(\d{2})(\d{3})(\d{2})(\d{2})$/, "$1 $2 $3 $4"), dest = pay === "om" ? om : wave;
  const enLigne = Compte.enabled && !!Compte.user;
  const msg = encodeURIComponent(`Bonjour, j'ai payé ${fcfa(CFG.price_fcfa)} par ${pay === "om" ? "Orange Money" : "Wave"} pour le pack premium Révision BAC BFEM${S.phone ? ` depuis le ${tel}` : ""}. Voici ma capture :`);
  $view.innerHTML = `<h1>Pack premium</h1>
    ${reason ? `<p><b>${esc(reason)}</b></p>` : ""}
    ${!S.premium ? `<div class="card"><p>${trialLeft() > 0 ? `🎁 Ton essai gratuit de ${TRIAL_DAYS} jours est en cours : encore <b>${trialLeft()} jour${trialLeft() > 1 ? "s" : ""}</b> avec tout débloqué.` : `Ton essai gratuit de ${TRIAL_DAYS} jours est terminé.`}</p></div>` : ""}
    ${S.premium ? `<div class="card"><p class="msg-ok">Ton pack premium est actif. Toutes les questions et les examens blancs sont débloqués.</p><a class="btn" href="#accueil">Réviser</a></div>` : `
    <div class="card">
      <p class="count">${fcfa(CFG.price_fcfa)}</p><p class="muted">Payé une seule fois, valable jusqu'à l'examen.</p>
      <ul class="steps"><li>Les <b>${total}</b> questions de la 6e à la Terminale, toutes corrigées</li><li>Les examens et devoirs blancs chronométrés, notés sur 20</li><li>Les nouvelles questions ajoutées pendant l'année</li></ul>
    </div>
    <div class="card"><h2>Comment payer</h2>
      ${wave || om ? `<p class="small muted">Choisis ton moyen de paiement :</p>
        <div class="row">${wave ? `<button class="btn${pay === "wave" ? "" : " alt"}" style="flex:1" data-pay="wave">Wave</button>` : ""}${om ? `<button class="btn${pay === "om" ? "" : " alt"}" style="flex:1" data-pay="om">Orange Money</button>` : ""}</div>
        ${tel ? `<div class="card" style="border:2px solid #f5a623;margin:8px 0"><p>⚠️ Paie <b>obligatoirement avec le numéro de ton compte : ${esc(tel)}</b>.</p><p class="small muted">C'est avec ce numéro qu'on retrouve ton paiement. Un paiement fait depuis un autre numéro ne pourra pas être reconnu.</p></div>` : ""}
        <ol class="steps">
        <li>${pay === "om" ? `Envoie <b>${fcfa(CFG.price_fcfa)}</b> par Orange Money au <b>${esc(om)}</b> (code #144# ou appli Orange Money).` : `Envoie <b>${fcfa(CFG.price_fcfa)}</b> par Wave au <b>${esc(wave)}</b>.`}${tel ? ` Depuis ton numéro <b>${esc(tel)}</b>.` : ""}
        <div class="row" style="margin-top:8px">${pay === "om" ? `<a class="btn" style="flex:1" href="tel:%23144%23">📞 Ouvrir Orange Money (#144#)</a>` : ""}<button class="btn alt" style="flex:1" id="cpnum">📋 Copier le numéro ${esc(dest)}</button></div></li>
        ${enLigne ? `<li>Fais une <b>capture d'écran</b> du paiement réussi.</li>
        <li>Envoie-la ici. Dès que le paiement est vérifié, ton appli se débloque toute seule, là où tu en étais.</li></ol>
        <div id="paybox"></div>` : `<li>Envoie la capture du paiement sur WhatsApp.</li>
        <li>Tu reçois ton code. Entre-le ci-dessous.</li></ol>
        ${wa ? `<a class="btn hi-btn" href="https://wa.me/${esc(wa)}?text=${msg}" target="_blank" rel="noopener">Envoyer la capture sur WhatsApp</a>` : ""}`}`
      : `<p class="muted">Le paiement arrive très bientôt. Si tu as déjà un code, entre-le ci-dessous.</p>`}
    </div>
    <div class="card"><h2>${enLigne ? "Tu as reçu un code ?" : "J'ai un code"}</h2>
      <input class="code" id="code" placeholder="XXXXX-XXXXXX" autocomplete="off" maxlength="12">
      <button class="btn" id="unlock">Débloquer</button><p id="codemsg" class="small"></p></div>`}`;
  $view.querySelectorAll("[data-pay]").forEach((b) => b.onclick = () => viewPremium(reason, b.dataset.pay));
  if (enLigne && document.getElementById("paybox")) payBox(pay);
  const cp = document.getElementById("cpnum");
  if (cp) cp.onclick = () => navigator.clipboard?.writeText(dest.replace(/\s/g, "")).then(() => { cp.textContent = "Numéro copié ✓ : colle-le dans " + (pay === "om" ? "Orange Money" : "Wave"); }).catch(() => {});
  const btn = document.getElementById("unlock");
  if (btn) btn.onclick = async () => {
    const raw = document.getElementById("code").value.trim().toUpperCase().replace(/\s/g, "");
    const code = raw.length === 11 && !raw.includes("-") ? raw.slice(0, 5) + "-" + raw.slice(5) : raw;
    const m = document.getElementById("codemsg");
    let ok = CFG.codes.includes(await sha256(CFG.salt + code));
    // avec les comptes, c'est le serveur qui valide le code et refuse un code déjà utilisé
    if (ok && Compte.enabled) ok = await Compte.claim(code).then(() => true, () => false);
    if (ok) { S.premium = true; S.code = code; store.save(); m.className = "msg-ok"; m.textContent = "Code accepté !"; setTimeout(render, 700); }
    else { m.className = "msg-ko"; m.textContent = "Code inconnu ou déjà utilisé. Vérifie les lettres et les chiffres."; }
  };
}

// Capture du paiement : réduite sur le téléphone (JPEG, 1 000 px au plus) pour tenir dans Firestore gratuitement
function reduireCapture(file) {
  return new Promise((ok, ko) => {
    const img = new Image(), url = URL.createObjectURL(file);
    img.onload = () => {
      URL.revokeObjectURL(url);
      let side = 1000, q = 0.7, out = "";
      for (let k = 0; k < 6; k++) {
        const r = Math.min(1, side / Math.max(img.width, img.height)), c = document.createElement("canvas");
        c.width = Math.round(img.width * r); c.height = Math.round(img.height * r);
        c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
        out = c.toDataURL("image/jpeg", q);
        if (out.length <= 440000) return ok(out);
        side *= 0.8; q = Math.max(0.4, q - 0.1);
      }
      ko(new Error("image trop lourde"));
    };
    img.onerror = () => ko(new Error("image illisible"));
    img.src = url;
  });
}
// Encadré « J'ai payé » : envoi de la capture, puis état du paiement suivi en direct
// notification possible ici et pas encore activée pour ce téléphone
const peutNotifier = () => !!(CFG && CFG.vapid) && "Notification" in window && "serviceWorker" in navigator && Notification.permission !== "denied" && !(Notification.permission === "granted" && S.pushOn);
async function payBox(via) {
  const box = document.getElementById("paybox");
  if (!box) return;
  const p = await Compte.myPay();
  if (!document.body.contains(box)) return;
  const quand = (d) => d ? d.toLocaleString("fr-FR", { day: "numeric", month: "long", hour: "2-digit", minute: "2-digit" }) : "à l'instant";
  if (p && p.statut === "attente") {
    box.innerHTML = `<div class="card" style="border:2px solid var(--hi,#f5a623)"><p>⏳ <b>Capture reçue</b> ${esc(quand(p.at))}. Ton paiement est en cours de vérification.</p>
      <p class="small muted">Tu n'as rien d'autre à faire. Garde l'appli ouverte ou reviens plus tard : elle se débloque toute seule dès la validation.</p>
      ${peutNotifier() ? `<button class="btn small" id="paynotif">🔔 Me prévenir par notification dès la validation</button><p class="small" id="paynmsg"></p>` : ""}
      <button class="btn alt small" id="payredo">Renvoyer une autre capture</button></div>`;
    document.getElementById("payredo").onclick = () => formulaire(true);
    const bn = document.getElementById("paynotif");
    if (bn) bn.onclick = async () => {
      const m = document.getElementById("paynmsg");
      try {
        if ((await Notification.requestPermission()) !== "granted") { m.className = "small msg-ko"; m.textContent = "Notifications refusées : l'appli se débloquera quand même à ta prochaine visite."; return; }
        await Compte.enablePush(CFG.vapid);
        S.pushOn = true; store.save(); bn.remove(); m.className = "small msg-ok"; m.textContent = "C'est noté : tu recevras une notification dès que ton paiement est validé. 👍";
      } catch (err) { m.className = "small msg-ko"; m.textContent = "Notifications impossibles sur ce téléphone : l'appli se débloquera quand même à ta prochaine visite."; }
    };
    return;
  }
  formulaire(false, p && p.statut === "refuse" ? p.motif || "La capture n'a pas permis de retrouver le paiement." : "");
  function formulaire(redo, refus) {
    box.innerHTML = `${refus ? `<p class="msg-ko">❌ Paiement non validé : ${esc(refus)} Renvoie une capture lisible du paiement.</p>` : ""}
      <label class="btn hi-btn" style="display:block;text-align:center">📷 ${redo ? "Choisir une nouvelle capture" : "J'ai payé : joindre la capture"}<input type="file" id="payimg" accept="image/*" hidden></label>
      <div id="payprev"></div><p id="paymsg" class="small"></p>`;
    document.getElementById("payimg").onchange = async (e) => {
      const f = e.target.files[0], m = document.getElementById("paymsg");
      if (!f) return;
      m.className = "small muted"; m.textContent = "Préparation de la capture…";
      let img;
      try { img = await reduireCapture(f); } catch (err) { m.className = "msg-ko"; m.textContent = "Cette image ne peut pas être lue. Essaie une autre capture."; return; }
      document.getElementById("payprev").innerHTML = `<img src="${img}" alt="Capture du paiement" style="max-width:100%;max-height:320px;border-radius:8px;margin:8px 0"><button class="btn" id="paysend" style="width:100%">Envoyer la capture</button>`;
      m.textContent = "";
      document.getElementById("paysend").onclick = async (ev) => {
        ev.target.disabled = true; ev.target.textContent = "Envoi…";
        try {
          await Compte.declarePay({ name: (Compte.user.displayName || "").slice(0, 60), phone: (S.phone || "").slice(0, 20), level: (S.level || "").slice(0, 30), via: via === "om" ? "om" : "wave", img });
          payBox(via);
        } catch (err) { ev.target.disabled = false; ev.target.textContent = "Envoyer la capture"; m.className = "msg-ko"; m.textContent = "L'envoi n'a pas abouti. Vérifie ta connexion et réessaie."; }
      };
    };
  }
}
// Dès que l'admin valide le paiement, l'appli se débloque là où l'élève se trouve, sans redémarrer
let stopWatch = null;
function suivrePremium() {
  if (Compte.enabled && Compte.user && Compte.isAdmin() && !stopWatch) {
    // l'admin voit en direct les paiements à vérifier, sur toutes les pages
    stopWatch = Compte.watchPays((n) => {
      let b = document.getElementById("paybadge");
      if (!n) { if (b) b.remove(); return; }
      if (!b) { b = document.createElement("a"); b.id = "paybadge"; b.href = "#admin"; b.style.cssText = "position:fixed;right:12px;bottom:80px;z-index:98;background:#f5a623;color:#000;padding:10px 14px;border-radius:24px;font-weight:bold;box-shadow:0 4px 16px rgba(0,0,0,.3);text-decoration:none"; document.body.appendChild(b); }
      b.textContent = `💰 ${n} paiement${n > 1 ? "s" : ""} à valider`;
      b.hidden = location.hash.startsWith("#admin");
    });
    // sur l'espace admin, l'onglet Paiements suffit : la pastille ne doit pas cacher les boutons
    window.addEventListener("hashchange", () => { const b = document.getElementById("paybadge"); if (b) b.hidden = location.hash.startsWith("#admin"); });
    return;
  }
  if (stopWatch || !Compte.enabled || !Compte.user || S.premium) return;
  stopWatch = Compte.watchPremium((premium, pay) => {
    if (premium && !S.premium) {
      S.premium = true; S.premiumVu = true; store.save();
      stopWatch(); stopWatch = null;
      render();
      bravoPremium();
    } else if (pay && document.getElementById("paybox")) payBox(pay.via);
  });
}
function bravoPremium() {
  const d = document.createElement("div");
  d.setAttribute("role", "status");
  d.style.cssText = "position:fixed;left:12px;right:12px;bottom:80px;z-index:99;background:#1f9d55;color:#fff;padding:16px;border-radius:12px;box-shadow:0 6px 24px rgba(0,0,0,.3);font-size:1.05em;text-align:center";
  d.innerHTML = "🎉 <b>Paiement validé : tu es premium !</b><br>Tout est débloqué. Continue là où tu étais.";
  d.onclick = () => d.remove();
  document.body.appendChild(d);
  setTimeout(() => d.remove(), 9000);
}

// Partage : sur Android, la vidéo de présentation part avec le lien (WhatsApp l'affiche directement) ;
// sinon, le lien seul, dont l'aperçu montre l'image de présentation.
async function share() {
  const url = location.href.split("#")[0].split("?")[0] + "?qr";
  const text = `Je révise le BAC et le BFEM avec cette appli : 1 300 QCM corrigés, sujets officiels, cours et devoirs. 10 jours gratuits 👉 ${url}`;
  try {
    const blob = await fetch("tuto.mp4").then((r) => r.blob());
    const files = [new File([blob], "revision-bac-bfem.mp4", { type: "video/mp4" })];
    if (navigator.canShare && navigator.canShare({ files })) return await navigator.share({ files, text, title: "Révision BAC BFEM" });
  } catch (e) { if (e && e.name === "AbortError") return; }
  if (navigator.share) navigator.share({ title: "Révision BAC BFEM", text, url }).catch(() => {});
  else window.open(`https://wa.me/?text=${encodeURIComponent(text)}`, "_blank");
}

// Partager : QR code à faire scanner en face, ou à envoyer en image avec le lien
function viewPartager() {
  const url = location.href.split("#")[0].split("?")[0] + "?qr";
  $view.innerHTML = `<h1>Partager l'appli</h1>
    <div class="card" style="text-align:center"><img src="icons/qr.png" alt="QR code de l'appli" style="width:100%;max-width:320px;background:#fff;padding:10px;border-radius:12px">
      <p class="small muted">En face : ton camarade vise ce code avec l'appareil photo de son téléphone. L'appli s'ouvre avec les étapes pour l'installer et créer son compte.</p></div>
    <button class="btn" id="sqr">Envoyer le QR code et le lien (WhatsApp…)</button>
    <button class="btn alt" id="slink">Envoyer seulement le lien</button>
    <div class="card small"><p>Le lien de l'appli :</p><p><b style="word-break:break-all">${esc(url)}</b></p><button class="btn alt small" id="cp">Copier le lien</button></div>
    <p class="small muted">Chaque camarade a ses 10 jours d'essai gratuit avec son propre compte.</p>`;
  const text = `Je révise le BAC et le BFEM avec cette appli : QCM corrigés, sujets du BAC, cours et devoirs. 10 jours gratuits. Ouvre le lien ou scanne le QR code 👉 ${url}`;
  document.getElementById("sqr").onclick = async () => {
    try {
      const blob = await fetch("icons/qr.png").then((r) => r.blob());
      const files = [new File([blob], "qr-revision.png", { type: "image/png" })];
      if (navigator.canShare && navigator.canShare({ files })) return await navigator.share({ files, text, title: "Révision BAC BFEM" });
    } catch (e) { if (e && e.name === "AbortError") return; }
    share();
  };
  document.getElementById("slink").onclick = share;
  document.getElementById("cp").onclick = (e) => navigator.clipboard?.writeText(url).then(() => { e.target.textContent = "Lien copié ✓"; }).catch(() => {});
}

// ---------- Navigation
function go(h) { location.hash = h; }
// carte d'installation (affichée avant la connexion, utile quand on arrive en scannant le QR code)
const installCard = () => standalone ? "" : `<div class="card small"><b>📲 Installe l'appli sur ton téléphone</b><br>${isIOS
  ? "Dans Safari, touche Partager (carré avec une flèche), puis « Sur l'écran d'accueil », puis « Ajouter »."
  : `Touche « Installer l'appli » s'il apparaît, sinon le menu ⋮ du navigateur puis « Installer l'application » (ou « Ajouter à l'écran d'accueil »).${deferred ? `<button class="btn" id="install2" style="margin-top:8px">Installer l'appli</button>` : ""}`}</div>`;
function viewLogin(err = "", ok = "") {
  $view.innerHTML = `${installCard()}<div class="card" style="gap:14px">
    <h1 style="text-align:center">Bienvenue sur Révision</h1>
    <p class="muted" style="text-align:center">Connecte-toi pour garder tes progrès et profiter de ${TRIAL_DAYS} jours d'essai gratuit avec tout débloqué.</p>
    <input class="field" id="tname" autocomplete="name" placeholder="Ton prénom et ton nom (nouveau compte)">
    <input class="field" id="tel" type="tel" inputmode="numeric" autocomplete="tel" placeholder="Ton numéro de téléphone (77 123 45 67)">
    <input class="field" id="tcode" type="password" inputmode="numeric" maxlength="6" autocomplete="current-password" placeholder="Code à 6 chiffres">
    <div class="row"><button class="btn" style="flex:1" id="tsignup">Créer mon compte</button><button class="btn alt" style="flex:1" id="tlogin">Me connecter</button></div>
    <p class="small muted" style="text-align:center">Première fois ? Choisis un code secret de <b>6 chiffres</b> pour l'appli. Ce n'est <b>pas</b> ton code Wave ou Orange Money : ne le donne jamais.</p>
    <details class="small"><summary>Ancien compte : Google ou e-mail</summary><div style="display:grid;gap:10px;margin-top:10px">
    <button class="btn alt" id="google">Se connecter avec Google</button>
    <input class="field" id="mail" type="email" autocomplete="email" placeholder="Adresse e-mail">
    <input class="field" id="pass" type="password" autocomplete="current-password" placeholder="Mot de passe (6 caractères minimum)">
    <div class="row"><button class="btn alt" style="flex:1" id="login">Se connecter</button><button class="btn alt" style="flex:1" id="signup">Créer un compte</button></div>
    <p class="small muted" style="text-align:center">Première fois ? Choisis un <b>nouveau</b> mot de passe pour l'appli (pas celui de ta boîte mail), puis touche « Créer un compte ».</p>
    <button class="linkbtn small" id="forgot">Mot de passe oublié ?</button></div></details>
    <p id="lmsg" class="${err ? "msg-ko" : "msg-ok"} small">${esc(err || ok)}</p></div>`;
  const done = (p) => { applyProfile(p); render(); suivrePremium(); };
  const mail = () => document.getElementById("mail").value.trim(), pass = () => document.getElementById("pass").value;
  // message d'erreur affiché sans effacer ce que l'élève a déjà tapé
  const fail = (e) => { const el = document.getElementById("lmsg"); el.className = "msg-ko small"; el.textContent = e && e.msg || ({
    "auth/invalid-email": "Adresse e-mail invalide.",
    "auth/missing-password": "Entre ton mot de passe.",
    "auth/weak-password": "Le mot de passe doit faire au moins 6 caractères.",
    "auth/email-already-in-use": "Ce compte existe déjà : appuie sur « Me connecter ».",
    "auth/invalid-credential": "Identifiants incorrects. Vérifie le numéro et le code (ou l'e-mail et le mot de passe).",
    "auth/wrong-password": "E-mail ou mot de passe incorrect.",
    "auth/user-not-found": "Aucun compte avec cet e-mail : appuie sur « Créer un compte ».",
    "auth/too-many-requests": "Trop d'essais. Attends quelques minutes.",
  })[e && e.code] || "La connexion n'a pas abouti. Réessaie."; };
  const i2 = document.getElementById("install2"); if (i2) i2.onclick = () => document.getElementById("install").click();
  // connexion par numéro : nom demandé seulement pour créer le compte
  const tel = (create) => {
    const t = Compte.normTel(document.getElementById("tel").value), c = document.getElementById("tcode").value.trim(), n = document.getElementById("tname").value.trim();
    if (!t) return fail({ msg: "Numéro invalide : écris les 9 chiffres, par exemple 77 123 45 67." });
    if (!/^\d{6}$/.test(c)) return fail({ msg: "Le code doit faire exactement 6 chiffres." });
    if (create && n.length < 2) return fail({ msg: "Écris ton prénom et ton nom pour créer ton compte." });
    Compte.signInTel(n.slice(0, 40), t, c, create).then(done).catch(fail);
  };
  document.getElementById("tsignup").onclick = () => tel(true);
  document.getElementById("tlogin").onclick = () => tel(false);
  document.getElementById("google").onclick = () => Compte.signIn().then(done).catch(fail);
  document.getElementById("login").onclick = () => Compte.signInEmail(mail(), pass(), false).then(done).catch(fail);
  document.getElementById("signup").onclick = () => Compte.signInEmail(mail(), pass(), true).then(done).catch(fail);
  document.getElementById("forgot").onclick = () => mail()
    ? Compte.resetPassword(mail()).then(() => viewLogin("", "Un e-mail pour changer ton mot de passe a été envoyé."), fail)
    : viewLogin("Écris d'abord ton adresse e-mail.");
}
// Ancien compte (Google ou e-mail) : on demande une fois le numéro et un code, sans rien perdre
function viewTel(err = "") {
  $view.innerHTML = `<div class="card" style="gap:14px">
    <h1>📱 Nouveau : connexion par numéro</h1>
    <p>Pour te connecter plus facilement, sur iPhone comme sur Android, ajoute ton numéro de téléphone et choisis un code de 6 chiffres. Tu gardes tous tes progrès${S.premium ? " et ton premium" : ""}.</p>
    <input class="field" id="tel" type="tel" inputmode="numeric" autocomplete="tel" placeholder="Ton numéro (77 123 45 67)">
    <input class="field" id="tcode" type="password" inputmode="numeric" maxlength="6" autocomplete="new-password" placeholder="Code à 6 chiffres">
    <p class="small muted">Ce code sert seulement à ouvrir l'appli. Ce n'est <b>pas</b> ton code Wave ou Orange Money.</p>
    <button class="btn" id="tok">Enregistrer</button>
    ${err ? `<p class="msg-ko small">${esc(err)}</p>` : ""}</div>`;
  document.getElementById("tok").onclick = () => {
    const t = Compte.normTel(document.getElementById("tel").value), c = document.getElementById("tcode").value.trim();
    if (!t) return viewTel("Numéro invalide : écris les 9 chiffres, par exemple 77 123 45 67.");
    if (!/^\d{6}$/.test(c)) return viewTel("Le code doit faire exactement 6 chiffres.");
    Compte.linkTel(t, c).then((how) => {
      S.phone = t; try { localStorage.setItem("rev", JSON.stringify(S)); } catch {}
      if (how === "email") alert("Numéro enregistré. Continue à te connecter avec ton e-mail et ton mot de passe.");
      render();
    }).catch((e) => viewTel(({ "auth/email-already-in-use": "Ce numéro est déjà utilisé par un autre compte.", "auth/credential-already-in-use": "Ce numéro est déjà utilisé par un autre compte.", "auth/requires-recent-login": "Déconnecte-toi puis reconnecte-toi, et recommence." })[e && e.code] || "L'enregistrement n'a pas abouti. Réessaie."));
  };
}
// le profil en ligne fait foi pour l'essai et le premium ; les progrès les plus complets sont gardés
function applyProfile(p) {
  if (!p) return;
  S.trialStart = p.created.toISOString().slice(0, 10);
  // validé par l'admin pendant que l'appli était fermée : on le dit une fois à l'ouverture
  if (p.premium && !S.premium && !S.premiumVu && p.premiumAt && Date.now() - p.premiumAt < 30 * 864e5) { S.premiumVu = true; setTimeout(bravoPremium, 800); }
  S.premium = p.premium;
  S.suspended = p.suspended;
  S.phone = p.phone || "";
  const d = p.data || {};
  if (Object.keys(d.stats || {}).length > Object.keys(S.stats).length) Object.assign(S, { stats: d.stats, sessions: d.sessions || [], days: d.days || [], daily: d.daily || {}, challenges: d.challenges || {}, done: d.done || {} });
  if (!S.level && d.level) S.level = d.level;
  // emploi du temps et devoirs : retrouvés en se connectant sur un autre téléphone
  if (!Object.keys(S.edt || {}).length && d.edt) S.edt = d.edt;
  if (!(S.todo || []).length && d.todo) S.todo = d.todo;
  try { localStorage.setItem("rev", JSON.stringify(S)); } catch {}
}

function render() {
  clearInterval(timer);
  // hors connexion (Firebase injoignable), l'appli reste utilisable en local
  if (Compte.enabled && Compte.ready && !Compte.user) return viewLogin();
  if (Compte.enabled && Compte.user && !S.phone && !Compte.isAdmin()) return viewTel();
  const [tab, ...rest] = (location.hash.slice(1) || "accueil").split("/"), arg = rest.length ? rest.join("/") : undefined;
  if (tab === "admin" && globalThis.viewAdmin) { viewAdmin(arg); window.scrollTo(0, 0); return; }
  if (S.suspended) { $view.innerHTML = `<div class="card"><h1>Compte suspendu</h1><p>Ton compte est suspendu pour le moment. Contacte-nous pour le réactiver.</p>${CFG.wave_number || CFG.whatsapp ? `<p class="small muted">WhatsApp : ${esc(CFG.wave_number || CFG.whatsapp)}</p>` : ""}</div>`; return; }
  document.getElementById("exam-tag").textContent = S.level || "";
  if ((!S.level || !DATA.levels.includes(S.level)) && tab !== "classe" && tab !== "partager") { S.level = null; return viewLevel(); }
  // après l'essai, l'appli est la même pour tous mais réservée aux abonnés : seuls l'accueil, la classe et les progrès restent visibles
  if (!isPremium() && !["accueil", "classe", "premium", "progres", "partager", "bienvenue", "nouveautes"].includes(tab)) return viewPremium(`Ton essai gratuit de ${TRIAL_DAYS} jours est terminé. Abonne-toi pour continuer à réviser.`);
  document.querySelectorAll(".tabs a").forEach((a) => { if (a.dataset.tab === tab) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current"); });
  if ((globalThis.ROUTES || {})[tab]) { ROUTES[tab](arg); window.scrollTo(0, 0); return; }
  if (tab === "accueil" && arg === "organiser") { viewOrganiser(); window.scrollTo(0, 0); return; }
  ({ bienvenue: viewBienvenue, classe: viewLevel, partager: viewPartager, annales: viewAnnales, exercices: viewExercices, "qcm-list": viewQcmList, devoir: () => viewDevoir(arg), duo: () => viewDuo(arg), challenge: viewChallenge, fiches: viewFiches, fiche: () => viewFiche(arg), assistant: () => viewAssistant(arg), agenda: () => viewAgenda(arg), notions: () => viewNotions(arg), notion: () => viewNotion(arg), sujet: () => viewGuided(arg), quiz: () => viewQuiz(arg), examen: viewExam, vie: () => viewVie(arg), outils: () => viewOutils(arg), erreurs: viewErrors, progres: viewProgress, premium: () => viewPremium() }[tab] || viewHome)();
  window.scrollTo(0, 0);
}
window.addEventListener("hashchange", render);

let deferred = null;
window.addEventListener("beforeinstallprompt", (e) => { e.preventDefault(); deferred = e; document.getElementById("install").hidden = false; if (!document.getElementById("install2") && document.getElementById("google")) { const c = document.createElement("div"); c.innerHTML = `<button class="btn" id="install2">Installer l'appli</button>`; $view.prepend(c.firstChild); document.getElementById("install2").onclick = () => document.getElementById("install").click(); } });
document.getElementById("install").onclick = () => { if (deferred) { deferred.prompt(); deferred = null; document.getElementById("install").hidden = true; } };
if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});

Promise.all([fetch("data/questions.json", { cache: "no-cache" }).then((r) => r.json()), fetch("data/config.json", { cache: "no-cache" }).then((r) => r.json())])
  .then(async ([d, c]) => { DATA = d; CFG = c; applyProfile(await Compte.start().catch(() => null)); render(); suivrePremium(); })
  .catch(() => { $view.innerHTML = `<div class="card"><p>Impossible de charger les questions. Vérifie ta connexion puis recharge la page.</p></div>`; });
