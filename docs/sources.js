// Sources : documents officiels et publics qui ont servi au contenu, en texte (sans lien), par classe et par matière.
function viewSources(sid) {
  const lv = S.level || "", cls = lv.split(" ")[0];
  const pour = (e) => e.lv.some((l) => l === lv || l === cls || (typeof family === "function" && l === family(lv)));
  const norm = (x) => String(x).normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  const sub = sid && DATA.subjects.find((x) => x.id === sid);
  const memeMatiere = (e) => !sub || e.m === "Toutes matières" || norm(sub.name).includes(norm(e.m).split(/[ (]/)[0]) || norm(e.m).includes(norm(sub.name).split(/[ (]/)[0]);
  const liste = (DATA.sources || []).filter((e) => pour(e) && memeMatiere(e));
  const parM = {};
  liste.forEach((e) => { const k = e.m.split(/ \(|, /)[0]; (parM[k] = parM[k] || []).push(e); });
  const nbOff = liste.filter((e) => /^(Examen|Sujet)/.test(e.k)).length;
  $view.innerHTML = `<h1>🔎 Sources${sub ? " · " + esc(sub.name) : ""}</h1>
    <div class="card small"><p><b>Comment le contenu est construit</b></p><ul class="steps">
      <li>Chaque cours, QCM et exercice suit un <b>chapitre du programme officiel</b> du Sénégal (${esc(lv)}). Le chapitre est écrit sous chaque question.</li>
      <li>Les questions tirées d'un <b>vrai sujet du BAC ou du BFEM</b> portent le nom exact de l'épreuve (année, série, exercice).</li>
      <li>Le reste est rédigé et corrigé par l'équipe Révision, sur le modèle des sujets officiels. Les sujets types sont indiqués comme des sujets d'entraînement.</li>
      <li>Seuls des <b>documents officiels et publics</b> sont utilisés et listés ici : programmes du ministère, sujets d'examen d'État, documents de l'Office du BAC. Aucun document privé ou réservé.</li></ul>
      <p class="muted">${liste.length} documents officiels${sub ? " pour cette matière" : ` pour la ${esc(cls)}`}, dont ${nbOff} sujets d'examen officiels.</p></div>
    ${sub ? "" : `<div class="card small"><p>Choisir une matière :</p><div class="row" style="flex-wrap:wrap;gap:6px">${subjectsOf(lv).map((s) => `<a class="btn alt small" href="#sources/${s.id}">${esc(s.name)}</a>`).join("")}</div></div>`}
    ${Object.entries(parM).map(([m, es]) => `<details class="card"${sub ? " open" : ""}><summary><b>${esc(m)}</b> <span class="small muted">· ${es.length}</span></summary>
      <ul class="steps small">${es.map((e) => `<li>${esc(e.t)}<br><span class="muted">${esc(e.k)} · ${esc(e.o)}</span></li>`).join("")}</ul></details>`).join("") || `<div class="card"><p>Pas de document externe listé pour cette matière : le contenu suit le programme officiel, chapitre par chapitre.</p></div>`}
    ${sub ? `<a class="btn alt" href="#sources">Toutes les matières</a>` : ""}<a class="btn alt" href="#comment">Comment ça marche</a>`;
}
