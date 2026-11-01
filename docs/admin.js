"use strict";
// Espace propriétaire (#admin) : comptes clients, chiffres d'utilisation, journal des erreurs, suspension d'un compte.
// Seul le compte de l'admin y entre ; les règles Firestore refusent ces lectures à tout autre compte.
(() => {
  const fmt = (d) => (d ? d.toLocaleDateString("fr-FR", { day: "2-digit", month: "2-digit", year: "2-digit" }) + " " + d.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" }) : "—");
  const ago = (d, j) => d && Date.now() - d.getTime() < j * 864e5;
  let suivis = null, users = null, errors = null, pays = null, partages = {}, filtre = "", accs = null, ventes = null, societe = null;

  async function viewAdmin(arg) {
    if (!Compte.user) { $view.innerHTML = `<div class="card"><h1>Espace admin</h1><p>Connecte-toi d'abord avec ton compte Google propriétaire.</p></div>`; return; }
    if (!Compte.isAdmin()) { $view.innerHTML = `<div class="card"><h1>Accès refusé</h1><p>Cet espace est réservé au propriétaire de l'appli.</p><a class="btn alt" href="#accueil">Retour à l'accueil</a></div>`; return; }
    const onglet = ["chiffres", "activite", "erreurs", "comptes", "qr", "accords", "ventes", "societe", "parents"].includes(arg) ? arg : "paiements";
    $view.innerHTML = `<h1>Espace admin</h1><p class="small muted">Connecté en tant que ${esc(Compte.user.email)} · identifiant ${esc(Compte.user.uid)}</p>
      <div class="row onglets">${[["paiements", "💰 Paiements"], ["ventes", "🧾 Ventes"], ["societe", "🏢 Société"], ["parents", "👨‍👩‍👧 Modes & parents"], ["chiffres", "Chiffres"], ["activite", "Nouveautés"], ["comptes", "Comptes"], ["accords", "👪 Accords"], ["erreurs", "Erreurs"], ["qr", "QR code"]].map(([k, t]) => `<a class="btn alt small${k === onglet ? " on" : ""}" href="#admin/${k}">${t}</a>`).join("")}</div>
      <div id="adm"><p class="muted">Chargement…</p></div><button class="btn alt" id="reload">Actualiser</button>`;
    document.getElementById("reload").onclick = () => { users = errors = pays = accs = ventes = societe = suivis = null; partages = {}; viewAdmin(arg); };
    const box = document.getElementById("adm");
    if (onglet === "qr") {
      box.innerHTML = `<div class="card" style="text-align:center"><h2>Fais scanner ce code</h2><img src="icons/qr.png" alt="QR code de l'appli Révision" style="width:100%;max-width:340px;background:#fff;padding:12px;border-radius:12px">
        <p class="small muted">La personne ouvre l'appareil photo de son téléphone et vise le code : l'appli s'ouvre avec les étapes pour l'installer. Monte la luminosité de ton écran.</p><a class="btn alt" href="#partager">Envoyer ce QR code ou le lien</a></div>`;
      document.getElementById("reload").hidden = true;
      return;
    }
    if (onglet === "ventes") {
      try { if (!ventes) ventes = await Compte.adminVentes(); } catch (e) { box.innerHTML = `<div class="card"><p>Lecture refusée (${esc(e.code || e.message)}). Publie les nouvelles règles Firestore (fichier firestore.rules).</p></div>`; return; }
      if (!societe) societe = { ...(CFG.societe || {}), ...((await Compte.getSocietePrivee().catch(() => null)) || {}) };
      return registre(box);
    }
    if (onglet === "societe") {
      if (!societe) societe = { ...(CFG.societe || {}), ...((await Compte.getSocietePrivee().catch(() => null)) || {}) };
      return fiche(box);
    }
    if (onglet === "accords") {
      try { if (!accs) accs = await Compte.adminAccords(); } catch (e) { box.innerHTML = `<div class="card"><p>Lecture refusée (${esc(e.code || e.message)}). Publie les nouvelles règles Firestore (fichier firestore.rules).</p></div>`; return; }
      return accords(box);
    }
    if (onglet === "paiements") {
      if (!accs) accs = await Compte.adminAccords().catch(() => []);
      try { if (!pays) pays = await Compte.adminPays(); } catch (e) { box.innerHTML = `<div class="card"><p>Lecture refusée (${esc(e.code || e.message)}). Publie les nouvelles règles Firestore (fichier firestore.rules).</p></div>`; return; }
      return paiements(box);
    }
    if (onglet === "parents") {
      try { if (!users) { users = await Compte.adminUsers(); partages = await Compte.adminDevices().catch(() => ({})); } if (!suivis) suivis = await Compte.adminSuivis().catch(() => []); }
      catch (e) { box.innerHTML = `<div class="card"><p>Lecture refusée (${esc(e.code || e.message)}). Publie les nouvelles règles Firestore.</p></div>`; return; }
      return parents(box);
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
      <div class="card"><h2>🟢 Dernières connexions</h2>${connexions.map((u) => ligne(u, "lastSeen", "vu")).join("") || '<p class="muted">Aucune connexion enregistrée.</p>'}</div>
      <div class="card"><h2>💬 Réponses des élèves</h2><p class="small muted">Questions posées à la pause de midi et après l'école.</p>${(() => {
        const all = users.flatMap((u) => (u.avis || []).map((a) => ({ ...a, u })));
        if (!all.length) return '<p class="muted">Pas encore de réponse.</p>';
        const parQ = {}; all.forEach((a) => { (parQ[a.q] = parQ[a.q] || {})[a.r] = (parQ[a.q][a.r] || 0) + 1; });
        return Object.entries(parQ).map(([q, rs]) => `<p><b>${esc(q)}</b></p><ul class="steps">${Object.entries(rs).sort((x, y) => y[1] - x[1]).map(([r, n]) => `<li>${esc(r)} : <b>${n}</b></li>`).join("")}</ul>`).join("")
          + `<p class="small muted">Dernières réponses : ${all.sort((x, y) => (y.d || "").localeCompare(x.d || "")).slice(0, 15).map((a) => `${esc(a.u.name || a.u.phone || "élève")} (${esc(a.r)})`).join(" · ")}</p>`;
      })()}</div>`;
  }

  function comptes(box) {
    // un numéro se cherche avec ou sans espaces (77 123 45 67 ou 771234567)
    const f2 = /^[\d\s+]+$/.test(filtre) ? filtre.replace(/\D/g, "").replace(/^(00)?221(?=\d{9}$)/, "") : filtre;
    const liste = users.filter((u) => !filtre || `${u.name} ${u.email} ${u.phone}`.toLowerCase().includes(f2)).sort((a, b) => (b.lastSeen || b.created || 0) - (a.lastSeen || a.created || 0));
    box.innerHTML = `<input class="field" id="af" type="search" placeholder="Chercher un nom, un numéro ou un e-mail" value="${esc(filtre)}" aria-label="Chercher un compte">
      <p class="small muted">${liste.length} compte${liste.length > 1 ? "s" : ""}</p>
      ${liste.slice(0, 300).map((u) => `<div class="card"><p><b>${esc(u.name || "Sans nom")}</b> ${u.suspended ? "🚫 suspendu" : ago(u.lastSeen, 7) ? "🟢 actif" : "⚪ inactif"}${u.premium ? ` · ⭐ premium${u.code ? " (code " + esc(u.code) + ")" : ""}` : ""}</p>
        <p class="small muted">${esc(u.phone ? "📱 " + u.phone : u.email || u.uid)}${u.level ? " · " + esc(u.level) : ""}<br>Inscrit le ${fmt(u.created)} · dernière activité ${fmt(u.lastSeen)}${meme(u)}</p>
        ${u.premium ? "" : `<button class="btn small" data-prem="${esc(u.uid)}">⭐ Passer premium (payé hors appli)</button> `}<button class="btn alt small" data-sus="${esc(u.uid)}" data-on="${u.suspended ? 0 : 1}">${u.suspended ? "Réactiver le compte" : "Suspendre le compte"}</button></div>`).join("")}`;
    const f = document.getElementById("af"); f.oninput = () => { filtre = f.value.trim().toLowerCase(); comptes(box); const g = document.getElementById("af"); g.focus(); g.setSelectionRange(g.value.length, g.value.length); };
    box.querySelectorAll("[data-prem]").forEach((b) => (b.onclick = async () => {
      const u = users.find((x) => x.uid === b.dataset.prem);
      if (!confirmer(b, `${u.name || u.phone} premium ?`)) return;
      b.disabled = true;
      try { await Compte.adminSetPremium(u.uid); u.premium = true; comptes(box); } catch (e) { b.disabled = false; b.textContent = "Refusé : " + (e.code || e.message); }
    }));
    box.querySelectorAll("[data-sus]").forEach((b) => (b.onclick = async () => {
      const on = b.dataset.on === "1", u = users.find((x) => x.uid === b.dataset.sus);
      if (on && !confirmer(b, `Suspendre ${u.name || u.email} ?`)) return;
      b.disabled = true;
      try { await Compte.adminSuspend(u.uid, on); u.suspended = on; comptes(box); } catch (e) { b.disabled = false; b.textContent = "Refusé : " + (e.code || e.message); }
    }));
  }
  // paiements déclarés dans l'appli : un toucher sur Valider passe l'élève en premium, son appli se débloque aussitôt
  // trace de l'accord : le plus récent accepté (parent ou majeur) pour cet élève
  const LI = () => globalThis.LIENS_PARENT || {};
  const accordOk = (uid) => (accs || []).filter((a) => a.uid === uid && (a.statut === "ok" || a.statut === "majeur")).sort((a, b) => (b.okAt || b.at || 0) - (a.okAt || a.at || 0))[0];
  const texteAccord = (a) => a.statut === "majeur" ? `🧑 Déclaré majeur (né le ${esc(a.naissance || "?")}) le ${fmt(a.at)}` : `👪 Accord de ${esc(a.parent || "?")} (${esc(LI()[a.lien] || a.lien || "")}, 📱 ${esc(a.ptel || "")}) le ${fmt(a.okAt)}`;
  const accordDe = (uid) => { if (accs === null) return ""; const a = accordOk(uid); return `<p class="small">${a ? texteAccord(a) : `<span class="msg-ko">⚠️ Aucun accord parent enregistré</span>`}</p>`; };
  function accords(box) {
    const l = (accs || []).slice().sort((a, b) => (b.okAt || b.at || 0) - (a.okAt || a.at || 0));
    const n = (s) => l.filter((a) => a.statut === s).length;
    const csv = () => { const q = (v) => `"${String(v ?? "").replace(/"/g, '""')}"`; const rows = [["eleve", "tel_eleve", "classe", "statut", "parent", "lien", "tel_parent", "naissance", "demande", "accord", "version_conditions", "uid"]].concat(l.map((a) => [a.eleve, a.tel, a.level, a.statut, a.parent, LI()[a.lien] || a.lien, a.ptel, a.naissance, fmt(a.at), fmt(a.okAt), a.v, a.uid])); return rows.map((r) => r.map(q).join(";")).join("\n"); };
    box.innerHTML = `<div class="card"><p><b>${n("ok")}</b> accords de parent · <b>${n("majeur")}</b> élèves déclarés majeurs · <b>${n("attente")}</b> demandes en attente</p><button class="btn alt small" id="acc-csv">📥 Télécharger la liste (tableur)</button></div>
      ${l.map((a) => `<div class="card small"><p><b>${esc(a.eleve || "Sans nom")}</b> · ${esc(a.level || "")} · 📱 ${esc(a.tel || "")}</p><p>${a.statut === "attente" ? `⏳ Demande envoyée le ${fmt(a.at)}, pas encore acceptée` : texteAccord(a)}</p><p class="muted">Conditions version ${esc(a.v || "?")}</p></div>`).join("") || `<div class="card"><p>Aucune demande d'accord pour l'instant.</p></div>`}`;
    document.getElementById("acc-csv").onclick = () => { const b = new Blob(["\ufeff" + csv()], { type: "text/csv" }), u = URL.createObjectURL(b), x = document.createElement("a"); x.href = u; x.download = "accords-parents.csv"; x.click(); setTimeout(() => URL.revokeObjectURL(u), 2000); };
  }
  // ---------- Registre des ventes : une ligne par paiement reçu, numéro de reçu, export tableur
  const venteDe = (p, d) => ({ uid: p.uid || "", nom: (p.name || "").slice(0, 60), tel: (p.phone || "").slice(0, 20), classe: (p.level || "").slice(0, 30), via: p.via || "", montant: p.montant || CFG.price_fcfa, formule: p.formule || "eleve", ms: d ? d.getTime() : Date.now(), source: p.source || "capture" });
  const VIA = { wave: "Wave", om: "Orange Money", especes: "Espèces", code: "Code", autre: "Autre" };
  const telf = (t) => (t || "").replace(/^(\d{2})(\d{3})(\d{2})(\d{2})$/, "$1 $2 $3 $4");
  const numeros = (l) => { const parAn = {}; return l.slice().sort((a, b) => (a.at || 0) - (b.at || 0)).map((v) => { const an = v.at ? v.at.getFullYear() : "????"; parAn[an] = (parAn[an] || 0) + 1; return { ...v, recu: `R-${an}-${String(parAn[an]).padStart(4, "0")}` }; }); };
  function registre(box) {
    const l = numeros(ventes || []).reverse();
    const total = l.reduce((s, v) => s + (+v.montant || 0), 0);
    const mois = {}; l.forEach((v) => { const k = v.at ? v.at.toLocaleDateString("fr-FR", { month: "long", year: "numeric" }) : "?"; (mois[k] = mois[k] || { n: 0, s: 0 }).n++; mois[k].s += +v.montant || 0; });
    box.innerHTML = `<div class="card"><p><b>${l.length}</b> vente${l.length > 1 ? "s" : ""} · total <b>${fcfa(total)}</b></p>
      ${Object.entries(mois).map(([k, m]) => `<p class="small">${esc(k)} : ${m.n} vente${m.n > 1 ? "s" : ""}, ${fcfa(m.s)}</p>`).join("")}
      <p class="small muted">Chaque paiement que tu valides s'ajoute ici tout seul. À garder pour les impôts.</p>
      <div class="row" style="flex-wrap:wrap;gap:6px"><button class="btn alt small" id="v-csv">📥 Télécharger (tableur)</button><button class="btn alt small" id="v-add">➕ Ajouter une vente</button><button class="btn alt small" id="v-old">↩️ Reprendre les anciens paiements</button></div><p class="small" id="v-msg"></p>
      <div id="v-form" hidden><div style="display:grid;gap:8px;margin-top:8px"><input class="field" id="v-nom" maxlength="60" placeholder="Nom de l'élève ou de l'école"><input class="field" id="v-tel" inputmode="numeric" placeholder="Numéro (77 123 45 67)"><input class="field" id="v-cl" maxlength="30" placeholder="Classe (facultatif)">
        <select class="field" id="v-via">${Object.entries(VIA).map(([k, t]) => `<option value="${k}">${t}</option>`).join("")}</select><input class="field" id="v-mt" inputmode="numeric" value="${CFG.price_fcfa}" placeholder="Montant (F)"><input class="field" id="v-date" type="date" value="${new Date().toISOString().slice(0, 10)}">
        <button class="btn" id="v-save">Enregistrer la vente</button></div></div></div>
      ${l.map((v) => `<div class="card small"><p><b>${esc(v.recu)}</b> · ${fmt(v.at)} · <b>${fcfa(+v.montant || 0)}</b> · ${esc(VIA[v.via] || v.via || "")}</p><p>${esc(v.nom || "Sans nom")} · 📱 ${esc(telf(v.tel))}${v.classe ? " · " + esc(v.classe) : ""}</p>
        <div class="row" style="gap:6px"><button class="btn alt small" data-recu="${esc(v.id)}">🧾 Reçu</button><button class="btn alt small" data-del="${esc(v.id)}">Supprimer</button></div><div data-rbox="${esc(v.id)}"></div></div>`).join("") || `<div class="card"><p>Aucune vente enregistrée pour l'instant.</p></div>`}`;
    const msg = (t, ok) => { const m = document.getElementById("v-msg"); m.className = ok ? "small msg-ok" : "small msg-ko"; m.textContent = t; };
    document.getElementById("v-csv").onclick = () => {
      const q = (x) => `"${String(x ?? "").replace(/"/g, '""')}"`;
      const rows = [["recu", "date", "nom", "telephone", "classe", "moyen", "montant_fcfa", "uid"]].concat(numeros(ventes || []).map((v) => [v.recu, fmt(v.at), v.nom, telf(v.tel), v.classe, VIA[v.via] || v.via, v.montant, v.uid]));
      const b = new Blob(["\ufeff" + rows.map((r) => r.map(q).join(";")).join("\n")], { type: "text/csv" }), u = URL.createObjectURL(b), a = document.createElement("a"); a.href = u; a.download = "registre-ventes.csv"; a.click(); setTimeout(() => URL.revokeObjectURL(u), 2000);
    };
    document.getElementById("v-add").onclick = () => { const f = document.getElementById("v-form"); f.hidden = !f.hidden; };
    document.getElementById("v-save").onclick = async () => {
      const nom = document.getElementById("v-nom").value.trim(), mt = parseInt(document.getElementById("v-mt").value.replace(/\D/g, ""), 10), d = document.getElementById("v-date").value;
      if (nom.length < 2) return msg("Écris le nom.");
      if (!(mt > 0)) return msg("Montant invalide.");
      const at = d ? new Date(d + "T12:00") : new Date();
      const rec = { uid: "", nom: nom.slice(0, 60), tel: (Compte.normTel(document.getElementById("v-tel").value) || "").slice(0, 20), classe: document.getElementById("v-cl").value.trim().slice(0, 30), via: document.getElementById("v-via").value, montant: mt, ms: at.getTime(), source: "manuel" };
      try { await Compte.adminAddVente(`m-${Date.now()}`, rec); ventes = null; viewAdmin("ventes"); } catch (e) { msg("Enregistrement refusé (" + (e.code || e.message) + "). Publie les nouvelles règles Firestore."); }
    };
    document.getElementById("v-old").onclick = async () => {
      const b = document.getElementById("v-old"); if (!confirmer(b, "Reprendre ?")) return; b.disabled = true; msg("Lecture des paiements validés…", true);
      try {
        const old = await Compte.adminPaysValides(), deja = new Set((ventes || []).map((v) => v.uid).filter(Boolean)); let n = 0;
        for (const p of old) { if (deja.has(p.uid)) continue; await Compte.adminAddVente(`${p.uid}-old`, venteDe(p, p.at)); n++; }
        ventes = null; msg(`${n} ancien${n > 1 ? "s" : ""} paiement${n > 1 ? "s" : ""} ajouté${n > 1 ? "s" : ""}.`, true); setTimeout(() => viewAdmin("ventes"), 1200);
      } catch (e) { b.disabled = false; msg("Lecture refusée (" + (e.code || e.message) + "). Publie les nouvelles règles Firestore."); }
    };
    box.querySelectorAll("[data-del]").forEach((b) => (b.onclick = async () => { if (!confirmer(b, "Supprimer ?")) return; await Compte.adminDelVente(b.dataset.del).catch(() => {}); ventes = null; viewAdmin("ventes"); }));
    box.querySelectorAll("[data-recu]").forEach((b) => (b.onclick = () => {
      const v = l.find((x) => x.id === b.dataset.recu), s = societe || {}, r = box.querySelector(`[data-rbox="${b.dataset.recu}"]`);
      const txt = [`REÇU ${v.recu}`, s.nom || "Révision", [s.rccm && `RCCM ${s.rccm}`, s.ninea && `NINEA ${s.ninea}`].filter(Boolean).join(" · "), s.adresse || "", "", `Date : ${fmt(v.at)}`, `Client : ${v.nom || ""}${v.tel ? " (" + telf(v.tel) + ")" : ""}`, `Objet : pack premium Révision${v.classe ? " – " + v.classe : ""}, valable jusqu'à l'examen`, `Montant : ${fcfa(+v.montant || 0)}`, `Payé par : ${VIA[v.via] || v.via || ""}`, "", "Merci pour votre confiance."].filter((x, i, a) => x !== "" || a[i - 1] !== "").join("\n");
      r.innerHTML = `<pre class="small" style="white-space:pre-wrap;background:var(--card2,#f4f4f4);padding:8px;border-radius:8px">${esc(txt)}</pre><button class="btn alt small" data-cp>📋 Copier pour WhatsApp</button>`;
      r.querySelector("[data-cp]").onclick = (e) => navigator.clipboard?.writeText(txt).then(() => { e.target.textContent = "Copié ✓"; }).catch(() => {});
    }));
  }

  // ---------- Fiche société : alimente les mentions légales et les reçus
  const CHAMPS = [["nom", "Nom de l'entreprise ou ton nom"], ["forme", "Forme (entreprise individuelle, SUARL…)"], ["rccm", "Numéro RCCM"], ["ninea", "NINEA"], ["adresse", "Adresse"], ["responsable", "Responsable de la publication"], ["cdp", "Déclaration CDP (numéro et date)"]];
  function fiche(box) {
    const s = societe || {};
    const manque = CHAMPS.filter(([k]) => !s[k]).map(([, t]) => t);
    box.innerHTML = `<div class="card"><h2>🏢 Ma société</h2><p class="small muted">🔒 Ces informations restent privées : seul toi les vois, sur tes reçus. Elles ne seront affichées dans l'appli (mentions légales) que le jour où tu le décideras.</p>
      ${manque.length ? `<p class="small msg-ko">À compléter : ${esc(manque.join(", "))}.</p>` : `<p class="small msg-ok">Tout est rempli. 👍</p>`}
      <div style="display:grid;gap:8px">${CHAMPS.map(([k, t]) => `<label class="small">${t}<input class="field" data-f="${k}" maxlength="120" value="${esc(s[k] || "")}"></label>`).join("")}</div>
      <button class="btn" id="s-save" style="margin-top:8px">Enregistrer</button><p class="small" id="s-msg"></p>
      </div>
      <div class="card small"><h2>À faire pour être en règle</h2><ol class="steps"><li>Vérifier le RCCM à l'APIX (actif, activité « édition d'applications éducatives »).</li><li>Déclarer le début d'activité au centre des impôts avec RCCM et NINEA.</li><li>Déclarer l'appli à la CDP et demander l'autorisation de transfert (Firebase en Europe).</li><li>Garder le registre des ventes (onglet 🧾 Ventes) et donner un reçu sur demande.</li></ol></div>`;
    document.getElementById("s-save").onclick = async () => {
      const rec = {}; box.querySelectorAll("[data-f]").forEach((i) => { rec[i.dataset.f] = i.value.trim().slice(0, 120); });
      const m = document.getElementById("s-msg");
      try { await Compte.setSociete(rec); societe = rec; m.className = "small msg-ok"; m.textContent = "Enregistré (privé)."; setTimeout(() => { if (document.body.contains(box)) fiche(box); }, 1200); }
      catch (e) { m.className = "small msg-ko"; m.textContent = "Enregistrement refusé (" + (e.code || e.message) + "). Publie les nouvelles règles Firestore."; }
    };
  }

  function paiements(box) {
    const tel = (t) => (t || "").replace(/^(\d{2})(\d{3})(\d{2})(\d{2})$/, "$1 $2 $3 $4");
    box.innerHTML = pays.length ? `<p class="small muted">${pays.length} paiement${pays.length > 1 ? "s" : ""} à vérifier (le plus ancien d'abord). Compare le numéro, le montant (${fcfa(CFG.price_fcfa)}) et l'heure avec ton relevé ${"Wave"} ou Orange Money.</p>
      ${pays.map((p) => `<div class="card"><p><b>${esc(p.name || "Sans nom")}</b> · 📱 ${esc(tel(p.phone) || "numéro inconnu")} · ${p.via === "om" ? "Orange Money" : "Wave"}</p>
        <p class="small muted">${esc(p.level || "")} · envoyé ${fmt(p.at)}</p>${p.formule && p.formule !== "eleve" ? `<p class="small" style="background:var(--hi);color:var(--hi-ink);padding:2px 6px;border-radius:6px">👨‍👩‍👧 Formule parent${p.formule === "suivi" ? " + suivi spécifique" : ""} · ${p.enfants || 1} enfant${(p.enfants || 1) > 1 ? "s" : ""} · montant attendu ${fcfa(p.montant || 0)}</p>` : ""}${accordDe(p.uid)}
        <img src="${esc(p.img)}" alt="Capture du paiement" style="max-width:100%;max-height:420px;border-radius:8px;display:block;margin:8px 0">
        <div class="row"><button class="btn" style="flex:1" data-ok="${esc(p.uid)}">✅ Valider : passer premium</button><button class="btn alt" style="flex:1" data-ko="${esc(p.uid)}">❌ Refuser</button></div>
        <div data-motif="${esc(p.uid)}" hidden><input class="field" placeholder="Motif (ex. capture illisible, montant incomplet)" maxlength="200"><button class="btn alt small" data-kosend="${esc(p.uid)}">Envoyer le refus</button></div>
        <p class="small" data-res="${esc(p.uid)}"></p></div>`).join("")}`
      : `<div class="card"><p>Aucun paiement en attente. 👍</p><p class="small muted">Quand un élève envoie la capture de son paiement dans l'appli, elle apparaît ici. Touche « Actualiser » pour vérifier.</p></div>`;
    const fin = (uid, txt) => { pays = pays.filter((x) => x.uid !== uid); const r = box.querySelector(`[data-res="${uid}"]`); if (r) { r.className = "msg-ok"; r.textContent = txt; } setTimeout(() => paiements(box), 1500); };
    box.querySelectorAll("[data-ok]").forEach((b) => (b.onclick = async () => {
      b.disabled = true; b.textContent = "Validation…";
      const pv = pays.find((x) => x.uid === b.dataset.ok);
      try { await Compte.adminValidate(b.dataset.ok);
        // formule parent : les enfants reliés avec leur propre compte passent aussi premium
        if (pv && pv.formule && pv.formule !== "eleve") { if (!users) users = await Compte.adminUsers().catch(() => null); const u = (users || []).find((x) => x.uid === pv.uid);
          for (const e of ((u && u.famille && u.famille.enfants) || []).filter((e) => e.uid)) await Compte.adminSetPremium(e.uid).catch(() => {}); } if (pv) Compte.adminAddVente(`${pv.uid}-${Date.now()}`, venteDe(pv, new Date())).then(() => { ventes = null; }).catch(() => {}); if (users) { const u = users.find((x) => x.uid === b.dataset.ok); if (u) u.premium = true; } fin(b.dataset.ok, "Validé : l'élève est premium, son appli se débloque."); }
      catch (e) { b.disabled = false; b.textContent = "Refusé : " + (e.code || e.message); }
    }));
    box.querySelectorAll("[data-ko]").forEach((b) => (b.onclick = () => { box.querySelector(`[data-motif="${b.dataset.ko}"]`).hidden = false; }));
    box.querySelectorAll("[data-kosend]").forEach((b) => (b.onclick = async () => {
      const motif = b.previousElementSibling.value.trim() || "La capture n'a pas permis de retrouver le paiement.";
      b.disabled = true;
      try { await Compte.adminRefuse(b.dataset.kosend, motif); fin(b.dataset.kosend, "Refus envoyé à l'élève."); } catch (e) { b.disabled = false; b.textContent = "Refusé : " + (e.code || e.message); }
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

  // Les deux modes de l'appli : élève seul et parent répétiteur ; tarifs modulables ; suivis spécifiques demandés
  function parents(box) {
    const par = users.filter((u) => u.mode === "parent"), seuls = users.filter((u) => u.mode !== "parent");
    const enf = par.flatMap((u) => ((u.famille && u.famille.enfants) || []).map((e) => ({ ...e, p: u })));
    const relies = users.filter((u) => (u.parents || []).length);
    const tile = (v, t) => `<div class="card" style="text-align:center"><p class="score">${v}</p><p class="small muted">${t}</p></div>`;
    const t = { eleve: CFG.price_fcfa, parent: 1500, enfant_sup: 500, suivi: 2000, ...(CFG.formules || {}) };
    const st = { attente: "⏳ en attente", en_cours: "🟢 en cours", termine: "✅ terminé" };
    box.innerHTML = `<div class="grid">${tile(seuls.length, "🎒 comptes élève seul")}${tile(par.length, "👨‍👩‍👧 comptes parent")}${tile(enf.length, "enfants suivis par un parent")}${tile(enf.filter((e) => e.type === "local").length, "sur le téléphone du parent")}${tile(relies.length, "élèves reliés à un parent")}${tile(par.filter((u) => u.premium).length, "parents premium")}${tile((suivis || []).filter((x) => x.statut === "attente").length, "suivis à traiter")}${tile((suivis || []).length, "suivis demandés")}</div>
      <div class="card"><h2>👁 Voir l'appli comme…</h2><p class="small muted">Ton propre compte passe dans le mode choisi (rien ne change pour les clients).</p><div class="row"><button class="btn alt" style="flex:1" data-voir="eleve">🎒 Élève seul</button><button class="btn alt" style="flex:1" data-voir="parent">👨‍👩‍👧 Parent répétiteur</button></div></div>
      <div class="card"><h2>💲 Tarifs (modulables)</h2><p class="small muted">Changés ici, ils s'appliquent tout de suite dans l'appli de chacun (au prochain lancement).</p>
        ${[["eleve", "🎒 Élève seul"], ["parent", "👨‍👩‍👧 Parent répétiteur (1 enfant)"], ["enfant_sup", "➕ Par enfant en plus"], ["suivi", "🎯 Suivi spécifique (par enfant)"]].map(([k, l]) => `<label class="small">${l}</label><input class="field" inputmode="numeric" data-tarif="${k}" value="${t[k]}">`).join("")}
        <button class="btn" id="tsave">Enregistrer les tarifs</button><p class="small" id="tmsg"></p></div>
      <div class="card"><h2>🎯 Suivis spécifiques</h2>${(suivis || []).length ? suivis.sort((a, b) => (a.statut === "attente" ? -1 : 1) - (b.statut === "attente" ? -1 : 1) || (b.at || 0) - (a.at || 0)).map((x) => `<div class="card"><p><b>${esc(x.enfant || "")}</b> · ${esc(x.level || "")} · ${st[x.statut] || esc(x.statut || "")}</p>
          <p class="small muted">Parent : ${esc(x.pnom || "")} · 📱 ${esc(x.tel || "")} · ${fmt(x.at)}</p><p class="small"><b>Objectif :</b> ${esc(x.objectif || "")}</p>
          ${x.dispo ? `<p class="small"><b>Disponibilités :</b> ${esc(x.dispo)}</p>` : ""}${(x.matieres || []).length ? `<p class="small"><b>Matières :</b> ${esc(x.matieres.map(subjName).join(", "))}</p>` : ""}
          ${x.resume ? `<details class="small"><summary>Résultats de l'enfant</summary><pre style="white-space:pre-wrap">${esc(x.resume)}</pre></details>` : ""}
          ${(x.conseils || []).map((c) => `<p class="small" style="border-left:3px solid var(--accent);padding-left:6px">${esc(c.t)}<br><span class="muted">${new Date(c.at).toLocaleDateString("fr-FR")}</span></p>`).join("")}
          <textarea class="field" rows="3" maxlength="1500" data-cons="${esc(x.id)}" placeholder="Plan ou conseil pour ce parent (il le voit dans la fiche de l'enfant)"></textarea>
          <div class="row"><select class="field" data-st="${esc(x.id)}" style="flex:1">${Object.entries(st).map(([k, v]) => `<option value="${k}"${k === (x.statut === "attente" ? "en_cours" : x.statut) ? " selected" : ""}>${v}</option>`).join("")}</select><button class="btn small" data-envoi="${esc(x.id)}">Envoyer</button></div>
          ${x.tel ? `<a class="small" target="_blank" rel="noopener" href="https://wa.me/221${esc(String(x.tel).replace(/\D/g, "").slice(-9))}">Écrire sur WhatsApp</a>` : ""}<p class="small" data-res="${esc(x.id)}"></p></div>`).join("") : `<p class="small muted">Aucune demande pour le moment.</p>`}</div>
      <div class="card"><h2>👨‍👩‍👧 Comptes parent</h2>${par.length ? par.map((u) => `<div style="padding:6px 0;border-bottom:1px solid rgba(127,127,127,.2)"><p class="small"><b>${esc(u.name || "Sans nom")}</b>${u.premium ? " ⭐" : ""} · ${esc(u.phone ? "📱 " + u.phone : u.email)}${meme(u)}</p>
          <p class="small muted">${((u.famille && u.famille.enfants) || []).map((e) => `${e.type === "compte" ? "📱" : "👦"} ${esc(e.nom)} (${esc(e.level)}${e.type === "compte" && !e.uid ? ", code non tapé" : ""}) · ${(e.missions || []).length} missions · ${(e.seances || []).length} séances`).join("<br>") || "aucun enfant ajouté"}</p></div>`).join("") : `<p class="small muted">Aucun compte parent pour l'instant.</p>`}</div>`;
    box.querySelectorAll("[data-voir]").forEach((b) => (b.onclick = () => { S.mode = b.dataset.voir; store.save(); Compte.setFamille(S.mode, S.famille || null); go(S.mode === "parent" ? "famille" : "accueil"); }));
    document.getElementById("tsave").onclick = async () => {
      const rec = {}; box.querySelectorAll("[data-tarif]").forEach((i) => { const v = parseInt(i.value.replace(/\D/g, ""), 10); if (v >= 0) rec[i.dataset.tarif] = v; });
      const m = document.getElementById("tmsg");
      try { await Compte.setTarifs(rec); CFG.formules = { ...(CFG.formules || {}), ...rec }; if (rec.eleve) CFG.price_fcfa = rec.eleve; m.className = "msg-ok small"; m.textContent = "Tarifs enregistrés ✓"; }
      catch (e) { m.className = "msg-ko small"; m.textContent = "Refusé : " + (e.code || e.message); }
    };
    box.querySelectorAll("[data-envoi]").forEach((b) => (b.onclick = async () => {
      const id = b.dataset.envoi, txt = box.querySelector(`[data-cons="${id}"]`).value.trim(), statut = box.querySelector(`[data-st="${id}"]`).value, r = box.querySelector(`[data-res="${id}"]`);
      b.disabled = true;
      try { await Compte.adminConseil(id, txt, statut); suivis = null; r.className = "msg-ok small"; r.textContent = "Envoyé ✓ : le parent le voit dans la fiche de l'enfant."; }
      catch (e) { b.disabled = false; r.className = "msg-ko small"; r.textContent = "Refusé : " + (e.code || e.message); }
    }));
  }

  globalThis.viewAdmin = viewAdmin;
})();
