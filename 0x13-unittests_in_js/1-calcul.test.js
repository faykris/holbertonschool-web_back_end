const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  it('checks SUM', function() {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
    assert.equal(calculateNumber('SUM', 1, 3.7), 5);
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
  });

  it('checks SUBTRACT', function(){
    assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.equal(calculateNumber('SUBTRACT', 4.2, 3), 1);
    assert.equal(calculateNumber('SUBTRACT', 3.1, 0), 3);
  });

  it('checks DIVIDE', function(){
    assert.equal(calculateNumber('DIVIDE', 4, 2), 2);
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.equal(calculateNumber('DIVIDE', 0, 4.2), 0);
    assert.equal(calculateNumber('DIVIDE', 3.1, 0), 'Error');
  });
});
