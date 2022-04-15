const getPaymentTokenFromAPI = require('./6-payment_token');
const expect = require("chai").expect;

describe('getPaymentTokenFromAPI', function () {
  describe('promise with true argument', function () {
    it('Checks if success', function (done) {
      getPaymentTokenFromAPI(true)
        .then((res) => {
          expect(res).to.include({ data: 'Successful response from the API' });
          done();
        })
        .catch((err) => done(err));
    });
  });
});
