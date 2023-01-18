// reverse rows/cols until a quadrant has max possible sum
// medium, matrix

// only need to find max of each char
// a b b a
// d c c d
// d c c d
// a b b a
// rotation (reversal) to place values similar to rubix cube

function maxMatrixQuadrant(matrix) {
  const n = matrix.length;
  let sum = 0;
  for (let i = 0; i < n / 2; i++) {
    for (let j = 0; j < n / 2; j++) {
      const maxValue = Math.max(
        matrix[i][j],
        matrix[n - i - 1][j],
        matrix[i][n - j - 1],
        matrix[n - i - 1][n - j - 1]
      );
      sum += maxValue;
    }
  }
  return sum;
}

module.exports = maxMatrixQuadrant;
