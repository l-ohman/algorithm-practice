// search | medium

// [
//   [1, 2, 4, 10],
//   [3, 5, 8, 12],
//   [6, 7, 9, 15],
// ]

// brute force method: O(n*m)
function searchInSortedMatrixBruteForce(matrix, target) {
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (matrix[i][j] === target) return [i, j];
      else if (matrix[i][j] > target) break; // this line does not reduce big O, but i believe it reduces big omega
    }
  }
  return [-1, -1];
}

// start at TOP RIGHT square: O(n + m)
function searchInSortedMatrix(matrix, target) {
  let x = matrix[0].length - 1;
  let y = 0;

  while (y < matrix.length && x >= 0) {
    if (target === matrix[y][x]) return [y, x];

    if (target < matrix[y][x]) {
      x--;
    } else if (target > matrix[y][x]) {
      y++;
    }
  }

  return [-1, -1];
}

module.exports = searchInSortedMatrix;
