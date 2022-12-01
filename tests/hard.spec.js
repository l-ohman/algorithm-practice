const { expect } = require("chai");
const { solveSudoku } = require("../hard");

describe("Solve Sudoku", () => {
  let inputBoard;
  let outputBoard;
  const correctOutput = [
    [7, 8, 5, 4, 3, 9, 1, 2, 6],
    [6, 1, 2, 8, 7, 5, 3, 4, 9],
    [4, 9, 3, 6, 2, 1, 5, 7, 8],
    [8, 5, 7, 9, 4, 3, 2, 6, 1],
    [2, 6, 1, 7, 5, 8, 9, 3, 4],
    [9, 3, 4, 1, 6, 2, 7, 8, 5],
    [5, 7, 8, 3, 9, 4, 6, 1, 2],
    [1, 2, 6, 5, 8, 7, 4, 9, 3],
    [3, 4, 9, 2, 1, 6, 8, 5, 7],
  ];

  beforeEach(() => {
    inputBoard = [
      [7, 8, 0, 4, 0, 0, 1, 2, 0],
      [6, 0, 0, 0, 7, 5, 0, 0, 9],
      [0, 0, 0, 6, 0, 1, 0, 7, 8],
      [0, 0, 7, 0, 4, 0, 2, 6, 0],
      [0, 0, 1, 0, 5, 0, 9, 3, 0],
      [9, 0, 4, 0, 6, 0, 0, 0, 5],
      [0, 7, 0, 3, 0, 0, 0, 1, 2],
      [1, 2, 0, 0, 0, 7, 4, 0, 0],
      [0, 4, 9, 2, 0, 6, 0, 0, 7],
    ];
    outputBoard = solveSudoku(inputBoard);
  });

  it("The output is correctly structured", () => {
    // some might say this test is unnecessary... and while i would agree with them, i already wrote it.
    expect(Array.isArray(outputBoard)).to.equal(true, "Output is not an array");
    expect(outputBoard.length).to.equal(9, "Invalid row count");
    expect(outputBoard[6].length).to.equal(9, "Invalid column count"); // column selected arbitrarily
  });

  it("Each row has 9 unique values", () => {
    for (let i = 0; i < 9; i++) {
      const row = new Set(outputBoard[i]);
      expect(row.size).to.equal(9, `Row ${i+1} has less than 9 unique values`);
    }
  });

  it("Each column has 9 unique values", () => {
    for (let i = 0; i < 9; i++) {
      const column = new Set(outputBoard.map(row => row[i]))
      expect(column.size).to.equal(9, `Column ${i+1} has less than 9 unique values`);
    }
  });

  xit("Each subsquare (3x3) has 9 unique values", () => {
    for (let i = 0; i < 9; i++) {
      // not sure how to (efficiently) test this yet.
      // may start working on problem first and return to this.
    }
  });
});
