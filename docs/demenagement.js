"use strict";
// Déménagement de l'appli vers sa nouvelle adresse (Cloudflare Pages).
// Sur l'ancienne adresse (github.io), un bandeau propose d'aller à la nouvelle en emportant les progrès du téléphone.
// Sur la nouvelle adresse, les progrès reçus sont rangés dans le téléphone, puis l'appli redémarre.
// NOUVELLE_ADRESSE vide = rien ne change (le bandeau n'apparaît pas).
const NOUVELLE_ADRESSE = "";

(() => {
  const b64 = {
    enc: (u8) => { let s = ""; for (let i = 0; i < u8.length; i += 0x8000) s += String.fromCharCode.apply(null, u8.subarray(i, i + 0x8000)); return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, ""); },
    dec: (t) => { const s = atob(t.replace(/-/g, "+").replace(/_/g, "/")); const u8 = new Uint8Array(s.length); for (let i = 0; i < s.length; i++) u8[i] = s.charCodeAt(i); return u8; },
  };
  const zip = async (txt) => new Uint8Array(await new Response(new Blob([txt]).stream().pipeThrough(new CompressionStream("deflate-raw"))).arrayBuffer());
  const unzip = async (u8) => new Response(new Blob([u8]).stream().pipeThrough(new DecompressionStream("deflate-raw"))).text();
  const peuCompresser = typeof CompressionStream === "function" && typeof DecompressionStream === "function";

  // 1. Nouvelle adresse : on reçoit les progrès (#emporter=…) et on les range si ce téléphone n'en a pas encore ici
  const h = location.hash;
  if (h.startsWith("#emporter=") && peuCompresser) {
    unzip(b64.dec(h.slice(10))).then((txt) => {
      const recu = JSON.parse(txt);
      let ici = {}; try { ici = JSON.parse(localStorage.getItem("rev") || "{}"); } catch {}
      const dejaUtilise = (ici.sessions || []).length > 0;
      if (!dejaUtilise && recu && typeof recu === "object") localStorage.setItem("rev", JSON.stringify(recu));
    }).catch(() => {}).finally(() => { location.replace(location.pathname + "#accueil"); location.reload(); });
    return;
  }

  // 2. Ancienne adresse : bandeau « l'appli a déménagé »
  if (!NOUVELLE_ADRESSE || !location.hostname.endsWith("github.io")) return;
  const montrer = () => {
    if (document.getElementById("demenage")) return;
    const d = document.createElement("div");
    d.id = "demenage";
    d.style.cssText = "position:fixed;left:10px;right:10px;bottom:84px;z-index:99;background:#1b5e20;color:#fff;padding:14px;border-radius:14px;box-shadow:0 6px 20px rgba(0,0,0,.3);font-size:15px;line-height:1.35";
    d.innerHTML = '<b>📦 Révision a déménagé</b><br>La nouvelle adresse est plus rapide. Tes progrès partent avec toi.<br>'
      + '<button id="demenage-go" style="margin-top:10px;width:100%;padding:12px;border:0;border-radius:10px;background:#fff;color:#1b5e20;font-weight:700;font-size:16px">Aller à la nouvelle appli</button>'
      + '<p style="margin:8px 0 0;font-size:13px;opacity:.9">Ensuite, installe-la sur ton écran d\'accueil et supprime l\'ancienne icône.</p>';
    document.body.appendChild(d);
    document.getElementById("demenage-go").onclick = async () => {
      let url = NOUVELLE_ADRESSE;
      try {
        const txt = localStorage.getItem("rev");
        if (txt && peuCompresser) url += "#emporter=" + b64.enc(await zip(txt));
      } catch {}
      location.href = url;
    };
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", montrer); else montrer();
})();
