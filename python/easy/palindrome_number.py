# https://leetcode.com/problems/palindrome-number/
# easy, string

def isPalindromeBasic(x):
    x = str(x)
    j = len(x)
    for i in range(j // 2):
        if x[i] != x[j - 1 - i]:
            return False
    return True

# Follow-up challenge: Could you solve it without converting the integer to a string?
# medium, math(?)

def isPalindrome(x):
    if x < 0:
        return False
    
    y = x
    reverse = 0
    while y > 0:
        reverse = reverse * 10 + y % 10
        y = y // 10
    return x == reverse
