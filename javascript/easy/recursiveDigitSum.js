// easy, recursion (string)
// https://www.hackerrank.com/challenges/recursive-digit-sum/problem

function superDigit(n, k = 1) {
  const nString = n.toString();
  if (nString.length === 1) return n;

  let sum = 0;
  for (let i = 0; i < nString.length; i++) {
    sum += Number(nString[i]);
  }
  return superDigit(sum * k);
}
