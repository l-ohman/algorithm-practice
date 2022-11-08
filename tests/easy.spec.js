const { expect } = require("chai");
const { twoNumberSum } = require("../easy");

describe("Two Number Sum", () => {
  it("Returns an array of two numbers when they add up to the target sum", () => {
    const array = [1, 4, -9, 8, 15, 3, -1, 6];
    const targetSum = 10;
    const output = twoNumberSum(array, targetSum);

    expect(output.length).to.equal(2);
    expect(output).to.include(4);
    expect(output).to.include(6);
  });

  it("Return an empty array if no pair adds up to the target sum", () => {
    const array = [10, 14, -7, 4, -1, 7];
    const targetSum = 8;
    expect(twoNumberSum(array, targetSum)).to.eql([]);
  });

  it("Handles input arrays of one number", () => {
    const array = [10];
    const targetSum = 10;
    expect(twoNumberSum(array, targetSum)).to.eql([]);
  });
});

describe("Validate Subsequence", () => {

});
