const express = require('express');
const router = express.Router();
const ctrl = require('../controllers/paymentController');

router.post('/payments', ctrl.createPayment);
router.get('/payments', ctrl.listPayments);
router.get('/payments/stats', ctrl.getStats);
router.get('/payments/:reference', ctrl.getPayment);
router.post('/payments/:reference/confirm', ctrl.confirmPayment);
router.post('/payments/:reference/cancel', ctrl.cancelPayment);

module.exports = router;
