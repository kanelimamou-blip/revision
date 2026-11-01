"use strict";
// Comptes élèves : connexion Google (Firebase Auth), essai et premium enregistrés en ligne (Firestore).
// Sans configuration Firebase, l'appli garde le fonctionnement local (Compte.enabled = false).
// Configuration publique du projet Firebase « Revision » (pas secrète : la sécurité vient des règles Firestore)
const FIREBASE_CONFIG = {
  apiKey: "AIzaSyBVN2IYDi7Sz5z2FdJox4pJbsIUdyz5Bis",
  authDomain: "revision-981b3.firebaseapp.com",
  projectId: "revision-981b3",
  storageBucket: "revision-981b3.firebasestorage.app",
  messagingSenderId: "565000904373",
  appId: "1:565000904373:web:c7026a0072470aeb0728fc",
};

const Compte = (() => {
  const SDK = "https://www.gstatic.com/firebasejs/10.12.2/";
  const enabled = !!FIREBASE_CONFIG;
  let auth = null, db = null, user = null, doc = null, timer = null, ready = false;

  const load = (src) => new Promise((ok, ko) => { const s = document.createElement("script"); s.src = src; s.onload = ok; s.onerror = ko; document.head.appendChild(s); });

  // Résout avec le profil en ligne ({ created, premium, data }) ou null si l'élève n'est pas connecté
  async function start() {
    if (!enabled) return null;
    await load(SDK + "firebase-app-compat.js");
    await Promise.all([load(SDK + "firebase-auth-compat.js"), load(SDK + "firebase-firestore-compat.js")]);
    firebase.initializeApp(FIREBASE_CONFIG);
    auth = firebase.auth(); db = firebase.firestore();
    await auth.getRedirectResult().catch(() => null);
    user = await new Promise((ok) => { const off = auth.onAuthStateChanged((u) => { off(); ok(u); }); });
    ready = true;
    return user ? profile() : null;
  }

  async function profile() {
    const ref = db.collection("users").doc(user.uid);
    let snap = await ref.get();
    if (!snap.exists) {
      // la date de création vient du serveur : effacer le téléphone ne relance pas l'essai
      await ref.set({ created: firebase.firestore.FieldValue.serverTimestamp(), premium: false, name: user.displayName || "", data: {} });
      snap = await ref.get();
    }
    doc = snap.data();
    // dernière activité, au plus une écriture par 12 h (reste dans le quota gratuit)
    const seen = doc.lastSeen && doc.lastSeen.toDate ? doc.lastSeen.toDate() : null;
    if (!seen || Date.now() - seen.getTime() > 12 * 3600e3)
      ref.update({ lastSeen: firebase.firestore.FieldValue.serverTimestamp(), name: user.displayName || doc.name || "", email: user.email || "" }).catch((e) => logError("Mise à jour du profil refusée : " + (e.code || e.message)));
    // un seul essai gratuit par téléphone : un nouveau compte sur le même téléphone reprend la date du premier
    const created = doc.created ? doc.created.toDate() : new Date(), first = await device();
    // numéro de téléphone : celui du compte (connexion par numéro) ou celui ajouté par un ancien compte
    if (!doc.phone && telOf(user.email)) { doc.phone = telOf(user.email); ref.update({ phone: doc.phone }).catch(() => {}); }
    return { mode: doc.mode || "", formule: doc.formule || "", famille: doc.famille || null, phone: doc.phone || "", suspended: !!doc.suspended, created: first && first < created ? first : created, premium: !!doc.premium, premiumAt: doc.premiumAt && doc.premiumAt.toDate ? doc.premiumAt.toDate().getTime() : 0, data: doc.data || {}, name: user.displayName || "", email: user.email || "" };
  }

  // Identifiant secret du téléphone, tiré au hasard au premier lancement (gardé aussi dans le cache de l'appli)
  async function deviceId() {
    let id = null;
    try { id = localStorage.getItem("rdev"); } catch (e) {}
    const c = await caches.open("rprefs").catch(() => null);
    if (!id && c) id = await c.match("dev").then((r) => (r ? r.text() : null)).catch(() => null);
    if (!id || !/^[a-z0-9]{20}$/.test(id)) id = [...crypto.getRandomValues(new Uint8Array(20))].map((b) => "abcdefghijklmnopqrstuvwxyz0123456789"[b % 36]).join("");
    try { localStorage.setItem("rdev", id); } catch (e) {}
    if (c) c.put("dev", new Response(id)).catch(() => {});
    return id;
  }
  // Rattache le compte au téléphone ; renvoie la date du premier compte ouvert sur ce téléphone
  async function device() {
    try {
      const ref = db.collection("devices").doc(await deviceId());
      const snap = await ref.get();
      if (!snap.exists) { await ref.set({ first: firebase.firestore.FieldValue.serverTimestamp(), uids: [user.uid] }); return null; }
      const d = snap.data();
      if (!(d.uids || []).includes(user.uid)) await ref.update({ uids: firebase.firestore.FieldValue.arrayUnion(user.uid) });
      return d.first && d.first.toDate ? d.first.toDate() : null;
    } catch (e) { return null; }
  }

  async function signIn() {
    const provider = new firebase.auth.GoogleAuthProvider();
    try { await auth.signInWithPopup(provider); }
    catch (e) {
      if (/popup|operation-not-supported/.test(e.code || "")) return auth.signInWithRedirect(provider);
      throw e;
    }
    user = auth.currentUser;
    return profile();
  }

  // Connexion par numéro de téléphone et code à 6 chiffres : sous le capot, un compte e-mail/mot de passe
  // dont l'adresse est fabriquée à partir du numéro (aucun e-mail n'est envoyé, rien à configurer).
  const TEL = "@tel.revision-sn.app";
  const telOf = (mail) => (mail || "").endsWith(TEL) ? mail.slice(0, -TEL.length) : "";
  // numéro sénégalais à 9 chiffres, avec ou sans +221 ; null s'il est invalide
  function normTel(t) {
    let d = String(t || "").replace(/\D/g, "");
    if (d.length > 9 && d.startsWith("00221")) d = d.slice(5); else if (d.length > 9 && d.startsWith("221")) d = d.slice(3);
    return /^[37]\d{8}$/.test(d) ? d : null;
  }
  async function signInTel(name, tel, code, create) {
    const r = create ? await auth.createUserWithEmailAndPassword(tel + TEL, code) : await auth.signInWithEmailAndPassword(tel + TEL, code);
    user = r.user;
    if (create && name) await user.updateProfile({ displayName: name }).catch(() => {});
    return profile();
  }
  // Ancien compte (Google ou e-mail) : on lui ajoute le numéro et le code, il garde ses progrès et son premium
  async function linkTel(tel, code) {
    const hasPass = user.providerData.some((p) => p.providerId === "password");
    if (!hasPass) await user.linkWithCredential(firebase.auth.EmailAuthProvider.credential(tel + TEL, code));
    await db.collection("users").doc(user.uid).update({ phone: tel });
    return hasPass ? "email" : "tel";
  }

  // Connexion par e-mail et mot de passe (utile sur iPhone si la fenêtre Google ne s'ouvre pas)
  async function signInEmail(email, pass, create) {
    const r = create ? await auth.createUserWithEmailAndPassword(email, pass) : await auth.signInWithEmailAndPassword(email, pass);
    user = r.user;
    return profile();
  }
  const resetPassword = (email) => auth.sendPasswordResetEmail(email);

  async function signOut() { if (auth) await auth.signOut(); user = null; }

  // Un code premium ne sert qu'une fois : la règle Firestore refuse de recréer claims/{code}
  async function claim(code) {
    const batch = db.batch();
    batch.set(db.collection("claims").doc(code), { uid: user.uid, at: firebase.firestore.FieldValue.serverTimestamp() });
    batch.update(db.collection("users").doc(user.uid), { premium: true, code });
    await batch.commit();
  }

  // Paiement déclaré dans l'appli : l'élève envoie la capture, l'admin valide, le premium s'active tout seul.
  // La capture est réduite sur le téléphone et gardée dans Firestore (pas besoin de stockage payant).
  async function declarePay(rec) {
    await db.collection("paiements").doc(user.uid).set({ ...rec, uid: user.uid, statut: "attente", at: firebase.firestore.FieldValue.serverTimestamp() });
  }
  async function myPay() {
    const s = await db.collection("paiements").doc(user.uid).get().catch(() => null);
    return s && s.exists ? { ...s.data(), at: ts(s.data().at) } : null;
  }
  // suit le compte en direct : appelle cb(premium, paiement) dès que l'admin valide ou refuse
  function watchPremium(cb) {
    if (!user || !db) return () => {};
    const a = db.collection("users").doc(user.uid).onSnapshot((d) => d.exists && cb(!!d.data().premium, null), () => {});
    const b = db.collection("paiements").doc(user.uid).onSnapshot((d) => d.exists && cb(null, { ...d.data(), at: ts(d.data().at) }), () => {});
    return () => { a(); b(); };
  }

  // Réponses aux petites questions de l'appli (pause de midi, après l'école) : gardées dans le compte, lues par l'admin
  const avis = (rec) => (user && db ? db.collection("users").doc(user.uid).update({ avis: firebase.firestore.FieldValue.arrayUnion(rec) }) : Promise.resolve());

  // Notifications : jeton Firebase Cloud Messaging lié au service worker de l'appli, gardé dans le compte (champ push).
  // Un robot GitHub (rappels.yml) envoie les rappels à 13 h 15 et 17 h 15.
  async function enablePush(vapidKey) {
    if (!user || !db) throw new Error("hors ligne");
    if (!firebase.messaging) await load(SDK + "firebase-messaging-compat.js");
    const reg = await navigator.serviceWorker.ready;
    const token = await firebase.messaging().getToken({ vapidKey, serviceWorkerRegistration: reg });
    if (!token) throw new Error("pas de jeton");
    await db.collection("users").doc(user.uid).update({ push: { t: token, at: firebase.firestore.FieldValue.serverTimestamp() } });
    return token;
  }

  // Sauvegarde des progrès : au plus une écriture par minute, et tout de suite quand l'élève quitte l'appli.
  // Cela garde 10 000 élèves dans le quota gratuit de Firestore (20 000 écritures par jour).
  let pending = null;
  function flush() {
    if (!pending || !user || !db) return;
    const state = pending; pending = null; clearTimeout(timer); timer = null;
    const last = (o, n) => Object.fromEntries(Object.entries(o || {}).sort().slice(-n));
    const data = { level: state.level || null, stats: state.stats, sessions: state.sessions.slice(-50), days: state.days.slice(-120), daily: last(state.daily, 60), challenges: last(state.challenges, 60), done: last(state.done, 14), edt: state.edt || {}, todo: (state.todo || []).slice(-100) };
    // mode parent : les progrès d'un enfant qui révise sur le téléphone du parent vont dans sa propre fiche
    const ref = db.collection("users").doc(user.uid);
    (state.actif ? ref.collection("enfants").doc(state.actif).set({ data, level: data.level, at: SRV() }, { merge: true }) : ref.update({ data }))
      .catch((e) => logError("Sauvegarde des progrès refusée : " + (e.code || e.message)));
  }
  function save(state) {
    if (!user || !db) return;
    pending = state;
    if (!timer) timer = setTimeout(flush, 60000);
  }
  document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") flush(); });

  // ---------- Mode parent répétiteur : enfants, missions, suivi spécifique, tarifs
  // fiche famille et mode gardés dans le compte du parent (petits objets, une écriture à chaque changement)
  const setFamille = (mode, famille) => (user && db ? db.collection("users").doc(user.uid).update({ mode, famille: JSON.parse(JSON.stringify(famille || null)) }).catch((e) => logError("Famille non enregistrée : " + (e.code || e.message))) : Promise.resolve());
  async function lireEnfant(eid) { if (!user || !db) return null; const d = await db.collection("users").doc(user.uid).collection("enfants").doc(eid).get().catch(() => null); return d && d.exists ? d.data() : null; }
  // enfant qui a son propre compte : le parent lit sa fiche (règle : le parent figure dans « parents »)
  async function lireEleve(uid) { const d = await db.collection("users").doc(uid).get(); if (!d.exists) return null; const x = d.data(); return { uid, name: x.name || "", phone: x.phone || telOf(x.email), lastSeen: ts(x.lastSeen), premium: !!x.premium, data: x.data || {} }; }
  // code de liaison : le parent le crée, l'enfant le tape dans son appli, le parent retrouve ainsi le compte de l'enfant
  const liens = () => db.collection("liens");
  const creerLien = (code, pnom) => liens().doc(code).set({ parent: user.uid, pnom: String(pnom || "").slice(0, 60), at: SRV() });
  async function lireLien(code) { const d = await liens().doc(code).get(); return d.exists ? d.data() : null; }
  async function accepterLien(code, enom, level) {
    const l = await lireLien(code);
    if (!l) throw { msg: "Code inconnu. Vérifie les 8 caractères donnés par ton parent." };
    if (l.enfant && l.enfant !== user.uid) throw { msg: "Ce code a déjà servi. Demande un nouveau code à ton parent." };
    if (l.parent === user.uid) throw { msg: "C'est ton propre code : il faut le taper sur le téléphone de l'enfant." };
    const b = db.batch();
    b.update(db.collection("users").doc(user.uid), { parents: firebase.firestore.FieldValue.arrayUnion(l.parent) });
    b.update(liens().doc(code), { enfant: user.uid, enom: String(enom || "").slice(0, 60), level: String(level || "").slice(0, 30), okAt: SRV() });
    await b.commit();
    return l;
  }
  const retirerParent = (puid) => db.collection("users").doc(user.uid).update({ parents: firebase.firestore.FieldValue.arrayRemove(puid) });
  // missions données par le parent à un enfant qui a son propre compte
  async function lireMissions(uid) { if (!db) return null; const d = await db.collection("missions").doc(uid).get().catch(() => null); return d && d.exists ? d.data() : null; }
  const ecrireMissions = (uid, rec) => db.collection("missions").doc(uid).set({ ...JSON.parse(JSON.stringify(rec)), at: SRV() }, { merge: true });
  // suivi spécifique demandé par le parent : l'équipe (admin) répond par des conseils
  const suivis = () => db.collection("suivis");
  const demanderSuivi = (id, rec) => suivis().doc(id).set({ ...rec, parent: user.uid, statut: "attente", conseils: [], at: SRV() });
  const majSuivi = (id, rec) => suivis().doc(id).update({ ...rec, maj: SRV() });
  async function lireSuivis() { if (!user || !db) return []; const q = await suivis().where("parent", "==", user.uid).limit(20).get().catch(() => null); return q ? q.docs.map((d) => ({ id: d.id, ...d.data(), at: ts(d.data().at) })) : []; }
  async function adminSuivis() { const q = await suivis().limit(2000).get(); return q.docs.map((d) => ({ id: d.id, ...d.data(), at: ts(d.data().at) })); }
  const adminConseil = (id, texte, statut) => suivis().doc(id).update(texte ? { conseils: firebase.firestore.FieldValue.arrayUnion({ t: String(texte).slice(0, 1500), at: Date.now() }), statut } : { statut });
  async function adminEnfants(uid) { const q = await db.collection("users").doc(uid).collection("enfants").limit(20).get(); return q.docs.map((d) => ({ id: d.id, ...d.data() })); }
  // tarifs modulables : réglés par l'admin dans l'appli (config/tarifs), lus par tous
  async function getTarifs() { if (!db) return null; const d = await db.collection("config").doc("tarifs").get().catch(() => null); return d && d.exists ? d.data() : null; }
  const setTarifs = (rec) => db.collection("config").doc("tarifs").set(rec);

  // Session de groupe : chaque élève publie sa note, tout le groupe voit le classement se remplir en direct
  function postScore(code, rec) {
    if (!user || !db) return Promise.reject(new Error("hors ligne"));
    return db.collection("sessions").doc(code).collection("scores").doc(user.uid)
      .set({ ...rec, at: firebase.firestore.FieldValue.serverTimestamp() });
  }
  function listenScores(code, cb, err) {
    if (!user || !db) return () => {};
    return db.collection("sessions").doc(code).collection("scores").limit(50)
      .onSnapshot((snap) => cb(snap.docs.map((d) => ({ ...d.data(), me: d.id === user.uid }))), err);
  }

  // Journal des erreurs : au plus 5 envois par session, sans doublon ; lisible seulement par l'admin
  const sent = new Set();
  function logError(msg) {
    msg = String(msg || "Erreur inconnue").slice(0, 500);
    if (!db || sent.size >= 5 || sent.has(msg)) return;
    sent.add(msg);
    let level = ""; try { level = (JSON.parse(localStorage.getItem("rev") || "{}").level || "").slice(0, 20); } catch (e) {}
    db.collection("errors").add({ uid: user ? user.uid : null, email: user ? (user.email || "").slice(0, 100) : "", page: (location.hash || "#accueil").slice(0, 100), msg, ua: navigator.userAgent.slice(0, 200), level, at: firebase.firestore.FieldValue.serverTimestamp() }).catch(() => {});
  }
  window.addEventListener("error", (e) => logError(`${e.message || "Erreur"} (${(e.filename || "").split("/").pop()}:${e.lineno || 0})`));
  window.addEventListener("unhandledrejection", (e) => logError("Promesse rejetée : " + ((e.reason && (e.reason.code || e.reason.message)) || e.reason)));

  // Espace propriétaire : seul ce compte Google y a accès (même adresse dans les règles Firestore)
  const ADMIN_EMAIL = "kanelimamou@gmail.com";
  const isAdmin = () => !!user && user.email === ADMIN_EMAIL && user.emailVerified;
  const ts = (v) => (v && v.toDate ? v.toDate() : null);
  async function adminUsers() {
    const snap = await db.collection("users").limit(5000).get();
    return snap.docs.map((d) => { const x = d.data(); return { uid: d.id, name: x.name || "", email: x.email || "", created: ts(x.created), lastSeen: ts(x.lastSeen), premium: !!x.premium, code: x.code || "", phone: x.phone || telOf(x.email), mode: x.mode || "", formule: x.formule || "", famille: x.famille || null, parents: x.parents || [], avis: x.avis || [], suspended: !!x.suspended, level: (x.data || {}).level || "" }; });
  }
  async function adminErrors() {
    const snap = await db.collection("errors").orderBy("at", "desc").limit(200).get();
    return snap.docs.map((d) => ({ id: d.id, ...d.data(), at: ts(d.data().at) }));
  }
  // téléphones partagés : {uid: [autres uid du même téléphone]}
  async function adminDevices() {
    const snap = await db.collection("devices").limit(5000).get(), out = {};
    snap.docs.forEach((d) => { const u = d.data().uids || []; if (u.length > 1) u.forEach((x) => { out[x] = [...new Set([...(out[x] || []), ...u.filter((y) => y !== x)])]; }); });
    return out;
  }
  const adminSetMode = (uid, mode) => db.collection("users").doc(uid).update({ mode });
  const adminSuspend = (uid, on) => db.collection("users").doc(uid).update({ suspended: on });
  async function adminPays() {
    const snap = await db.collection("paiements").where("statut", "==", "attente").limit(200).get();
    return snap.docs.map((d) => ({ ...d.data(), uid: d.id, at: ts(d.data().at) })).sort((a, b) => (a.at || 0) - (b.at || 0));
  }
  // la vue du client suit la formule payée : élève seul → vue élève ; parent (avec ou sans suivi) → vue parent
  function adminValidate(uid, formule = "eleve") {
    const b = db.batch(), now = firebase.firestore.FieldValue.serverTimestamp();
    b.update(db.collection("users").doc(uid), { premium: true, premiumAt: now, formule, mode: formule === "eleve" ? "eleve" : "parent" });
    b.update(db.collection("paiements").doc(uid), { statut: "valide", fin: now });
    return b.commit();
  }
  const adminSetPremium = (uid) => db.collection("users").doc(uid).update({ premium: true, premiumAt: firebase.firestore.FieldValue.serverTimestamp() });
  // pour l'admin : nombre de paiements en attente, suivi en direct
  const watchPays = (cb) => db.collection("paiements").where("statut", "==", "attente").limit(200).onSnapshot((q) => cb(q.size), () => {});
  const adminRefuse = (uid, motif) => db.collection("paiements").doc(uid).update({ statut: "refuse", motif: String(motif || "").slice(0, 200), fin: firebase.firestore.FieldValue.serverTimestamp() });
  // Registre des ventes (trace de chaque paiement reçu) et fiche société, gérés par l'admin
  async function adminVentes() { const snap = await db.collection("ventes").limit(10000).get(); return snap.docs.filter((d) => d.id !== "_societe").map((d) => ({ id: d.id, ...d.data(), at: ts(d.data().at) || (d.data().ms ? new Date(d.data().ms) : null) })); }
  const adminAddVente = (id, rec) => db.collection("ventes").doc(id).set({ ...rec, enreg: SRV() }, { merge: true });
  const adminDelVente = (id) => db.collection("ventes").doc(id).delete();
  // une seule fois, pour reprendre les paiements validés avant le registre (télécharge aussi les captures)
  async function adminPaysValides() { const snap = await db.collection("paiements").where("statut", "==", "valide").limit(2000).get(); return snap.docs.map((d) => { const x = d.data(); return { uid: d.id, name: x.name || "", phone: x.phone || "", level: x.level || "", via: x.via || "", at: ts(x.fin) || ts(x.at) }; }); }
  async function getSociete() { if (!db) return null; const d = await db.collection("config").doc("societe").get().catch(() => null); return d && d.exists ? d.data() : null; }
  // fiche privée (admin seul) ; elle ne sera copiée dans config/societe (public) que lorsqu'Est décidera de publier ses mentions
  async function getSocietePrivee() { const d = await db.collection("ventes").doc("_societe").get(); return d.exists ? d.data() : null; }
  const setSociete = (rec) => db.collection("ventes").doc("_societe").set(rec);
  // Accord du parent (#accord/<jeton>) : l'élève crée la demande, le parent l'accepte sans compte, l'admin garde la trace
  const accords = () => db.collection("accords");
  const SRV = () => firebase.firestore.FieldValue.serverTimestamp();
  async function demanderAccord(token, rec) { await accords().doc(token).set({ ...rec, uid: user.uid, at: SRV() }); }
  async function lireAccord(token) { if (!db || !token) return null; const d = await accords().doc(token).get(); return d.exists ? { ...d.data(), at: ts(d.data().at), okAt: ts(d.data().okAt) } : null; }
  const donnerAccord = (token, rec) => accords().doc(token).update({ ...rec, statut: "ok", okAt: SRV() });
  async function adminAccords() { const snap = await accords().limit(5000).get(); return snap.docs.map((d) => ({ id: d.id, ...d.data(), at: ts(d.data().at), okAt: ts(d.data().okAt) })); }
  const adminClearErrors = async (ids) => { const b = db.batch(); ids.slice(0, 450).forEach((id) => b.delete(db.collection("errors").doc(id))); await b.commit(); };

  return { enabled, start, flush, setFamille, lireEnfant, lireEleve, creerLien, lireLien, accepterLien, retirerParent, lireMissions, ecrireMissions, demanderSuivi, majSuivi, lireSuivis, adminSuivis, adminConseil, adminEnfants, getTarifs, setTarifs, adminVentes, adminAddVente, adminDelVente, adminPaysValides, getSociete, getSocietePrivee, setSociete, demanderAccord, lireAccord, donnerAccord, adminAccords, logError, isAdmin, declarePay, myPay, watchPremium, adminPays, adminValidate, adminRefuse, adminSetPremium, watchPays, adminUsers, adminErrors, adminDevices, adminSuspend, adminSetMode, adminClearErrors, postScore, listenScores, signIn, signInEmail, signInTel, linkTel, normTel, avis, enablePush, resetPassword, signOut, claim, save, get user() { return user; }, get ready() { return ready; } };
})();
