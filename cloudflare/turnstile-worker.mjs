/**
 * Service de verification Cloudflare Turnstile.
 *
 * Le Worker est appele par le backend Django (Render) sur
 * `POST /verify` avec `{"token": "..."}`. Il interroge Cloudflare
 * `siteverify` avec le secret stocke dans les variables chiffrees du Worker.
 * Il n'intercepte aucune route du site : le secret reste donc hors du depot
 * et hors de Render.
 */

const VERIFY_URL = 'https://challenges.cloudflare.com/turnstile/v0/siteverify';

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

  // Pas de `remoteip` : le Worker est appele par le serveur Django, pas par
  // le navigateur du visiteur. L'IP transmise ne serait donc pas la bonne.
  const body = new URLSearchParams({ secret, response: token });

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

export async function handleRequest(request, env, fetchImpl = fetch) {
  const url = new URL(request.url);
  if (url.pathname !== '/verify' && url.pathname !== '/') {
    return jsonBody({ success: false, error: 'not_found' }, 404);
  }
  if (request.method !== 'POST') {
    return jsonBody({ success: false, error: 'method_not_allowed' }, 405);
  }

  let payload;
  try {
    payload = await request.json();
  } catch (err) {
    return jsonBody({ success: false, error: 'invalid_json' }, 400);
  }

  const token = String((payload && payload.token) || '').trim();
  if (!token) {
    return jsonBody({
      success: false,
      error: 'missing_token',
      error_codes: ['missing-input-response'],
    }, 400);
  }

  const result = await verifyTurnstile(token, request, env, fetchImpl);
  if (result.ok) return jsonBody({ success: true });
  return jsonBody({
    success: false,
    error: result.reason,
    error_codes: result.codes || [],
  }, result.reason === 'unavailable' ? 503 : 200);
}

export default {
  fetch(request, env) {
    return handleRequest(request, env);
  },
};
