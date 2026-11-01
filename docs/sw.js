const CACHE = "revision-v95";
const SHELL = ["./", "index.html", "app.css", "app.js", "compte.js", "generateurs.js", "generateurs_plus.js", "generateurs_lettres.js", "generateurs_modeles.js", "exos_gen.js", "generateurs_vague2.js", "generateurs_vague3.js", "generateurs_vague4.js", "generateurs_vague5.js", "generateurs_vague6.js", "parcours.js", "legal.js", "accord.js", "assistant.js", "agenda.js", "edt-import.js", "trajectoire.js", "notes.js", "aide.js", "vie.js", "apprendre.js", "admin.js", "rappels.js", "installer.js", "sources.js", "manifest.webmanifest", "data/questions.json", "data/config.json", "icons/icon-192.png", "icons/qr.svg", "icons/qr.png"];
self.addEventListener("install", (e) => { e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL))); self.skipWaiting(); });
self.addEventListener("activate", (e) => { e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k.startsWith("revision-") && k !== CACHE).map((k) => caches.delete(k))))); self.clients.claim(); });
// Réseau d'abord (dernières questions), cache si hors ligne : l'appli marche sans connexion.
// En économie de données (drapeau « eco » dans le cache rprefs), tout est lu dans le cache ; « ?fresh » force la mise à jour.
const keyOf = (req) => { const u = new URL(req.url); return u.origin + u.pathname; };
// « no-cache » : on redemande toujours au serveur s'il y a du nouveau, sinon une mise à jour peut mettre 10 min à arriver
const fresh = (req) => (req.mode === "navigate" ? fetch(req.url, { cache: "no-cache", credentials: "same-origin" }) : fetch(req, { cache: "no-cache" }));
const net = (req) => fresh(req).then((r) => { if (r.ok) { const copy = r.clone(); caches.open(CACHE).then((c) => c.put(keyOf(req), copy)); } return r; }).catch(() => caches.match(keyOf(req)));
const eco = () => caches.open("rprefs").then((c) => c.match("eco")).then((r) => (r ? r.text() : "0")).catch(() => "0");
// Rappels envoyés par Firebase Cloud Messaging (pause de midi, après l'école) : affichés même appli fermée
self.addEventListener("push", (e) => {
  let m = {}; try { const j = e.data ? e.data.json() : {}; m = { ...(j.notification || {}), ...(j.data || {}) }; } catch (err) {}
  e.waitUntil(self.registration.showNotification(m.title || "Révision", { body: m.body || "5 minutes pour réviser ?", icon: "icons/icon-192.png", badge: "icons/icon-192.png", tag: m.tag || "rappel", data: { link: m.link || "./#accueil" } }));
});
self.addEventListener("notificationclick", (e) => {
  e.notification.close();
  const url = new URL(e.notification.data && e.notification.data.link || "./#accueil", self.registration.scope).href;
  e.waitUntil(self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((cs) => { const c = cs.find((x) => x.url.startsWith(self.registration.scope)); return c ? c.navigate(url).then((w) => (w || c).focus()) : self.clients.openWindow(url); }));
});
self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  const u = new URL(e.request.url);
  // polices : gardées une fois pour toutes
  if (/^fonts\.(googleapis|gstatic)\.com$/.test(u.hostname)) { e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request).then((res) => { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(e.request, copy)); return res; }))); return; }
  if (u.origin !== self.location.origin) return;
  e.respondWith(eco().then((on) => (on === "1" && !u.search.includes("fresh") ? caches.match(keyOf(e.request)).then((r) => r || net(e.request)) : net(e.request))));
});
