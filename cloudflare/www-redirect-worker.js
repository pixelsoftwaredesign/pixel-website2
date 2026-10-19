/**
 * Redirige www.pixelsoftwaredesign.xyz vers l'apex (301), en conservant le
 * chemin et la query. Remplace l'ancien domaine Render « www » (limite de
 * 2 domaines personnalisés par service, désormais utilisé par GestiActiv).
 * Aucun sous-fetch : pas de risque de boucle Cloudflare.
 */
const APEX = 'https://pixelsoftwaredesign.xyz';

export default {
  fetch(request) {
    const url = new URL(request.url);
    return Response.redirect(APEX + url.pathname + url.search, 301);
  },
};
