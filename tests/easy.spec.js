const { expect } = require("chai");
const { twoNumberSum, isValidSubsequence } = require("../easy");

xdescribe("Two Number Sum", () => {
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
  it("Returns true when the subsequence is valid", () => {
    let array = [5, 1, 22, 25, 6, -1, 8, 10];
    let sequence = [1, 6, -1, 10];
    expect(isValidSubsequence(array, sequence)).to.equal(true);

    array = [5, 5, 5, 5, 5];
    sequence = [5, 5, 5];
    expect(isValidSubsequence(array, sequence)).to.equal(true);
  });

  it("Returns false when the subsequence is not valid", () => {
    let array = [10, 52, 8, 1, 37, 99, -10];
    let sequence = [52, 8, 99, 1];
    expect(isValidSubsequence(array, sequence)).to.equal(false);

    array = [1, 1, 10, 1];
    sequence = [1, 1, 1, 10];
    expect(isValidSubsequence(array, sequence)).to.equal(false);
  });

  it("Handles subsequences of zero or one integers", () => {
    const array = [10, 52, 8, 1, 37, 99, -10];
    expect(isValidSubsequence(array, [])).to.equal(true);
    expect(isValidSubsequence(array, [1])).to.equal(true);
  });

  it("Handles duplicate numbers in subsequence", () => {
    let array = [1, 4, 7, 9, 15];
    let sequence = [1, 7, 7, 15];
    expect(isValidSubsequence(array, sequence)).to.equal(false);
  });
});
