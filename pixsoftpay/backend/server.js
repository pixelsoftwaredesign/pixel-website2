require('dotenv').config();
const express = require('express');
const cors = require('cors');
const connectDB = require('./config/db');
const paymentRoutes = require('./routes/payments');

const app = express();
const PORT = process.env.PORT || 5000;

connectDB();

app.use(cors({ origin: process.env.FRONTEND_URL, credentials: true }));
app.use(express.json());

app.use('/api', paymentRoutes);

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', service: 'PixSoftPay API' });
});

app.listen(PORT, () => {
  console.log(`PixSoftPay API running on port ${PORT}`);
});
