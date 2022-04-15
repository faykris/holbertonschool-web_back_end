const sinon = require('sinon');
const expect = require("chai").expect;
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('Hooks', function () {
  let spyConsole;
  beforeEach(() => spyConsole = sinon.spy(console, 'log'));
  afterEach(() => spyConsole.restore());

  it('checks output with 100 + 20', function () {
    sendPaymentRequestToApi(100, 20);
    expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(spyConsole.calledOnce).to.be.true;
  });

  it('checks output with 100 + 10', function() {
    sendPaymentRequestToApi(10, 10);
    expect(spyConsole.calledOnceWithExactly('The total is: 20')).to.be.true;
    expect(spyConsole.calledOnce).to.be.true;
  });
});
