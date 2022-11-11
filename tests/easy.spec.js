const { expect } = require("chai");
const { binaryTreeLogger } = require("./utils");
const {
  twoNumberSum,
  isValidSubsequence,
  branchSums,
  BinaryTree,
} = require("../easy");

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

xdescribe("Validate Subsequence", () => {
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

describe("Branch Sums", () => {
  let binaryTree;

  before(() => {
    // constructing a basic BST to test
    const nodes = [];
    for (let i = 0; i < 10; i++) {
      nodes.push(new BinaryTree(i + 1));
    }
    // left side
    nodes[3].left = nodes[7];
    nodes[3].right = nodes[8];
    nodes[4].left = nodes[9];
    nodes[1].left = nodes[3];
    nodes[1].right = nodes[4];
    // right side
    nodes[2].left = nodes[5];
    nodes[2].right = nodes[6];
    // root node
    nodes[0].left = nodes[1];
    nodes[0].right = nodes[2];
    binaryTree = nodes[0];
  });

  it("Output contains the correct number of sums", () => {
    expect(branchSums(binaryTree).length).to.equal(5);
  });

  it("Returns the correct sums", () => {
    expect(branchSums(binaryTree)).to.eql([15, 16, 18, 10, 11]);
  });
});
