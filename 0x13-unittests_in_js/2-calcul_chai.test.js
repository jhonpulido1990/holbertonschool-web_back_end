const expect = require('chai').expect
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  it('Checks equality', function(){
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('Checks equality', function(){
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(4);
  });
  it('Checks equality', function(){
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it('Checks equality', function(){
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
});
