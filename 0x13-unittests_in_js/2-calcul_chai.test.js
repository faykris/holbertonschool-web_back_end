const expect = require("chai").expect;
const calculateNumber = require('./2-calcul_chai');

describe("calculateNumber", function() {
  it("checks SUM", function() {
    expect(calculateNumber('SUM', 1, 3) === 4).to.be.true;
    expect(calculateNumber('SUM', 1, 3.7) === 5).to.be.true;
    expect(calculateNumber('SUM', 1.2, 3.7) === 5).to.be.true;
    expect(calculateNumber('SUM', 1.4, 4.5) === 6).to.be.true;
  });

  it('checks SUBTRACT', function(){
    expect(calculateNumber('SUBTRACT', 1, 3) === -2).to.be.true;
    expect(calculateNumber('SUBTRACT', 1.4, 4.5) === -4).to.be.true;
    expect(calculateNumber('SUBTRACT', 4.2, 3) === 1).to.be.true;
    expect(calculateNumber('SUBTRACT', 3.1, 0) === 3).to.be.true;
  });

  it('checks DIVIDE', function(){
    expect(calculateNumber('DIVIDE', 4, 2) === 2).to.be.true;
    expect(calculateNumber('DIVIDE', 1.4, 4.5) === 0.2).to.be.true;
    expect(calculateNumber('DIVIDE', 0, 4.2) === 0).to.be.true;
    expect(calculateNumber('DIVIDE', 3.1, 0) === 'Error').to.be.true;
  });
});
