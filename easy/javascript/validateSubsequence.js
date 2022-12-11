// input: two non-empty arrays of integers
// output: boolean representing if the second array is a subsequence of the first array

// assumptions:
// a subsequence is a set of numbers that appear in the same order, but aren't necessarily adjacent.
// a single number in an array and the array itself are both valid subsequences.

function isValidSubsequence(array, sequence) {
  let currentIndex = 0;

  for (let i = 0; i < sequence.length; i++) {
    let match = false;
    for (let j = currentIndex; j < array.length; j++) {
      currentIndex = j;
      if (sequence[i] === array[j]) {
        match = true;
        currentIndex++;
        break;
      }
    }
    if (!match) return false;
  }
  return true;
}

module.exports = isValidSubsequence;

// optimal solution for this iterates through the array, and keeps an idx for sequence,
// rather than using nested for-loops
