// hard, dynamic programming
// https://www.hackerrank.com/challenges/lego-blocks/problem

// to prevent int overflow
const mod = 1000000007 // 10 ** 9 + 7;

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
  const sequence = tetranacci(m);
  for (let i = 0; i < sequence.length; i++) {
    sequence[i] = sequence[i] ** n % mod;
  }
  // above we get all possible combinations
  // need to filter out combinations that include 'breakable' walls
  let combinationsToRemove = 0;
  for (let i = 0; i <= Math.floor(sequence.length / 2); i++) {
    combinationsToRemove += sequence[i] * sequence[sequence.length - 2 - i];
    combinationsToRemove % mod;
  }
  return sequence[sequence.length - 1] - combinationsToRemove;
}

// console.log(legoBlocks(2, 2)); // 2 2 -> 3
// console.log(legoBlocks(3, 2)); // 3 2 -> 7
// console.log(legoBlocks(2, 3)); // 2 3 -> 9
console.log(legoBlocks(4, 4)); // 4 4 -> 3375
