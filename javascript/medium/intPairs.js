// medium, array
// https://www.hackerrank.com/challenges/pairs/problem
// 11 min

function pairs(k, arr) {
  arr.sort((a, b) => a - b);
  let pairCount = 0;

  for (let i = 0; i < arr.length - 1; i++) {
    const valueToPair = arr[i] + k;

    for (let j = i; j < arr.length; j++) {
      if (arr[j] === valueToPair) pairCount += 1;
      if (arr[j] >= valueToPair) break;
    }
  }

  return pairCount;
}
