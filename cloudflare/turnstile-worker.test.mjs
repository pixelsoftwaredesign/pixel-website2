import test from 'node:test';
import assert from 'node:assert/strict';

import { handleRequest, verifyTurnstile } from './turnstile-worker.mjs';

const ENV = {
  TURNSTILE_SECRET_KEY: 'test-secret',
};

function verifyResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

function fetchMock({ verify = { success: true }, verifyStatus = 200 } = {}) {
  const calls = [];
  const impl = async (url, init = {}) => {
    const target = typeof url === 'string' ? url : url.url;
    calls.push({ url: target, init });
    return verifyResponse(verify, verifyStatus);
  };
  return { impl, calls };
}

function verifyRequest(payload, { method = 'POST', path = '/verify' } = {}) {
  return new Request(`https://pixelsoftwaredesign-contact.example.workers.dev${path}`, {
    method,
    headers: { 'Content-Type': 'application/json' },
    body: method === 'POST' ? JSON.stringify(payload) : undefined,
  });
}

test('verifyTurnstile refuse un jeton absent', async () => {
  const { impl } = fetchMock();
  const result = await verifyTurnstile('', verifyRequest({}), ENV, impl);
  assert.deepEqual(result, { ok: false, reason: 'missing' });
});

test('verifyTurnstile refuse si le secret manque', async () => {
  const { impl } = fetchMock();
  const result = await verifyTurnstile('token', verifyRequest({}), {}, impl);
  assert.deepEqual(result, { ok: false, reason: 'unavailable' });
});

test('verifyTurnstile accepte une reponse success', async () => {
  const { impl, calls } = fetchMock({ verify: { success: true } });
  const result = await verifyTurnstile('token', verifyRequest({}), ENV, impl);
  assert.equal(result.ok, true);
  assert.equal(calls.length, 1);
  assert.match(calls[0].url, /siteverify/);
  assert.equal(calls[0].init.body.get('secret'), 'test-secret');
  assert.equal(calls[0].init.body.get('response'), 'token');
});

test('verifyTurnstile refuse une reponse invalide', async () => {
  const { impl } = fetchMock({
    verify: { success: false, 'error-codes': ['invalid-input-response'] },
  });
  const result = await verifyTurnstile('token', verifyRequest({}), ENV, impl);
  assert.equal(result.ok, false);
  assert.equal(result.reason, 'invalid');
  assert.deepEqual(result.codes, ['invalid-input-response']);
});

test('verifyTurnstile signale un service indisponible', async () => {
  const { impl } = fetchMock({ verify: { success: false }, verifyStatus: 500 });
  const result = await verifyTurnstile('token', verifyRequest({}), ENV, impl);
  assert.deepEqual(result, { ok: false, reason: 'unavailable' });
});

test('POST /verify avec jeton valide : success', async () => {
  const { impl, calls } = fetchMock({ verify: { success: true } });
  const response = await handleRequest(verifyRequest({ token: 'token' }), ENV, impl);
  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { success: true });
  assert.equal(calls.length, 1);
  assert.equal(calls[0].init.body.get('response'), 'token');
});

test('POST /verify avec jeton invalide : success false et codes', async () => {
  const { impl } = fetchMock({
    verify: { success: false, 'error-codes': ['invalid-input-response'] },
  });
  const response = await handleRequest(verifyRequest({ token: 'bad' }), ENV, impl);
  assert.equal(response.status, 200);
  const body = await response.json();
  assert.equal(body.success, false);
  assert.equal(body.error, 'invalid');
  assert.deepEqual(body.error_codes, ['invalid-input-response']);
});

test('POST /verify sans jeton : 400 sans appel a siteverify', async () => {
  const { impl, calls } = fetchMock();
  const response = await handleRequest(verifyRequest({}), ENV, impl);
  assert.equal(response.status, 400);
  const body = await response.json();
  assert.equal(body.success, false);
  assert.equal(body.error, 'missing_token');
  assert.equal(calls.length, 0);
});

test('POST /verify avec JSON invalide : 400', async () => {
  const { impl } = fetchMock();
  const request = new Request('https://pixelsoftwaredesign-contact.example.workers.dev/verify', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: 'pas du json',
  });
  const response = await handleRequest(request, ENV, impl);
  assert.equal(response.status, 400);
  assert.equal((await response.json()).error, 'invalid_json');
});

test('POST /verify si siteverify est indisponible : 503', async () => {
  const { impl } = fetchMock({ verify: { success: false }, verifyStatus: 503 });
  const response = await handleRequest(verifyRequest({ token: 'token' }), ENV, impl);
  assert.equal(response.status, 503);
  assert.equal((await response.json()).error, 'unavailable');
});

test('GET /verify : 405', async () => {
  const { impl } = fetchMock();
  const response = await handleRequest(verifyRequest({}, { method: 'GET' }), ENV, impl);
  assert.equal(response.status, 405);
});

test('chemin inconnu : 404', async () => {
  const { impl } = fetchMock();
  const response = await handleRequest(verifyRequest({ token: 'token' }, { path: '/autre' }), ENV, impl);
  assert.equal(response.status, 404);
});

test('POST / (alias racine) fonctionne', async () => {
  const { impl } = fetchMock({ verify: { success: true } });
  const response = await handleRequest(verifyRequest({ token: 'token' }, { path: '/' }), ENV, impl);
  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { success: true });
});
