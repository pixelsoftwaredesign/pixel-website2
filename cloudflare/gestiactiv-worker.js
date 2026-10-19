/**
 * Worker GestiActiv — expose l'espace GestiActiv sur
 * gestiactiv.pixelsoftwaredesign.xyz en proxy vers le backend Render.
 *
 * Le backend Render n'accepte que ses hôtes déclarés : on réécrit donc le
 * Host vers l'hôte onrender, et on signale la requête via `X-GestiActiv`
 * pour que Django route vers l'URLconf GestiActiv (SSO partagé).
 * Les cookies posés par Django (Domain=.pixelsoftwaredesign.xyz) sont
 * transmis tels quels, ce qui assure le SSO entre le site et GestiActiv.
 */
const BACKEND = 'https://pixelsoftwaredesign.onrender.com';

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const target = new URL(url.pathname + url.search, BACKEND);

    const headers = new Headers(request.headers);
    headers.set('X-Forwarded-Host', url.hostname);
    headers.set('X-Forwarded-Proto', 'https');
    headers.set('X-GestiActiv', '1');
    const ip = headers.get('CF-Connecting-IP');
    if (ip) headers.set('X-Real-IP', ip);
    headers.delete('host');

    const init = { method: request.method, headers, redirect: 'manual' };
    if (request.method !== 'GET' && request.method !== 'HEAD') {
      init.body = request.body;
    }

    const upstream = await fetch(new Request(target, init));
    return new Response(upstream.body, upstream);
  },
};
