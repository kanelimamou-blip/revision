// Envoie les rappels de révision à tous les élèves qui les ont activés (champ push.t de users/{uid}).
// Lancé par GitHub Actions (rappels.yml) à 13 h 15 et 17 h 15, heure de Dakar. Gratuit : Firebase Cloud Messaging
// et Firestore (une lecture par élève abonné) restent dans le quota gratuit.
// Secret GitHub FIREBASE_SA : le fichier JSON du compte de service Firebase, collé tel quel.
import admin from "firebase-admin";

const sa = JSON.parse(process.env.FIREBASE_SA || "{}");
if (!sa.project_id) { console.log("Secret FIREBASE_SA absent : aucun rappel envoyé."); process.exit(0); }
admin.initializeApp({ credential: admin.credential.cert(sa) });
const db = admin.firestore();

const heure = new Date().getUTCHours(); // Dakar = UTC
const midi = heure < 15;
const jour = Math.floor(Date.now() / 864e5);
const MIDI = [
  ["☀️ C'est la pause !", "5 minutes pour le challenge du jour ? Ta série t'attend 🔥", "#challenge"],
  ["☀️ Petite pause révision", "Une question du jour corrigée, en 1 minute.", "#accueil"],
  ["☀️ Pause de midi", "Un QCM sur un chapitre pour préparer ton prochain devoir ?", "#qcm-list"],
  ["☀️ 5 minutes pour toi", "Revois tes erreurs : celles que tu réussis disparaissent.", "#erreurs"],
];
const SOIR = [
  ["🎒 De retour de l'école ?", "Regarde ce que tu dois réviser pour demain.", "#agenda"],
  ["🎒 Fin des cours", "Tes 3 missions du jour t'attendent (20 minutes).", "#accueil"],
  ["🎒 Un devoir bientôt ?", "Prépare-le chapitre par chapitre, avec corrigés.", "#devoir"],
  ["🎒 Une notion pas claire ?", "Pose ta question, même au micro 🎤", "#assistant"],
];
const [title, body, link] = (midi ? MIDI : SOIR)[jour % 4];

const snap = await db.collection("users").where("push.t", ">", "").get();
const subs = snap.docs.filter((d) => !d.data().suspended).map((d) => ({ ref: d.ref, t: d.data().push.t, name: (d.data().name || "").split(" ")[0] }));
console.log(`${subs.length} élève(s) abonné(s)`);
let ok = 0, ko = 0;
for (let i = 0; i < subs.length; i += 500) {
  const lot = subs.slice(i, i + 500);
  const r = await admin.messaging().sendEach(lot.map((s) => ({
    token: s.t,
    data: { title, body: s.name ? `${s.name}, ${body[0].toLowerCase()}${body.slice(1)}` : body, link: "./" + link },
    webpush: { headers: { Urgency: "normal", TTL: "5400" } },
  })));
  r.responses.forEach((x, k) => {
    if (x.success) return ok++;
    ko++;
    // jeton expiré ou désinstallé : on l'efface pour ne plus le relire
    if (/registration-token-not-registered|invalid-argument|invalid-registration-token/.test(x.error && x.error.code || "")) lot[k].ref.update({ push: admin.firestore.FieldValue.delete() }).catch(() => {});
  });
}
console.log(`envoyés : ${ok}, échecs : ${ko}`);
