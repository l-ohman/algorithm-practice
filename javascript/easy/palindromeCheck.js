// input: non-empty string
// output: boolean representing if the input is a palindrome

function palindromeCheck(string) {
  for (let i = 0; i < string.length / 2; i++) {
    if (string[i] !== string[string.length - 1 - i]) return false;
  }
  return true;
}

module.exports = palindromeCheck;
