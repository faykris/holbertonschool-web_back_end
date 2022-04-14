const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('checks positive numbers', function() {
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });

  it('checks negative numbers', function() {
    assert.equal(calculateNumber(-1, -3), -4);
    assert.equal(calculateNumber(-1, -3.7), -4);
    assert.equal(calculateNumber(-1.2, -3.7), -4);
    assert.equal(calculateNumber(-1.5, -3.7), -5);
  });

  it('checks combined numbers', function() {
    assert.equal(calculateNumber(-1, 3), 2);
    assert.equal(calculateNumber(1, -3.7), -2);
    assert.equal(calculateNumber(0, -3.7), -3);
    assert.equal(calculateNumber(-1.5, 0), -1);
    assert.equal(calculateNumber(0, 0), 0);
  });

  it('checks with Infinity', function() {
    assert.equal(calculateNumber(Infinity, 0), Infinity);
    assert.equal(calculateNumber(Infinity, Infinity), Infinity);
    assert.equal(calculateNumber(Infinity, 1000000000), Infinity);
    assert.equal(calculateNumber(Infinity, -Infinity), NaN);
    assert.equal(calculateNumber(-Infinity, -Infinity), -Infinity);
  });
});
