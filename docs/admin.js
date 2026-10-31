"use strict";
// Espace propriétaire (#admin) : comptes clients, chiffres d'utilisation, journal des erreurs, suspension d'un compte.
// Seul le compte de l'admin y entre ; les règles Firestore refusent ces lectures à tout autre compte.
(() => {
  const fmt = (d) => (d ? d.toLocaleDateString("fr-FR", { day: "2-digit", month: "2-digit", year: "2-digit" }) + " " + d.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" }) : "—");
  const ago = (d, j) => d && Date.now() - d.getTime() < j * 864e5;
  let users = null, errors = null, partages = {}, filtre = "";

  async function viewAdmin(arg) {
    if (!Compte.user) { $view.innerHTML = `<div class="card"><h1>Espace admin</h1><p>Connecte-toi d'abord avec ton compte Google propriétaire.</p></div>`; return; }
    if (!Compte.isAdmin()) { $view.innerHTML = `<div class="card"><h1>Accès refusé</h1><p>Cet espace est réservé au propriétaire de l'appli.</p><a class="btn alt" href="#accueil">Retour à l'accueil</a></div>`; return; }
    const onglet = ["activite", "erreurs", "comptes", "qr"].includes(arg) ? arg : "chiffres";
    $view.innerHTML = `<h1>Espace admin</h1><p class="small muted">Connecté en tant que ${esc(Compte.user.email)} · identifiant ${esc(Compte.user.uid)}</p>
      <div class="row onglets">${[["chiffres", "Chiffres"], ["activite", "Nouveautés"], ["comptes", "Comptes"], ["erreurs", "Erreurs"], ["qr", "QR code"]].map(([k, t]) => `<a class="btn alt small${k === onglet ? " on" : ""}" href="#admin/${k}">${t}</a>`).join("")}</div>
      <div id="adm"><p class="muted">Chargement…</p></div><button class="btn alt" id="reload">Actualiser</button>`;
    document.getElementById("reload").onclick = () => { users = errors = null; partages = {}; viewAdmin(arg); };
    const box = document.getElementById("adm");
    if (onglet === "qr") {
      box.innerHTML = `<div class="card" style="text-align:center"><h2>Fais scanner ce code</h2><img src="icons/qr.png" alt="QR code de l'appli Révision" style="width:100%;max-width:340px;background:#fff;padding:12px;border-radius:12px">
        <p class="small muted">La personne ouvre l'appareil photo de son téléphone et vise le code : l'appli s'ouvre avec les étapes pour l'installer. Monte la luminosité de ton écran.</p><a class="btn alt" href="#partager">Envoyer ce QR code ou le lien</a></div>`;
      document.getElementById("reload").hidden = true;
      return;
    }
    try {
      if (!users) { users = await Compte.adminUsers(); partages = await Compte.adminDevices().catch(() => ({})); }
      if (onglet === "erreurs" && !errors) errors = await Compte.adminErrors();
    } catch (e) { box.innerHTML = `<div class="card"><p>Lecture refusée (${esc(e.code || e.message)}). Vérifie que les règles Firestore à jour sont publiées.</p></div>`; return; }
    if (onglet === "chiffres") return chiffres(box);
    if (onglet === "activite") return activite(box);
    if (onglet === "comptes") return comptes(box);
    return journal(box);
  }

  // « même téléphone que … » : comptes ouverts sur le même téléphone (un seul essai gratuit pour eux tous)
  const meme = (u) => { const a = partages[u.uid]; if (!a || !a.length) return ""; const noms = a.map((x) => { const v = users.find((y) => y.uid === x); return v ? v.name || v.email : "compte supprimé"; });
    return `<br><span style="color:var(--hi-ink);background:var(--hi);padding:0 4px;border-radius:4px">📱 même téléphone que ${esc(noms.join(", "))}</span>`; };

  function chiffres(box) {
    const n = (f) => users.filter(f).length, tile = (v, t) => `<div class="card" style="text-align:center"><p class="score">${v}</p><p class="small muted">${t}</p></div>`;
    const niveaux = {}; users.forEach((u) => { const k = (u.level || "sans classe").split(" ")[0]; niveaux[k] = (niveaux[k] || 0) + 1; });
    box.innerHTML = `<div class="grid">${tile(users.length, "comptes inscrits")}${tile(n((u) => ago(u.lastSeen, 1)), "actifs aujourd'hui")}${tile(n((u) => ago(u.lastSeen, 7)), "actifs cette semaine")}${tile(n((u) => ago(u.lastSeen, 30)), "actifs ce mois")}
      ${tile(n((u) => ago(u.created, 1)), "inscrits aujourd'hui")}${tile(n((u) => ago(u.created, 7)), "inscrits cette semaine")}${tile(n((u) => ago(u.created, 30)), "inscrits ce mois")}${tile(n((u) => u.premium), "premium")}${tile(n((u) => u.suspended), "suspendus")}${tile(n((u) => (partages[u.uid] || []).length), "comptes sur un téléphone partagé")}</div>
      <div class="card"><h2>Par classe</h2><ul class="steps">${Object.entries(niveaux).sort((a, b) => b[1] - a[1]).map(([k, v]) => `<li>${esc(k)} : <b>${v}</b></li>`).join("")}</ul></div>
      <p class="small muted">« Actif » = a ouvert l'appli (mise à jour au plus toutes les 12 heures).</p>`;
  }

  // nouveaux comptes et dernières connexions, avec les inscriptions des 14 derniers jours
  const depuis = (d) => { if (!d) return "—"; const m = Math.round((Date.now() - d.getTime()) / 6e4); return m < 60 ? `il y a ${m} min` : m < 1440 ? `il y a ${Math.round(m / 60)} h` : `il y a ${Math.round(m / 1440)} j`; };
  function activite(box) {
    const jours = [...Array(14)].map((_, i) => { const d = new Date(); d.setHours(0, 0, 0, 0); d.setDate(d.getDate() - 13 + i); return d; });
    const parJour = (k) => jours.map((d) => users.filter((u) => u[k] && u[k] >= d && u[k] - d < 864e5).length);
    const ins = parJour("created"), vus = parJour("lastSeen"), max = Math.max(1, ...ins, ...vus);
    const barres = (v, t) => `<div style="display:flex;align-items:flex-end;gap:3px;height:90px">${v.map((n, i) => `<div style="flex:1;text-align:center" title="${jours[i].toLocaleDateString("fr-FR")} : ${n}"><span class="small">${n || ""}</span><div style="height:${(70 * n) / max}px;min-height:2px;background:var(--accent,#7c5cff);border-radius:3px"></div></div>`).join("")}</div><p class="small muted">${t}</p>`;
    const ligne = (u, k, t) => `<div class="row small" style="padding:6px 0;border-bottom:1px solid rgba(127,127,127,.2)"><span><b>${esc(u.name || "Sans nom")}</b>${u.premium ? " ⭐" : ""}<br><span class="muted">${esc(u.phone ? "📱 " + u.phone : u.email || u.uid)}${u.level ? " · " + esc(u.level) : ""}${meme(u)}</span></span><span class="muted" style="text-align:right">${t}<br>${depuis(u[k])}</span></div>`;
    const nouveaux = users.filter((u) => u.created).sort((a, b) => b.created - a.created).slice(0, 30);
    const connexions = users.filter((u) => u.lastSeen).sort((a, b) => b.lastSeen - a.lastSeen).slice(0, 30);
    box.innerHTML = `<div class="card"><h2>Inscriptions par jour (14 jours)</h2>${barres(ins, "Du plus ancien (à gauche) à aujourd'hui (à droite).")}</div>
      <div class="card"><h2>Dernière connexion par jour (14 jours)</h2>${barres(vus, "Chaque compte compte une fois, le jour de sa dernière ouverture de l'appli.")}</div>
      <div class="card"><h2>🆕 Nouveaux comptes</h2>${nouveaux.map((u) => ligne(u, "created", "inscrit")).join("") || '<p class="muted">Aucun compte pour l\'instant.</p>'}</div>
      <div class="card"><h2>🟢 Dernières connexions</h2>${connexions.map((u) => ligne(u, "lastSeen", "vu")).join("") || '<p class="muted">Aucune connexion enregistrée.</p>'}</div>`;
  }

  function comptes(box) {
    const liste = users.filter((u) => !filtre || `${u.name} ${u.email} ${u.phone}`.toLowerCase().includes(filtre)).sort((a, b) => (b.lastSeen || b.created || 0) - (a.lastSeen || a.created || 0));
    box.innerHTML = `<input class="field" id="af" type="search" placeholder="Chercher un nom ou un e-mail" value="${esc(filtre)}" aria-label="Chercher un compte">
      <p class="small muted">${liste.length} compte${liste.length > 1 ? "s" : ""}</p>
      ${liste.slice(0, 300).map((u) => `<div class="card"><p><b>${esc(u.name || "Sans nom")}</b> ${u.suspended ? "🚫 suspendu" : ago(u.lastSeen, 7) ? "🟢 actif" : "⚪ inactif"}${u.premium ? ` · ⭐ premium${u.code ? " (code " + esc(u.code) + ")" : ""}` : ""}</p>
        <p class="small muted">${esc(u.phone ? "📱 " + u.phone : u.email || u.uid)}${u.level ? " · " + esc(u.level) : ""}<br>Inscrit le ${fmt(u.created)} · dernière activité ${fmt(u.lastSeen)}${meme(u)}</p>
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
