// ── BURGER MENU ──
const burgerBtn = document.getElementById('burgerBtn');
const navMenu = document.getElementById('navMenu');
if (burgerBtn) {
  burgerBtn.addEventListener('click', () => navMenu.classList.toggle('open'));
  document.querySelectorAll('.nav-menu a').forEach(l => l.addEventListener('click', () => navMenu.classList.remove('open')));
}

// ── TABS ──
function switchTab(event, tabId) {
  document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  event.currentTarget.classList.add('active');
}

// ── AUTH MODAL ──
function toggleAuthModal() {
  document.getElementById('authOverlay').classList.toggle('open');
}
function showRegister() {
  document.getElementById('authLogin').style.display = 'none';
  document.getElementById('authRegister').style.display = 'block';
}
function showLogin() {
  document.getElementById('authRegister').style.display = 'none';
  document.getElementById('authLogin').style.display = 'block';
}
function executerConnexion() {
  const username = document.getElementById('loginUsername').value.trim();
  const password = document.getElementById('loginPassword').value.trim();
  const status = document.getElementById('authStatus');
  fetch('/api/connexion/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken') },
    body: JSON.stringify({ username, password })
  }).then(r => r.json()).then(d => {
    status.style.color = d.status === 'success' ? 'var(--accent)' : '#FF6B6B';
    status.innerText = d.message;
    if (d.status === 'success') { setTimeout(() => location.reload(), 800); }
  });
}
function executerInscription() {
  const username = document.getElementById('regUsername').value.trim();
  const email = document.getElementById('regEmail').value.trim();
  const password = document.getElementById('regPassword').value.trim();
  const entreprise = document.getElementById('regEntreprise').value.trim();
  const role = (document.getElementById('regRole')||{}).value || 'designer';
  const status = document.getElementById('regStatus');
  fetch('/api/inscription/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken') },
    body: JSON.stringify({ username, email, password, entreprise, role })
  }).then(r => r.json()).then(d => {
    status.style.color = d.status === 'success' ? 'var(--accent)' : '#FF6B6B';
    status.innerText = d.message;
    if (d.status === 'success') { setTimeout(() => location.reload(), 800); }
  });
}
function executerDeconnexion() {
  fetch('/api/deconnexion/').then(r => r.json()).then(() => location.reload());
}
function getCookie(name) {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? match[2] : '';
}
// Check auth state on load
fetch('/api/me/').then(r => r.json()).then(d => {
  if (d.status === 'success' && d.user) {
    document.getElementById('authNav').innerHTML = `<a href="#" class="nav-link" onclick="toggleAuthModal()" style="color:var(--accent)">${d.user.username}</a>`;
    document.getElementById('authLogin').style.display = 'none';
    document.getElementById('authRegister').style.display = 'none';
    document.getElementById('authLogged').style.display = 'block';
    document.getElementById('loggedUsername').innerText = d.user.username;
  }
});

// ── CONTACT FORM ──
function handleFormSubmit(event) {
  event.preventDefault();
  const payload = {
    username: document.getElementById('username').value.trim(),
    useremail: document.getElementById('useremail').value.trim(),
    usermessage: document.getElementById('usermessage').value.trim()
  };
  const statusDiv = document.getElementById('formStatus');
  fetch('/api/contact/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken') },
    body: JSON.stringify(payload)
  }).then(r => r.json()).then(data => {
    statusDiv.className = data.status === 'success' ? 'success' : 'error';
    statusDiv.innerText = data.message;
    if (data.status === 'success') document.getElementById('projectForm').reset();
  }).catch(() => {
    statusDiv.className = 'error';
    statusDiv.innerText = 'Erreur de connexion avec le serveur.';
  });
}

