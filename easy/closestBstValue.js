// input: BST and target number
// output: integer value of the node closest to the target number

// assumptions:
// there will only be one closest value.

function selectCloser(val1, val2, target) {
  const dist1 = Math.abs(target - val1);
  const dist2 = Math.abs(target - val2);
  return dist1 > dist2 ? val2 : val1;
}

function closestBstValue(tree, target) {
  if (tree.value > target && tree.left) {
    const compValue = closestBstValue(tree.left, target);
    return selectCloser(compValue, tree.value, target);
  } else if (tree.value < target && tree.right) {
    const compValue = closestBstValue(tree.right, target);
    return selectCloser(compValue, tree.value, target);
  } else {
    return tree.value;
  }
}

module.exports = closestBstValue;
