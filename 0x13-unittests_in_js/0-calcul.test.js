const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('checks positive numbers', function() {
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
    assert.equal(calculateNumber(-1, 3), 2);
    assert.equal(calculateNumber(1, -3.7), -2);
    assert.equal(calculateNumber(0, -3.7), -3);
    assert.equal(calculateNumber(-1.5, 0), -1);
    assert.equal(calculateNumber(-1, 3), 2);
    assert.equal(calculateNumber(1, -3.7), -2);
    assert.equal(calculateNumber(0, -3.7), -3);
    assert.equal(calculateNumber(-1.5, 0), -1);
  });
});
