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
// alternatively, we could guess some square, and see if the puzzle can be solved with that guess.

// === assuming the 'comparePossibleValues' method does not work === //
// if we pass over the board and find nothing, we should:
// fill in the first empty space with one of its possible values (cell [i, j]);
// then pass over the board again and continue the loop.
// if at any point the puzzle becomes impossible to solve:
// return to the point at which we guessed [i, j] and enter it's next possible value.
// continue this process.

// util
const emptyBoard = new Array(9).fill(new Array(9).fill(0));

function solveSudoku(board, depth=0) {
  let numberOfPasses = 0; // just out of curiosity...

  let isSolved = false;
  let previousPassFailed = false;
  let isPossible = true;

  // storing board before guessing and values to iterate
  let boardCopy = JSON.parse(JSON.stringify(board));
  let guessIdx = 0;

  while (!isSolved) {
    // return an empty board if the puzzle is impossible
    // note: this is only used when guessing values
    if (isPossible === false && depth > 0) {
      return emptyBoard;
    }

    numberOfPasses++;
    if ((guessIdx > 80 || numberOfPasses > 15)) {
      // console.log(`Infinite loop detected, exiting...`);
      return board;
    }

    // using 'isRoot' so the recursive calls don't assume the starting puzzle is possible
    if (previousPassFailed && isPossible && depth < 3) {
      const emptySquares = countEmptySquares(board);
      for (let i = 0; i < emptySquares; i++) {
        boardCopy = guessNthEmptyCell(boardCopy, guessIdx, depth+1);

        if (countEmptySquares(boardCopy) === 0) {
          // if it was successful with the guess, return it
          console.log(`Final solution (using a guess): Passes: ${numberOfPasses} | guessIdx ${guessIdx} | depth: ${depth}`);
          console.log(boardCopy);
          return boardCopy;
        } else {
          // if the attempt to solve with a guess fails, increment guessIdx and continue
          guessIdx++;
          previousPassFailed = false;
        }
      }
    }

    [isSolved, previousPassFailed, isPossible] = iterateOverBoard(
      board,
      previousPassFailed,
      numberOfPasses
    );

    // console.log(
    //   `Depth: ${depth} | isSolved: ${isSolved} | isPossible: ${isPossible}`
    // );
  }

  console.log(`Final solution: Passes: ${numberOfPasses} | guessIdx ${guessIdx} | depth: ${depth}`);
  console.log(board);
  return board;
}

// iterates over board and updates necessary values
// returns boolean of whether or not puzzle is solved
function iterateOverBoard(board, previousPassFailed, pass) {
  let isSolved = true;
  let isPossible = true;
  let squaresAttempted = 0;
  let squaresSolved = 0;

  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] === 0) {
        let newValue = attemptSolveSquare(board, [i, j]);
        board[i][j] = newValue;
        squaresAttempted++;

        if (newValue) {
          squaresSolved++;
        } else {
          isSolved = false;
        }
      }
    }
  }

  // if we fail to make progress in 2 passes, then puzzle must be impossible with this method
  if (previousPassFailed && squaresSolved === 0) {
    isPossible = false;
  } else if (squaresSolved === 0) {
    previousPassFailed = true;
  } else if (squaresSolved > 0) {
    previousPassFailed = false;
  }

  // console.log(
  //   `Pass ${pass} | Squares Attempted: ${squaresAttempted} | Squares Solved: ${squaresSolved} (${(
  //     (squaresSolved / squaresAttempted) *
  //     100
  //   ).toPrecision(4)}%)`
  // );
  return [isSolved, previousPassFailed, isPossible];
}

function attemptSolveSquare(board, coord) {
  const possibleValues = getPossibleValues(board, coord);
  if (possibleValues.length === 1) return possibleValues[0];
  else return 0;
}

// [y, x] or [i, j]
function getPossibleValues(board, coord) {
  const usedValues = [];

  for (let i = 0; i < 9; i++) {
    // add items to row (if it is no 0 or an array)
    if (board[coord[0]][i]) {
      usedValues.push(board[coord[0]][i]);
    }
    // add items to column (if it is no 0 or an array)
    if (board[i][coord[1]]) {
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

  const usedValuesSet = new Set(usedValues);
  let possibleValues = [];
  for (let i = 1; i <= 9; i++) {
    if (!usedValuesSet.has(i)) possibleValues.push(i);
  }
  return possibleValues;
}

function guessNthEmptyCell(board, n, depth) {
  let zeroesToSkip = n;
  let boardCopy;

  // find the nth cell with '0' and replace it with its mth possible value
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] !== 0) continue;

      if (zeroesToSkip === 0) {
        // console.log(`\nGuessing cell ${n}`);
        zeroesToSkip--;
        // get the possible values for this square and attempt to solve with each of them
        const possibleValues = getPossibleValues(board, [i, j]);
        // console.log(
        //   `${possibleValues.length} possible values detected for [${i}, ${j}]`
        // );

        for (let k = 0; k < possibleValues.length; k++) {
          boardCopy = JSON.parse(JSON.stringify(board));
          boardCopy[i][j] = possibleValues[k];

          boardCopy = solveSudoku(boardCopy, depth);
          if (countEmptySquares(boardCopy) === 0) {
            console.log(`Success`);
            console.log(boardCopy, "\n");
            return boardCopy;
          } else {
            // console.log(
            //   `Attempt to solve with [${i}, ${j}] as ${possibleValues[k]} failed`
            // );
          }
        }
      }
      zeroesToSkip--;
    }
  }

  return board;
}

function countEmptySquares(board) {
  // console.log(board);
  let n = 0;
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] === 0) n++;
    }
  }
  return n;
}

module.exports = solveSudoku;
