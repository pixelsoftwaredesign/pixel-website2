/**
 * Redirige cabine.pixelsoftwaredesign.xyz vers l'app cabine hébergée sur
 * Render (https://cabine-backend.onrender.com), en conservant chemin et query.
 *
 * Contexte : Render n'autorise que 2 domaines personnalisés par workspace
 * sans moyen de paiement ; le slot « cabine » a été libéré au profit de
 * l'apex pixelsoftwaredesign.xyz et de GestiActiv. L'app cabine reste donc
 * servie sur son URL Render, accessible via cette redirection.
 *
 * Aucun sous-fetch (le fetch d'un Worker avec domaine personnalisé déclenche
 * l'erreur Cloudflare 1042) : uniquement une réponse de redirection.
 */
const TARGET = 'https://cabine-backend.onrender.com';

export default {
  fetch(request) {
    const url = new URL(request.url);
    const dest = TARGET + url.pathname + url.search;
    // GET/HEAD : 301 (permanent, SEO). Autres méthodes : 308 pour conserver
    // la méthode et le corps (les POST d'API ne doivent pas devenir des GET).
    const code = request.method === 'GET' || request.method === 'HEAD' ? 301 : 308;
    return Response.redirect(dest, code);
  },
};
