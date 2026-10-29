/**
 * Protection Cloudflare Turnstile des demandes de devis / contact.
 *
 * Le Worker n'intercepte que `/contact*` et `/api/contact*`. Il vérifie le
 * jeton Turnstile auprès de Cloudflare puis transmet la requête à l'origine
 * Render. Le secret reste dans les variables chiffrées du Worker.
 */

const VERIFY_URL = 'https://challenges.cloudflare.com/turnstile/v0/siteverify';
const DEFAULT_BACKEND = 'https://pixelsoftwaredesign.onrender.com';

const MESSAGES = {
  missing: "Merci de valider la vérification anti-robot avant d'envoyer.",
  invalid: 'Vérification anti-robot échouée. Merci de réessayer.',
  unavailable: 'Vérification anti-robot indisponible. Réessayez dans un instant.',
};

function jsonBody(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
    },
  });
}

export async function verifyTurnstile(token, request, env, fetchImpl = fetch) {
  if (!token) return { ok: false, reason: 'missing' };
  const secret = env && env.TURNSTILE_SECRET_KEY;
  if (!secret) return { ok: false, reason: 'unavailable' };

  const body = new URLSearchParams({ secret, response: token });
  const ip = request.headers.get('CF-Connecting-IP');
  if (ip) body.set('remoteip', ip);

  let response;
  try {
    response = await fetchImpl(VERIFY_URL, { method: 'POST', body });
  } catch (err) {
    return { ok: false, reason: 'unavailable' };
  }
  if (!response.ok) return { ok: false, reason: 'unavailable' };

  let result;
  try {
    result = await response.json();
  } catch (err) {
    return { ok: false, reason: 'unavailable' };
  }
  if (result && result.success === true) return { ok: true, reason: '' };
  return {
    ok: false,
    reason: 'invalid',
    codes: (result && result['error-codes']) || [],
  };
}

async function forward(request, env, bodyText, fetchImpl) {
  const url = new URL(request.url);
  const backend = (env && env.BACKEND_ORIGIN) || DEFAULT_BACKEND;
  const target = new URL(url.pathname + url.search, backend);
  const headers = new Headers(request.headers);
  headers.delete('host');
  headers.set('X-Forwarded-Host', url.host);
  headers.set('X-Forwarded-Proto', 'https');
  const ip = request.headers.get('CF-Connecting-IP');
  if (ip) headers.set('X-Real-IP', ip);

  const init = { method: request.method, headers, redirect: 'manual' };
  if (bodyText !== undefined) init.body = bodyText;
  else if (request.method !== 'GET' && request.method !== 'HEAD') init.body = request.body;
  return fetchImpl(target.toString(), init);
}

export async function handleRequest(request, env, fetchImpl = fetch) {
  const url = new URL(request.url);
  const isApi = url.pathname === '/api/contact' || url.pathname === '/api/contact/';
  const isForm = url.pathname === '/contact' || url.pathname === '/contact/';

  if (request.method !== 'POST' || (!isApi && !isForm)) {
    return forward(request, env, undefined, fetchImpl);
  }

  const bodyText = await request.text();
  let token = '';
  let form = null;

  if (isApi) {
    let payload;
    try {
      payload = JSON.parse(bodyText);
    } catch (err) {
      return jsonBody({ status: 'error', message: 'Requête invalide.' }, 400);
    }
    token = String((payload && (payload.turnstile_token || payload['cf-turnstile-response'])) || '').trim();
  } else {
    form = new URLSearchParams(bodyText);
    token = String(form.get('cf-turnstile-response') || '').trim();
  }

  const result = await verifyTurnstile(token, request, env, fetchImpl);

  if (!result.ok) {
    if (isApi) {
      const status = result.reason === 'unavailable' ? 503 : 400;
      return jsonBody({ status: 'error', message: MESSAGES[result.reason] || MESSAGES.invalid }, status);
    }
    const params = new URLSearchParams();
    if (form && form.get('devis') === '1') params.set('devis', '1');
    const offre = form && form.get('offre');
    if (offre) params.set('offre', offre);
    params.set('erreur', result.reason === 'unavailable' ? 'indisponible' : 'robot');
    return Response.redirect(new URL('/contact/?' + params.toString(), url.origin).toString(), 303);
  }

  return forward(request, env, bodyText, fetchImpl);
}

export default {
  fetch(request, env) {
    return handleRequest(request, env);
  },
};
