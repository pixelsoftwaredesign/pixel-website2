import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import QRCode from 'react-qr-code';

export default function PaymentPage() {
  const { reference } = useParams();
  const [payment, setPayment] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [confirming, setConfirming] = useState(false);

  useEffect(() => {
    fetch(`/api/payments/${reference}`)
      .then(r => {
        if (!r.ok) throw new Error('Paiement non trouvé');
        return r.json();
      })
      .then(setPayment)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, [reference]);

  const handleConfirm = async () => {
    setConfirming(true);
    try {
      const res = await fetch(`/api/payments/${reference}/confirm`, { method: 'POST' });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error);
      setPayment({ ...payment, status: 'paid', paid_at: data.paid_at });
    } catch (err) {
      setError(err.message);
    } finally {
      setConfirming(false);
    }
  };

  if (loading) return <div className="loading">Chargement...</div>;
  if (error) return <div className="card"><p style={{ color: 'var(--danger)' }}>{error}</p></div>;
  if (!payment) return null;

  const isExpired = new Date(payment.expires_at) < new Date();

  return (
    <div className="payment-page">
      <div className="card">
        <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>{payment.merchant_name}</p>
        {payment.description && <p style={{ marginTop: 8, fontSize: '0.9rem' }}>{payment.description}</p>}
        <div className="amount">{payment.amount} {payment.currency}</div>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>
          Référence: {payment.reference}
        </p>

        <div className="qr-display" style={{ marginTop: 20 }}>
          <QRCode value={payment.payment_url} size={220} />
        </div>

        <div style={{ marginTop: 20 }}>
          {payment.status === 'paid' && (
            <div>
              <span className="badge badge-paid" style={{ fontSize: '1rem', padding: '8px 20px' }}>Payé</span>
              <p style={{ marginTop: 12, color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                Payé le {new Date(payment.paid_at).toLocaleString('fr-FR')}
              </p>
            </div>
          )}
          {payment.status === 'pending' && !isExpired && (
            <div>
              <span className="badge badge-pending" style={{ fontSize: '1rem', padding: '8px 20px' }}>En attente</span>
              <div className="payment-actions" style={{ marginTop: 16 }}>
                <button className="btn btn-success" onClick={handleConfirm} disabled={confirming}>
                  {confirming ? 'Confirmation...' : 'Confirmer le paiement'}
                </button>
              </div>
            </div>
          )}
          {isExpired && (
            <span className="badge badge-expired" style={{ fontSize: '1rem', padding: '8px 20px' }}>Expiré</span>
          )}
          {payment.status === 'cancelled' && (
            <span className="badge badge-cancelled" style={{ fontSize: '1rem', padding: '8px 20px' }}>Annulé</span>
          )}
        </div>
      </div>
    </div>
  );
}
