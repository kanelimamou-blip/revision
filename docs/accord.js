"use strict";
// Accord du parent avant l'abonnement.
// 1) L'élève demande l'accord : un lien personnel (#accord/<jeton>) part par WhatsApp vers son parent.
// 2) Le parent ouvre le lien sans compte, lit le résumé, écrit son nom et son numéro, et touche « J'autorise ».
// 3) Le paiement se débloque chez l'élève. L'admin garde la trace (élève, parent, lien, date, version des conditions).
// En 1re et en Terminale seulement, un élève majeur peut déclarer sa date de naissance à la place.
(() => {
  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  const OK = ["ok", "majeur"];
  const LIENS = { pere: "Père", mere: "Mère", tuteur: "Tuteur ou tutrice" };
  const jeton = () => [...crypto.getRandomValues(new Uint8Array(24))].map((b) => "abcdefghijkmnopqrstuvwxyz23456789"[b % 33]).join("");
  const lien = (t) => location.origin + location.pathname + "#accord/" + t;
  const date = (d) => (d ? d.toLocaleString("fr-FR", { day: "numeric", month: "long", year: "numeric", hour: "2-digit", minute: "2-digit" }) : "");
  const nomEleve = () => ((Compte.user && Compte.user.displayName) || S.name || "").slice(0, 60);
  const peutMajeur = () => /^(1ère|Tle)/.test(S.level || "");
  const age = (n) => { const d = new Date(n + "T12:00"), t = new Date(); let a = t.getFullYear() - d.getFullYear(); if (t < new Date(t.getFullYear(), d.getMonth(), d.getDate())) a--; return a; };

  // l'accord est-il nécessaire avant de payer ?
  globalThis.accordRequis = () => !!(CFG && CFG.accord_parent) && Compte.enabled && !!Compte.user && !Compte.isAdmin() && !S.premium && !(S.accord && OK.includes(S.accord.statut));

  const message = (t) => `Bonjour, c'est ${nomEleve() || "ton enfant"}. Pour m'abonner à l'appli de révision Révision (${fcfa(CFG.price_fcfa)}, une seule fois, jusqu'à l'examen), j'ai besoin de ton accord. Ouvre ce lien, lis et touche « J'autorise » : ${lien(t)}`;
  function envoyer(t) {
    const txt = message(t);
    if (navigator.share) return navigator.share({ text: txt }).catch(() => {});
    window.open("https://wa.me/?text=" + encodeURIComponent(txt), "_blank", "noopener");
  }

  // Encadré dans Premium, à la place du paiement tant que l'accord manque
  globalThis.accordBox = async function accordBox() {
    const box = document.getElementById("accordbox"); if (!box) return;
    const a = S.accord;
    if (a && a.token && a.statut === "attente") {
      box.innerHTML = `<div class="card" style="border:2px solid #f5a623"><h2>👪 Accord de ton parent</h2><p>⏳ Demande envoyée${a.at ? " le " + esc(date(new Date(a.at))) : ""}. On attend que ton parent touche « J'autorise ».</p>
        <p class="small muted">Dès qu'il a accepté, le paiement apparaît ici.</p>
        <div class="row"><button class="btn" style="flex:1" id="acc-check">Vérifier</button><button class="btn alt" style="flex:1" id="acc-send">Renvoyer le message</button></div>
        <button class="linkbtn small" id="acc-new">Faire une nouvelle demande</button><p class="small" id="acc-msg"></p></div>`;
      const verifier = async (manuel) => {
        const d = await Compte.lireAccord(a.token).catch(() => null);
        if (d && d.statut === "ok") { S.accord = { ...a, statut: "ok", parent: d.parent, ptel: d.ptel || "", okAt: d.okAt ? d.okAt.getTime() : Date.now() }; store.save(); return viewPremium(); }
        if (manuel) { const m = document.getElementById("acc-msg"); if (m) { m.className = "small muted"; m.textContent = d ? "Pas encore d'accord. Demande à ton parent d'ouvrir le lien." : "Demande introuvable : fais une nouvelle demande."; } }
      };
      document.getElementById("acc-check").onclick = () => verifier(true);
      document.getElementById("acc-send").onclick = () => envoyer(a.token);
      document.getElementById("acc-new").onclick = () => { S.accord = null; store.save(); accordBox(); };
      verifier(false);
      return;
    }
    box.innerHTML = `<div class="card"><h2>👪 D'abord, l'accord de ton parent</h2>
      <p>Avant de payer, un parent ou un tuteur doit être d'accord. Tu lui envoies un lien par WhatsApp. Il l'ouvre, lit et touche « J'autorise ». C'est tout.</p>
      <button class="btn hi-btn" id="acc-ask">Demander l'accord de mon parent</button>
      ${peutMajeur() ? `<details class="small" style="margin-top:10px"><summary>J'ai 18 ans ou plus</summary><div style="display:grid;gap:8px;margin-top:8px">
        <label>Ma date de naissance<input class="field" type="date" id="acc-nais" max="${new Date().toISOString().slice(0, 10)}"></label>
        <label style="display:flex;gap:8px;align-items:flex-start"><input type="checkbox" id="acc-cert" style="margin-top:3px"><span>Je certifie avoir 18 ans ou plus. Une fausse déclaration est de ma seule responsabilité.</span></label>
        <button class="btn alt" id="acc-maj">Valider</button></div></details>` : ""}
      <p class="small" id="acc-msg"></p><p class="small muted"><a href="#legal/parents">Ce que l'on dit aux parents</a></p></div>`;
    const msg = (t, ok) => { const m = document.getElementById("acc-msg"); m.className = ok ? "small msg-ok" : "small msg-ko"; m.textContent = t; };
    const base = () => ({ eleve: nomEleve(), tel: (S.phone || "").slice(0, 20), level: (S.level || "").slice(0, 30), v: globalThis.CGU_V || "" });
    document.getElementById("acc-ask").onclick = async () => {
      const t = jeton();
      try { await Compte.demanderAccord(t, { ...base(), statut: "attente" }); }
      catch (e) { return msg("La demande n'a pas pu être enregistrée. Vérifie ta connexion et réessaie."); }
      S.accord = { token: t, statut: "attente", at: Date.now() }; store.save();
      envoyer(t); accordBox();
    };
    const bm = document.getElementById("acc-maj");
    if (bm) bm.onclick = async () => {
      const n = document.getElementById("acc-nais").value;
      if (!/^\d{4}-\d{2}-\d{2}$/.test(n)) return msg("Écris ta date de naissance.");
      if (age(n) < 18) return msg("Tu as moins de 18 ans : demande l'accord de ton parent.");
      if (!document.getElementById("acc-cert").checked) return msg("Coche la case pour certifier ton âge.");
      const t = jeton();
      try { await Compte.demanderAccord(t, { ...base(), statut: "majeur", naissance: n }); }
      catch (e) { return msg("L'enregistrement n'a pas abouti. Vérifie ta connexion et réessaie."); }
      S.accord = { token: t, statut: "majeur", naissance: n, at: Date.now() }; store.save(); viewPremium();
    };
  };

  // Page du parent : sans compte, ouverte depuis le lien reçu
  async function viewAccord(t) {
    $view.innerHTML = `<div class="card"><p class="muted">Chargement…</p></div>`;
    const d = /^[a-z0-9]{20,40}$/.test(t || "") ? await Compte.lireAccord(t).catch(() => null) : null;
    if (!d || !["attente", "ok"].includes(d.statut)) { $view.innerHTML = `<div class="card"><h1>Lien invalide</h1><p>Ce lien d'accord n'existe pas ou n'est plus valable. Demandez à votre enfant de vous renvoyer le message depuis l'appli.</p></div>`; return; }
    const prix = fcfa(CFG.price_fcfa), pay = CFG.wave_number || CFG.om_number || "";
    if (d.statut === "ok") { $view.innerHTML = `<div class="card"><h1>✅ Accord déjà donné</h1><p>Vous avez autorisé l'abonnement de <b>${esc(d.eleve)}</b>${d.okAt ? " le " + esc(date(d.okAt)) : ""}. Merci.</p>${pay ? `<p class="small muted">Paiement : ${prix} par Wave ou Orange Money au ${esc(pay)}, de préférence depuis votre propre téléphone.</p>` : ""}</div>`; return; }
    $view.innerHTML = `<div class="card"><h1>👪 Accord du parent</h1>
      <p><b>${esc(d.eleve || "Votre enfant")}</b>${d.level ? ` (${esc(d.level)})` : ""} souhaite s'abonner à <b>Révision</b>, une appli de révision scolaire qui suit les programmes officiels du Sénégal.</p>
      <ul class="steps"><li>Prix : <b>${prix}</b>, payé une seule fois, valable jusqu'à l'examen. Aucun prélèvement automatique.</li><li>Usage uniquement éducatif : cours, exercices, sujets corrigés.</li><li>Pas de publicité, pas de discussion avec des inconnus. Les données ne sont jamais revendues.</li></ul>
      <p class="small"><a href="#legal/cgu">Conditions d'utilisation</a> · <a href="#legal/confidentialite">Confidentialité</a> · <a href="#legal/parents">Mot aux parents</a></p>
      <input class="field" id="p-nom" autocomplete="name" maxlength="60" placeholder="Votre prénom et nom">
      <input class="field" id="p-tel" type="tel" inputmode="numeric" autocomplete="tel" placeholder="Votre numéro (77 123 45 67)">
      <div class="row" style="flex-wrap:wrap;gap:6px">${Object.entries(LIENS).map(([k, v]) => `<label class="btn alt small" style="flex:1"><input type="radio" name="p-lien" value="${k}"> ${v}</label>`).join("")}</div>
      <label class="small" style="display:flex;gap:8px;align-items:flex-start"><input type="checkbox" id="p-ok" style="margin-top:3px"><span>Je suis le parent ou le tuteur légal de ${esc(d.eleve || "cet élève")}. J'autorise son abonnement à Révision et j'accepte les conditions d'utilisation.</span></label>
      <button class="btn hi-btn" id="p-go">J'autorise</button><p class="small" id="p-msg"></p></div>`;
    const msg = (x) => { const m = document.getElementById("p-msg"); m.className = "small msg-ko"; m.textContent = x; };
    document.getElementById("p-go").onclick = async () => {
      const nom = document.getElementById("p-nom").value.trim(), tel = Compte.normTel(document.getElementById("p-tel").value), l = (document.querySelector('input[name="p-lien"]:checked') || {}).value;
      if (nom.length < 2) return msg("Écrivez votre prénom et votre nom.");
      if (!tel) return msg("Numéro invalide : écrivez les 9 chiffres, par exemple 77 123 45 67.");
      if (!LIENS[l]) return msg("Indiquez si vous êtes le père, la mère ou le tuteur.");
      if (!document.getElementById("p-ok").checked) return msg("Cochez la case pour donner votre accord.");
      try { await Compte.donnerAccord(t, { parent: nom.slice(0, 60), ptel: tel.slice(0, 20), lien: l }); }
      catch (e) { return msg("L'accord n'a pas pu être enregistré. Vérifiez votre connexion et réessayez."); }
      $view.innerHTML = `<div class="card"><h1>✅ Merci, c'est noté</h1><p>Votre accord pour <b>${esc(d.eleve)}</b> est enregistré. Votre enfant peut maintenant payer dans l'appli.</p>${pay ? `<p>Pour plus de sûreté, vous pouvez payer vous-même : <b>${prix}</b> par Wave ou Orange Money au <b>${esc(pay)}</b>, puis votre enfant envoie la capture dans l'appli.</p>` : ""}</div>`;
    };
  }
  globalThis.viewAccord = viewAccord;
  ROUTES.accord = viewAccord;
  globalThis.LIENS_PARENT = LIENS;
})();
