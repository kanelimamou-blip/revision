"use strict";
// Mode parent répétiteur (#famille) : la même appli, deux façons de l'utiliser.
//  - Élève seul : l'élève se forme tout seul (fonctionnement habituel).
//  - Parent répétiteur : le parent a son compte, il ajoute un ou plusieurs enfants (du CE1 à la Terminale, selon les
//    classes de l'appli), il donne des missions, il fait réviser avec une séance guidée (l'essentiel, questions à poser
//    avec les réponses, pièges, exercice corrigé) et il suit les progrès. Il peut demander un suivi spécifique à l'équipe.
// Un enfant révise soit sur le téléphone du parent (profil dans le compte du parent), soit sur son propre téléphone
// avec son compte, relié au parent par un code à 8 caractères. Tout reste gratuit côté technique (Firestore Spark).
(() => {
  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  // champs du compte, communs à tous les profils du téléphone (le reste appartient au profil en cours)
  const GARDER = ["premium", "premiumVu", "premiumAt", "trialStart", "phone", "suspended", "cgu", "mode", "famille", "actif", "newsSeen", "pushOn", "accord", "code", "pseudo", "liens"];
  const F = () => { const f = S.famille || (S.famille = {}); if (!Array.isArray(f.enfants)) f.enfants = []; return f; };
  const enfant = (id) => F().enfants.find((e) => e.id === id);
  const actif = () => (S.actif ? enfant(S.actif) : null);
  const estParent = () => S.mode === "parent";
  const enreg = () => { store.save(); Compte.setFamille(S.mode || "", S.famille || null); };
  const rid = (n) => [...crypto.getRandomValues(new Uint8Array(n))].map((b) => "abcdefghjkmnpqrstuvwxyz23456789"[b % 31]).join("");
  const T = () => ({ eleve: CFG.price_fcfa || 1000, parent: 1500, enfant_sup: 500, suivi: 2000, ...(CFG.formules || {}) });
  const prenom = (e) => esc((e.nom || "").split(" ")[0] || "l'enfant");
  const tel = (t) => (t || "").replace(/^(\d{2})(\d{3})(\d{2})(\d{2})$/, "$1 $2 $3 $4");
  const etape = (lvl) => /^(CI|CP|CE|CM)/i.test(lvl || "") ? "primaire" : /^(6e|5e|4e|3e)/.test(lvl || "") ? "college" : "lycee";
  const base = () => location.href.split("#")[0];

  // ---------- Bascule d'un profil à l'autre sur le même téléphone (parent ↔ enfants)
  async function basculer(id) {
    Compte.flush && Compte.flush();
    const cur = S.actif || "_parent", snap = {};
    Object.keys(S).forEach((k) => { if (!GARDER.includes(k)) snap[k] = S[k]; });
    try { localStorage.setItem("rev:" + cur, JSON.stringify(snap)); } catch (e) {}
    let next = null;
    try { next = JSON.parse(localStorage.getItem("rev:" + (id || "_parent")) || "null"); } catch (e) {}
    if (id) {
      // profil retrouvé en ligne (autre téléphone, appli réinstallée) s'il est plus complet
      const r = await Compte.lireEnfant(id).catch(() => null);
      if (r && r.data && Object.keys(r.data.stats || {}).length > Object.keys((next || {}).stats || {}).length) next = { ...r.data };
      next = next || {};
      next.level = enfant(id).level;
    }
    Object.keys(S).forEach((k) => { if (!GARDER.includes(k)) delete S[k]; });
    Object.assign(S, { level: null, stats: {}, sessions: [], days: [] }, next || {});
    S.actif = id || null;
    try { localStorage.setItem("rev", JSON.stringify(S)); } catch (e) {}
    location.hash = id ? "#accueil" : "#famille";
    location.reload();
  }

  // ---------- Avant chaque page (appelé par render dans app.js)
  globalThis.familleAvant = (tab, arg) => {
    document.body.classList.toggle("mode-parent", estParent() && !S.actif);
    bandeau();
    if (tab === "famille") { if (S.actif && !/^(retour|relier)/.test(arg || "")) return viewRetour(), true; viewFamille(arg); return true; }
    if (!S.mode && !S.level && !Compte.isAdmin()) { viewMode(); return true; }
    if (estParent() && !S.actif) {
      if (tab === "partager") return false;
      if (tab === "premium") { viewPremium(); return true; }
      viewFamille(); return true;
    }
    return false;
  };
  function bandeau() {
    let b = document.getElementById("fambtn");
    const tag = document.getElementById("exam-tag");
    if (estParent() && !S.actif && tag) tag.textContent = "👨‍👩‍👧 Parent";
    const e = actif();
    if (!(estParent() && e)) { if (b) b.remove(); return; }
    if (!b) { b = document.createElement("a"); b.id = "fambtn"; b.className = "btn-ghost small"; b.href = "#famille/retour"; document.querySelector(".top-r").prepend(b); }
    b.textContent = `${e.nom.split(" ")[0]} · ↩ Parent`;
  }

  // ---------- Choix du mode (nouveau compte) ou changement de mode
  function viewMode() {
    const t = T();
    $view.innerHTML = `<h1>Comment veux-tu utiliser Révision ?</h1><p class="muted">C'est la même appli, avec le même contenu du programme sénégalais. Tu pourras changer plus tard.</p>
      <button class="card lib-card modechoix" data-m="eleve"><b>🎒 Je révise tout seul</b><span class="small muted">Je suis élève : cours, QCM, exercices, sujets types, mon suivi et ma trajectoire. ${fcfa(t.eleve)} après l'essai.</span></button>
      <button class="card lib-card modechoix" data-m="parent"><b>👨‍👩‍👧 Je suis parent : je fais réviser mes enfants</b><span class="small muted">Je deviens le répétiteur : j'ajoute un ou plusieurs enfants, je donne des missions, je fais la séance avec les réponses sous les yeux et je suis leurs progrès. À partir de ${fcfa(t.parent)}.</span></button>
      ${S.mode ? `<a class="btn alt" href="${estParent() ? "#famille" : "#accueil"}">Garder le mode actuel</a>` : ""}`;
    $view.querySelectorAll("[data-m]").forEach((b) => (b.onclick = () => {
      S.mode = b.dataset.m; enreg();
      go(S.mode === "parent" ? (F().enfants.length ? "famille" : "famille/ajouter") : "accueil");
      render();
    }));
  }

  // ---------- Retour à l'espace parent (code parent facultatif, pour que l'enfant ne modifie pas ses missions)
  function viewRetour(err = "") {
    const e = actif();
    if (!e) { S.actif = null; return render(); }
    if (!F().pin) return basculer(null);
    $view.innerHTML = `<div class="card"><h1>↩ Espace parent</h1><p>Tape le code parent pour quitter le profil de ${prenom(e)}.</p>
      <input class="field" id="pin" type="password" inputmode="numeric" maxlength="4" placeholder="Code parent (4 chiffres)"><button class="btn" id="pok">Ouvrir l'espace parent</button>
      ${err ? `<p class="msg-ko small">${esc(err)}</p>` : ""}<a class="btn alt" href="#accueil">Rester sur le profil de ${prenom(e)}</a></div>`;
    document.getElementById("pok").onclick = async () => (await sha256("pin:" + document.getElementById("pin").value.trim())) === F().pin ? basculer(null) : viewRetour("Code incorrect.");
  }

  // ---------- Progrès d'un enfant, lus sur le téléphone ou dans son compte
  let QMAP = null;
  const qmap = () => QMAP || (QMAP = Object.fromEntries(DATA.questions.map((q) => [q.id, q])));
  const cache = {};
  async function dataOf(e) {
    if (e.type === "compte") {
      if (!e.uid && e.code) { const l = await Compte.lireLien(e.code).catch(() => null); if (l && l.enfant) { e.uid = l.enfant; if (l.level && !e.level) e.level = l.level; enreg(); } }
      if (!e.uid) return { attente: true, stats: {}, daily: {}, days: [], sessions: [] };
      const u = await Compte.lireEleve(e.uid).catch(() => null);
      if (!u) return { erreur: true, stats: {}, daily: {}, days: [], sessions: [] };
      if (u.data.level && u.data.level !== e.level) { e.level = u.data.level; enreg(); }
      const m = await Compte.lireMissions(e.uid).catch(() => null);
      if (m && Array.isArray(m.items)) (e.missions || []).forEach((x) => { const r = m.items.find((y) => y.id === x.id); if (r && r.fait && !x.fait) x.fait = r.fait; });
      return (cache[e.id] = { stats: {}, daily: {}, days: [], sessions: [], ...u.data, lastSeen: u.lastSeen, premium: u.premium });
    }
    if (S.actif === e.id) return S;
    let d = null;
    try { d = JSON.parse(localStorage.getItem("rev:" + e.id) || "null"); } catch (x) {}
    if (!d) { const r = await Compte.lireEnfant(e.id).catch(() => null); d = r && r.data; }
    return (cache[e.id] = { stats: {}, daily: {}, days: [], sessions: [], ...(d || {}) });
  }
  const jours = (n) => [...Array(n)].map((_, i) => { const d = new Date(); d.setDate(d.getDate() - i); return d.toISOString().slice(0, 10); });
  function bilan(e, d) {
    const j7 = jours(7), daily = d.daily || {}, days = d.days || [];
    const n = j7.reduce((s, k) => s + ((daily[k] || {}).n || 0), 0), ok = j7.reduce((s, k) => s + ((daily[k] || {}).ok || 0), 0);
    const actifs = j7.filter((k) => days.includes(k)).length, dernier = days.slice().sort().pop() || null;
    const absent = dernier ? Math.round((new Date(today()) - new Date(dernier)) / 864e5) : null;
    const mat = {}, chap = {};
    for (const [id, st] of Object.entries(d.stats || {})) {
      const q = qmap()[id]; if (!q) continue;
      const m = (mat[q.s] = mat[q.s] || { ok: 0, ko: 0, vus: 0 }); m.ok += st.ok || 0; m.ko += st.ko || 0; m.vus++;
      if (q.ch !== undefined) { const c = (chap[q.s + "~" + q.ch] = chap[q.s + "~" + q.ch] || { sid: q.s, ch: q.ch, ok: 0, ko: 0 }); c.ok += st.ok || 0; c.ko += st.ko || 0; }
    }
    const matieres = subjectsOf(e.level).map((s) => { const m = mat[s.id] || { ok: 0, ko: 0, vus: 0 }; const t = m.ok + m.ko;
      return { sid: s.id, nom: s.name, taux: t ? Math.round((100 * m.ok) / t) : null, couv: Math.min(100, Math.round((100 * m.vus) / Math.max(1, s.count))) }; });
    const faibles = Object.values(chap).filter((c) => c.ok + c.ko >= 3 && c.ok / (c.ok + c.ko) < 0.6 && subjectsOf(e.level).some((s) => s.id === c.sid))
      .sort((a, b) => a.ok / (a.ok + a.ko) - b.ok / (b.ok + b.ko)).slice(0, 5)
      .map((c) => ({ ...c, taux: Math.round((100 * c.ok) / (c.ok + c.ko)), titre: ((DATA.programmes || {})[c.sid] || [])[c.ch] || subjName(c.sid) }));
    const notes = (d.sessions || []).slice(-5).reverse().map((s) => ({ t: s.t, note: s.total ? Math.round((200 * s.score) / s.total) / 10 : 0, d: s.d }));
    return { n, taux: n ? Math.round((100 * ok) / n) : null, actifs, dernier, absent, matieres, faibles, notes };
  }
  const resumeTexte = (e, b) => [`${e.nom} (${e.level})`, `7 derniers jours : ${b.n} questions, ${b.taux ?? "—"} % de réussite, ${b.actifs}/7 jours actifs.`,
    `Matières : ${b.matieres.filter((m) => m.taux !== null).map((m) => `${m.nom} ${m.taux} %`).join(", ") || "pas encore de réponses"}.`,
    b.faibles.length ? `Points faibles : ${b.faibles.map((f) => `${f.titre} (${f.taux} %)`).join(" ; ")}.` : "",
    b.notes.length ? `Dernières notes : ${b.notes.map((x) => `${x.note}/20`).join(", ")}.` : "",
    `Séances avec le parent : ${(e.seances || []).length}. Missions faites : ${(e.missions || []).filter((m) => m.fait).length}/${(e.missions || []).length}.`].filter(Boolean).join("\n").slice(0, 3000);

  // ---------- Missions : QCM d'un chapitre, cours, exercice corrigé, synthèse
  const TYPES = { qcm: ["✅", "QCM du chapitre (10 questions)"], cours: ["📖", "Lire le cours"], exo: ["✏️", "Exercice corrigé"], fiche: ["📝", "Lire la synthèse"] };
  const notionDe = (sid, ch) => ((DATA.notions || {})[sid] || []).find((n) => n.pch === ch);
  const ficheDe = (sid, ch) => { const f = (DATA.fiches || {})[sid] || []; const i = f.findIndex((c) => c.p === ch); return i < 0 ? null : { i, c: f[i] }; };
  function lienMission(m) {
    const n = notionDe(m.sid, m.ch), f = ficheDe(m.sid, m.ch);
    if (m.t === "cours") return n ? `#notion/${n.id}` : f ? `#fiche/${m.sid}~${f.i}` : `#notions/${m.sid}`;
    if (m.t === "fiche") return f ? `#fiche/${m.sid}~${f.i}` : n ? `#notion/${n.id}` : `#fiches`;
    if (m.t === "exo") return n ? `#sujet/ch-${n.id}` : `#quiz/${m.sid}/${m.ch}`;
    return `#quiz/${m.sid}/${m.ch}`;
  }
  // avancement d'un QCM : questions du chapitre répondues depuis que la mission a été donnée
  const faitesQcm = (m, stats) => Object.entries(stats || {}).filter(([id, st]) => { const q = qmap()[id]; return q && q.s === m.sid && q.ch === m.ch && (st.t || 0) >= (m.cree || 0); }).length;
  const estFaite = (m, stats) => !!m.fait || (m.t === "qcm" && faitesQcm(m, stats) >= 10);
  const titreMission = (m) => `${TYPES[m.t][0]} ${TYPES[m.t][1]} · ${subjName(m.sid)} · ${((DATA.programmes || {})[m.sid] || [])[m.ch] || ""}`;
  async function publierMissions(e) {
    if (e.type !== "compte" || !e.uid) return;
    const r = await Compte.lireMissions(e.uid).catch(() => null);
    if (r && Array.isArray(r.items)) e.missions.forEach((x) => { const y = r.items.find((z) => z.id === x.id); if (y && y.fait && !x.fait) x.fait = y.fait; });
    await Compte.ecrireMissions(e.uid, { items: (e.missions || []).slice(-60), seances: (e.seances || []).slice(-120), pnom: (Compte.user && Compte.user.displayName) || "" }).catch(() => {});
  }

  // Carte « Missions de ton parent » sur l'accueil de l'enfant (profil sur le téléphone du parent ou compte relié)
  let distantes = null;
  globalThis.missionsCard = () => {
    const e = actif();
    if (e) return carteMissions(e.missions || [], (id) => { const m = e.missions.find((x) => x.id === id); if (m) { m.fait = today(); enreg(); } });
    if (estParent() || !Compte.user) return "";
    // compte relié : missions lues en ligne (une fois par ouverture de l'accueil)
    Compte.lireMissions(Compte.user.uid).then((r) => {
      distantes = r; const box = document.getElementById("mismiss");
      if (box && r && (r.items || []).length) { box.outerHTML = carteMissions(r.items, async (id) => { const m = r.items.find((x) => x.id === id); if (m) { m.fait = today(); await Compte.ecrireMissions(Compte.user.uid, { items: r.items }).catch(() => {}); } }, r.pnom); lierBoutons(); }
    }).catch(() => {});
    return `<div id="mismiss"></div>`;
  };
  let surFait = null;
  function carteMissions(items, fait, pnom = "") {
    const a = items.filter((m) => !estFaite(m, S.stats)), f = items.length - a.length;
    surFait = fait;
    if (!items.length) return "";
    setTimeout(lierBoutons, 0);
    return `<div class="card" id="missions" style="border:2px solid var(--accent)"><h2>📋 Missions de ${pnom ? esc(pnom.split(" ")[0]) : "ton parent"}</h2>
      ${a.length ? a.slice(0, 6).map((m) => `<div class="row" style="align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid rgba(127,127,127,.2)"><a href="${lienMission(m)}" style="flex:1"><b>${esc(titreMission(m))}</b>${m.pour ? `<br><span class="small muted">pour le ${new Date(m.pour).toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long" })}</span>` : ""}${m.t === "qcm" ? `<br><span class="small muted">${Math.min(10, faitesQcm(m, S.stats))}/10 questions</span>` : ""}</a><button class="btn small" data-fait="${m.id}">✓ Fait</button></div>`).join("")
        : `<p class="msg-ok">Bravo, toutes tes missions sont faites ! 🎉</p>`}
      ${f ? `<p class="small muted">${f} mission${f > 1 ? "s" : ""} déjà faite${f > 1 ? "s" : ""}.</p>` : ""}</div>`;
  }
  function lierBoutons() { document.querySelectorAll("[data-fait]").forEach((b) => (b.onclick = async () => { b.disabled = true; await surFait(b.dataset.fait); render(); })); }

  // ---------- Espace parent
  async function viewFamille(arg = "") {
    const [p, a, b, c] = (arg || "").split("/");
    if (p === "retour") return viewRetour();
    if (p === "relier") return viewRelier(a);
    if (p === "mode") return viewMode();
    if (!estParent()) {
      // un élève arrive ici : il peut se relier à son parent ou passer en mode parent
      $view.innerHTML = `<h1>👨‍👩‍👧 Mode parent répétiteur</h1><div class="card"><p>Tu es en mode <b>élève seul</b>.</p>
        <a class="btn" href="#famille/relier">👨‍👩 Relier mon compte à mon parent</a><a class="btn alt" href="#famille/mode">Je suis parent : passer en mode parent</a></div>`;
      return;
    }
    if (p === "ajouter") return viewAjouter();
    if (p === "pin") return viewPin();
    if (p === "guide") return viewGuide();
    const e = a ? enfant(a) : null;
    if (p === "enfant" && e) return viewEnfant(e);
    if (p === "mission" && e) return viewMission(e);
    if (p === "seance" && e) return viewSeance(e, b, c);
    if (p === "suivi" && e) return viewSuivi(e);
    if (p === "modifier" && e) return viewModifier(e);
    return viewTableau();
  }

  async function viewTableau() {
    const f = F(), t = T(), nom = myName();
    $view.innerHTML = `${Compte.isAdmin() ? `<a class="btn" href="#admin/parents">🛠️ Espace admin</a>` : ""}
      <h1>👨‍👩‍👧 ${nom ? `Bonjour ${esc(nom)}` : "Espace parent"}</h1>
      <p class="muted">Tu es le répétiteur : tu donnes les missions, tu fais réviser avec les réponses sous les yeux, et tu suis chaque enfant.</p>
      ${!S.premium && trialLeft() > 0 ? `<a class="trial" href="#premium">🎁 Essai gratuit pour toute la famille : encore <b>${trialLeft()} jour${trialLeft() > 1 ? "s" : ""}</b></a>` : ""}
      ${!isPremium() ? `<a class="trial" href="#premium">🔒 L'essai est terminé. Formule parent : ${fcfa(t.parent)}${f.enfants.length > 1 ? ` + ${fcfa(t.enfant_sup)} par enfant en plus` : ""}.</a>` : ""}
      <div id="enfants">${f.enfants.length ? f.enfants.map((e) => `<div class="card"><p><b>${e.type === "compte" ? "📱" : "👦"} ${esc(e.nom)}</b> · ${esc(e.level)}</p><p class="small muted">Chargement du suivi…</p></div>`).join("") : `<div class="card"><p>Ajoute ton premier enfant pour commencer.</p></div>`}</div>
      <a class="btn hi-btn" href="#famille/ajouter">➕ Ajouter un enfant</a>
      <a class="card lib-card" href="#famille/guide"><b>📘 Guide du parent répétiteur</b><span class="small muted">Comment faire une bonne séance de 20 minutes, même sans être enseignant</span></a>
      <div class="card"><h2>🎯 Suivi spécifique par la plateforme</h2><p class="small">Tu veux que l'équipe Révision suive un enfant de près ? Donne ton objectif (ex. passer de 8 à 12 en maths) : nous t'envoyons un plan et des conseils adaptés à ses résultats. ${fcfa(t.suivi)} par enfant.</p><p class="small muted">Ouvre la fiche d'un enfant puis touche « Demander un suivi spécifique ».</p></div>
      <div class="row"><a class="btn alt small" style="flex:1" href="#famille/pin">🔐 Code parent${f.pin ? " (activé)" : ""}</a><a class="btn alt small" style="flex:1" href="#famille/mode">Changer de mode</a></div>
      ${globalThis.legalFooter ? legalFooter() : ""}`;
    const box = document.getElementById("enfants");
    const cartes = await Promise.all(f.enfants.map(async (e) => {
      const d = await dataOf(e), b = bilan(e, d), miss = (e.missions || []), restantes = miss.filter((m) => !estFaite(m, d.stats)).length;
      const alerte = d.attente ? `⏳ En attente : ${prenom(e)} doit taper le code <b>${esc(e.code)}</b> dans son appli.` : d.erreur ? "Suivi illisible pour le moment (règles en cours de mise à jour ou compte retiré)." : b.absent === null ? "Pas encore commencé." : b.absent >= 3 ? `⚠️ Pas de révision depuis ${b.absent} jours.` : b.absent === 0 ? "✅ A révisé aujourd'hui." : `A révisé il y a ${b.absent} jour${b.absent > 1 ? "s" : ""}.`;
      return `<div class="card"><div class="row" style="justify-content:space-between"><b>${e.type === "compte" ? "📱" : "👦"} ${esc(e.nom)}</b><span class="small muted">${esc(e.level)}</span></div>
        <p class="small">${alerte}</p>
        <div class="grid" style="grid-template-columns:repeat(3,1fr);gap:6px;text-align:center"><div><b>${b.n}</b><br><span class="small muted">questions (7 j)</span></div><div><b>${b.taux ?? "—"}${b.taux !== null ? " %" : ""}</b><br><span class="small muted">réussite</span></div><div><b>${b.actifs}/7</b><br><span class="small muted">jours actifs</span></div></div>
        <p class="small muted">${miss.length ? `📋 ${restantes} mission${restantes > 1 ? "s" : ""} en cours sur ${miss.length}` : "📋 Aucune mission"}${(e.seances || []).length ? ` · 🧑‍🏫 ${(e.seances || []).length} séance${e.seances.length > 1 ? "s" : ""}` : ""}${b.faibles[0] ? ` · à revoir : ${esc(b.faibles[0].titre)}` : ""}</p>
        <div class="row"><a class="btn small" style="flex:1" href="#famille/enfant/${e.id}">Voir le suivi</a>${e.type === "local" ? `<button class="btn alt small" style="flex:1" data-rev="${e.id}">▶ Le faire réviser</button>` : `<a class="btn alt small" style="flex:1" href="#famille/seance/${e.id}">🧑‍🏫 Séance</a>`}</div></div>`;
    }));
    if (!document.body.contains(box)) return;
    if (cartes.length) box.innerHTML = cartes.join("");
    box.querySelectorAll("[data-rev]").forEach((x) => (x.onclick = () => basculer(x.dataset.rev)));
  }

  function viewAjouter(err = "") {
    const lv = DATA.levels.filter((l) => subjectsOf(l).length); // classes sans contenu cachées (comme le choix de classe)
    $view.innerHTML = `<h1>➕ Ajouter un enfant</h1>
      <div class="card" style="gap:12px"><input class="field" id="enom" maxlength="40" placeholder="Prénom et nom de l'enfant">
      <label class="small">Sa classe</label><select class="field" id="elvl">${lv.map((l) => `<option>${esc(l)}</option>`).join("")}</select>
      <label class="small">Où révise-t-il ?</label>
      <label class="row small" style="gap:8px;align-items:flex-start"><input type="radio" name="etype" value="local" checked> <span><b>Sur mon téléphone</b> : il n'a pas de téléphone, ou on partage le même. Je passe sur son profil pour le faire réviser.</span></label>
      <label class="row small" style="gap:8px;align-items:flex-start"><input type="radio" name="etype" value="compte"> <span><b>Sur son propre téléphone</b>, avec son compte Révision : je reçois un code à lui donner, puis je vois ses progrès à distance.</span></label>
      <button class="btn" id="eok">Ajouter</button>${err ? `<p class="msg-ko small">${esc(err)}</p>` : ""}</div>
      <p class="small muted">Classes proposées : celles du programme sénégalais disponibles dans l'appli${lv.some((l) => /^C[EM]/.test(l)) ? "" : " (le primaire arrive bientôt)"}.</p>
      <a class="btn alt" href="#famille">Retour</a>`;
    document.getElementById("eok").onclick = async (ev) => {
      const nom = document.getElementById("enom").value.trim().slice(0, 40), level = document.getElementById("elvl").value, type = $view.querySelector("[name=etype]:checked").value;
      if (nom.length < 2) return viewAjouter("Écris le prénom de l'enfant.");
      if (F().enfants.length >= 10) return viewAjouter("10 enfants au maximum par compte parent.");
      ev.target.disabled = true;
      const e = { id: rid(8), nom, level, type, missions: [], seances: [], cree: Date.now() };
      if (type === "compte") {
        e.code = rid(8).toUpperCase();
        try { await Compte.creerLien(e.code, (Compte.user && Compte.user.displayName) || ""); } catch (x) { ev.target.disabled = false; return viewAjouter("Le code n'a pas pu être créé (" + (x.code || x.message) + "). Vérifie ta connexion."); }
      }
      F().enfants.push(e); enreg();
      go("famille/enfant/" + e.id);
    };
  }

  async function viewEnfant(e) {
    $view.innerHTML = `<h1>${e.type === "compte" ? "📱" : "👦"} ${esc(e.nom)}</h1><p class="muted">${esc(e.level)}</p><p class="muted">Chargement…</p>`;
    const d = await dataOf(e), b = bilan(e, d), t = T();
    const suivis = await Compte.lireSuivis().catch(() => []), sv = suivis.find((x) => x.id === `${Compte.user && Compte.user.uid}_${e.id}`);
    // le résumé du suivi spécifique est remis à jour au plus une fois par jour pour l'équipe
    if (sv && e.resumeLe !== today()) { Compte.majSuivi(sv.id, { objectif: sv.objectif || "", resume: resumeTexte(e, b), level: e.level }).catch(() => {}); e.resumeLe = today(); enreg(); }
    const miss = (e.missions || []).slice().reverse();
    const conseil = b.faibles[0] || null;
    const lien = `${base()}#famille/relier/${e.code}`;
    $view.innerHTML = `<h1>${e.type === "compte" ? "📱" : "👦"} ${esc(e.nom)}</h1><p class="muted">${esc(e.level)} · ${e.type === "compte" ? "révise sur son téléphone" : "révise sur ton téléphone"}</p>
      ${d.attente ? `<div class="card" style="border:2px solid var(--hi,#f5a623)"><h2>📲 Dernière étape</h2><p>Sur le téléphone de ${prenom(e)}, ouvre Révision (avec son compte), puis tape ce code dans « Mon parent » :</p><p class="count" style="letter-spacing:3px">${esc(e.code)}</p>
        <a class="btn hi-btn" target="_blank" rel="noopener" href="https://wa.me/?text=${encodeURIComponent(`Ouvre ce lien sur ton téléphone pour relier ton compte Révision au mien (code ${e.code}) : ${lien}`)}">Lui envoyer le code sur WhatsApp</a><button class="btn alt small" id="recharger">J'ai fait : actualiser</button></div>` : ""}
      <div class="card"><h2>📊 Ses 7 derniers jours</h2><div class="grid" style="grid-template-columns:repeat(3,1fr);gap:6px;text-align:center"><div><b>${b.n}</b><br><span class="small muted">questions</span></div><div><b>${b.taux ?? "—"}${b.taux !== null ? " %" : ""}</b><br><span class="small muted">réussite</span></div><div><b>${b.actifs}/7</b><br><span class="small muted">jours actifs</span></div></div>
        <p class="small muted">${b.dernier ? `Dernière révision : ${new Date(b.dernier).toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long" })}` : "Pas encore de révision enregistrée."}${d.lastSeen ? ` · appli ouverte ${d.lastSeen.toLocaleDateString("fr-FR")}` : ""}</p></div>
      ${conseil ? `<div class="card" style="border:2px solid var(--accent)"><h2>💡 Séance conseillée</h2><p><b>${esc(subjName(conseil.sid))} : ${esc(conseil.titre)}</b> (${conseil.taux} % de bonnes réponses).</p><a class="btn hi-btn" href="#famille/seance/${e.id}/${conseil.sid}/${conseil.ch}">🧑‍🏫 Faire cette séance avec ${prenom(e)}</a></div>` : ""}
      <div class="btns">${e.type === "local" ? `<button class="btn" id="rev">▶ Passer sur son profil pour réviser</button>` : ""}<a class="btn${e.type === "local" ? " alt" : ""}" href="#famille/seance/${e.id}">🧑‍🏫 Séance répétiteur</a><a class="btn alt" href="#famille/mission/${e.id}">➕ Donner une mission</a></div>
      <div class="card"><h2>📚 Par matière</h2>${b.matieres.map((m) => `<div style="margin:6px 0"><div class="row small" style="justify-content:space-between"><span>${matIco(m.sid)} ${esc(m.nom)}</span><span class="muted">${m.taux === null ? "pas commencé" : `${m.taux} % juste · ${m.couv} % vu`}</span></div><span class="bar"><i style="width:${m.couv}%"></i></span></div>`).join("") || `<p class="small muted">Aucune matière pour cette classe.</p>`}</div>
      ${b.faibles.length ? `<div class="card"><h2>⚠️ Chapitres à revoir</h2>${b.faibles.map((f) => `<a class="row lib" href="#famille/seance/${e.id}/${f.sid}/${f.ch}"><span>${esc(subjName(f.sid))} · ${esc(f.titre)}</span><span class="small muted">${f.taux} % ›</span></a>`).join("")}</div>` : ""}
      ${b.notes.length ? `<div class="card"><h2>📝 Dernières notes</h2>${b.notes.map((x) => `<p class="small">${esc(x.t)} : <b>${String(x.note).replace(".", ",")}/20</b> <span class="muted">(${esc(x.d || "")})</span></p>`).join("")}</div>` : ""}
      <div class="card"><h2>📋 Missions</h2>${miss.length ? miss.slice(0, 15).map((m) => `<div class="row small" style="padding:6px 0;border-bottom:1px solid rgba(127,127,127,.2);align-items:center;gap:8px"><span style="flex:1">${estFaite(m, d.stats) ? "✅" : "⏳"} ${esc(titreMission(m))}${m.pour ? ` <span class="muted">· pour le ${new Date(m.pour).toLocaleDateString("fr-FR")}</span>` : ""}${m.t === "qcm" && !estFaite(m, d.stats) ? ` <span class="muted">· ${faitesQcm(m, d.stats)}/10</span>` : ""}</span><button class="linkbtn small" data-del="${m.id}">retirer</button></div>`).join("") : `<p class="small muted">Aucune mission. Donne-lui un chapitre à travailler : il le verra en haut de son accueil.</p>`}</div>
      ${(e.seances || []).length ? `<div class="card"><h2>🧑‍🏫 Séances faites avec toi</h2>${e.seances.slice(-8).reverse().map((s) => `<p class="small">${esc(s.d)} · ${esc(subjName(s.sid))} · ${esc(((DATA.programmes || {})[s.sid] || [])[s.ch] || "")} : <b>${s.ok}/${s.n}</b> ${({ ok: "😀 compris", moyen: "😐 à revoir", ko: "😟 pas compris" })[s.avis] || ""}</p>`).join("")}</div>` : ""}
      <div class="card"><h2>🎯 Suivi spécifique par la plateforme</h2>${sv ? `<p>Demande envoyée le ${sv.at ? sv.at.toLocaleDateString("fr-FR") : "aujourd'hui"} · <b>${({ attente: "en attente", en_cours: "en cours", termine: "terminé" })[sv.statut] || esc(sv.statut)}</b></p><p class="small muted">Objectif : ${esc(sv.objectif || "")}</p>
        ${(sv.conseils || []).length ? sv.conseils.slice().reverse().map((x) => `<div class="card" style="background:var(--card2,rgba(127,127,127,.08))"><p class="small muted">Conseil de l'équipe · ${new Date(x.at).toLocaleDateString("fr-FR")}</p><p>${esc(x.t).replace(/\n/g, "<br>")}</p></div>`).join("") : `<p class="small">L'équipe prépare son plan. Il apparaîtra ici.</p>`}
        <a class="btn alt small" href="#famille/suivi/${e.id}">Modifier l'objectif</a>` : `<p class="small">L'équipe suit ${prenom(e)} de près à partir de ses résultats et t'envoie un plan et des conseils. ${fcfa(t.suivi)} par enfant.</p><a class="btn alt" href="#famille/suivi/${e.id}">Demander un suivi spécifique</a>`}</div>
      <div class="row"><a class="btn alt small" style="flex:1" href="#famille/modifier/${e.id}">✏️ Nom, classe</a><a class="btn alt small" style="flex:1" href="#famille">Tous mes enfants</a></div>`;
    const r = document.getElementById("rev"); if (r) r.onclick = () => basculer(e.id);
    const rc = document.getElementById("recharger"); if (rc) rc.onclick = () => viewEnfant(e);
    $view.querySelectorAll("[data-del]").forEach((x) => (x.onclick = () => { e.missions = e.missions.filter((m) => m.id !== x.dataset.del); enreg(); publierMissions(e); viewEnfant(e); }));
  }

  function choixChapitre(e, sid, onPick) {
    const subs = subjectsOf(e.level);
    return `<label class="small">Matière</label><select class="field" id="msid">${subs.map((s) => `<option value="${s.id}"${s.id === sid ? " selected" : ""}>${esc(s.name)}</option>`).join("")}</select>
      <label class="small">Chapitre du programme</label><select class="field" id="mch"></select>`;
  }
  function remplirChapitres(ch) {
    const sel = document.getElementById("msid"), out = document.getElementById("mch");
    const fill = () => { const t = (DATA.programmes || {})[sel.value] || []; out.innerHTML = t.map((x, i) => `<option value="${i}"${i === ch ? " selected" : ""}>${i + 1}. ${esc(x)}</option>`).join("") || `<option value="0">Toute la matière</option>`; };
    sel.onchange = () => { ch = 0; fill(); }; fill();
  }

  function viewMission(e) {
    $view.innerHTML = `<h1>➕ Mission pour ${prenom(e)}</h1><div class="card" style="gap:10px">
      <label class="small">Que doit-il faire ?</label><select class="field" id="mt">${Object.entries(TYPES).map(([k, [i, t]]) => `<option value="${k}">${i} ${t}</option>`).join("")}</select>
      ${choixChapitre(e)}
      <label class="small">Pour quand ?</label><input class="field" id="mpour" type="date" value="${new Date(Date.now() + 864e5).toISOString().slice(0, 10)}">
      <button class="btn" id="mok">Donner la mission</button><p class="small muted">${prenom(e)} la voit en haut de son accueil. Un QCM est coché tout seul après 10 questions du chapitre.</p></div>
      <a class="btn alt" href="#famille/enfant/${e.id}">Retour</a>`;
    remplirChapitres(0);
    document.getElementById("mok").onclick = async () => {
      const m = { id: rid(6), t: document.getElementById("mt").value, sid: document.getElementById("msid").value, ch: +document.getElementById("mch").value, pour: document.getElementById("mpour").value || null, cree: Date.now() };
      (e.missions = e.missions || []).push(m); e.missions = e.missions.slice(-60); enreg();
      await publierMissions(e);
      go("famille/enfant/" + e.id);
    };
  }

  // ---------- Séance répétiteur : le parent a l'essentiel, les questions et les réponses sous les yeux
  const CONSEILS = {
    primaire: ["Séance courte : 15 minutes, à heure fixe (après le goûter par exemple).", "Fais lire l'énoncé à voix haute par l'enfant, puis demande-lui de le redire avec ses mots.", "Félicite chaque bonne réponse ; sur une erreur, montre la bonne méthode sur un exemple simple, sans gronder."],
    college: ["20 minutes suffisent : 5 min l'essentiel, 10 min de questions, 5 min d'exercice.", "Demande-lui d'expliquer comme s'il était le professeur : s'il sait l'expliquer, il a compris.", "Note les chapitres « à revoir » : refais une séance dessus dans 2 ou 3 jours."],
    lycee: ["Laisse-le chercher seul 2 à 3 minutes avant de donner un indice.", "Exige la rédaction complète (justifier, unités, conclusion) : c'est ce qui rapporte des points au BAC.", "Un QCM raté ? Demande pourquoi les autres réponses sont fausses."],
  };
  function viewSeance(e, sid, ch) {
    if (!isPremium()) return viewPremium("La séance répétiteur fait partie de la formule parent.");
    if (sid === undefined) {
      $view.innerHTML = `<h1>🧑‍🏫 Séance avec ${prenom(e)}</h1><p class="muted">Choisis le chapitre à travailler (par exemple celui de son prochain devoir).</p>
        <div class="card" style="gap:10px">${choixChapitre(e)}<button class="btn" id="sgo">Commencer la séance</button></div><a class="btn alt" href="#famille/enfant/${e.id}">Retour</a>`;
      remplirChapitres(0);
      document.getElementById("sgo").onclick = () => go(`famille/seance/${e.id}/${document.getElementById("msid").value}/${document.getElementById("mch").value}`);
      return;
    }
    ch = +ch;
    const titre = ((DATA.programmes || {})[sid] || [])[ch] || subjName(sid), f = ficheDe(sid, ch), n = notionDe(sid, ch);
    const cles = f ? f.c.cles : n ? n.enonce : [];
    const qs = shuffle(qsOf(sid).filter((q) => q.ch === ch)).slice(0, 6);
    const exo = f && (f.c.exemple || (f.c.exemples || [])[0]) || (n && n.exemples[0]);
    const met = f && (f.c.methodes || [])[0];
    const rep = {};
    $view.innerHTML = `<p class="tag-src">Séance répétiteur · ${esc(subjName(sid))}</p><h1>${esc(titre)}</h1><p class="muted">Avec ${prenom(e)} (${esc(e.level)}) · 15 à 20 minutes. Toi seul vois les réponses.</p>
      <details class="card"><summary><b>👀 Conseils pour cette séance</b></summary><ul class="steps">${CONSEILS[etape(e.level)].map((x) => `<li>${esc(x)}</li>`).join("")}</ul></details>
      ${cles.length ? `<div class="card notion-key"><h2>1. 📌 L'essentiel à lui faire redire</h2><p class="small muted">Lis une ligne, puis demande-lui de l'expliquer ou de donner un exemple.</p><ul class="steps">${cles.slice(0, 8).map((x) => `<li>${esc(x)}</li>`).join("")}</ul>${n ? `<a class="small" href="#notion/${n.id}">Lire tout le cours ›</a>` : ""}</div>` : ""}
      <div class="card"><h2>2. 🗣️ Questions à lui poser</h2>${qs.length ? `<p class="small muted">Pose la question et les choix à voix haute. Touche ✓ ou ✗ selon sa réponse.</p>
        ${qs.map((q, i) => `<div style="padding:8px 0;border-bottom:1px solid rgba(127,127,127,.2)"><p><b>${i + 1}. ${esc(q.q)}</b></p><p class="small">${q.c.map((c, j) => `${LETTERS[j]}. ${esc(c)}`).join("<br>")}</p>
          <details class="small"><summary>Voir la réponse</summary><p class="msg-ok">${LETTERS[q.a]}. ${esc(q.c[q.a])}</p><p class="muted">${esc(q.e || "")}</p></details>
          <div class="row" style="margin-top:6px"><button class="btn small alt" style="flex:1" data-q="${i}" data-v="1">✓ Juste</button><button class="btn small alt" style="flex:1" data-q="${i}" data-v="0">✗ Faux</button></div></div>`).join("")}`
        : `<p class="small">Pas encore de QCM sur ce chapitre : demande-lui de réciter l'essentiel ci-dessus, puis passe à l'exercice.</p>`}</div>
      ${met ? `<div class="card"><h2>3. 🛠️ La méthode à vérifier</h2><p><b>${esc(met[0])}</b></p><ol class="steps">${met[1].map((x) => `<li>${esc(x)}</li>`).join("")}</ol></div>` : ""}
      ${f && f.c.pieges ? `<div class="card"><h2>⚠️ Pièges à surveiller</h2><ul class="steps">${f.c.pieges.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>` : ""}
      ${exo ? `<div class="card"><h2>4. ✏️ Exercice à lui donner</h2><p><b>${esc(exo[0])}</b></p><p class="small muted">Laisse-le chercher sur une feuille, puis compare avec le corrigé.</p><details><summary class="small">Corrigé (pour toi)</summary><ol class="steps">${exo[1].map((x) => `<li>${esc(x)}</li>`).join("")}</ol></details></div>` : ""}
      <div class="card"><h2>5. 🏁 Bilan de la séance</h2><p id="sscore" class="small muted">Réponses notées : 0/${qs.length}</p>
        <div class="row">${[["ok", "😀 Compris"], ["moyen", "😐 À revoir"], ["ko", "😟 Pas compris"]].map(([k, t]) => `<button class="btn alt small" style="flex:1" data-avis="${k}">${t}</button>`).join("")}</div><p class="small" id="smsg"></p></div>
      <a class="btn alt" href="#famille/enfant/${e.id}">Retour à la fiche de ${prenom(e)}</a>`;
    const score = () => { const v = Object.values(rep); document.getElementById("sscore").textContent = `Réponses notées : ${v.length}/${qs.length} · ${v.filter(Boolean).length} juste${v.filter(Boolean).length > 1 ? "s" : ""}`; };
    $view.querySelectorAll("[data-q]").forEach((x) => (x.onclick = () => {
      rep[x.dataset.q] = x.dataset.v === "1";
      $view.querySelectorAll(`[data-q="${x.dataset.q}"]`).forEach((y) => y.classList.toggle("on", y === x)); score();
    }));
    $view.querySelectorAll("[data-avis]").forEach((x) => (x.onclick = async () => {
      const v = Object.entries(rep), s = { d: today(), sid, ch, n: v.length, ok: v.filter(([, o]) => o).length, avis: x.dataset.avis };
      (e.seances = e.seances || []).push(s); e.seances = e.seances.slice(-120);
      // les réponses données à l'oral comptent aussi dans ses progrès (profil sur ce téléphone)
      if (e.type === "local") {
        let d = null; try { d = JSON.parse(localStorage.getItem("rev:" + e.id) || "null"); } catch (z) {}
        d = d || { level: e.level, stats: {}, sessions: [], days: [], daily: {} };
        v.forEach(([i, o]) => { const q = qs[+i], st = d.stats[q.id] || { ok: 0, ko: 0 }; st[o ? "ok" : "ko"]++; st.last = o; st.t = Date.now(); d.stats[q.id] = st; });
        if (v.length) { if (!d.days.includes(today())) d.days.push(today()); const j = (d.daily = d.daily || {})[today()] || { n: 0, ok: 0 }; j.n += s.n; j.ok += s.ok; d.daily[today()] = j; }
        try { localStorage.setItem("rev:" + e.id, JSON.stringify(d)); } catch (z) {}
      }
      enreg(); await publierMissions(e);
      $view.querySelectorAll("[data-avis]").forEach((y) => (y.disabled = true));
      const m = document.getElementById("smsg"); m.className = "msg-ok"; m.innerHTML = `Séance enregistrée ✓${x.dataset.avis !== "ok" ? ` Refais ce chapitre dans 2 ou 3 jours : <a href="#famille/mission/${e.id}">donner une mission</a>.` : " Bravo à vous deux !"}`;
    }));
  }

  async function viewSuivi(e) {
    const uid = Compte.user && Compte.user.uid;
    if (!uid) { $view.innerHTML = `<div class="card"><p>Connecte-toi pour demander un suivi.</p></div>`; return; }
    const id = `${uid}_${e.id}`, sv = (await Compte.lireSuivis().catch(() => [])).find((x) => x.id === id), t = T();
    const subs = subjectsOf(e.level);
    $view.innerHTML = `<h1>🎯 Suivi spécifique de ${prenom(e)}</h1>
      <div class="card"><p>L'équipe Révision regarde ses résultats dans l'appli et t'envoie un plan et des conseils ici. ${fcfa(t.suivi)} par enfant, à ajouter à ta formule dans <a href="#premium">Premium</a>.</p></div>
      <div class="card" style="gap:10px"><label class="small">Ton objectif pour ${prenom(e)}</label><textarea class="field" id="sobj" rows="3" maxlength="600" placeholder="Ex. passer de 8 à 12 de moyenne en maths avant le 2e trimestre">${esc((sv && sv.objectif) || "")}</textarea>
        <label class="small">Matières prioritaires</label><div>${subs.map((s) => `<label class="small" style="display:inline-flex;gap:4px;margin:3px 8px 3px 0"><input type="checkbox" value="${s.id}"${sv && (sv.matieres || []).includes(s.id) ? " checked" : ""}> ${esc(s.name)}</label>`).join("")}</div>
        <label class="small">Quand révise-t-il ? (jours, heures)</label><input class="field" id="sdispo" maxlength="200" value="${esc((sv && sv.dispo) || "")}" placeholder="Ex. lundi, mercredi et samedi, 18 h à 19 h">
        <label class="small">Ton numéro WhatsApp</label><input class="field" id="stel" maxlength="20" value="${esc((sv && sv.tel) || S.phone || "")}">
        <button class="btn" id="sok">${sv ? "Mettre à jour" : "Envoyer la demande"}</button><p class="small" id="smsg"></p></div>
      <a class="btn alt" href="#famille/enfant/${e.id}">Retour</a>`;
    document.getElementById("sok").onclick = async (ev) => {
      const objectif = document.getElementById("sobj").value.trim().slice(0, 600), m = document.getElementById("smsg");
      if (objectif.length < 5) { m.className = "msg-ko small"; m.textContent = "Écris l'objectif en quelques mots."; return; }
      ev.target.disabled = true;
      const d = await dataOf(e), rec = { objectif, matieres: [...$view.querySelectorAll("input[type=checkbox]:checked")].map((x) => x.value).slice(0, 20), dispo: document.getElementById("sdispo").value.trim().slice(0, 200), tel: document.getElementById("stel").value.trim().slice(0, 20), resume: resumeTexte(e, bilan(e, d)), level: e.level };
      try {
        if (sv) await Compte.majSuivi(id, rec);
        else await Compte.demanderSuivi(id, { ...rec, pnom: ((Compte.user && Compte.user.displayName) || "").slice(0, 60), enfant: e.nom.slice(0, 60) });
        e.suivi = true; e.resumeLe = today(); enreg(); go("famille/enfant/" + e.id);
      } catch (x) { ev.target.disabled = false; m.className = "msg-ko small"; m.textContent = "Envoi refusé (" + (x.code || x.message) + "). Réessaie plus tard."; }
    };
  }

  function viewModifier(e) {
    $view.innerHTML = `<h1>✏️ ${esc(e.nom)}</h1><div class="card" style="gap:10px"><input class="field" id="enom" maxlength="40" value="${esc(e.nom)}">
      ${e.type === "local" ? `<label class="small">Classe</label><select class="field" id="elvl">${DATA.levels.filter((l) => subjectsOf(l).length).map((l) => `<option${l === e.level ? " selected" : ""}>${esc(l)}</option>`).join("")}</select>` : `<p class="small muted">Sa classe se change dans son appli (elle est reprise ici automatiquement).</p>`}
      <button class="btn" id="eok">Enregistrer</button></div>
      <button class="btn alt" id="edel">🗑️ Retirer ${prenom(e)} de mon compte</button><a class="btn alt" href="#famille/enfant/${e.id}">Retour</a>`;
    document.getElementById("eok").onclick = () => {
      e.nom = document.getElementById("enom").value.trim().slice(0, 40) || e.nom;
      const l = document.getElementById("elvl");
      if (l && l.value !== e.level) { e.level = l.value; try { const d = JSON.parse(localStorage.getItem("rev:" + e.id) || "null"); if (d) { d.level = e.level; localStorage.setItem("rev:" + e.id, JSON.stringify(d)); } } catch (z) {} }
      enreg(); go("famille/enfant/" + e.id);
    };
    const del = document.getElementById("edel");
    del.onclick = () => {
      if (!del.dataset.sure) { del.dataset.sure = "1"; del.textContent = "Touche encore pour confirmer (ses missions et séances seront effacées)"; return; }
      F().enfants = F().enfants.filter((x) => x.id !== e.id); enreg(); go("famille");
    };
  }

  function viewPin(msg = "") {
    $view.innerHTML = `<h1>🔐 Code parent</h1><div class="card" style="gap:10px"><p>Avec un code parent, l'enfant qui révise sur ton téléphone ne peut pas revenir dans l'espace parent (missions, suivi) sans toi.</p>
      <input class="field" id="pin" type="password" inputmode="numeric" maxlength="4" placeholder="Nouveau code (4 chiffres)"><button class="btn" id="pok">Enregistrer le code</button>
      ${F().pin ? `<button class="btn alt" id="poff">Supprimer le code</button>` : ""}<p class="small">${esc(msg)}</p></div><a class="btn alt" href="#famille">Retour</a>`;
    document.getElementById("pok").onclick = async () => { const v = document.getElementById("pin").value.trim(); if (!/^\d{4}$/.test(v)) return viewPin("Le code doit faire 4 chiffres."); F().pin = await sha256("pin:" + v); enreg(); viewPin("Code enregistré ✓"); };
    const off = document.getElementById("poff"); if (off) off.onclick = () => { F().pin = null; enreg(); viewPin("Code supprimé."); };
  }

  function viewGuide() {
    $view.innerHTML = `<h1>📘 Guide du parent répétiteur</h1>
      <div class="card"><h2>Tu n'as pas besoin d'être enseignant</h2><p>Dans chaque séance, l'appli te montre l'essentiel du chapitre, les questions à poser avec les réponses et les explications, les pièges et un exercice corrigé. Ton rôle : faire travailler, écouter, encourager.</p></div>
      <div class="card"><h2>Une semaine type</h2><ul class="steps"><li>Lundi : donne 2 ou 3 missions (le chapitre du cours de la semaine).</li><li>Mercredi : une séance répétiteur de 20 minutes sur ce chapitre.</li><li>Samedi : regarde son suivi (jours actifs, réussite, chapitres à revoir) et refais une séance sur le plus faible.</li></ul></div>
      ${Object.entries({ primaire: "Primaire (CE1 au CM2)", college: "Collège (6e à 3e)", lycee: "Lycée (2nde à Terminale)" }).map(([k, t]) => `<div class="card"><h2>${t}</h2><ul class="steps">${CONSEILS[k].map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>`).join("")}
      <div class="card"><h2>Plusieurs enfants</h2><p>Chaque enfant a sa fiche, ses missions et son suivi. Sur un seul téléphone, passe d'un profil à l'autre ; un enfant qui a son propre téléphone se relie à toi avec un code.</p></div>
      <a class="btn alt" href="#famille">Retour</a>`;
  }

  // ---------- Côté enfant : relier son compte à celui de son parent
  function viewRelier(code = "", err = "", ok = "") {
    if (estParent() && !S.actif) { $view.innerHTML = `<div class="card"><h1>Relier un enfant</h1><p>Ce code se tape sur le téléphone de l'enfant, dans son propre compte Révision (pas dans le tien).</p><a class="btn alt" href="#famille">Retour</a></div>`; return; }
    if (S.actif) { $view.innerHTML = `<div class="card"><p>Ce profil est déjà sur le téléphone du parent : rien à relier.</p><a class="btn alt" href="#accueil">Retour</a></div>`; return; }
    const lies = S.liens || [];
    $view.innerHTML = `<h1>👨‍👩 Mon parent</h1><div class="card" style="gap:10px"><p>Ton parent (ou ton répétiteur) te donne un code de 8 caractères. Une fois relié, il voit tes progrès et te donne des missions. Il ne peut pas répondre à ta place.</p>
      <input class="code" id="lcode" maxlength="8" placeholder="CODE" value="${esc((code || "").toUpperCase())}" autocomplete="off"><button class="btn" id="lok">Relier mon compte</button>
      ${err ? `<p class="msg-ko small">${esc(err)}</p>` : ""}${ok ? `<p class="msg-ok">${esc(ok)}</p>` : ""}</div>
      ${lies.length ? `<div class="card"><h2>Relié à</h2>${lies.map((l) => `<p>👤 ${esc(l.pnom || "un parent")}</p>`).join("")}</div>` : ""}
      <a class="btn alt" href="#accueil">Retour à l'accueil</a>`;
    document.getElementById("lok").onclick = async (ev) => {
      const c = document.getElementById("lcode").value.trim().toUpperCase();
      if (!/^[A-Z0-9]{8}$/.test(c)) return viewRelier(c, "Le code fait 8 caractères (lettres et chiffres).");
      if (!Compte.user) return viewRelier(c, "Connecte-toi d'abord à ton compte.");
      ev.target.disabled = true;
      try {
        const l = await Compte.accepterLien(c, (Compte.user.displayName || myName() || "").slice(0, 60), S.level || "");
        S.liens = [...(S.liens || []).filter((x) => x.parent !== l.parent), { parent: l.parent, pnom: l.pnom }]; if (!S.mode) S.mode = "eleve"; store.save();
        viewRelier("", "", `C'est fait : ${l.pnom || "ton parent"} suit maintenant tes progrès. 👍`);
      } catch (x) { viewRelier(c, x.msg || "La liaison n'a pas abouti (" + (x.code || x.message) + ")."); }
    };
  }

  // ---------- Premium en mode parent : formule calculée selon le nombre d'enfants et les suivis spécifiques
  let dedans = false, avecSuivi = null;
  globalThis.premiumFamille = (reason, pay) => {
    if (!estParent() || dedans) return false;
    const t = T(), nb = Math.max(1, F().enfants.length);
    if (avecSuivi === null) avecSuivi = F().enfants.filter((e) => e.suivi).length;
    const total = t.parent + (nb - 1) * t.enfant_sup + avecSuivi * t.suivi;
    globalThis.payExtra = () => ({ formule: avecSuivi ? "suivi" : "parent", montant: total, enfants: nb });
    const prix = CFG.price_fcfa; CFG.price_fcfa = total; dedans = true;
    try { viewPremium(reason, pay); } finally { CFG.price_fcfa = prix; dedans = false; }
    $view.insertAdjacentHTML("afterbegin", `<h1>👨‍👩‍👧 Formule parent répétiteur</h1><div class="card"><h2>Les formules${CFG.promo ? ` <span class="small">🔥 −${CFG.promo.pct} %</span>` : ""}</h2>
      <ul class="steps"><li>🎒 Élève seul : <b>${fcfa(t.eleve)}</b></li><li>👨‍👩‍👧 Parent répétiteur, 1 enfant (missions, séances, suivi) : <b>${fcfa(t.parent)}</b></li><li>➕ Chaque enfant en plus : <b>${fcfa(t.enfant_sup)}</b></li><li>🎯 Suivi spécifique par la plateforme : <b>${fcfa(t.suivi)}</b> par enfant</li></ul>
      ${S.premium ? "" : `<p>Ta famille : <b>${nb} enfant${nb > 1 ? "s" : ""}</b>. Suivis spécifiques : <select id="nsuivi">${[...Array(nb + 1)].map((_, i) => `<option${i === avecSuivi ? " selected" : ""}>${i}</option>`).join("")}</select></p><p class="count">Total : ${fcfa(total)}</p><p class="small muted">Payé une fois, valable jusqu'aux examens, pour tous les enfants de ton compte (ceux reliés avec leur propre compte aussi).</p>`}</div>`);
    const h = $view.querySelectorAll("h1")[1]; if (h) h.remove();
    const sel = document.getElementById("nsuivi"); if (sel) sel.onchange = () => { avecSuivi = +sel.value; viewPremium(reason, pay); };
    return true;
  };

  ROUTES.famille = viewFamille;
})();
