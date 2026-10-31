"use strict";
// Flash actu : l'actualité du Sénégal mise à jour toutes les 30 minutes (data/actu.json, écrit par contenu/actu.py),
// et un fil « Pour toi » selon les centres d'intérêt choisis par l'élève, avec le lien vers ses cours.
(() => {
  let ACTU = null, at = 0;
  async function charger() {
    if (ACTU && Date.now() - at < 5 * 60e3) return ACTU;
    try { ACTU = await fetch("data/actu.json", { cache: "no-cache" }).then((r) => (r.ok ? r.json() : null)); at = Date.now(); } catch (e) {}
    return ACTU;
  }
  const depuis = (iso) => { const m = Math.max(1, Math.round((Date.now() - new Date(iso)) / 6e4)); return m < 60 ? `il y a ${m} min` : m < 1440 ? `il y a ${Math.round(m / 60)} h` : `il y a ${Math.round(m / 1440)} j`; };
  const recents = (a) => a.flash.filter((x) => Date.now() - new Date(x.d) < 4 * 864e5);
  const pourToi = (a) => recents(a).filter((x) => x.th.some((t) => (S.interets || []).includes(t)));
  const item = (a, x, lien) => `<div class="card actu"><p class="small muted">🔴 ${esc(x.s)} · ${depuis(x.d)}${x.th.length ? " · " + x.th.map((t) => esc((a.themes[t] || [t])[0])).join(" ") : ""}</p>
    <p><b>${esc(x.t)}</b></p>${x.r ? `<p class="small">${esc(x.r)}</p>` : ""}${lien && x.th[0] && a.themes[x.th[0]] ? `<p class="small muted">📘 ${esc(a.themes[x.th[0]][1])}</p>` : ""}</div>`;

  function choix(a, retour) {
    const sel = new Set(S.interets || []);
    $view.innerHTML = `<h1>⭐ Ce qui t'intéresse</h1><p class="muted">Choisis autant de sujets que tu veux : ton fil « Pour toi » ne montrera que ceux-là, avec le lien vers tes cours.</p>
      <div class="grid">${Object.entries(a.themes).map(([k, [lbl]]) => `<button class="subj tile" data-k="${k}"${sel.has(k) ? ' aria-pressed="true"' : ""} style="min-height:0"><b>${esc(lbl)}</b></button>`).join("")}</div>
      <button class="btn" id="ok">Enregistrer</button>`;
    $view.querySelectorAll("[data-k]").forEach((b) => b.onclick = () => { const k = b.dataset.k; sel.has(k) ? sel.delete(k) : sel.add(k); b.setAttribute("aria-pressed", String(sel.has(k))); });
    document.getElementById("ok").onclick = () => { S.interets = [...sel]; store.save(); retour(); };
  }

  async function viewActu(arg) {
    $view.innerHTML = `<h1>📰 Flash actu</h1><p class="muted">Chargement…</p>`;
    const a = await charger();
    if (!a || !a.flash.length) { $view.innerHTML = `<h1>📰 Flash actu</h1><div class="card"><p>L'actualité n'est pas disponible pour le moment. Réessaie dans quelques minutes.</p></div>`; return; }
    if (arg === "choix" || (arg === "pour-toi" && !(S.interets || []).length)) return choix(a, () => { history.replaceState(null, "", "#actu/pour-toi"); viewActu("pour-toi"); });
    const toi = arg === "pour-toi", liste = toi ? pourToi(a) : recents(a).filter((x) => x.loc);
    $view.innerHTML = `<h1>📰 Flash actu</h1>
      <p class="small muted">Mis à jour ${depuis(a.maj)} · toutes les 30 minutes</p>
      <div class="row"><a class="btn${toi ? " alt" : ""}" style="flex:1" href="#actu">🇸🇳 En direct</a><a class="btn${toi ? "" : " alt"}" style="flex:1" href="#actu/pour-toi">⭐ Pour toi</a></div>
      ${toi ? `<p class="small">Tes sujets : ${(S.interets || []).map((t) => esc((a.themes[t] || [t])[0])).join(", ")} · <a href="#actu/choix">changer</a></p>` : ""}
      ${liste.length ? liste.slice(0, 40).map((x) => item(a, x, toi)).join("") : `<div class="card"><p>Pas de flash récent sur tes sujets. Ajoute d'autres centres d'intérêt.</p><a class="btn alt" href="#actu/choix">Changer mes sujets</a></div>`}
      <p class="small muted">Titres et résumés publiés par les journaux cités. Les faits divers violents sont écartés.</p>`;
    if (typeof markDone === "function") markDone("actu");
  }

  // carte de l'accueil : 3 flashs du Sénégal, puis 1 flash « pour toi » ; remplie dès que le fichier arrive
  globalThis.actuCard = () => {
    charger().then((a) => {
      const box = document.getElementById("actu-home");
      if (!box) return;
      if (!a || !a.flash.length) { box.remove(); return; }
      const loc = recents(a).filter((x) => x.loc).slice(0, 3), toi = pourToi(a).filter((x) => !loc.includes(x))[0];
      box.innerHTML = `<div class="row"><h2>📰 Flash actu</h2><a class="small" href="#actu">tout voir ›</a></div>
        ${loc.map((x) => `<a class="mission" href="#actu"><span>🔴</span><span><b>${esc(x.t)}</b><br><span class="small muted">${esc(x.s)} · ${depuis(x.d)}</span></span></a>`).join("")}
        ${toi ? `<a class="mission" href="#actu/pour-toi"><span>⭐</span><span><b>Pour toi : ${esc(toi.t)}</b><br><span class="small muted">${esc((a.themes[toi.th[0]] || [""])[0])} · ${depuis(toi.d)}</span></span></a>`
          : `<a class="mission" href="#actu/choix"><span>⭐</span><span><b>Choisis tes centres d'intérêt</b><br><span class="small muted">Sport, sciences, culture… pour un fil rien que pour toi</span></span></a>`}`;
    });
    return `<div class="card" id="actu-home"><p class="small muted">📰 Chargement du flash actu…</p></div>`;
  };

  const ROUTES = (globalThis.ROUTES = globalThis.ROUTES || {});
  ROUTES.actu = viewActu;
})();
