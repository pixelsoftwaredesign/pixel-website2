const QRCode = require('qrcode');
const { v4: uuidv4 } = require('uuid');
const Payment = require('../models/Payment');

exports.createPayment = async (req, res) => {
  try {
    const { amount, currency, description, merchant_name, customer_name, customer_email, payment_method } = req.body;

    if (!amount || amount <= 0) {
      return res.status(400).json({ error: 'Montant invalide' });
    }

    const reference = `PSP-${uuidv4().slice(0, 8).toUpperCase()}`;
    const payment_url = `${process.env.FRONTEND_URL}/pay/${reference}`;

    const qr_data = await QRCode.toDataURL(payment_url, {
      width: 300,
      margin: 2,
      color: { dark: '#1a1a2e', light: '#ffffff' },
    });

    const payment = await Payment.create({
      reference,
      amount,
      currency: currency || 'TND',
      description: description || '',
      merchant_name: merchant_name || 'PixSoftPay',
      customer_name: customer_name || '',
      customer_email: customer_email || '',
      payment_method: payment_method || 'wallet',
      qr_data,
      payment_url,
    });

    res.status(201).json({
      id: payment._id,
      reference: payment.reference,
      amount: payment.amount,
      currency: payment.currency,
      status: payment.status,
      qr_data: payment.qr_data,
      payment_url: payment.payment_url,
      expires_at: payment.expires_at,
      created_at: payment.created_at,
    });
  } catch (err) {
    res.status(500).json({ error: 'Erreur serveur: ' + err.message });
  }
};

exports.getPayment = async (req, res) => {
  try {
    const payment = await Payment.findOne({ reference: req.params.reference });
    if (!payment) {
      return res.status(404).json({ error: 'Paiement non trouvé' });
    }
    res.json({
      id: payment._id,
      reference: payment.reference,
      amount: payment.amount,
      currency: payment.currency,
      description: payment.description,
      merchant_name: payment.merchant_name,
      status: payment.status,
      payment_method: payment.payment_method,
      qr_data: payment.qr_data,
      payment_url: payment.payment_url,
      expires_at: payment.expires_at,
      paid_at: payment.paid_at,
      created_at: payment.created_at,
    });
  } catch (err) {
    res.status(500).json({ error: 'Erreur serveur: ' + err.message });
  }
};

exports.confirmPayment = async (req, res) => {
  try {
    const payment = await Payment.findOne({ reference: req.params.reference });
    if (!payment) {
      return res.status(404).json({ error: 'Paiement non trouvé' });
    }
    if (payment.status !== 'pending') {
      return res.status(400).json({ error: 'Paiement déjà traité' });
    }
    if (new Date() > payment.expires_at) {
      payment.status = 'expired';
      await payment.save();
      return res.status(400).json({ error: 'Paiement expiré' });
    }

    payment.status = 'paid';
    payment.paid_at = new Date();
    await payment.save();

    res.json({
      reference: payment.reference,
      status: payment.status,
      paid_at: payment.paid_at,
      amount: payment.amount,
      currency: payment.currency,
    });
  } catch (err) {
    res.status(500).json({ error: 'Erreur serveur: ' + err.message });
  }
};

exports.cancelPayment = async (req, res) => {
  try {
    const payment = await Payment.findOne({ reference: req.params.reference });
    if (!payment) {
      return res.status(404).json({ error: 'Paiement non trouvé' });
    }
    if (payment.status !== 'pending') {
      return res.status(400).json({ error: 'Paiement déjà traité' });
    }

    payment.status = 'cancelled';
    await payment.save();

    res.json({ reference: payment.reference, status: payment.status });
  } catch (err) {
    res.status(500).json({ error: 'Erreur serveur: ' + err.message });
  }
};

exports.listPayments = async (req, res) => {
  try {
    const { status, page = 1, limit = 20 } = req.query;
    const filter = {};
    if (status) filter.status = status;

    const payments = await Payment.find(filter)
      .sort({ created_at: -1 })
      .skip((page - 1) * limit)
      .limit(Number(limit));

    const total = await Payment.countDocuments(filter);

    res.json({
      payments: payments.map(p => ({
        id: p._id,
        reference: p.reference,
        amount: p.amount,
        currency: p.currency,
        status: p.status,
        payment_method: p.payment_method,
        customer_name: p.customer_name,
        created_at: p.created_at,
        paid_at: p.paid_at,
      })),
      total,
      page: Number(page),
      pages: Math.ceil(total / limit),
    });
  } catch (err) {
    res.status(500).json({ error: 'Erreur serveur: ' + err.message });
  }
};

exports.getStats = async (req, res) => {
  try {
    const total = await Payment.countDocuments();
    const paid = await Payment.countDocuments({ status: 'paid' });
    const pending = await Payment.countDocuments({ status: 'pending' });
    const expired = await Payment.countDocuments({ status: 'expired' });
    const cancelled = await Payment.countDocuments({ status: 'cancelled' });

    const revenue = await Payment.aggregate([
      { $match: { status: 'paid' } },
      { $group: { _id: null, total: { $sum: '$amount' } } },
    ]);

    res.json({
      total,
      paid,
      pending,
      expired,
      cancelled,
      revenue: revenue.length > 0 ? revenue[0].total : 0,
    });
  } catch (err) {
    res.status(500).json({ error: 'Erreur serveur: ' + err.message });
  }
};
