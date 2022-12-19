// input is an array of 9 arrays, each with 9 elements
// the elements can be 0-9, where 1-9 are valid numbers and 0 represents an empty square
// output is valid sudoku board (unique rows, columns, and 3x3s)

// -- initial thought process -- //
// iterate over the board, and replace every value that only has one option
// repeat this process until there are no 0s left on the board

// -- taking a break -- //
// it seems my idea above works for easier puzzles, but not for more difficult ones:
// some puzzles have 0 squares that can be determined based only on row/column/grid,
// so we must find a way to compare possible values of related squares to determine some values.

// -- an idea about how to reapproach -- //
// iterate through a row, and replace each 0 with an array of possible values;
// if the row does not yet have a number 'n', but a single square has 'n' as a possible value,
// then fill that square in with the number 'n'.

function solveSudoku(board) {
  let isSolved = false;
  let numberOfPasses = 0; // just out of curiosity...
  while (!isSolved) {
    numberOfPasses++;
    isSolved = iterateOverBoard(board, numberOfPasses);
  }
  return board;
}

// iterates over board and updates necessary values
// returns boolean of whether or not puzzle is solved
function iterateOverBoard(board, pass = 0) {
  let isSolved = true;

  // just out of curiosity...
  let squaresAttempted = 0;
  let squaresSolved = 0;

  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] === 0 || Array.isArray(board[i][j])) {
        let newValue = attemptSolveSquare(board, [i, j]);
        board[i][j] = newValue;
        squaresAttempted++;

        if (newValue && !Array.isArray(newValue)) {
          squaresSolved++;
        } else if (pass > 1 && Array.isArray(newValue)) { 
          // console.log(`possible values at [${i}, ${j}]`);
          // console.log(newValue);
          newValue = comparingPossibleValues(board, [i, j]);
          if (newValue) {
            board[i][j] = newValue;
            squaresSolved++;
          } else {
            // here - set the coordinate to an array of possible values
            isSolved = false;
          }
        } else {
          isSolved = false;
        }
      }
    }
  }

  // tmp error handling to prevent infinite loops
  if (squaresSolved === 0) {
    console.log(
      `Error: Unable to solve any squares on Pass ${pass}\nSquares Attempted: ${squaresAttempted}`
    );
    // console.log(board);
    return true;
  } else {
    if (pass)
      console.log(
        `Pass ${pass} | Squares Attempted: ${squaresAttempted} | Squares Solved: ${squaresSolved} (${(
          (squaresSolved / squaresAttempted) *
          100
        ).toPrecision(4)}%)`
      );
    return isSolved;
  }
}

// coord: [y, x] or [i, j]
function attemptSolveSquare(board, coord = [0, 0]) {
  let usedValues = [];

  for (let i = 0; i < 9; i++) {
    // add items to row (if it is no 0 or an array)
    if (board[coord[0]][i] && !Array.isArray(board[coord[0]][i])) {
      usedValues.push(board[coord[0]][i]);
    }
    // add items to column (if it is no 0 or an array)
    if (board[i][coord[1]] && !Array.isArray(board[i][coord[1]])) {
      usedValues.push(board[i][coord[1]]);
    }
  }

  // (y, x)
  // 0 1 2 | (0,0) (0,1) (0,2)
  // 3 4 5 | (1,0) (1,1) (1,2)
  // 6 7 8 | (2,0) (2,1) (2,2)
  const x = Math.floor(coord[1] / 3);
  const y = Math.floor(coord[0] / 3);
  for (let i = x * 3; i < x * 3 + 3; i++) {
    for (let j = y * 3; j < y * 3 + 3; j++) {
      if (board[j][i] && !Array.isArray(board[j][i])) {
        usedValues.push(board[j][i]);
      }
    }
  }

  usedValues = new Set(usedValues);
  if (usedValues.size < 8) {
    let possibleValues = [];
    for (let i = 1; i <= 9; i++) {
      if (usedValues.has(i)) possibleValues.push(i);
    }
    return possibleValues;
  }

  for (let i = 1; i <= 9; i++) {
    if (!usedValues.has(i)) return i;
  }
}

// coord: [y, x] or [i, j]
function comparingPossibleValues(board, coord) {
  // comparing possible values within the row
  let possibleValues = {};
  for (let i = 0; i < 9; i++) {
    if (Array.isArray(board[coord[0]][i])) {
      // iterate through the array of possible values stored at this coord
      for (let j = 0; j < board[coord[0]][i].length; j++) {
        if (!possibleValues[board[coord[0]][i][j]]) {
          possibleValues[board[coord[0]][i][j]] = 1;
        } else {
          possibleValues[board[coord[0]][i][j]] += 1;
        }
      }
    }
  }
  for (int in possibleValues) {
    if (possibleValues[int] === 1) {
      return Number(int);
    }
  }

  // comparing possible values within the column
  possibleValues = {};
  for (let i = 0; i < 9; i++) {
    if (Array.isArray(board[i][coord[1]])) {
      // iterate through the array of possible values stored at this coord
      for (let j = 0; j < board[i][coord[1]].length; j++) {
        if (!possibleValues[board[i][coord[1]][j]]) {
          possibleValues[board[i][coord[1]][j]] = 1;
        } else {
          possibleValues[board[i][coord[1]][j]] += 1;
        }
      }
    }
  }
  console.log(possibleValues);
  // for (int in possibleValues) {
  //   if (possibleValues[int] === 1) {
  //     return Number(int);
  //   }
  // }
  // grid

  // return [] || "n";
}

module.exports = solveSudoku;
