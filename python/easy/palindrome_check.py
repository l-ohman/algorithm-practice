# string / easy
# input: non-empty string
# output: boolean representing if string is a palindrome

# O(n) time
def is_palindrome(string):
    for i in range(len(string)):
        if i >= len(string) - 1 - i:
            break
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True
