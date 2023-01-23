// hard, dynamic programming
// https://www.hackerrank.com/challenges/lego-blocks/problem

// works for smaller inputs but not for large ones (~n=100)

// to prevent int overflow
const mod = 1000000007; // 10 ** 9 + 7;

// tetranacci sequence: http://oeis.org/A000078
function tetranacci(m) {
  const sequence = [1, 2, 4, 8];
  if (m <= 4) return sequence.slice(0, m);

  for (let i = 4; i < m; i++) {
    let nextInSequence = 0;
    for (let j = 1; j <= 4; j++) {
      nextInSequence += sequence[i - j];
    }
    sequence.push(nextInSequence % mod);
  }
  return sequence;
}

function legoBlocks(n, m) {
  const allWalls = tetranacci(m);
  for (let i = 0; i < allWalls.length; i++) {
    allWalls[i] = allWalls[i] ** n % mod;
  }
  // above we get all possible combinations
  // need to filter out combinations that include 'breakable' walls

  const solidWalls = [1];
  for (let i = 1; i < allWalls.length; i++) {
    for (let j = 0; j < i; j++) {
      // removing duplicates from each L/R division
      solidWalls[i] -= solidWalls[j] * allWalls[i - 1 - j];
    }
    solidWalls[i] % mod;
  }
  return solidWalls[solidWalls.length - 1];
}

// console.log(legoBlocks(2, 2)); // 2 2 -> 3
// console.log(legoBlocks(3, 2)); // 3 2 -> 7
// console.log(legoBlocks(2, 3)); // 2 3 -> 9
console.log(legoBlocks(4, 4)); // 4 4 -> 3375