// ── HERO CANVAS ──
(function() {
  const HC = document.getElementById('hero-canvas');
  if (!HC) return;
  function resize() { HC.width = window.innerWidth; HC.height = window.innerHeight; }
  resize(); window.addEventListener('resize', resize);
  const HX = HC.getContext('2d');
  const COLS = ['#1EB482', '#1A9BAF', '#2DBD6E', '#1565C0', '#22C490'];
  const SZ = 26;
  const GC = Math.ceil(HC.width / SZ) + 1, GR = Math.ceil(HC.height / SZ) + 1;
  const cells = Array.from({ length: GC * GR }, (_, i) => ({
    x: (i % GC) * SZ, y: Math.floor(i / GC) * SZ,
    a: Math.random() * .05, t: Math.random() * .05,
    s: .003 + Math.random() * .007, c: COLS[Math.floor(Math.random() * COLS.length)]
  }));
  (function loop() {
    HX.clearRect(0, 0, HC.width, HC.height);
    cells.forEach(c => {
      c.a += (c.t - c.a) * c.s;
      if (Math.abs(c.a - c.t) < .001) c.t = Math.random() < .035 ? .2 + Math.random() * .35 : Math.random() * .05;
      if (c.a > .004) { HX.globalAlpha = c.a; HX.fillStyle = c.c; HX.fillRect(c.x + 1, c.y + 1, SZ - 2, SZ - 2); }
    });
    HX.globalAlpha = 1; requestAnimationFrame(loop);
  })();
})();

// ── WHY CANVAS ──
(function() {
  const WC = document.getElementById('why-canvas');
  if (!WC) return;
  const WX = WC.getContext('2d');
  const nodes = [
    { x: 190, y: 70, label: 'IA', r: 26, c: '#1EB482' },
    { x: 320, y: 160, label: 'IoT', r: 20, c: '#1A9BAF' },
    { x: 260, y: 290, label: 'Design', r: 24, c: '#2DBD6E' },
    { x: 110, y: 290, label: 'Media', r: 20, c: '#1565C0' },
    { x: 60, y: 160, label: 'Code', r: 20, c: '#1A9BAF' },
    { x: 190, y: 190, label: 'PXL', r: 34, c: '#1EB482', center: true },
  ];
  const edges = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [0, 1], [1, 2], [2, 3], [3, 4], [4, 0]];
  let wt = 0;
  (function wloop() {
    WX.clearRect(0, 0, 380, 380);
    wt += .008;
    edges.forEach(([a, b]) => {
      const na = nodes[a], nb = nodes[b];
      WX.strokeStyle = 'rgba(30,180,130,.16)'; WX.lineWidth = 1;
      WX.beginPath(); WX.moveTo(na.x, na.y); WX.lineTo(nb.x, nb.y); WX.stroke();
      const p = (Math.sin(wt + (a + b) * .5) + 1) / 2;
      const dx = na.x + (nb.x - na.x) * p, dy = na.y + (nb.y - na.y) * p;
      WX.fillStyle = 'rgba(30,180,130,.55)'; WX.beginPath(); WX.arc(dx, dy, 2, 0, Math.PI * 2); WX.fill();
    });
    nodes.forEach(n => {
      const pulse = n.center ? n.r + Math.sin(wt * 2) * 4 : n.r;
      WX.fillStyle = n.c + '22'; WX.beginPath(); WX.arc(n.x, n.y, pulse + 8, 0, Math.PI * 2); WX.fill();
      WX.fillStyle = n.c + '55'; WX.beginPath(); WX.arc(n.x, n.y, pulse, 0, Math.PI * 2); WX.fill();
      WX.fillStyle = n.c; WX.beginPath(); WX.arc(n.x, n.y, pulse * .6, 0, Math.PI * 2); WX.fill();
      WX.fillStyle = n.center ? 'rgba(232,245,240,.95)' : 'rgba(232,245,240,.8)';
      WX.font = `${n.center ? '700' : '500'} ${n.center ? 13 : 11}px "Space Grotesk",sans-serif`;
      WX.textAlign = 'center'; WX.textBaseline = 'middle'; WX.fillText(n.label, n.x, n.y);
    });
    requestAnimationFrame(wloop);
  })();
})();

// ── PROJECT CANVASES ──
function rr(ctx, x, y, w, h, r) { ctx.beginPath(); ctx.moveTo(x + r, y); ctx.lineTo(x + w - r, y); ctx.arcTo(x + w, y, x + w, y + r, r); ctx.lineTo(x + w, y + h - r); ctx.arcTo(x + w, y + h, x + w - r, y + h, r); ctx.lineTo(x + r, y + h); ctx.arcTo(x, y + h, x, y + h - r, r); ctx.lineTo(x, y + r); ctx.arcTo(x, y, x + r, y, r); ctx.closePath(); }

