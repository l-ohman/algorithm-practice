// fibonacci sequence: 'n' is sum of (n-1) and (n-2) in the sequence.
// the first 2 numbers in the sequence are 0 and 1.
// write a function that takes 'n' and returns the nth number in the sequence.
// [0,1,1,2,3,5,8,13,21]

function getNthFib(n) {
  const sequence = [0, 1];

  while (n > 2) {
    let nextValue = sequence[0] + sequence[1];
    sequence[0] = sequence[1];
    sequence[1] = nextValue;
    n--;
  }

  return sequence[n - 1];
}

module.exports = getNthFib;
