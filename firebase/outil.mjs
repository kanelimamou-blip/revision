// Outil d'administration Firebase lancé par GitHub Actions (workflow « Commandes Firebase »), avec le secret FIREBASE_SA.
//   node outil.mjs comparer          : montre les différences entre firebase/firestore.rules et les règles en ligne
//   node outil.mjs verifier          : compile firebase/firestore.rules sans rien publier
//   node outil.mjs regles            : publie firebase/firestore.rules (garde une copie des règles remplacées dans le journal)
//   node outil.mjs script <fichier>  : lance firebase/commandes/<fichier>.mjs avec { admin, db, sa } (lecture/écriture Firestore, Auth...)
// Le dépôt est public : le sel des codes premium n'y est pas. Il est écrit __SEL_CODES__ et repris des règles déjà en ligne.
import admin from "firebase-admin";
import { readFileSync } from "node:fs";
import { pathToFileURL } from "node:url";

const sa = JSON.parse(process.env.FIREBASE_SA || "{}");
if (!sa.project_id) { console.error("Secret FIREBASE_SA absent."); process.exit(1); }
admin.initializeApp({ credential: admin.credential.cert(sa) });
const [action = "comparer", arg = ""] = process.argv.slice(2);
const SEL_RE = /hashing\.sha256\('([0-9a-f]{16,64})'/;

async function enLigne() {
  const r = await admin.securityRules().getFirestoreRuleset();
  return r.source[0].content;
}
async function locales() {
  const actuel = await enLigne();
  const m = actuel.match(SEL_RE);
  if (!m) throw new Error("Sel des codes introuvable dans les règles en ligne : publication annulée.");
  console.log(`::add-mask::${m[1]}`);
  const src = readFileSync(new URL("./firestore.rules", import.meta.url), "utf8");
  if (!src.includes("__SEL_CODES__")) throw new Error("firebase/firestore.rules doit contenir __SEL_CODES__ (le sel ne va jamais dans le dépôt).");
  return { actuel, src: src.replaceAll("__SEL_CODES__", m[1]) };
}
const cacher = (t) => t.replace(/(hashing\.sha256\(')[0-9a-f]+'/g, "$1***'");
function diff(a, b) {
  const A = a.split("\n"), B = b.split("\n"), n = A.length, m = B.length;
  const L = Array.from({ length: n + 1 }, () => new Int32Array(m + 1));
  for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--) L[i][j] = A[i] === B[j] ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
  const out = []; let i = 0, j = 0;
  while (i < n || j < m) {
    if (i < n && j < m && A[i] === B[j]) { i++; j++; }
    else if (j < m && (i >= n || L[i][j + 1] >= L[i + 1][j])) out.push(`+ ${j + 1}: ${B[j++]}`);
    else out.push(`- ${i + 1}: ${A[i++]}`);
  }
  return out;
}

if (action === "comparer" || action === "verifier" || action === "regles") {
  const { actuel, src } = await locales();
  const d = diff(cacher(actuel), cacher(src));
  console.log(d.length ? `Différences (- en ligne, + dépôt) :\n${d.join("\n")}` : "Les règles du dépôt sont identiques aux règles en ligne.");
  if (action !== "comparer") {
    // la création du jeu de règles les compile : une erreur de syntaxe arrête tout avant la mise en ligne
    const rs = await admin.securityRules().createRuleset(admin.securityRules().createRulesFileFromSource("firestore.rules", src));
    console.log(`Règles compilées sans erreur (${rs.name}).`);
    if (action === "regles") {
      if (!d.length) console.log("Rien à publier.");
      else {
        console.log("Copie des règles remplacées :\n" + cacher(actuel));
        await admin.securityRules().releaseFirestoreRuleset(rs);
        console.log("✅ Nouvelles règles Firestore publiées.");
      }
    } else await admin.securityRules().deleteRuleset(rs.name);
  }
} else if (action === "script") {
  const nom = arg.replace(/\.mjs$/, "");
  if (!/^[\w-]+$/.test(nom)) throw new Error("Nom de script invalide : " + arg);
  const mod = await import(pathToFileURL(new URL(`./commandes/${nom}.mjs`, import.meta.url).pathname).href);
  await mod.default({ admin, db: admin.firestore(), sa });
} else throw new Error("Action inconnue : " + action);
