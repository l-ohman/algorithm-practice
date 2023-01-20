// easy, string
// https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem

function gridChallenge(grid) {
  for (let i = 0; i < grid.length; i++) {
      grid[i] = grid[i].split("").sort().join("");
  }
  
  for (let j = 0; j < grid.length; j++) {
      for (let i = 0; i < grid.length - 1; i++) {
          if (grid[i][j] > grid[i + 1][j]) return "NO";
      }
  }
  return "YES";
}
