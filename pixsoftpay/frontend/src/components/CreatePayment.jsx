import { useState } from 'react';
import QRCode from 'react-qr-code';
import { Link } from 'react-router-dom';

export default function CreatePayment() {
  const [form, setForm] = useState({
    amount: '',
    description: '',
    customer_name: '',
    customer_email: '',
    payment_method: 'wallet',
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const res = await fetch('/api/payments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...form, amount: Number(form.amount) }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (result) {
    return (
      <div className="card" style={{ textAlign: 'center' }}>
        <h2>QR Code généré</h2>
        <p style={{ color: 'var(--text-muted)', marginBottom: 16 }}>
          Référence: <strong>{result.reference}</strong>
        </p>
        <div className="qr-display">
          <QRCode value={result.payment_url} size={250} />
        </div>
        <p style={{ margin: '16px 0', fontSize: '0.9rem', color: 'var(--text-muted)' }}>
          Montant: <strong style={{ color: 'var(--primary)' }}>{result.amount} {result.currency}</strong>
        </p>
        <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', wordBreak: 'break-all' }}>
          Lien: {result.payment_url}
        </p>
        <div className="payment-actions">
          <Link to={`/pay/${result.reference}`}>
            <button className="btn btn-primary">Voir la page de paiement</button>
          </Link>
          <button className="btn btn-outline" onClick={() => setResult(null)}>
            Nouveau QR
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="card">
      <h2>Créer un paiement QR Code</h2>
      {error && <p style={{ color: 'var(--danger)', marginBottom: 12 }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Montant (TND)</label>
          <input
            type="number"
            name="amount"
            value={form.amount}
            onChange={handleChange}
            placeholder="0.00"
            min="0.01"
            step="0.01"
            required
          />
        </div>
        <div className="form-group">
          <label>Description</label>
          <input
            type="text"
            name="description"
            value={form.description}
            onChange={handleChange}
            placeholder="Ex: Paiement commande #123"
          />
        </div>
        <div className="form-group">
          <label>Nom du client</label>
          <input
            type="text"
            name="customer_name"
            value={form.customer_name}
            onChange={handleChange}
            placeholder="Nom complet"
          />
        </div>
        <div className="form-group">
          <label>Email du client</label>
          <input
            type="email"
            name="customer_email"
            value={form.customer_email}
            onChange={handleChange}
            placeholder="email@exemple.com"
          />
        </div>
        <div className="form-group">
          <label>Méthode de paiement</label>
          <select name="payment_method" value={form.payment_method} onChange={handleChange}>
            <option value="wallet">Wallet mobile</option>
            <option value="d17">D17</option>
            <option value="flouci">Flouci</option>
            <option value="konnect">Konnect</option>
            <option value="card">Carte bancaire</option>
            <option value="manual">Manuel</option>
          </select>
        </div>
        <button type="submit" className="btn btn-primary" disabled={loading} style={{ width: '100%' }}>
          {loading ? 'Génération...' : 'Générer le QR Code'}
        </button>
      </form>
    </div>
  );
}
