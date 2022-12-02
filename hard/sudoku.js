// input is an array of 9 arrays, each with 9 elements
// the elements can be 0-9, where 1-9 are valid numbers and 0 represents an empty square
// output is valid sudoku board (unique rows, columns, and 3x3s)

// [0, 1, 2, 3, 4, 5, 6, 7, 8]
// [0, 1, 2, 3, 4, 5, 6, 7, 8]
// [0, 1, 2, 3, 4, 5, 6, 7, 8]
// [0, 1, 2, 3, 4, 5, 6, 7, 8]
// [0, 1, 2, 3, 4, 5, 6, 7, 8]
// [0, 1, 2, 3, 4, 5, 6, 7, 8]
// [0, 1, 2, 3, 4, 5, 6, 7, 8]
// [0, 1, 2, 3, 4, 5, 6, 7, 8]
// [0, 1, 2, 3, 4, 5, 6, 7, 8]

function solveSudoku(board) {
  // rows: unique nums in each row array
  // columns: unique nums in array of row[i] where i >= 0 && i < 9
  // 3x3s: (i+1)%3 === 0

  return [];
}

module.exports = solveSudoku;
