// easy
// https://www.hackerrank.com/challenges/plus-minus/problem

function plusMinus(arr) {
  const counts = [0, 0, 0]; // positive, negative, zero

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) counts[0] += 1;
    else if (arr[i] < 0) counts[1] += 1;
    else if (arr[i] === 0) counts[2] += 1;
  }

  for (let i in counts) {
    const ratio = counts[i] / arr.length;
    console.log(ratio.toPrecision(7));
  }
}
