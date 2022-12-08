// inputs: an array of integers and nested arrays
// in each array, add up the values, and multiply the sum by the num representing how deeply it is nested
// ex: [x, [y, z]] == x + 2 * (y + z)
// output: a single integer

function productSum(array, idx = 1) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    if (Array.isArray(array[i])) {
      sum += productSum(array[i], idx + 1);
    } else {
      sum += array[i];
    }
  }
  return sum * idx;
}

module.exports = productSum;
