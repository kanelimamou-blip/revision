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
    return { phone: doc.phone || "", suspended: !!doc.suspended, created: first && first < created ? first : created, premium: !!doc.premium, premiumAt: doc.premiumAt && doc.premiumAt.toDate ? doc.premiumAt.toDate().getTime() : 0, data: doc.data || {}, name: user.displayName || "", email: user.email || "" };
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
    db.collection("users").doc(user.uid).update({ data }).catch((e) => logError("Sauvegarde des progrès refusée : " + (e.code || e.message)));
  }
  function save(state) {
    if (!user || !db) return;
    pending = state;
    if (!timer) timer = setTimeout(flush, 60000);
  }
  document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") flush(); });

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
    return snap.docs.map((d) => { const x = d.data(); return { uid: d.id, name: x.name || "", email: x.email || "", created: ts(x.created), lastSeen: ts(x.lastSeen), premium: !!x.premium, code: x.code || "", phone: x.phone || telOf(x.email), avis: x.avis || [], suspended: !!x.suspended, level: (x.data || {}).level || "" }; });
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
  const adminSuspend = (uid, on) => db.collection("users").doc(uid).update({ suspended: on });
  async function adminPays() {
    const snap = await db.collection("paiements").where("statut", "==", "attente").limit(200).get();
    return snap.docs.map((d) => ({ ...d.data(), uid: d.id, at: ts(d.data().at) })).sort((a, b) => (a.at || 0) - (b.at || 0));
  }
  function adminValidate(uid) {
    const b = db.batch(), now = firebase.firestore.FieldValue.serverTimestamp();
    b.update(db.collection("users").doc(uid), { premium: true, premiumAt: now });
    b.update(db.collection("paiements").doc(uid), { statut: "valide", fin: now });
    return b.commit();
  }
  const adminSetPremium = (uid) => db.collection("users").doc(uid).update({ premium: true, premiumAt: firebase.firestore.FieldValue.serverTimestamp() });
  // pour l'admin : nombre de paiements en attente, suivi en direct
  const watchPays = (cb) => db.collection("paiements").where("statut", "==", "attente").limit(200).onSnapshot((q) => cb(q.size), () => {});
  const adminRefuse = (uid, motif) => db.collection("paiements").doc(uid).update({ statut: "refuse", motif: String(motif || "").slice(0, 200), fin: firebase.firestore.FieldValue.serverTimestamp() });
  const adminClearErrors = async (ids) => { const b = db.batch(); ids.slice(0, 450).forEach((id) => b.delete(db.collection("errors").doc(id))); await b.commit(); };

  return { enabled, start, logError, isAdmin, declarePay, myPay, watchPremium, adminPays, adminValidate, adminRefuse, adminSetPremium, watchPays, adminUsers, adminErrors, adminDevices, adminSuspend, adminClearErrors, postScore, listenScores, signIn, signInEmail, signInTel, linkTel, normTel, avis, enablePush, resetPassword, signOut, claim, save, get user() { return user; }, get ready() { return ready; } };
})();
