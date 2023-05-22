// https://leetcode.com/problems/count-numbers-with-unique-digits/

function countNumbersWithUniqueDigits(n) {
  if (n === 0) return 1;
  if (n === 1) return 10;
  let mult = 9;
  let number = n;
  while (number > 1) {
    mult *= 10 - (number - 1);
    number -= 1;
  }
  return mult + countNumbersWithUniqueDigits(n - 1);
}
