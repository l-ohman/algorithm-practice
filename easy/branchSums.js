// input: a binary tree root node
// output: an array containing the sum of integers in every branch

// assumptions:
// branch sum - sum of all values in a single binary tree branch
// ordered from leftmost sum to rightmost sum

class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function branchSums(root) {
  if (!root.left && !root.right) return [root.value];

  const sums = [];
  if (root.left) {
    const newSums = branchSums(root.left);
    for (let i = 0; i < newSums.length; i++) {
      sums.push(root.value + newSums[i]);
    }
  }
  if (root.right) {
    const newSums = branchSums(root.right);
    for (let i = 0; i < newSums.length; i++) {
      sums.push(root.value + newSums[i]);
    }
  }
  return(sums);
}

module.exports = { branchSums, BinaryTree };
