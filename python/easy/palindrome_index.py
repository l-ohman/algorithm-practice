# string, easy
# check if s is a palindrome after deleting at most 1 char from s
# return index of char removed or -1

def isPalindrome(s):
    for i in range(len(s) // 2):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True


def palindromeIndex(s):
    for i in range(len(s) // 2):
        if (s[i] != s[len(s)-1-i]):
            if isPalindrome(s[i:len(s)-1-i]):
                return len(s)-1-i
            if isPalindrome(s[i+1:len(s)-i]):
                return i
    return -1
