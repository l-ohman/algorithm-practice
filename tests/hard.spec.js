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

  xit("The output is correctly structured", () => {
    // some might say this test is unnecessary... and while i would agree with them, i already wrote it; so i'm keeping it anyway.
    expect(Array.isArray(outputBoard)).to.equal(true, "Output is not an array");
    expect(outputBoard.length).to.equal(9, "Invalid row count");
    expect(outputBoard[6].length).to.equal(9, "Invalid column count"); // column selected arbitrarily
  });

  it("Each row has 9 unique values", () => {
    for (let i = 0; i < 9; i++) {
      const row = new Set(outputBoard[i]);
      expect(row.size).to.equal(
        9,
        `Row ${i + 1} has less than 9 unique values`
      );
    }
  });

  it("Each column has 9 unique values", () => {
    for (let i = 0; i < 9; i++) {
      const column = new Set(outputBoard.map((row) => row[i]));
      expect(column.size).to.equal(
        9,
        `Column ${i + 1} has less than 9 unique values`
      );
    }
  });

  it("Each subsquare (3x3) has 9 unique values", () => {
    // in this loop, 'currentGrid' keeps track of which 3x3 we are in at any point, as such:
    // const loop = [
    //   0, 0, 0, 1, 1, 1, 2, 2, 2,
    //   0, 0, 0, 1, 1, 1, 2, 2, 2,
    //   0, 0, 0, 1, 1, 1, 2, 2, 2,
    //   3, 3, 3, 4, 4, 4, 5, 5, 5,
    //   3, 3, 3, 4, 4, 4, 5, 5, 5,
    //   3, 3, 3, 4, 4, 4, 5, 5, 5,
    //   6, 6, 6, 7, 7, 7, 8, 8, 8,
    //   6, 6, 6, 7, 7, 7, 8, 8, 8,
    //   6, 6, 6, 7, 7, 7, 8, 8, 8
    // ];
    const grids = [];
    for (let i = 0; i < 9; i++) {
      grids.push([]);
    }

    // this creates a new matrix, where each 'row' contains the values of a 3x3
    let currentGrid = 0;
    for (let i = 0; i < 9; i++) {
      if (i && i % 3 === 0) currentGrid += 3;

      for (let j = 0; j < 9; j++) {
        if (j && j % 3 === 0) currentGrid++;
        if (!j && i) currentGrid -= 2;
        // console.log(grids[0]);
        grids[currentGrid].push(outputBoard[i][j]);
      }
    }

    for (let i = 0; i < 9; i++) {
      const grid = new Set(grids[i]);
      expect(grid.size).to.equal(9);
    }
  });
});
