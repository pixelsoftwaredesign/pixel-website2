// Academy study-time tracker: auto-detects reading time and saves to the API.
(function(){
  const meta = document.querySelector('meta[name="csrf-token"]');
  const csrf = meta ? meta.content : '';
  let seconds = 0;
  let saved = false;
  function saveTime() {
    if (seconds < 30) return; // only save if at least 30s
    const mins = Math.max(1, Math.round(seconds / 60));
    seconds = 0;
    fetch('/api/academy/study-time/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf },
      body: JSON.stringify({ minutes: mins })
    }).catch(() => {});
  }
  // track visible time
  let lastTick = Date.now();
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
    if (seconds >= 120) saveTime(); // save every 2 min
  }, 30000);
  window.addEventListener('beforeunload', () => {
    if (!document.hidden) {
      const now = Date.now();
      seconds += Math.round((now - lastTick) / 1000);
    }
    saveTime();
  });
})();