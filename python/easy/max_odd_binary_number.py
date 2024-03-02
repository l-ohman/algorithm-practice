# https://leetcode.com/problems/maximum-odd-binary-number/description/?envType=daily-question&envId=2024-03-01


# beats 93% time and 96% space
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = ["1"] * len(s)
        i = -2
        for char in s:
            if char == "1":
                continue
            res[i] = "0"
            i -= 1
        return "".join(res)
