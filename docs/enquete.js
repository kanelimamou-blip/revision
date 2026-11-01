"use strict";
// Questionnaire parents (#enquete ou #enquete/<source>, ex. #enquete/bureau) : ouvert sans compte.
// Présente l'appli en court, pose quelques questions sur les enfants et le soutien scolaire, puis propose l'essai gratuit.
// Les réponses vont dans Firestore « enquetes » (création seule, lecture par l'admin : onglet 📋 Enquête).
// Le téléphone n'est demandé que si le parent accepte d'être recontacté (loi sénégalaise 2008-12 sur les données personnelles).
(() => {
  const CLASSES = [["Élémentaire", ["CI", "CP", "CE1", "CE2", "CM1", "CM2"]], ["Collège", ["6e", "5e", "4e", "3e"]], ["Lycée", ["2nde", "1re", "Tle"]]];
  const REPET = ["Oui, un répétiteur à la maison", "Oui, des cours de renfort à l'école ou en groupe", "Non, je l'aide moi-même", "Non, personne ne l'aide"];
  const BUDGET = ["Rien", "Moins de 10 000 F", "10 000 à 25 000 F", "25 000 à 50 000 F", "Plus de 50 000 F"];
  const DIFF = ["Maths", "Français", "Sciences", "Anglais", "Méthode de travail", "Préparer un examen (CFEE, BFEM, BAC)", "Je n'ai pas le temps de suivre"];
  // prix proposés dans le questionnaire (à tester auprès des parents ; les prix de l'appli se règlent dans l'admin, onglet 💲 Prix)
  // ils se règlent dans l'admin (onglet 📋 Enquête), enregistrés dans config/enquete
  const DEF = { eleve: 1000, parent: 3000, suivi: 5000 };
  let PRIX = null;
  const T = () => ({ ...DEF, ...(PRIX || {}) });
  const radio = (n, opts) => opts.map((o, i) => `<label class="row chk"><span><input type="radio" name="${n}" value="${esc(o)}"${i === -1 ? " checked" : ""}> ${esc(o)}</span></label>`).join("");
  const cases = (n, opts) => opts.map((o) => `<label class="chip-c"><input type="checkbox" name="${n}" value="${esc(o)}"> ${esc(o)}</label>`).join("");
  const val = (f, n) => (f.querySelector(`[name="${n}"]:checked`) || {}).value || "";
  const vals = (f, n) => [...f.querySelectorAll(`[name="${n}"]:checked`)].map((x) => x.value);

  globalThis.viewEnquete = (src) => {
    src = String(src || "lien").replace(/[^\w-]/g, "").slice(0, 40) || "lien";
    document.getElementById("exam-tag").textContent = "";
    document.body.classList.add("enq-mode"); // le questionnaire seul : pas d'onglets ni de menu
    if (S.enqueteFaite) return merci(true);
    const t = T();
    $view.innerHTML = `<div class="card enq-hero"><h1>👋 2 minutes pour la réussite de vos enfants</h1>
      <p><b>Révision</b> est une appli sénégalaise de soutien scolaire, du CE1 à la Terminale : cours du programme officiel, exercices corrigés, sujets types du CFEE, du BFEM et du BAC, jeux éducatifs pour les petits, et un espace parent pour suivre son enfant.</p>
      <p class="small muted">Ce questionnaire nous aide à adapter l'appli aux familles. Il est anonyme : votre nom et votre numéro ne sont demandés que si vous voulez être recontacté.</p></div>
      <form id="enq" class="card">
        <h2>1. Combien d'enfants scolarisés avez-vous ?</h2><div class="row wrap">${["1", "2", "3", "4", "5 ou plus"].map((x) => `<label class="chip-c"><input type="radio" name="enfants" value="${x}"> ${x}</label>`).join("")}</div>
        <h2>2. Dans quelles classes sont-ils ?</h2>${CLASSES.map(([g, l]) => `<p class="small muted">${g}</p><div class="row wrap">${cases("classes", l)}</div>`).join("")}
        <h2>3. Ont-ils de l'aide pour leurs devoirs ?</h2>${radio("repet", REPET)}
        <h2>4. Combien payez-vous par mois pour cette aide (tous enfants) ?</h2>${radio("budget", BUDGET)}
        <h2>5. Où vos enfants ont-ils le plus de difficultés ?</h2><div class="row wrap">${cases("diff", DIFF)}</div>
        <h2>6. Un répétiteur sur téléphone vous intéresserait-il ?</h2>
        <p class="small muted">Leçons, exercices corrigés et devoirs types de leur classe, disponibles le soir et le week-end, avec le suivi des progrès.</p>
        ${radio("interet", ["Oui", "Peut-être, je veux d'abord essayer", "Non"])}
        <div class="enq-plus"><h2>💡 Ce que l'appli apporte à votre enfant</h2>
          <ul class="steps">
            <li><b>Tout le programme officiel sénégalais</b>, du CE1 à la Terminale, chapitre par chapitre : la leçon en court, puis des questions corrigées et expliquées.</li>
            <li><b>Des exercices corrigés étape par étape</b> et des devoirs types, avec des sujets types du CFEE, du BFEM et du BAC.</li>
            <li><b>Des exercices nouveaux à chaque fois</b> : l'enfant ne peut pas apprendre les réponses par cœur.</li>
            <li><b>« Je bloque »</b> : un indice, puis la méthode, puis un exercice semblable corrigé, au lieu de donner directement la réponse.</li>
            <li><b>Pour les petits</b> (CE1 à CM2) : gros boutons, leçons lues à voix haute, étoiles et jeux sur le programme de la classe.</li>
            <li><b>Pour vous, parent</b> : vous voyez ses progrès et ses erreurs, vous lui donnez des missions, et l'appli suit l'emploi du temps de l'école.</li></ul>
          <h2>🤝 La différence avec un répétiteur classique</h2>
          <ul class="steps">
            <li><b>Disponible tous les jours, à toute heure</b>, même le soir et le week-end, et même sans connexion une fois chargée.</li>
            <li><b>Beaucoup moins cher</b> qu'un répétiteur chaque mois, et un seul paiement couvre toutes les matières.</li>
            <li><b>Vous savez ce qui a été travaillé</b> : chaque séance et chaque note sont gardées.</li>
            <li><b>Ce n'est pas l'un ou l'autre</b> : l'appli peut aussi aider le répétiteur. Et avec la formule « suivi personnalisé », une personne de l'équipe suit votre enfant avec l'appli.</li></ul>
          <h2>📚 D'où vient le contenu</h2>
          <ul class="steps">
            <li>Il suit le <b>programme officiel du ministère de l'Éducation nationale du Sénégal</b>, classe par classe et chapitre par chapitre.</li>
            <li>Il utilise uniquement des <b>documents officiels et publics</b>, comme les programmes et les sujets d'examens publiés. Aucun document privé ou payant n'est copié.</li>
            <li>Les exercices et sujets types sont <b>rédigés pour l'appli</b> sur le modèle des examens, et ils sont présentés comme tels. Les sources sont indiquées dans l'appli.</li></ul>
          <h2>🔒 Vos données sont protégées</h2>
          <ul class="steps">
            <li>Le compte se crée avec <b>un numéro et un code secret</b>. Chacun ne voit que ses propres données, et le parent voit seulement les enfants qu'il a reliés.</li>
            <li>Les données sont gardées chez <b>Google Firebase</b>, un service sécurisé, sur des serveurs en Europe.</li>
            <li><b>Pas de publicité</b> dans l'appli. Les données ne sont <b>ni vendues ni partagées</b>.</li>
            <li>Il suffit de nous écrire pour faire <b>supprimer</b> un compte et ses données.</li></ul></div>
        <h2>7. Quelle formule vous conviendrait ?</h2>
        <label class="row chk"><span><input type="radio" name="formule" value="eleve"> 🎒 <b>L'enfant révise seul</b> : <b data-px="eleve">${fcfa(t.eleve)}</b></span></label>
        <label class="row chk"><span><input type="radio" name="formule" value="parent"> 👨‍👩‍👧 <b>Je suis son répétiteur</b> avec l'espace parent (missions, séances, suivi) : <b data-px="parent">${fcfa(t.parent)}</b></span></label>
        <label class="row chk"><span><input type="radio" name="formule" value="suivi"> 🧑‍🏫 <b>Un suivi personnalisé</b> par notre équipe, avec l'appli : <b data-px="suivi">${fcfa(t.suivi)}</b></span></label>
        <label class="row chk"><span><input type="radio" name="formule" value="aucune"> Aucune pour le moment</span></label>
        <h2>8. Voulez-vous être recontacté ?</h2>
        <label class="row chk"><span><input type="checkbox" name="contact" id="contact"> Oui, j'accepte d'être contacté par l'équipe Révision au sujet de l'appli</span></label>
        <div id="coord" hidden><input class="field" name="prenom" placeholder="Votre prénom" maxlength="60"><input class="field" name="tel" placeholder="Votre numéro (WhatsApp)" inputmode="tel" maxlength="20">
          <p class="small muted">Votre numéro sert uniquement à vous recontacter au sujet de l'appli. Il n'est ni vendu ni partagé. Vous pouvez demander sa suppression à tout moment.</p></div>
        <h2>Une remarque ? (facultatif)</h2><textarea class="field" name="remarque" rows="2" maxlength="500"></textarea>
        <p class="small" id="enq-msg"></p>
        <button class="btn" type="submit">Envoyer mes réponses</button></form>`;
    if (!PRIX) Compte.getEnquetePrix().then((p) => { if (!p) return; PRIX = p; const t2 = T(); $view.querySelectorAll("[data-px]").forEach((b) => (b.textContent = fcfa(t2[b.dataset.px] || 0))); }).catch(() => {});
    const f = $view.querySelector("#enq");
    f.querySelector("#contact").onchange = (e) => (f.querySelector("#coord").hidden = !e.target.checked);
    f.onsubmit = async (e) => {
      e.preventDefault();
      const m = f.querySelector("#enq-msg"), contact = f.querySelector("#contact").checked;
      const rec = { src, enfants: val(f, "enfants"), classes: vals(f, "classes").slice(0, 13), repet: val(f, "repet"), budget: val(f, "budget"), diff: vals(f, "diff").slice(0, 8),
        interet: val(f, "interet"), formule: val(f, "formule"), contact, prenom: contact ? f.prenom.value.trim().slice(0, 60) : "", tel: contact ? f.tel.value.replace(/[^\d+ ]/g, "").slice(0, 20) : "", remarque: f.remarque.value.trim().slice(0, 500) };
      if (!rec.enfants || !rec.interet) { m.textContent = "Merci de répondre au moins aux questions 1 et 6."; return; }
      if (contact && rec.tel.replace(/\D/g, "").length < 9) { m.textContent = "Indiquez un numéro à 9 chiffres pour être recontacté, ou décochez la case."; return; }
      const b = f.querySelector("button[type=submit]"); b.disabled = true; m.textContent = "Envoi…";
      try { await Compte.envoyerEnquete(rec); S.enqueteFaite = today(); S.enqueteFormule = rec.formule; store.save(); merci(false); }
      catch (er) { b.disabled = false; m.textContent = "L'envoi n'a pas marché. Vérifiez votre connexion et réessayez."; Compte.logError && Compte.logError("Enquête : " + (er.code || er.message)); }
    };
  };
  const merci = (deja) => {
    $view.innerHTML = `<div class="card enq-hero"><h1>🙏 Merci${deja ? ", vous avez déjà répondu" : " pour vos réponses"} !</h1>
      <p>Essayez maintenant l'appli avec votre enfant : <b>${typeof TRIAL_DAYS !== "undefined" ? TRIAL_DAYS : 15} jours gratuits</b>, tout est ouvert, sans paiement.</p>
      <ol class="steps"><li>Créez un compte avec votre numéro.</li><li>Choisissez « élève seul » ou « parent ».</li><li>Choisissez la classe de l'enfant et commencez.</li></ol>
      <a class="btn" href="#accueil">▶️ Essayer l'appli gratuitement</a></div>`;
  };

  // ---------- admin : synthèse et liste des réponses
  globalThis.enqueteAdmin = async (box) => {
    let rs; try { rs = await Compte.adminEnquetes(); } catch (e) { box.innerHTML = `<div class="card"><p>Lecture refusée (${esc(e.code || e.message)}). Publie les nouvelles règles Firestore.</p></div>`; return; }
    const n = rs.length, cnt = (k, multi) => { const o = {}; rs.forEach((r) => (multi ? r[k] || [] : [r[k] || "—"]).forEach((x) => (o[x] = (o[x] || 0) + 1))); return Object.entries(o).sort((a, b) => b[1] - a[1]); };
    const bloc = (titre, k, multi) => `<div class="card"><h2>${titre}</h2>${cnt(k, multi).map(([x, c]) => `<div class="row"><span>${esc(x)}</span><b>${c} · ${n ? Math.round((100 * c) / n) : 0} %</b></div>`).join("") || "<p class='muted'>Aucune réponse.</p>"}</div>`;
    const NOMS = { eleve: "🎒 Élève seul", parent: "👨‍👩‍👧 Parent répétiteur", suivi: "🧑‍🏫 Suivi par l'équipe", aucune: "Aucune" };
    const lien = location.origin + location.pathname + "#enquete/bureau"; // le QR code mène à #enquete/qr
    const px = { ...DEF, ...((await Compte.getEnquetePrix().catch(() => null)) || {}) };
    box.innerHTML = `<div class="card" style="text-align:center"><h2>📷 QR code du questionnaire</h2><img src="icons/qr-enquete.png" alt="QR code du questionnaire" style="width:100%;max-width:300px;background:#fff;padding:10px;border-radius:12px">
        <p class="small muted">Le parent vise le code avec l'appareil photo : il arrive directement sur le questionnaire, qu'il ait un compte ou non, sans les menus de l'appli.</p></div>
      <div class="card" style="gap:8px"><h2>💲 Prix proposés dans le questionnaire</h2><p class="small muted">En FCFA. Ils ne changent que le questionnaire, pas les prix de l'appli (onglet 💲 Prix).</p>
        ${[["eleve", "🎒 L'enfant révise seul"], ["parent", "👨‍👩‍👧 Le parent est le répétiteur"], ["suivi", "🧑‍🏫 Suivi personnalisé par l'équipe"]].map(([k, l]) => `<label class="small">${l}</label><input class="field" inputmode="numeric" data-ep="${k}" value="${px[k]}">`).join("")}
        <button class="btn" id="epsave">Enregistrer ces prix</button><p class="small" id="epmsg"></p></div>
      <div class="card"><h2>📋 Questionnaire parents</h2><p><b>${n}</b> réponse${n > 1 ? "s" : ""} · ${rs.filter((r) => r.contact).length} à recontacter</p>
      <p class="small">Lien à envoyer (le mot après « enquete/ » dit d'où vient la réponse : bureau, whatsapp, ecole…) :</p><p><code>${esc(lien)}</code></p>
      <button class="btn alt small" id="cp">Copier le lien</button></div>
      ${bloc("Intérêt pour un répétiteur sur téléphone", "interet")}
      ${bloc("Formule choisie", "formule").replace(/>(eleve|parent|suivi|aucune)</g, (_, k) => `>${NOMS[k]}<`)}
      ${bloc("Aide actuelle", "repet")}${bloc("Budget mensuel actuel", "budget")}${bloc("Classes", "classes", true)}${bloc("Difficultés", "diff", true)}${bloc("Source", "src")}
      <div class="card"><h2>À recontacter</h2>${rs.filter((r) => r.contact).map((r) => `<p><b>${esc(r.prenom || "—")}</b> · ${esc(r.tel)} · ${esc((r.classes || []).join(", "))} · ${esc(NOMS[r.formule] || "")}${r.remarque ? `<br><span class="small muted">« ${esc(r.remarque)} »</span>` : ""}<br><span class="small muted">${r.at ? r.at.toLocaleString("fr-FR") : ""}</span></p>`).join("") || "<p class='muted'>Personne pour le moment.</p>"}</div>
      <div class="card"><h2>Remarques</h2>${rs.filter((r) => r.remarque && !r.contact).map((r) => `<p class="small">« ${esc(r.remarque)} »</p>`).join("") || "<p class='muted'>Aucune.</p>"}</div>`;
    box.querySelector("#epsave").onclick = async (ev) => { const r = {}, m = box.querySelector("#epmsg");
      box.querySelectorAll("[data-ep]").forEach((i) => (r[i.dataset.ep] = parseInt(i.value.replace(/\D/g, ""), 10)));
      if (Object.values(r).some((v) => !(v >= 0))) { m.textContent = "Remplis les trois prix en chiffres."; return; }
      ev.target.disabled = true; try { await Compte.setEnquetePrix(r); PRIX = r; m.textContent = "Prix enregistrés ✓ Le questionnaire les affiche dès maintenant."; } catch (e) { m.textContent = "Refusé : " + (e.code || e.message); } ev.target.disabled = false; };
    box.querySelector("#cp").onclick = () => navigator.clipboard && navigator.clipboard.writeText(lien).then(() => (box.querySelector("#cp").textContent = "Copié ✔"));
  };
})();
