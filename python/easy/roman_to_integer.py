# https://leetcode.com/problems/roman-to-integer/


# 83% time and 58% space
class Solution:
    def romanToInt(self, s: str) -> int:
        key = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        prev = res = 0
        for char in s[::-1]:
            val = key[char]
            res += val if prev <= val else -val
            prev = val
        return res
