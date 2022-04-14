const sinon = require('sinon');
const expect = require("chai").expect;
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('Spies', function() {
  it('checks both have the same math', function() {
    const spyUtils = sinon.spy(Utils, 'calculateNumber');
    const spyConsole = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);
    expect(spyUtils.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;
    spyUtils.restore();
    spyConsole.restore();
  });
});
