import { useState, useEffect } from 'react';

const STATUS_LABELS = {
  pending: 'En attente',
  paid: 'Payé',
  expired: 'Expiré',
  cancelled: 'Annulé',
};

export default function History() {
  const [payments, setPayments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('');
  const [page, setPage] = useState(1);
  const [pages, setPages] = useState(1);

  const load = (p = 1, s = filter) => {
    setLoading(true);
    const params = new URLSearchParams({ page: p, limit: 15 });
    if (s) params.set('status', s);
    fetch(`/api/payments?${params}`)
      .then(r => r.json())
      .then(data => {
        setPayments(data.payments || []);
        setPages(data.pages || 1);
        setPage(data.page || 1);
      })
      .catch(() => {})
      .finally(() => setLoading(false));
  };

  useEffect(() => { load(); }, []);

  const handleFilter = (s) => {
    setFilter(s);
    load(1, s);
  };

  return (
    <div>
      <div className="flex-row" style={{ marginBottom: 20 }}>
        <h1>Historique</h1>
        <div style={{ display: 'flex', gap: 8 }}>
          {['', 'pending', 'paid', 'expired', 'cancelled'].map(s => (
            <button
              key={s}
              className={`btn ${filter === s ? 'btn-primary' : 'btn-outline'}`}
              style={{ fontSize: '0.8rem', padding: '6px 12px' }}
              onClick={() => handleFilter(s)}
            >
              {s ? STATUS_LABELS[s] : 'Tous'}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div className="loading">Chargement...</div>
      ) : payments.length === 0 ? (
        <div className="empty">Aucun paiement trouvé</div>
      ) : (
        <div className="card">
          <div className="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Référence</th>
                  <th>Montant</th>
                  <th>Client</th>
                  <th>Méthode</th>
                  <th>Statut</th>
                  <th>Date</th>
                </tr>
              </thead>
              <tbody>
                {payments.map(p => (
                  <tr key={p.id}>
                    <td style={{ fontFamily: 'monospace' }}>{p.reference}</td>
                    <td><strong>{p.amount} {p.currency}</strong></td>
                    <td>{p.customer_name || '—'}</td>
                    <td>{p.payment_method}</td>
                    <td><span className={`badge badge-${p.status}`}>{STATUS_LABELS[p.status]}</span></td>
                    <td>{new Date(p.created_at).toLocaleDateString('fr-FR')}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div style={{ display: 'flex', justifyContent: 'center', gap: 12, marginTop: 16 }}>
            <button className="btn btn-outline" disabled={page <= 1} onClick={() => load(page - 1)}>
              Précédent
            </button>
            <span style={{ lineHeight: '36px', color: 'var(--text-muted)' }}>Page {page}/{pages}</span>
            <button className="btn btn-outline" disabled={page >= pages} onClick={() => load(page + 1)}>
              Suivant
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
