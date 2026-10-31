"use strict";
// Ma trajectoire : un suivi propre à chaque élève. On croise sa classe et sa série, son objectif, le temps qu'il a chaque jour,
// l'avancement du programme en classe (estimé par la date, corrigeable), son emploi du temps et sa maîtrise de chaque chapitre.
// On en tire une courbe de référence (la « base de parcours ») jusqu'à l'examen, sa courbe réelle, et la semaine à venir séance par séance.
(() => {
  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  const subsT = () => subjectsOf(S.level).filter((s) => !/annales/.test(s.id) && ((DATA.programmes || {})[s.id] || []).length);
  const J = 864e5, iso = (d) => new Date(d.getTime() - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10);
  const plus = (d, n) => { const x = new Date(d); x.setDate(x.getDate() + n); return x; };

  // ---------- Calendrier scolaire : rentrée début octobre, programme bouclé 4 semaines avant l'examen (ou mi-juin sans examen)
  function calendrier() {
    const now = new Date(), y = now.getMonth() >= 8 ? now.getFullYear() : now.getFullYear() - 1;
    const rentree = new Date(y, 9, 1), ex = examOf(), examen = ex ? new Date(ex[1] + "T08:00") : new Date(y + 1, 5, 20);
    const finCours = plus(examen, ex ? -28 : -7);
    return { rentree, examen, finCours, nom: ex ? ex[0] : "fin d'année", frac: (d) => Math.max(0, Math.min(1, (d - rentree) / (finCours - rentree))) };
  }
  // chapitre où en est la classe : choisi par l'élève, sinon estimé d'après la date
  function chEnCours(sid) {
    const n = ((DATA.programmes || {})[sid] || []).length, a = (S.avance || {})[sid];
    if (a !== undefined && a < n) return a;
    return Math.min(n - 1, Math.floor(calendrier().frac(new Date()) * n));
  }
  globalThis.chEnCours = chEnCours;
  globalThis.maitriseCh = (sid, i) => maitrise(sid, i);
  function maitrise(sid, i) {
    const qs = qsOf(sid).filter((q) => q.ch === i && S.stats[q.id]), g = typeof maitriseGen === "function" ? maitriseGen(sid, i) : null;
    // questions de la base et questions générées (10 dernières réponses) comptent ensemble
    if (qs.length || g) { const ok = qs.filter((q) => S.stats[q.id].last).length + (g ? (g.m * g.n) / 100 : 0), n = qs.length + (g ? g.n : 0); return Math.round((100 * ok) / n); }
    const d = S.diag && S.diag.ch && S.diag.ch[`${sid}~${i}`];
    return d === undefined ? null : d ? 100 : 0;
  }
  // préparation : part du programme de l'année maîtrisée (un chapitre jamais travaillé compte 0)
  function preparation() {
    let tot = 0, n = 0;
    for (const s of subsT()) DATA.programmes[s.id].forEach((t, i) => { tot += maitrise(s.id, i) || 0; n++; });
    return n ? Math.round(tot / n) : 0;
  }
  // base de parcours : à chaque date, les chapitres déjà vus en classe maîtrisés au niveau de l'objectif, puis tout le programme à l'examen
  const cible = () => Math.min(95, (S.objectif || 12) * 5 + 10);
  function base(d) { const c = calendrier(); if (d >= c.finCours) return Math.round(cible() * (0.85 + 0.15 * Math.min(1, (d - c.finCours) / (c.examen - c.finCours)))); return Math.round(cible() * 0.85 * c.frac(d)); }
  // une mesure par jour d'activité, gardée sur l'année : c'est la courbe réelle de l'élève
  function noter() {
    const p = preparation(), t = today(), l = (S.traj = (S.traj || []).filter((x) => x.l === S.level));
    if (l.length && l[l.length - 1].d === t) l[l.length - 1].p = p; else l.push({ d: t, p, l: S.level });
    if (l.length > 120) l.splice(0, l.length - 120);
    return p;
  }

  // ---------- La semaine à venir, séance par séance : préparer le cours du lendemain, rattraper, puis s'entraîner aux sujets
  const DUREE = 15;
  function semaine() {
    const c = calendrier(), parJour = Math.max(1, Math.round((S.tempsJour || 30) / DUREE)), now = new Date();
    const finale = (c.examen - now) / J <= 42 && examOf();
    // chapitres déjà vus en classe et pas encore maîtrisés : les plus faibles d'abord
    const retard = [];
    for (const s of subsT()) for (let i = 0; i <= chEnCours(s.id); i++) { const m = maitrise(s.id, i); if (m === null || m < 60) retard.push({ sid: s.id, i, m }); }
    // on alterne les matières, et dans chacune on commence par le plus faible puis le plus ancien
    const par = {}; for (const r of retard.sort((a, b) => (a.m ?? -1) - (b.m ?? -1) || a.i - b.i)) (par[r.sid] = par[r.sid] || []).push(r);
    // les matières où les notes sont loin de l'objectif passent devant (réajustement à chaque note saisie)
    const prio = typeof notesPriorite === "function" ? notesPriorite() : {};
    retard.length = 0; for (let k = 0, ls = Object.entries(par).sort((a, b) => (prio[b[0]] || 0) - (prio[a[0]] || 0)).map((e) => e[1]); ls.some((l) => l.length); k++) { const l = ls[k % ls.length]; if (l.length) retard.push(l.shift()); }
    // ensuite : prendre de l'avance sur le chapitre suivant de chaque matière, puis consolider les chapitres déjà réussis
    const avance = [], conso = [];
    for (let k = 1; k <= 3; k++) for (const s of subsT()) { const i = chEnCours(s.id) + k; if (i < DATA.programmes[s.id].length) avance.push({ sid: s.id, i }); }
    for (const s of subsT()) for (let i = 0; i <= chEnCours(s.id); i++) { const m = maitrise(s.id, i); if (m !== null && m >= 60 && m < 90) conso.push({ sid: s.id, i, m }); }
    const jours = [];
    for (let k = 0; k < 7; k++) {
      const d = plus(now, k), demain = plus(d, 1), seances = [];
      for (const cr of ((S.edt || {})[demain.getDay()] || []).filter((x) => x.sid && DATA.programmes[x.sid])) {
        if (seances.some((x) => x.sid === cr.sid)) continue;
        const i = chEnCours(cr.sid);
        seances.push({ ico: "📘", sid: cr.sid, txt: `Cours de ${subjName(cr.sid)} demain : revois « ${DATA.programmes[cr.sid][i]} »`, href: `#quiz/${cr.sid}/${i}`, raison: "veille du cours" });
      }
      if (finale && (d.getDay() === 3 || d.getDay() === 6)) seances.push({ ico: "📚", txt: `Sujet type du ${examOf()[0]} en conditions réelles`, href: "#annales", raison: "dernières semaines" });
      while (seances.length < parJour && retard.length) { const r = retard.shift(); seances.push({ ico: r.m === null ? "🆕" : "🔁", sid: r.sid, txt: `${subjName(r.sid)} : ${DATA.programmes[r.sid][r.i]}`, href: `#quiz/${r.sid}/${r.i}`, raison: r.m === null ? "vu en classe, pas encore travaillé" : `maîtrisé à ${r.m} %` }); }
      while (seances.length < parJour && conso.length) { const r = conso.shift(); seances.push({ ico: "💪", sid: r.sid, txt: `${subjName(r.sid)} : ${DATA.programmes[r.sid][r.i]}`, href: `#quiz/${r.sid}/${r.i}`, raison: `consolider : ${r.m} %, vise 90 %` }); }
      while (seances.length < parJour && avance.length) { const r = avance.shift(); seances.push({ ico: "⏩", sid: r.sid, txt: `${subjName(r.sid)} : ${DATA.programmes[r.sid][r.i]}`, href: `#quiz/${r.sid}/${r.i}`, raison: "prendre de l'avance sur la classe" }); }
      if (!seances.length) seances.push({ ico: "🏆", txt: "Challenge du jour", href: "#challenge", raison: "garder le rythme" });
      jours.push({ d, seances: seances.slice(0, Math.max(parJour, seances.filter((x) => x.raison === "veille du cours").length)) });
    }
    return jours;
  }

  // ---------- Courbe : base de parcours (pointillés) et courbe réelle
  function courbe() {
    const c = calendrier(), W = 320, H = 150, x = (d) => 30 + ((d - c.rentree) / (c.examen - c.rentree)) * (W - 40), y = (p) => H - 20 - (p / 100) * (H - 30);
    const pts = []; for (let d = new Date(c.rentree); d <= c.examen; d = plus(d, 7)) pts.push(`${x(d).toFixed(1)},${y(base(d)).toFixed(1)}`);
    const reel = (S.traj || []).filter((t) => t.l === S.level).map((t) => `${x(new Date(t.d + "T12:00")).toFixed(1)},${y(t.p).toFixed(1)}`);
    const now = x(new Date());
    return `<svg viewBox="0 0 ${W} ${H}" style="width:100%;height:auto" role="img" aria-label="Ma trajectoire jusqu'à l'examen">
      ${[0, 50, 100].map((p) => `<line x1="30" x2="${W - 10}" y1="${y(p)}" y2="${y(p)}" stroke="var(--line)"/><text x="2" y="${y(p) + 4}" font-size="10" fill="var(--muted)">${p} %</text>`).join("")}
      <line x1="${now}" x2="${now}" y1="10" y2="${H - 20}" stroke="var(--muted)" stroke-dasharray="2 3"/><text x="${now + 3}" y="18" font-size="10" fill="var(--muted)">aujourd'hui</text>
      <polyline points="${pts.join(" ")}" fill="none" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 4"/>
      ${reel.length > 1 ? `<polyline points="${reel.join(" ")}" fill="none" stroke="var(--accent)" stroke-width="3"/>` : ""}${reel.length ? `<circle cx="${reel[reel.length - 1].split(",")[0]}" cy="${reel[reel.length - 1].split(",")[1]}" r="4" fill="var(--accent)"/>` : ""}
      <text x="30" y="${H - 4}" font-size="10" fill="var(--muted)">oct.</text><text x="${W - 10}" y="${H - 4}" font-size="10" fill="var(--muted)" text-anchor="end">${esc(c.nom)}</text></svg>
      <p class="small muted">Pointillés : ta base de parcours pour viser ${S.objectif || 12}/20. Trait bleu : ta progression réelle.</p>`;
  }
  function etat(p) {
    if (!S.diag && !Object.keys(S.stats || {}).length) return ["🏁", "Point de départ : fais ton diagnostic (15 min) pour placer ta courbe", ""];
    const b = base(new Date()), e = p - b;
    return e >= 5 ? ["🚀", "En avance sur ta base de parcours", "msg-ok"] : e >= -5 ? ["✅", "Dans les temps", "msg-ok"] : e >= -20 ? ["⚠️", `En retard de ${-e} points : suis le programme de la semaine`, "msg-ko"] : ["🆘", "Gros retard : commence par les séances 🔁 et 🆕 ci-dessous, un peu chaque jour", "msg-ko"];
  }

  function viewTrajectoire(arg) {
    if (arg === "profil" || !S.tempsJour) return profil();
    const p = noter(); store.save();
    const c = calendrier(), [ico, msg, cls] = etat(p), sem = semaine(), subs = subsT(), jx = Math.ceil((c.examen - new Date()) / J);
    const JR = ["dim.", "lun.", "mar.", "mer.", "jeu.", "ven.", "sam."];
    $view.innerHTML = `<h1>🧭 Ma trajectoire</h1>
      <p class="muted">${esc(S.level)} · objectif ${S.objectif || 12}/20 · ${S.tempsJour || 30} min par jour · ${c.nom === "fin d'année" ? "fin d'année" : `${esc(c.nom)} dans ${jx} jours`} <a href="#trajectoire/profil">modifier</a></p>
      <div class="card"><div class="row"><div><p class="small muted">Programme maîtrisé</p><p class="count">${p} %</p></div><div style="text-align:right"><p class="small muted">Base de parcours aujourd'hui</p><p class="count">${base(new Date())} %</p></div></div>
        <p class="${cls}">${ico} ${msg}</p>${ico === "🏁" ? `<a class="btn hi-btn" href="#diagnostic">Faire mon diagnostic</a>` : ""}${courbe()}</div>
      <div class="card small"><p><b>🎲 Un parcours fait pour toi</b></p><p>Les questions et les exercices sont tirés pour toi seul : d'abord le chapitre que ta classe voit en ce moment, le cours de demain dans ton emploi du temps, tes devoirs à venir, puis tes chapitres faibles et les matières où tes notes sont loin de ton objectif.</p>
        <p class="muted">${(S.vu || []).length + Object.keys(S.stats || {}).length} questions et exercices différents déjà faits. L'appli ne te les repropose pas tant qu'il en reste de nouveaux.</p></div>
      <h2>📅 Ma semaine, séance par séance</h2><p class="small muted">Séances de ${DUREE} minutes, calées sur ton emploi du temps${Object.values(S.edt || {}).some((l) => l.length) ? "" : ` (<a href="#agenda/guide">remplis-le</a> pour préparer chaque cours la veille)`} et sur ce que ta classe a déjà vu.</p>
      ${sem.map((j, k) => `<div class="card"${k ? "" : ' style="border:2px solid var(--accent)"'}><h2>${k === 0 ? "Aujourd'hui" : k === 1 ? "Demain" : JR[j.d.getDay()] + " " + j.d.getDate()}</h2>
        ${j.seances.map((s) => `<a class="mission" href="${s.href}"><span>${s.ico}</span><span><b>${esc(s.txt)}</b><br><span class="small muted">${esc(s.raison)}</span></span></a>`).join("")}</div>`).join("")}
      <h2>📍 Où en est ma classe</h2><p class="small muted">Estimé d'après la date. Corrige si ton professeur est plus avancé ou en retard : tout le plan s'ajuste.</p>
      <div class="card">${subs.map((s) => { const n = DATA.programmes[s.id].length, i = chEnCours(s.id), vus = DATA.programmes[s.id].slice(0, i + 1).map((t, k) => maitrise(s.id, k));
        const ok = vus.filter((m) => m !== null && m >= 60).length;
        return `<div style="padding:6px 0;border-bottom:1px solid var(--line)"><div class="row small"><b>${esc(s.name)}</b><span class="muted">${ok} / ${i + 1} chapitres vus maîtrisés</span></div>
          <select class="av" data-s="${s.id}">${DATA.programmes[s.id].map((t, k) => `<option value="${k}"${k === i ? " selected" : ""}>${k + 1}/${n}. ${esc(t)}</option>`).join("")}</select>
          <div class="bar"><i style="width:${Math.round((100 * (i + 1)) / n)}%"></i></div></div>`; }).join("")}</div>
      <a class="btn alt" href="#plan">Mon plan de révision détaillé</a><a class="btn alt" href="#accueil">Retour à l'accueil</a>`;
    $view.querySelectorAll(".av").forEach((x) => x.onchange = () => { S.avance = { ...(S.avance || {}), [x.dataset.s]: +x.value }; store.save(); viewTrajectoire(); });
    if (typeof markDone === "function") markDone("trajectoire");
  }
  function profil() {
    const ob = S.objectif || 12, tj = S.tempsJour || 30;
    $view.innerHTML = `<h1>🧭 Mon profil de révision</h1><p class="muted">Ta trajectoire dépend de ton objectif et du temps que tu peux y mettre. Tu pourras changer à tout moment.</p>
      <div class="card"><h2>🎯 Note visée${examOf() ? ` au ${examOf()[0]}` : " en fin d'année"}</h2><div class="grid">${[10, 12, 14, 16].map((n) => `<button class="subj tile pob" data-n="${n}"${n === ob ? ' aria-pressed="true"' : ""} style="min-height:0"><b>${n}/20</b><span class="small muted">${{ 10: "réussir", 12: "mention Assez bien", 14: "mention Bien", 16: "mention Très bien" }[n]}</span></button>`).join("")}</div></div>
      <div class="card"><h2>⏱️ Temps de révision par jour</h2><div class="grid">${[15, 30, 45, 60, 90].map((n) => `<button class="subj tile ptj" data-n="${n}"${n === tj ? ' aria-pressed="true"' : ""} style="min-height:0"><b>${n < 60 ? n + " min" : n / 60 === 1 ? "1 h" : "1 h 30"}</b></button>`).join("")}</div></div>
      <button class="btn hi-btn" id="pok">Voir ma trajectoire</button>`;
    const pick = (cls, key) => $view.querySelectorAll(cls).forEach((b) => b.onclick = () => { S[key] = +b.dataset.n; $view.querySelectorAll(cls).forEach((x) => x.setAttribute("aria-pressed", String(x === b))); });
    pick(".pob", "objectif"); pick(".ptj", "tempsJour");
    document.getElementById("pok").onclick = () => { S.objectif = S.objectif || 12; S.tempsJour = S.tempsJour || 30; store.save(); history.replaceState(null, "", "#trajectoire"); viewTrajectoire(); };
  }
  // carte de l'accueil : où j'en suis et la prochaine séance
  globalThis.trajCard = () => {
    if (!subsT().length) return "";
    const p = preparation(), [ico, msg] = etat(p), s = semaine()[0].seances[0];
    return `<div class="card"><div class="row"><h2>🧭 Ma trajectoire</h2><a class="small" href="#trajectoire">voir ›</a></div>
      <p class="small">${ico} ${msg} · programme maîtrisé ${p} % (base ${base(new Date())} %)</p>
      ${s ? `<a class="mission" href="${s.href}"><span>${s.ico}</span><span><b>${esc(s.txt)}</b><br><span class="small muted">Séance du jour · ${esc(s.raison)}</span></span></a>` : ""}</div>`;
  };
  ROUTES.trajectoire = viewTrajectoire;
})();
