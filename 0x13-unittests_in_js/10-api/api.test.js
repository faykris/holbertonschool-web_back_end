const request = require('request');
const expect = require("chai").expect;

describe('Index page', () => {
  it('Checks status code, message', (done) => {
    const options = { url: 'http://localhost:7865', method: 'GET' };

    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Valid id number', () => {
  it('Checks status code, message', (done) => {
    const options = { url: 'http://localhost:7865/cart/28', method: 'GET' };

    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 28');
      done();
    });
  });
});

describe('Without id number', () => {
  it('Checks 404 status code', (done) => {
    const options = { url: 'http://localhost:7865/cart/', method: 'GET' };

    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Not valid id number', () => {
  it('Checks 404 status code', (done) => {
    const options = { url: 'http://localhost:7865/cart/hello', method: 'GET' };

    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Validate JSON parsed', () => {
  it('Checks status code and object', (done) => {
    const options = { url: 'http://localhost:7865/available_payments', method: 'GET' };

    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      const bodyParsed = JSON.parse(body);
      const object = {
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      };
      expect(bodyParsed).to.deep.equal(object);
      done();
    });
  });
});

describe('Validate login with body', () => {
  it('Checks status code and welcome message', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: {
        userName: 'Betty',
      },
    };

    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});


describe('Validate login with body', () => {
  it('Checks status code and undefined welcome', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
    };

    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome undefined');
      done();
    });
  });
});
