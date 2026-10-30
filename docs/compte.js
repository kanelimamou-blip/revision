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
    return { suspended: !!doc.suspended, created: doc.created ? doc.created.toDate() : new Date(), premium: !!doc.premium, data: doc.data || {}, name: user.displayName || "", email: user.email || "" };
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
    return snap.docs.map((d) => { const x = d.data(); return { uid: d.id, name: x.name || "", email: x.email || "", created: ts(x.created), lastSeen: ts(x.lastSeen), premium: !!x.premium, suspended: !!x.suspended, level: (x.data || {}).level || "" }; });
  }
  async function adminErrors() {
    const snap = await db.collection("errors").orderBy("at", "desc").limit(200).get();
    return snap.docs.map((d) => ({ id: d.id, ...d.data(), at: ts(d.data().at) }));
  }
  const adminSuspend = (uid, on) => db.collection("users").doc(uid).update({ suspended: on });
  const adminClearErrors = async (ids) => { const b = db.batch(); ids.slice(0, 450).forEach((id) => b.delete(db.collection("errors").doc(id))); await b.commit(); };

  return { enabled, start, logError, isAdmin, adminUsers, adminErrors, adminSuspend, adminClearErrors, postScore, listenScores, signIn, signInEmail, resetPassword, signOut, claim, save, get user() { return user; }, get ready() { return ready; } };
})();
