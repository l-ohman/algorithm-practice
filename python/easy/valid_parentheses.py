# https://leetcode.com/problems/valid-parentheses/


# beats 63% time and 88% space
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}": "{", ")": "(", "]": "["}
        stack = []
        for char in s:
            if char in hashmap:
                if len(stack) == 0 or hashmap[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
