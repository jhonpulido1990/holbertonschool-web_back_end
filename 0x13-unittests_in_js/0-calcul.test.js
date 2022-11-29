const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(1, 3,7), 4);
  });
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(1.2, 3,7), 4);
  });
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(1.5, 3,7), 5);
  });
})
