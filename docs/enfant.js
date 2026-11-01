"use strict";
// Mode enfant (CE1 à CM2, 7 à 11 ans) : même appli, présentation adaptée à l'âge.
// Accueil simple en grosses tuiles, une matière = sa liste de leçons, séries de 10 questions,
// encouragements, étoiles au lieu des notes sur 20, lecture à voix haute (synthèse vocale du téléphone, gratuite).
// Branché dans app.js : render (classe CSS), viewHome, chooseMode, questionBlock/bindQuestion, fin de QCM.
(() => {
  const KID = ["CE1", "CE2", "CM1", "CM2"];
  globalThis.isKid = () => typeof S !== "undefined" && KID.includes(S.level);
  const petit = () => ["CE1", "CE2"].includes(S.level);

  // ---------- lecture à voix haute
  const voix = () => (window.speechSynthesis ? speechSynthesis.getVoices().find((v) => /^fr/i.test(v.lang)) : null);
  const parler = (txt) => {
    if (!window.speechSynthesis) return false;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(String(txt).replace(/___/g, "…").replace(/×/g, " fois ").replace(/÷/g, " divisé par ").replace(/−/g, " moins "));
    u.lang = "fr-FR"; u.rate = petit() ? 0.85 : 0.95; const v = voix(); if (v) u.voice = v;
    speechSynthesis.speak(u); return true;
  };
  globalThis.kidParler = parler;
  globalThis.kidSpeakBtn = () => (window.speechSynthesis ? `<button class="kid-voix" type="button" aria-label="Écouter">🔊 Écouter</button>` : "");
  globalThis.kidBindSpeak = (root, q) => { const b = root.querySelector(".kid-voix"); if (b) b.onclick = () => parler(`${q.q}. ${q.c.map((c, i) => `${LETTERS[i]} : ${c}`).join(". ")}`); };

  // ---------- encouragements
  const BRAVO = ["Bravo ! 🎉", "Super ! ⭐", "Génial ! 🥳", "Excellent ! 🏆", "Tu es fort ! 💪", "Bien joué ! 👏", "Champion ! 🦁"];
  const PRESQUE = ["Presque ! 💪", "Pas grave, on apprend ! 🌱", "Essaie encore la prochaine ! 🙂"];
  globalThis.kidCheer = (ok) => { const l = ok ? BRAVO : PRESQUE; return l[Math.floor(Math.random() * l.length)]; };
  globalThis.kidPop = (el) => { if (!el) return; const s = document.createElement("span"); s.className = "kid-pop"; s.textContent = "⭐"; el.appendChild(s); setTimeout(() => s.remove(), 900); };
  // fin de série : des étoiles plutôt qu'une note sur 20
  globalThis.kidScore = (score, total) => {
    const r = total ? score / total : 0, n = r >= 0.8 ? 3 : r >= 0.5 ? 2 : r > 0 ? 1 : 0;
    const mot = n === 3 ? "Bravo, tu as tout compris ! 🎉" : n === 2 ? "C'est bien ! Encore un petit effort. 👍" : n === 1 ? "Tu progresses ! Relis la leçon et recommence. 🌱" : "On recommence ensemble ? Relis d'abord la leçon. 📖";
    return `<p class="kid-etoiles" aria-label="${n} étoiles sur 3">${"⭐".repeat(n)}${"☆".repeat(3 - n)}</p>
      <p class="kid-big">${score} bonne${score > 1 ? "s" : ""} réponse${score > 1 ? "s" : ""} sur ${total}</p><p><b>${mot}</b></p>`;
  };
  globalThis.kidQuizLen = 10;

  // ---------- matières en couleurs
  const ICO = { maths: ["🔢", "#ffe9a8"], francais: ["📚", "#d9e6ff"], sciences: ["🌱", "#d6f2dc"], histoire: ["🏛️", "#f6dccb"], geo: ["🌍", "#d4eef4"], civique: ["🤝", "#efdaf3"] };
  const ico = (sid) => ICO[sid.split("-").slice(1).join("-")] || ["📘", "#eee"];
  const etoiles = () => Object.values(S.stats || {}).reduce((n, s) => n + (s.ok || 0), 0);

  globalThis.kidHome = () => {
    const nom = myName(), [href, label] = suite(), subs = subjectsOf(S.level);
    const free = DATA.questions.filter((q) => q.free && inLevel(q)), daily = free.length ? free[Math.floor(new Date(today()).getTime() / 864e5) % free.length] : null;
    const tuile = (h, i, t, c = "") => `<a class="kid-tuile" href="${h}"${c ? ` style="background:${c}"` : ""}><span class="kid-ico">${i}</span><b>${t}</b></a>`;
    $view.innerHTML = `
      ${Compte.isAdmin && Compte.isAdmin() ? `<a class="btn" href="#admin/activite">🛠️ Espace admin</a>` : ""}
      ${typeof missionsCard === "function" ? missionsCard() : ""}
      ${!S.premium && trialLeft() > 0 ? `<a class="trial" href="#premium">🎁 Essai gratuit : tout est ouvert encore <b>${trialLeft()} jour${trialLeft() > 1 ? "s" : ""}</b></a>` : ""}
      ${!isPremium() ? `<a class="trial" href="#premium">🔒 L'essai gratuit est terminé. Demande à un parent de t'abonner pour continuer.</a>` : ""}
      <div class="card kid-hello"><div class="kid-mascotte">🦁</div><div><h1>${nom ? `Bonjour ${esc(nom)} !` : "Bonjour !"}</h1>
        <p>Tu as gagné <b>${etoiles().toLocaleString("fr-FR")} ⭐</b> · Série : <b>${streak()} 🔥</b></p></div></div>
      <a class="kid-go" href="${href}">▶️ <span>On continue !<small>${esc(label)}</small></span></a>
      ${typeof planSoirCard === "function" ? planSoirCard(true) : ""}
      <h2 class="kid-h">Mes matières</h2>
      <div class="kid-grille">${subs.map((s) => { const [i, c] = ico(s.id); return tuile(`#matiere/${s.id}`, i, esc(s.name), c); }).join("")}</div>
      <h2 class="kid-h">Je m'entraîne</h2>
      <div class="kid-grille">${tuile("#annales", "📝", examOf() ? `Sujets du ${examOf()[0]}` : "Devoirs types")}${tuile("#exercices", "✏️", "Exercices")}${tuile("#erreurs", "🔁", "Mes erreurs")}${tuile("#aide", "🆘", "Je bloque")}${tuile("#pilotage", "📅", "Mon emploi du temps")}${tuile("#progres", "📈", "Mes progrès")}</div>
      ${daily ? `<div class="card" id="daily"><h2>❓ La question du jour</h2><p class="small muted">${esc(subjName(daily.s))}</p>${questionBlock(daily)}</div>` : ""}
      ${globalThis.legalFooter ? legalFooter() : ""}`;
    if (daily) bindQuestion($view.querySelector("#daily"), daily, () => {});
  };

  // une matière : ses leçons dans l'ordre, chacune avec « Leçon » et « Questions »
  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  ROUTES.matiere = (sid) => {
    const s = (DATA.subjects || []).find((x) => x.id === sid);
    if (!s) return go("accueil");
    const [i, c] = ico(sid), titres = (DATA.programmes || {})[sid] || [], nots = (DATA.notions || {})[sid] || [];
    const nq = (k) => qsOf(sid).filter((q) => q.ch === k).length;
    $view.innerHTML = `<div class="kid-titre" style="background:${c}"><span class="kid-ico">${i}</span><h1>${esc(s.name)}</h1></div>
      <p class="muted">Choisis une leçon. Lis-la (ou écoute-la), puis réponds aux questions pour gagner des étoiles.</p>
      ${titres.map((t, k) => { const n = nots.find((x) => +x.pch === k) || nots[k];
        return `<div class="card kid-lecon"><b>${k + 1}. ${esc(t)}</b><div class="kid-btns">
          ${n ? `<a class="btn alt" href="#notion/${n.id}">📖 La leçon</a>` : ""}${nq(k) ? `<a class="btn" href="#quiz/${sid}/${k}">🎮 Les questions</a>` : ""}</div></div>`; }).join("")}
      <a class="btn alt" href="#accueil">↩ Retour</a>`;
  };

  // bouton « Écouter la leçon » sur les pages de cours
  const apres = () => {
    document.body.classList.toggle("kid", isKid());
    if (!isKid() || !window.speechSynthesis) return;
    if (/^#(notion|fiche)\//.test(location.hash) && !$view.querySelector(".kid-voix-lecon") && !$view.querySelector("[data-say]")) {
      const b = document.createElement("button"); b.className = "btn kid-voix-lecon"; b.type = "button"; b.textContent = "🔊 Écouter la leçon";
      let on = false;
      b.onclick = () => { if (on) { speechSynthesis.cancel(); on = false; b.textContent = "🔊 Écouter la leçon"; return; }
        on = true; b.textContent = "⏹️ Arrêter"; parler($view.innerText.replace(/🔊 Écouter la leçon|⏹️ Arrêter/g, "").slice(0, 4000)); };
      $view.prepend(b);
    }
  };
  window.addEventListener("hashchange", () => { if (window.speechSynthesis) speechSynthesis.cancel(); setTimeout(apres, 0); });
  globalThis.kidApres = apres;
})();
