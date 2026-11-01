// Exemple de commande : compte les documents des principales collections (lecture seule).
export default async function ({ db, sa }) {
  console.log("Projet :", sa.project_id);
  for (const c of ["users", "paiements", "codes", "notifs"]) {
    const n = (await db.collection(c).count().get()).data().count;
    console.log(`${c} : ${n}`);
  }
}
