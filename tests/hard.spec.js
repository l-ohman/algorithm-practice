const { expect } = require("chai");
const { solveSudoku } = require("../hard/javascript");

xdescribe("Solve Sudoku", () => {
  // board1: relatively easy puzzle
  const inputBoard = [
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
  // board2: extremely difficult puzzle
  const inputBoard2 = [
    [0, 2, 0, 0, 9, 0, 1, 0, 0],
    [0, 0, 7, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 6, 0],
    [0, 0, 1, 9, 0, 4, 0, 0, 0],
    [0, 0, 0, 6, 0, 5, 0, 0, 7],
    [8, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 8, 5],
    [4, 9, 0, 0, 3, 0, 0, 0, 0]
  ];
  
  // console.log("\nAttempting to solve easy puzzle...")
  // const outputBoard = solveSudoku(inputBoard);
  // console.log("\nAttempting to solve hard puzzle...")
  // const outputBoard2 = solveSudoku(inputBoard2);
  
  // const correctOutput = [
  //   [7, 8, 5, 4, 3, 9, 1, 2, 6],
  //   [6, 1, 2, 8, 7, 5, 3, 4, 9],
  //   [4, 9, 3, 6, 2, 1, 5, 7, 8],
  //   [8, 5, 7, 9, 4, 3, 2, 6, 1],
  //   [2, 6, 1, 7, 5, 8, 9, 3, 4],
  //   [9, 3, 4, 1, 6, 2, 7, 8, 5],
  //   [5, 7, 8, 3, 9, 4, 6, 1, 2],
  //   [1, 2, 6, 5, 8, 7, 4, 9, 3],
  //   [3, 4, 9, 2, 1, 6, 8, 5, 7],
  // ];

  // console.log(outputBoard);
  // logging boards for debugging purposes

  it("The output is correctly structured", () => {
    // some might say this test is unnecessary... and while i would agree with them, i already wrote it; so i'm keeping it anyway.
    expect(Array.isArray(outputBoard)).to.equal(true, "Output is not an array");
    expect(outputBoard.length).to.equal(9, "Invalid row count");
    expect(outputBoard[6].length).to.equal(9, "Invalid column count"); // column selected arbitrarily
  });

  it("Each row has 9 unique integers", () => {
    // easy puzzle
    for (let i = 0; i < 9; i++) {
      const row = new Set(outputBoard[i]);
      expect(row.size).to.equal(
        9,
        `Row i=${i} has less than 9 unique integers (Easy Puzzle)`
      );
      row.forEach(itm => expect(typeof itm).to.equal("number"));
    }

    // hard puzzle
    for (let i = 0; i < 9; i++) {
      const row = new Set(outputBoard2[i]);
      expect(row.size).to.equal(
        9,
        `Row i=${i} has less than 9 unique integers (Hard Puzzle)`
      );
      row.forEach(itm => expect(typeof itm).to.equal("number"));
    }
  });

  it("Each column has 9 unique integers", () => {
    // easy puzzle
    for (let i = 0; i < 9; i++) {
      const column = new Set(outputBoard.map((row) => row[i]));
      expect(column.size).to.equal(
        9,
        `Column i=${i} has less than 9 unique integers (Easy Puzzle)`
      );
      column.forEach(itm => expect(typeof itm).to.equal("number"));
    }

    // hard puzzle
    for (let i = 0; i < 9; i++) {
      const column = new Set(outputBoard2.map((row) => row[i]));
      expect(column.size).to.equal(
        9,
        `Column i=${i} has less than 9 unique integers (Hard Puzzle)`
      );
      column.forEach(itm => expect(typeof itm).to.equal("number"));
    }
  });

  it("Each subsquare (3x3) has 9 unique integers", () => {
    // easy puzzle
    let grids = [];
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
        grids[currentGrid].push(outputBoard[i][j]);
      }
    }

    for (let i = 0; i < 9; i++) {
      const grid = new Set(grids[i]);
      expect(grid.size).to.equal(9, `Grid i=${i} has less than 9 unique integers (Easy Puzzle)`);
      grid.forEach(itm => expect(typeof itm).to.equal("number"));
    }

    // hard puzzle
    grids = [];
    for (let i = 0; i < 9; i++) {
      grids.push([]);
    }

    currentGrid = 0;
    for (let i = 0; i < 9; i++) {
      if (i && i % 3 === 0) currentGrid += 3;

      for (let j = 0; j < 9; j++) {
        if (j && j % 3 === 0) currentGrid++;
        if (!j && i) currentGrid -= 2;
        grids[currentGrid].push(outputBoard2[i][j]);
      }
    }

    for (let i = 0; i < 9; i++) {
      const grid = new Set(grids[i]);
      expect(grid.size).to.equal(9, `Grid i=${i} has less than 9 unique integers (Hard Puzzle)`);
      grid.forEach(itm => expect(typeof itm).to.equal("number"));
    }
  });
});
