import test from 'node:test';
import assert from 'node:assert/strict';

import { handleRequest, verifyTurnstile } from './turnstile-worker.mjs';

const ENV = {
  TURNSTILE_SECRET_KEY: 'test-secret',
  BACKEND_ORIGIN: 'https://backend.example',
};

function verifyResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

function fetchMock({ verify = { success: true }, verifyStatus = 200, forwardStatus = 201 } = {}) {
  const calls = [];
  const impl = async (url, init = {}) => {
    const target = typeof url === 'string' ? url : url.url;
    calls.push({ url: target, init });
    if (target.includes('siteverify')) return verifyResponse(verify, verifyStatus);
    return new Response(JSON.stringify({ status: 'success' }), {
      status: forwardStatus,
      headers: { 'Content-Type': 'application/json' },
    });
  };
  return { impl, calls };
}

function apiRequest(payload, headers = {}) {
  return new Request('https://pixelsoftwaredesign.xyz/api/contact/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...headers },
    body: JSON.stringify(payload),
  });
}

function formRequest(fields, url = 'https://pixelsoftwaredesign.xyz/contact/?devis=1') {
  return new Request(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(fields).toString(),
  });
}

test('verifyTurnstile refuse un jeton absent', async () => {
  const { impl } = fetchMock();
  const result = await verifyTurnstile('', apiRequest({}), ENV, impl);
  assert.deepEqual(result, { ok: false, reason: 'missing' });
});

test('verifyTurnstile refuse si le secret manque', async () => {
  const { impl } = fetchMock();
  const result = await verifyTurnstile('token', apiRequest({}), {}, impl);
  assert.deepEqual(result, { ok: false, reason: 'unavailable' });
});

test('verifyTurnstile accepte une reponse success', async () => {
  const { impl, calls } = fetchMock({ verify: { success: true } });
  const result = await verifyTurnstile('token', apiRequest({}), ENV, impl);
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
  const result = await verifyTurnstile('token', apiRequest({}), ENV, impl);
  assert.equal(result.ok, false);
  assert.equal(result.reason, 'invalid');
  assert.deepEqual(result.codes, ['invalid-input-response']);
});

test('verifyTurnstile signale un service indisponible', async () => {
  const { impl } = fetchMock({ verify: { success: false }, verifyStatus: 500 });
  const result = await verifyTurnstile('token', apiRequest({}), ENV, impl);
  assert.deepEqual(result, { ok: false, reason: 'unavailable' });
});

test('API sans jeton : 400 et aucun transfert', async () => {
  const { impl, calls } = fetchMock();
  const response = await handleRequest(apiRequest({ username: 'A' }), ENV, impl);
  assert.equal(response.status, 400);
  const body = await response.json();
  assert.match(body.message, /vérification anti-robot/i);
  assert.equal(calls.length, 0);
});

test('API avec jeton valide : transferee a Render', async () => {
  const { impl, calls } = fetchMock({ verify: { success: true } });
  const payload = { username: 'A', useremail: 'a@example.com', usermessage: 'Projet', turnstile_token: 'token' };
  const response = await handleRequest(apiRequest(payload), ENV, impl);
  assert.equal(response.status, 201);
  assert.equal(calls.length, 2);
  assert.equal(calls[1].url, 'https://backend.example/api/contact/');
  assert.equal(calls[1].init.body, JSON.stringify(payload));
});

test('API avec jeton invalide : 400', async () => {
  const { impl, calls } = fetchMock({ verify: { success: false } });
  const response = await handleRequest(apiRequest({ turnstile_token: 'bad' }), ENV, impl);
  assert.equal(response.status, 400);
  const body = await response.json();
  assert.match(body.message, /échouée/i);
  assert.equal(calls.length, 1);
});

test('formulaire sans jeton : redirection vers /contact/?erreur=robot', async () => {
  const { impl, calls } = fetchMock();
  const response = await handleRequest(formRequest({ nom: 'A', devis: '1' }), ENV, impl);
  assert.equal(response.status, 303);
  const location = new URL(response.headers.get('location'));
  assert.equal(location.pathname, '/contact/');
  assert.equal(location.searchParams.get('devis'), '1');
  assert.equal(location.searchParams.get('erreur'), 'robot');
  assert.equal(calls.length, 0);
});

test('formulaire avec jeton valide : transfere a Render', async () => {
  const { impl, calls } = fetchMock({ verify: { success: true } });
  const body = new URLSearchParams({ nom: 'A', 'cf-turnstile-response': 'token', devis: '1' }).toString();
  const response = await handleRequest(formRequest({ nom: 'A', 'cf-turnstile-response': 'token', devis: '1' }), ENV, impl);
  assert.equal(response.status, 201);
  assert.equal(calls.length, 2);
  assert.equal(calls[1].url, 'https://backend.example/contact/?devis=1');
  assert.equal(calls[1].init.body, body);
});

test('GET /contact/ est transmis sans verification', async () => {
  const { impl, calls } = fetchMock({ forwardStatus: 200 });
  const request = new Request('https://pixelsoftwaredesign.xyz/contact/', { method: 'GET' });
  const response = await handleRequest(request, ENV, impl);
  assert.equal(response.status, 200);
  assert.equal(calls.length, 1);
  assert.equal(calls[0].url, 'https://backend.example/contact/');
  assert.equal(calls[0].init.method, 'GET');
});
