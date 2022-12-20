// search | easy

// O(n) time | O(1) space
function findThreeLargestNumbers(array) {
  const largestNumbers = new Array(3).fill(-Infinity);

  for (let i = 0; i < array.length; i++) {
    if (array[i] <= largestNumbers[0]) continue;

    // find the correct index for array[i]
    let placeAtIndex = 0;
    for (let j = 1; j < largestNumbers.length; j++) {
      if (array[i] > largestNumbers[j]) placeAtIndex++;
      else break;
    }

    // remove the previous smallest int and insert array[i]
    largestNumbers.shift();
    largestNumbers.splice(placeAtIndex, 0, array[i]);
  }

  return largestNumbers;
}

module.exports = findThreeLargestNumbers;