(function() {
  const c1 = document.getElementById('pc1'); if (!c1) return;
  const x1 = c1.getContext('2d');
  x1.fillStyle = '#060E0A'; x1.fillRect(0, 0, 480, 280);
  x1.strokeStyle = 'rgba(30,180,130,.18)'; x1.lineWidth = 1; x1.strokeRect(20, 20, 190, 190);
  for (let i = 0; i < 5; i++) { x1.strokeStyle = 'rgba(30,180,130,.07)'; x1.beginPath(); x1.moveTo(20, 210 - i * 38); x1.lineTo(210, 210 - i * 38); x1.stroke(); }
  x1.fillStyle = 'rgba(30,180,130,.13)'; rr(x1, 35, 130, 85, 55, 4); x1.fill();
  x1.fillStyle = 'rgba(26,155,175,.18)'; rr(x1, 135, 160, 55, 35, 4); x1.fill();
  x1.fillStyle = 'rgba(21,101,192,.18)'; rr(x1, 35, 30, 55, 75, 4); x1.fill();
  [[85, 50, '#1EB482'], [165, 80, '#1A9BAF'], [60, 175, '#2DBD6E'], [180, 115, '#1565C0']].forEach(([dx, dy, c]) => {
    x1.fillStyle = c + '44'; x1.beginPath(); x1.arc(dx, dy, 9, 0, Math.PI * 2); x1.fill();
    x1.fillStyle = c; x1.beginPath(); x1.arc(dx, dy, 3.5, 0, Math.PI * 2); x1.fill();
  });
  x1.fillStyle = '#0A1810'; rr(x1, 230, 20, 210, 240, 8); x1.fill();
  x1.fillStyle = 'rgba(30,180,130,.9)'; x1.font = 'bold 10px "Space Mono",monospace'; x1.fillText('SMART HOME', 242, 42);
  [['Temp', '22°C', '#1EB482'], ['Lumière', '78%', '#1A9BAF'], ['Sécurité', 'ON', '#2DBD6E'], ['Énergie', '1.2kW', '#1565C0']].forEach(([l, v, c], i) => {
    x1.fillStyle = '#0E1F17'; rr(x1, 242, 56 + i * 48, 86, 36, 5); x1.fill();
    x1.fillStyle = 'rgba(232,245,240,.45)'; x1.font = '8px "Space Mono",monospace'; x1.fillText(l, 250, 72 + i * 48);
    x1.fillStyle = c; x1.font = 'bold 14px "Space Grotesk",sans-serif'; x1.fillText(v, 250, 86 + i * 48);
    x1.fillStyle = c + '22'; x1.fillRect(340, 60 + i * 48, 88, 28);
    x1.fillStyle = c + '66'; x1.fillRect(340, 60 + i * 48, (88 * [.7, .78, .9, .52][i]) | 0, 28);
  });
})();

(function() {
  const c2 = document.getElementById('pc2'); if (!c2) return;
  const x2 = c2.getContext('2d');
  x2.fillStyle = '#050B09'; x2.fillRect(0, 0, 230, 130);
  x2.fillStyle = '#0A1610'; rr(x2, 8, 8, 60, 114, 6); x2.fill();
  [20, 40, 60, 80, 100].forEach((y, i) => {
    x2.fillStyle = i === 1 ? '#1EB482' : '#122018'; rr(x2, 12, y, 52, 14, 3); x2.fill();
    x2.fillStyle = i === 1 ? 'rgba(255,255,255,.8)' : 'rgba(255,255,255,.2)'; x2.fillRect(18, y + 3, 22, 8);
  });
  x2.fillStyle = '#090E0C'; rr(x2, 74, 8, 148, 114, 6); x2.fill();
  [.4, .7, .5, .9, .6, .82, .95].forEach((h, i) => { const bx = 80 + i * 18, bh = h * 60, by = 8 + 108 - bh; x2.fillStyle = i === 6 ? '#1EB482' : '#152C22'; x2.fillRect(bx, by, 12, bh); });
  x2.strokeStyle = '#1A9BAF'; x2.lineWidth = 1.2; x2.beginPath();
  [.4, .7, .5, .9, .6, .82, .95].forEach((h, i) => { const bx = 86 + i * 18, by = 8 + 112 - h * 60; i === 0 ? x2.moveTo(bx, by) : x2.lineTo(bx, by); }); x2.stroke();
})();

