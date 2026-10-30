"use strict";
// Espace propriétaire (#admin) : comptes clients, chiffres d'utilisation, journal des erreurs, suspension d'un compte.
// Seul le compte de l'admin y entre ; les règles Firestore refusent ces lectures à tout autre compte.
(() => {
  const fmt = (d) => (d ? d.toLocaleDateString("fr-FR", { day: "2-digit", month: "2-digit", year: "2-digit" }) + " " + d.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" }) : "—");
  const ago = (d, j) => d && Date.now() - d.getTime() < j * 864e5;
  let users = null, errors = null, filtre = "";

  async function viewAdmin(arg) {
    if (!Compte.user) { $view.innerHTML = `<div class="card"><h1>Espace admin</h1><p>Connecte-toi d'abord avec ton compte Google propriétaire.</p></div>`; return; }
    if (!Compte.isAdmin()) { $view.innerHTML = `<div class="card"><h1>Accès refusé</h1><p>Cet espace est réservé au propriétaire de l'appli.</p><a class="btn alt" href="#accueil">Retour à l'accueil</a></div>`; return; }
    const onglet = ["erreurs", "comptes", "qr"].includes(arg) ? arg : "chiffres";
    $view.innerHTML = `<h1>Espace admin</h1><p class="small muted">Connecté en tant que ${esc(Compte.user.email)} · identifiant ${esc(Compte.user.uid)}</p>
      <div class="row onglets">${[["chiffres", "Chiffres"], ["comptes", "Comptes"], ["erreurs", "Erreurs"], ["qr", "QR code"]].map(([k, t]) => `<a class="btn alt small${k === onglet ? " on" : ""}" href="#admin/${k}">${t}</a>`).join("")}</div>
      <div id="adm"><p class="muted">Chargement…</p></div><button class="btn alt" id="reload">Actualiser</button>`;
    document.getElementById("reload").onclick = () => { users = errors = null; viewAdmin(arg); };
    const box = document.getElementById("adm");
    if (onglet === "qr") {
      box.innerHTML = `<div class="card" style="text-align:center"><h2>Fais scanner ce code</h2><img src="icons/qr.svg" alt="QR code de l'appli Révision" style="width:100%;max-width:340px;background:#fff;padding:12px;border-radius:12px">
        <p class="small muted">La personne ouvre l'appareil photo de son téléphone et vise le code : l'appli s'ouvre avec les étapes pour l'installer. Monte la luminosité de ton écran.</p></div>`;
      document.getElementById("reload").hidden = true;
      return;
    }
    try {
      if (!users) users = await Compte.adminUsers();
      if (onglet === "erreurs" && !errors) errors = await Compte.adminErrors();
    } catch (e) { box.innerHTML = `<div class="card"><p>Lecture refusée (${esc(e.code || e.message)}). Vérifie que les règles Firestore à jour sont publiées.</p></div>`; return; }
    if (onglet === "chiffres") return chiffres(box);
    if (onglet === "comptes") return comptes(box);
    return journal(box);
  }

  function chiffres(box) {
    const n = (f) => users.filter(f).length, tile = (v, t) => `<div class="card" style="text-align:center"><p class="score">${v}</p><p class="small muted">${t}</p></div>`;
    const niveaux = {}; users.forEach((u) => { const k = (u.level || "sans classe").split(" ")[0]; niveaux[k] = (niveaux[k] || 0) + 1; });
    box.innerHTML = `<div class="grid">${tile(users.length, "comptes inscrits")}${tile(n((u) => ago(u.lastSeen, 1)), "actifs aujourd'hui")}${tile(n((u) => ago(u.lastSeen, 7)), "actifs cette semaine")}${tile(n((u) => ago(u.lastSeen, 30)), "actifs ce mois")}
      ${tile(n((u) => ago(u.created, 1)), "inscrits aujourd'hui")}${tile(n((u) => ago(u.created, 7)), "inscrits cette semaine")}${tile(n((u) => ago(u.created, 30)), "inscrits ce mois")}${tile(n((u) => u.premium), "premium")}${tile(n((u) => u.suspended), "suspendus")}</div>
      <div class="card"><h2>Par classe</h2><ul class="steps">${Object.entries(niveaux).sort((a, b) => b[1] - a[1]).map(([k, v]) => `<li>${esc(k)} : <b>${v}</b></li>`).join("")}</ul></div>
      <p class="small muted">« Actif » = a ouvert l'appli (mise à jour au plus toutes les 12 heures).</p>`;
  }

  function comptes(box) {
    const liste = users.filter((u) => !filtre || `${u.name} ${u.email}`.toLowerCase().includes(filtre)).sort((a, b) => (b.lastSeen || b.created || 0) - (a.lastSeen || a.created || 0));
    box.innerHTML = `<input class="field" id="af" type="search" placeholder="Chercher un nom ou un e-mail" value="${esc(filtre)}" aria-label="Chercher un compte">
      <p class="small muted">${liste.length} compte${liste.length > 1 ? "s" : ""}</p>
      ${liste.slice(0, 300).map((u) => `<div class="card"><p><b>${esc(u.name || "Sans nom")}</b> ${u.suspended ? "🚫 suspendu" : ago(u.lastSeen, 7) ? "🟢 actif" : "⚪ inactif"}${u.premium ? " · ⭐ premium" : ""}</p>
        <p class="small muted">${esc(u.email || u.uid)}${u.level ? " · " + esc(u.level) : ""}<br>Inscrit le ${fmt(u.created)} · dernière activité ${fmt(u.lastSeen)}</p>
        <button class="btn alt small" data-sus="${esc(u.uid)}" data-on="${u.suspended ? 0 : 1}">${u.suspended ? "Réactiver le compte" : "Suspendre le compte"}</button></div>`).join("")}`;
    const f = document.getElementById("af"); f.oninput = () => { filtre = f.value.trim().toLowerCase(); comptes(box); const g = document.getElementById("af"); g.focus(); g.setSelectionRange(g.value.length, g.value.length); };
    box.querySelectorAll("[data-sus]").forEach((b) => (b.onclick = async () => {
      const on = b.dataset.on === "1", u = users.find((x) => x.uid === b.dataset.sus);
      if (on && !confirmer(b, `Suspendre ${u.name || u.email} ?`)) return;
      b.disabled = true;
      try { await Compte.adminSuspend(u.uid, on); u.suspended = on; comptes(box); } catch (e) { b.disabled = false; b.textContent = "Refusé : " + (e.code || e.message); }
    }));
  }
  // confirmation en deux touches, sans fenêtre du navigateur
  function confirmer(b, txt) { if (b.dataset.sure) return true; b.dataset.sure = "1"; b.textContent = txt + " Touche encore pour confirmer"; setTimeout(() => { delete b.dataset.sure; }, 5000); return false; }

  function journal(box) {
    box.innerHTML = errors.length ? `<p class="small muted">${errors.length} erreur${errors.length > 1 ? "s" : ""} récente${errors.length > 1 ? "s" : ""} (les plus récentes d'abord).</p>
      ${errors.map((e) => `<div class="card"><p><b>${esc(e.msg)}</b></p><p class="small muted">${fmt(e.at)} · page ${esc(e.page)}${e.level ? " · " + esc(e.level) : ""}<br>${esc(e.email || (e.uid ? e.uid : "non connecté"))}<br>${esc(e.ua)}</p></div>`).join("")}
      <button class="btn alt" id="clr">Vider le journal</button>` : `<div class="card"><p>Aucune erreur enregistrée. 👍</p></div>`;
    const c = document.getElementById("clr");
    if (c) c.onclick = async () => { if (!confirmer(c, "Tout effacer ?")) return; c.disabled = true; await Compte.adminClearErrors(errors.map((e) => e.id)).catch(() => {}); errors = null; viewAdmin("erreurs"); };
  }

  globalThis.viewAdmin = viewAdmin;
})();
