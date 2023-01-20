// string, easy
// check if s is a palindrome after deleting at most 1 char from s
// return index of char removed or -1

function validPalindromeWithRemoval(s) {
  const isPalindrome = (str) => {
    for (let i = 0; i < Math.floor(str.length / 2); i++) {
      if (str[i] !== str[str.length - 1 - i]) return false;
    }
    return true;
  }
  if (isPalindrome(s)) return -1;

  for (let i = 0; i < Math.floor(s.length / 2); i++) {
    let j = s.length - 1 - i;

    if (s[i] !== s[j]) {
      if (isPalindrome(s.slice(0,i) + s.slice(i+1))) return i;
      else if (isPalindrome(s.slice(0,j) + s.slice(j+1))) return j;
      else return -1;
    }
  }

  return -1;
}