(function() {
  const c3 = document.getElementById('pc3'); if (!c3) return;
  const x3 = c3.getContext('2d');
  x3.fillStyle = '#050A0C'; x3.fillRect(0, 0, 230, 130);
  x3.strokeStyle = 'rgba(26,155,175,.3)'; x3.lineWidth = .8;
  const pts = [[115, 60], [10, 10], [220, 10], [220, 120], [10, 120]];
  pts.reduce((p, c, i) => {
    x3.beginPath(); x3.moveTo(p[0], p[1]); x3.lineTo(c[0], c[1]); x3.stroke();
    x3.beginPath(); x3.moveTo(115, 60); x3.lineTo(c[0], c[1]); x3.stroke(); return c;
  }, pts[0]);
  x3.fillStyle = 'rgba(26,155,175,.15)'; x3.fillRect(30, 80, 55, 28);
  x3.fillStyle = 'rgba(30,180,130,.12)'; x3.fillRect(140, 70, 45, 36);
  x3.fillStyle = 'rgba(21,101,192,.15)'; x3.fillRect(90, 83, 36, 22);
  x3.fillStyle = 'rgba(26,155,175,.7)'; x3.font = 'bold 8px "Space Mono",monospace'; x3.fillText('● VR LIVE', 10, 15);
  x3.fillStyle = 'rgba(30,180,130,.35)'; x3.strokeStyle = 'rgba(30,180,130,.35)'; x3.lineWidth = .5;
  for (let i = 0; i < 4; i++) { rr(x3, 100 + i * 3, 55 + i * 3, 26 - i * 5, 18 - i * 4, 2); x3.stroke(); }
})();

// ── PROCESS CANVAS ──
(function() {
  const PC = document.getElementById('proc-canvas'); if (!PC) return;
  const PX = PC.getContext('2d');
  const PSTEPS = ['Découverte', 'Design', 'Développement', 'Tests', 'Évolution'];
  const PCOLORS = ['#1EB482', '#1A9BAF', '#2DBD6E', '#1565C0', '#22C490'];
  const PDESC = ['Audit · Roadmap', 'Plans · Maquettes', 'Sprint · Intégration', 'QA · UAT', 'Monitoring · Updates'];
  let pt = 0;
  (function ploop() {
    PX.clearRect(0, 0, 340, 380); pt += .005;
    PX.strokeStyle = 'rgba(30,180,130,.12)'; PX.lineWidth = 1;
    PX.beginPath(); PX.moveTo(55, 35); PX.lineTo(55, 345); PX.stroke();
    PSTEPS.forEach((s, i) => {
      const y = 55 + i * 65, active = Math.floor(((pt * .5) % 5)), isActive = i === active;
      PX.fillStyle = isActive ? PCOLORS[i] : PCOLORS[i] + '44';
      PX.beginPath(); PX.arc(55, y, isActive ? 9 : 6, 0, Math.PI * 2); PX.fill();
      if (isActive) { PX.fillStyle = PCOLORS[i] + '22'; PX.beginPath(); PX.arc(55, y, 16 + Math.sin(pt * 3) * 3, 0, Math.PI * 2); PX.fill(); }
      PX.strokeStyle = PCOLORS[i] + (isActive ? '88' : '33'); PX.lineWidth = 1;
      PX.beginPath(); PX.moveTo(65, y); PX.lineTo(90, y); PX.stroke();
      PX.fillStyle = isActive ? PCOLORS[i] + '22' : 'rgba(12,32,24,.8)';
      PX.strokeStyle = isActive ? PCOLORS[i] + '88' : PCOLORS[i] + '22'; PX.lineWidth = 1;
      rr(PX, 90, y - 20, 220, 40, 6); PX.fill(); PX.stroke();
      PX.fillStyle = isActive ? PCOLORS[i] : 'rgba(232,245,240,.5)';
      PX.font = `${isActive ? '600' : '400'} 11px "Space Grotesk",sans-serif`;
      PX.textAlign = 'left'; PX.textBaseline = 'middle'; PX.fillText(s, 104, y);
      if (isActive) { PX.fillStyle = 'rgba(232,245,240,.35)'; PX.font = '9px "Space Mono",monospace'; PX.fillText(PDESC[i], 104, y + 13); }
    });
    requestAnimationFrame(ploop);
  })();
})();

// ── SCROLL SPY ──
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => { if (pageYOffset >= s.offsetTop - 120) current = s.getAttribute('id'); });
  navLinks.forEach(l => { l.classList.remove('active'); if (l.getAttribute('href').includes(current)) l.classList.add('active'); });
});
