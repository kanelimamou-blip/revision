// Prévient l'élève par notification dès que l'admin valide (ou refuse) son paiement, même appli fermée.
// Lancé par GitHub Actions (premium.yml) toutes les 10 minutes. Gratuit : il ne lit que les comptes passés premium
// et les paiements traités depuis 2 heures, et garde dans « notifs » ce qui a déjà été envoyé (une seule notification).
import admin from "firebase-admin";

const sa = JSON.parse(process.env.FIREBASE_SA || "{}");
if (!sa.project_id) { console.log("Secret FIREBASE_SA absent : aucune notification envoyée."); process.exit(0); }
admin.initializeApp({ credential: admin.credential.cert(sa) });
const db = admin.firestore();
const depuis = admin.firestore.Timestamp.fromMillis(Date.now() - 2 * 3600e3);

const aEnvoyer = [];
const prems = await db.collection("users").where("premiumAt", ">", depuis).get();
prems.docs.forEach((d) => aEnvoyer.push({ uid: d.id, ms: d.data().premiumAt.toMillis(), user: d.data(),
  title: "🎉 Tu es premium !", body: "Ton paiement est validé : tout le contenu est débloqué. Bonnes révisions !", link: "./#accueil" }));
const refus = await db.collection("paiements").where("fin", ">", depuis).get();
for (const d of refus.docs) {
  const p = d.data();
  if (p.statut !== "refuse") continue;
  const u = await db.collection("users").doc(d.id).get();
  aEnvoyer.push({ uid: d.id, ms: p.fin.toMillis(), user: u.exists ? u.data() : {},
    title: "❌ Paiement non validé", body: (p.motif || "La capture n'a pas permis de retrouver le paiement.") + " Renvoie une capture dans l'appli.", link: "./#premium" });
}

let ok = 0;
for (const n of aEnvoyer) {
  const ref = db.collection("notifs").doc(`${n.uid}-${n.ms}`);
  if ((await ref.get()).exists) continue;
  const t = n.user.push && n.user.push.t;
  let res = "sans notification";
  if (t) {
    const prenom = (n.user.name || "").split(" ")[0];
    try {
      await admin.messaging().send({ token: t, data: { title: n.title, body: prenom ? `${prenom}, ${n.body[0].toLowerCase()}${n.body.slice(1)}` : n.body, link: n.link, tag: "premium" },
        webpush: { headers: { Urgency: "high", TTL: "86400" } } });
      res = "envoyée"; ok++;
    } catch (e) { res = "échec " + (e.code || e.message); }
  }
  await ref.set({ uid: n.uid, title: n.title, res, at: admin.firestore.FieldValue.serverTimestamp() });
}
console.log(`${aEnvoyer.length} à traiter, ${ok} notification(s) envoyée(s)`);
