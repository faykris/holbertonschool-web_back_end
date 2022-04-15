const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.end('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  res.end(`Payment methods for cart ${req.params.id}`);
});

app.get('/available_payments', (req, res) => {
  const object = {
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  };
  res.json(object);
});

app.post('/login', (req, res) => {
  const username = req.body.userName;
  res.end(`Welcome ${username}`);
});

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});
