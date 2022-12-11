# string / medium
# input: a string
# output: the longest palindrome substring
# assumptions: there will be only 1 longest palindromic substring.

# this solution is O(n^3), because it calls "is_palindrome" which is O(n^2)
# there is an O(n) solution using "Manacher's algorithm":
# https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
def is_palindrome(string):
    for i in range(len(string)):
        if i >= len(string) - 1 - i:
            break
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

def longest_palindromic_substring(string):
    current_longest = string[0]
    longest = 1

    for i in range(len(string) - 1):
        for j in range(len(string) - 1, i, -1):
            if string[i] == string[j] and len(string[i:j+1]) > longest and is_palindrome(string[i:j+1]):
                current_longest = string[i:j+1]
                longest = len(current_longest)

    return current_longest
