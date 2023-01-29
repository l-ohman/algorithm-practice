# medium
# https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem

def isBalanced(s):
    closing = {"}": "{", "]": "[", ")": "("}
    stack = []
    for char in s:
        if char not in closing:
            stack.append(char)
        elif len(stack) == 0 or stack.pop() != closing[char]:
            return "NO"
    return "YES" if len(stack) == 0 else "NO"
