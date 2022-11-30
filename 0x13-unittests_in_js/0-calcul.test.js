const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(1.4, 4.5), 6);
  });
  it('Checks equality', function() {
    assert.strictEqual(calculateNumber(0.5, 3.7), 5);
  });
});
