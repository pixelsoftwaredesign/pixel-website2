export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const backend = env.RAILWAY_BACKEND || 'https://pixel-website2-production.up.railway.app';

    const proxyHeaders = new Headers(request.headers);
    proxyHeaders.set('X-Forwarded-Host', url.hostname);
    proxyHeaders.set('X-Forwarded-Proto', 'https');
    proxyHeaders.set('X-Real-IP', proxyHeaders.get('CF-Connecting-IP') || '');

    const backendUrl = new URL(url.pathname + url.search, backend);
    const proxyRequest = new Request(backendUrl, {
      method: request.method,
      headers: proxyHeaders,
      body: request.method !== 'GET' && request.method !== 'HEAD' ? request.body : undefined,
      redirect: 'manual',
    });

    const response = await fetch(proxyRequest);

    const newResponse = new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: response.headers,
    });

    const setCookies = response.headers.getSetCookie?.() || [];
    if (setCookies.length) {
      newResponse.headers.delete('Set-Cookie');
      for (const cookie of setCookies) {
        let fixed = cookie
          .replace(/;?\s*Secure;?/gi, ';')
          .replace(/;?\s*SameSite=None;?/gi, ';SameSite=Lax;')
          .replace(/Domain=[^;]+;?/gi, ';');
        newResponse.headers.append('Set-Cookie', fixed);
      }
    }

    newResponse.headers.set('X-Proxy', 'Cloudflare-Worker');

    return newResponse;
  },
};
