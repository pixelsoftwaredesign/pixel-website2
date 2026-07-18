import { useState, useEffect } from 'react';

export default function Dashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/payments/stats')
      .then(r => r.json())
      .then(setStats)
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="loading">Chargement...</div>;

  return (
    <div>
      <h1 style={{ marginBottom: 24 }}>Dashboard</h1>
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-value">{stats?.total || 0}</div>
          <div className="stat-label">Total paiements</div>
        </div>
        <div className="stat-card">
          <div className="stat-value" style={{ color: '#00c853' }}>{stats?.paid || 0}</div>
          <div className="stat-label">Payés</div>
        </div>
        <div className="stat-card">
          <div className="stat-value" style={{ color: '#ffab00' }}>{stats?.pending || 0}</div>
          <div className="stat-label">En attente</div>
        </div>
        <div className="stat-card">
          <div className="stat-value" style={{ color: '#ff1744' }}>{stats?.expired || 0}</div>
          <div className="stat-label">Expirés</div>
        </div>
        <div className="stat-card">
          <div className="stat-value">{stats?.revenue?.toFixed(2) || '0.00'}</div>
          <div className="stat-label">Revenu (TND)</div>
        </div>
      </div>
    </div>
  );
}
