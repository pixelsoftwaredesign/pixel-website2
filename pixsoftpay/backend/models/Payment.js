const mongoose = require('mongoose');

const paymentSchema = new mongoose.Schema({
  reference: {
    type: String,
    required: true,
    unique: true,
  },
  amount: {
    type: Number,
    required: true,
    min: 0,
  },
  currency: {
    type: String,
    default: 'TND',
  },
  description: {
    type: String,
    default: '',
  },
  merchant_name: {
    type: String,
    default: 'PixSoftPay',
  },
  customer_name: {
    type: String,
    default: '',
  },
  customer_email: {
    type: String,
    default: '',
  },
  status: {
    type: String,
    enum: ['pending', 'paid', 'expired', 'cancelled'],
    default: 'pending',
  },
  payment_method: {
    type: String,
    enum: ['d17', 'flouci', 'konnect', 'wallet', 'card', 'manual'],
    default: 'wallet',
  },
  qr_data: {
    type: String,
  },
  payment_url: {
    type: String,
  },
  paid_at: {
    type: Date,
  },
  expires_at: {
    type: Date,
    default: () => new Date(Date.now() + 24 * 60 * 60 * 1000),
  },
}, {
  timestamps: true,
});

paymentSchema.index({ reference: 1 });
paymentSchema.index({ status: 1 });
paymentSchema.index({ created_at: -1 });

module.exports = mongoose.model('Payment', paymentSchema);
