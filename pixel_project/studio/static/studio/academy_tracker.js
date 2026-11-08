// Academy study-time tracker: auto-detects reading time and saves to the API.
// Also adds a "Terminer le cours" button on course pages.
(function(){
  const meta = document.querySelector('meta[name="csrf-token"]');
  const csrf = meta ? meta.content : '';
  let seconds = 0;
  let lastTick = Date.now();
  let saved = false;
  function saveTime() {
    if (seconds < 30) return;
    const mins = Math.max(1, Math.round(seconds / 60));
    seconds = 0;
    fetch('/api/academy/study-time/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf },
      body: JSON.stringify({ minutes: mins })
    }).catch(() => {});
  }
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      const now = Date.now();
      seconds += Math.round((now - lastTick) / 1000);
      lastTick = now;
      saveTime();
    } else {
      lastTick = Date.now();
    }
  });
  setInterval(() => {
    if (!document.hidden) {
      const now = Date.now();
      seconds += Math.round((now - lastTick) / 1000);
      lastTick = now;
    }
    if (seconds >= 120) saveTime();
  }, 30000);
  window.addEventListener('beforeunload', () => {
    if (!document.hidden) {
      const now = Date.now();
      seconds += Math.round((now - lastTick) / 1000);
    }
    saveTime();
  });

  // "Terminer le cours" button on course pages
  if (window.location.pathname.indexOf('/academy/') === 0 && window.location.pathname !== '/academy/' && window.location.pathname !== '/academy/espace/' && window.location.pathname !== '/academy/professeur/' && window.location.pathname !== '/academy/administration/') {
    const btn = document.createElement('button');
    btn.id = 'finish-course-btn';
    btn.textContent = '✓ Terminer le cours (+10 pts)';
    btn.style.cssText = 'position:fixed;bottom:20px;right:20px;z-index:9999;background:#159d8b;color:#fff;border:0;border-radius:10px;padding:.7rem 1rem;font:700 .85rem Inter,system-ui,sans-serif;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,.3);';
    btn.onclick = function() {
      const title = document.title || 'Cours';
      fetch('/api/academy/activity/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf },
        body: JSON.stringify({ activity_type: 'course_completed', title: title, detail: window.location.pathname, points: 10 })
      }).then(r => r.json()).then(d => {
        if (d.status === 'success') {
          btn.textContent = '✓ Cours terminé !';
          btn.style.background = '#2e8b57';
          btn.disabled = true;
        }
      }).catch(() => {});
    };
    document.body.appendChild(btn);
  }
})();