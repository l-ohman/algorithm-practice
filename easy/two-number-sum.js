// input: array of distinct integers, and an integer which is target sum
// output: if any numbers in array add up to target sum, return array of those two numbers. otherwise return an empty array.

// assumptions:
// there will be at most one pair of numbers summing up to the target sum.
// you cannot add a single integer to itself to reach the sum.
// the order of the numbers in the output does not matter.
// the problem does NOT state if 0 can be in the input array.
// the problem does NOT state if negative numbers are permitted (the tests reveal that they are).

// optimal space&time complexity:
// O(n) time | O(n) space

// my solution: O(n^2) time | O(1) space
function twoNumberSum(array, targetSum) {
    for (let i = 0; i < array.length - 1; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] + array[j] === targetSum) {
                return [array[i], array[j]];
            }
        }
    }
    return [];
}

// the optimal solution (O(n)) uses an object to store each 'potentialMatch'
