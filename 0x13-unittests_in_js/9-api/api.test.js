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
    it('Responds with 404', (done) => {
      const options = { url: 'http://localhost:7865/cart/hello', method: 'GET' };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

});
