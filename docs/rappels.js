"use strict";
// Nouveautés (pastille rouge tant que l'élève n'a pas lu), rappels guidés à la pause de midi et après l'école,
// petites questions à l'élève (réponses visibles dans l'admin), micro et lecture à voix haute dans l'assistant.
(() => {
  // ---------- Nouveautés : ajouter une entrée en tête à chaque changement visible, la pastille se rallume
  const NEWS = [
    ["2026-10-31b", "🧭 Bien démarrer, accueil à ton goût, micro", ["Après le choix de ta classe, un parcours en 7 étapes te dit par où commencer.", "« ⭐ Organiser mon accueil » : range les blocs, masque ce qui ne te sert pas, épingle tes rubriques préférées.", "Dans « Pose ta question », tu peux parler au micro et écouter la réponse.", "Sur chaque notion, le bouton « 🤔 Je ne comprends pas » t'explique le chapitre autrement."]],
    ["2026-10-31a", "📱 Connexion par numéro", ["Tu te connectes avec ton numéro de téléphone et un code de 6 chiffres, sur iPhone comme sur Android.", "Pour le premium, paie avec le numéro de ton compte : c'est ta preuve de paiement."]],
    ["2026-10-30", "📚 Terminale : 5 fois plus de contenu", ["39 sujets du BAC corrigés pas à pas, pour toutes les séries.", "Des dizaines de nouvelles notions de cours avec exercice corrigé.", "Des centaines de nouveaux QCM, à faire aussi par thème pour préparer un devoir."]],
  ];
  const unread = () => NEWS.findIndex((n) => n[0] === S.newsSeen) === -1 ? NEWS.length : NEWS.findIndex((n) => n[0] === S.newsSeen);
  function badge() {
    let a = document.getElementById("news");
    if (!a) {
      a = document.createElement("a"); a.id = "news"; a.href = "#nouveautes"; a.className = "news-btn"; a.setAttribute("aria-label", "Nouveautés");
      document.querySelector(".top-r").prepend(a);
    }
    const n = unread();
    a.innerHTML = `🔔${n ? `<i class="dot">${n}</i>` : ""}`;
  }
  function viewNouveautes() {
    const n = unread();
    $view.innerHTML = `<h1>🔔 Nouveautés</h1><p class="muted">Ce qui a changé dans l'appli, du plus récent au plus ancien.</p>
      ${NEWS.map(([id, t, l], i) => `<div class="card"${i < n ? ' style="border:2px solid var(--accent)"' : ""}><p class="small muted">${i < n ? "🔴 Nouveau · " : ""}${new Date(id.slice(0, 10)).toLocaleDateString("fr-FR", { day: "numeric", month: "long" })}</p><h2>${esc(t)}</h2><ul class="steps">${l.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>`).join("")}
      <a class="btn" href="#accueil">Retour à l'accueil</a>`;
    S.newsSeen = NEWS[0][0]; store.save(); badge();
  }

  // ---------- Rappels guidés : pause de midi (13 h – 14 h 30) et après l'école (17 h – 18 h)
  const QUESTIONS = [
    ["Qu'est-ce que tu veux réviser en ce moment ?", ["Une matière où j'ai des difficultés", "Préparer un devoir qui arrive", "Le BAC ou le BFEM", "Juste m'entraîner"]],
    ["Qu'est-ce qui te manque le plus dans l'appli ?", ["Plus de cours expliqués", "Plus d'exercices corrigés", "Des vidéos", "Rien, c'est très bien"]],
    ["Comment tu préfères réviser ?", ["En lisant le cours", "En faisant des QCM", "En faisant des exercices", "En groupe avec des amis"]],
    ["Quelle matière te pose le plus de problèmes ?", ["Mathématiques", "Physique-Chimie ou SVT", "Français ou philosophie", "Langues ou histoire-géo"]],
    ["Combien de temps tu peux réviser par jour ?", ["Moins de 15 minutes", "Environ 30 minutes", "Environ 1 heure", "Plus d'une heure"]],
    ["L'appli t'aide-t-elle à avoir de meilleures notes ?", ["Oui, beaucoup", "Un peu", "Pas encore", "Je viens de commencer"]],
  ];
  function creneau() {
    const d = new Date(), m = d.getHours() * 60 + d.getMinutes();
    return m >= 13 * 60 && m < 14 * 60 + 30 ? "midi" : m >= 17 * 60 && m < 18 * 60 ? "soir" : null;
  }
  globalThis.pauseCard = () => {
    const c = creneau(); if (!c) return "";
    const key = today() + c, day = Math.floor(Date.now() / 864e5), [q, opts] = QUESTIONS[(day * 2 + (c === "soir")) % QUESTIONS.length];
    const asked = (S.avis || []).some((a) => a.k === key);
    const go = c === "midi" ? ["#challenge", "🏆 Le challenge du jour en 5 minutes"] : ["#agenda", "🗓️ Voir ce que je dois réviser pour demain"];
    return `<div class="card prog" id="pause"><h2>${c === "midi" ? "☀️ C'est la pause : 5 minutes pour réviser ?" : "🎒 De retour de l'école ?"}</h2>
      <a class="mission" href="${go[0]}"><span>👉</span><span><b>${go[1]}</b></span></a>
      ${asked ? `<p class="small msg-ok">Merci pour ta réponse ! 🙏</p>` : `<p><b>Petite question :</b> ${esc(q)}</p><div class="grid">${opts.map((o, i) => `<button class="subj tile avis" data-i="${i}" style="min-height:0"><span class="small">${esc(o)}</span></button>`).join("")}</div>`}</div>`;
  };
  document.addEventListener("click", (e) => {
    const b = e.target.closest && e.target.closest("#pause .avis");
    if (!b) return;
    const c = creneau() || "midi", day = Math.floor(Date.now() / 864e5), [q, opts] = QUESTIONS[(day * 2 + (c === "soir")) % QUESTIONS.length];
    const rec = { k: today() + c, q, r: opts[+b.dataset.i], d: today() };
    S.avis = [...(S.avis || []), rec].slice(-30); store.save();
    if (Compte.avis) Compte.avis(rec).catch(() => {});
    const card = document.getElementById("pause"); if (card) card.outerHTML = pauseCard();
  });

  // ---------- Assistant : parler au micro et écouter la réponse
  const Rec = window.SpeechRecognition || window.webkitSpeechRecognition;
  globalThis.assistVoice = (input, send) => {
    const form = document.getElementById("ask");
    if (Rec && form) {
      const mic = document.createElement("button"); mic.type = "button"; mic.className = "btn alt"; mic.style.width = "auto"; mic.textContent = "🎤"; mic.setAttribute("aria-label", "Parler au micro");
      form.insertBefore(mic, form.lastElementChild);
      mic.onclick = () => {
        const r = new Rec(); r.lang = "fr-FR"; r.interimResults = false; r.maxAlternatives = 1;
        mic.textContent = "🔴"; input.placeholder = "Je t'écoute…";
        r.onresult = (ev) => { const t = ev.results[0][0].transcript; input.value = t; send(t); };
        r.onerror = () => { input.placeholder = "Micro indisponible : écris ta question"; };
        r.onend = () => { mic.textContent = "🎤"; };
        try { r.start(); } catch (err) { mic.textContent = "🎤"; }
      };
    }
  };
  globalThis.sayBtn = () => ("speechSynthesis" in window ? `<button class="btn alt small say-ans">🔊 Écouter la réponse</button>` : "");
  document.addEventListener("click", (e) => {
    const b = e.target.closest && e.target.closest(".say-ans");
    if (!b) return;
    if (speechSynthesis.speaking) { speechSynthesis.cancel(); b.textContent = "🔊 Écouter la réponse"; return; }
    const box = b.closest(".bubble");
    const txt = [...box.querySelectorAll("p, li")].filter((el) => !el.closest("details") && !el.closest(".mini")).map((el) => el.innerText).join(". ");
    const u = new SpeechSynthesisUtterance(txt); u.lang = "fr-FR"; u.rate = 0.95; u.onend = () => { b.textContent = "🔊 Écouter la réponse"; };
    speechSynthesis.cancel(); speechSynthesis.speak(u); b.textContent = "⏹️ Arrêter";
  });

  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  ROUTES.nouveautes = viewNouveautes;
  window.addEventListener("hashchange", badge);
  document.addEventListener("DOMContentLoaded", badge);
  if (document.readyState !== "loading") badge();
})();
