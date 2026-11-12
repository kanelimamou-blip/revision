// Autorise la nouvelle adresse de l'appli (Cloudflare Pages) pour la connexion Firebase (Authentication › Settings › Authorized domains).
// N'enlève aucun domaine : ajoute seulement ceux qui manquent, puis affiche la liste.
const NOUVEAUX = ["revision-49v.pages.dev"];

export default async function ({ admin, sa }) {
  const { access_token } = await admin.app().options.credential.getAccessToken();
  const url = `https://identitytoolkit.googleapis.com/admin/v2/projects/${sa.project_id}/config`;
  const h = { Authorization: `Bearer ${access_token}`, "Content-Type": "application/json" };
  const cfg = await (await fetch(url, { headers: h })).json();
  if (cfg.error) throw new Error("Lecture impossible : " + JSON.stringify(cfg.error));
  const avant = cfg.authorizedDomains || [];
  console.log("Domaines autorisés avant :", avant.join(", "));
  const manquants = NOUVEAUX.filter((d) => !avant.includes(d));
  if (!manquants.length) { console.log("Rien à ajouter."); return; }
  const r = await fetch(url + "?updateMask=authorizedDomains", { method: "PATCH", headers: h, body: JSON.stringify({ authorizedDomains: [...avant, ...manquants] }) });
  const j = await r.json();
  if (j.error) throw new Error("Mise à jour impossible : " + JSON.stringify(j.error));
  console.log("Ajouté :", manquants.join(", "));
  console.log("Domaines autorisés après :", (j.authorizedDomains || []).join(", "));
}
