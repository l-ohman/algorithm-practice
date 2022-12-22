// input is an array of 9 arrays, each with 9 elements
// the elements can be 0-9, where 1-9 are valid numbers and 0 represents an empty square
// output is valid sudoku board (unique rows, columns, and 3x3s)

// O(1) time and space (!)

// returns solved sudoku board
function solveSudoku(board) {
  isBoardSolvable(board, 0, 0);
  return board;
}

// returns a bool: if the input board is solvable
function isBoardSolvable(board, x, y) {
  // handles current coordinates
  if (x === 9) {
    x = 0;
    y++;
    if (y === 9) return true;
  }

  if (board[y][x] === 0) {
    return tryValuesAtCoord(board, x, y);
  } else {
    return isBoardSolvable(board, x + 1, y);
  }
}

// returns an array: possible values for a coordinate
function getPossibleValues(board, x, y) {
  const usedValues = [];

  for (let i = 0; i < 9; i++) {
    // add values from row
    if (board[y][i]) usedValues.push(board[y][i]);
    // add values from column
    if (board[i][x]) usedValues.push(board[i][x]);
  }

  // add values from subgrid
  const xGrid = Math.floor(x / 3);
  const yGrid = Math.floor(y / 3);
  for (let i = xGrid * 3; i < xGrid * 3 + 3; i++) {
    for (let j = yGrid * 3; j < yGrid * 3 + 3; j++) {
      if (board[j][i]) usedValues.push(board[j][i]);
    }
  }

  // remove duplicates and return all possible values in an array
  const usedValuesSet = new Set(usedValues);
  let possibleValues = [];
  for (let i = 1; i <= 9; i++) {
    if (!usedValuesSet.has(i)) possibleValues.push(i);
  }
  return possibleValues;
}

// returns a bool: is 'board' solvable filling cells with any ints from possibleValues
function tryValuesAtCoord(board, x, y) {
  const possibleValues = getPossibleValues(board, x, y);
  for (let i = 0; i < possibleValues.length; i++) {
    board[y][x] = possibleValues[i];
    if (isBoardSolvable(board, x + 1, y)) return true;
  }
  // reset value to 0 if none of the possibleValues are valid
  board[y][x] = 0;
  return false;
}

module.exports = solveSudoku;
