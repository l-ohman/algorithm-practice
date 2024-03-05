# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-05


# First attempt--beats 88% time and 93% space
class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            char = s[i]
            while i < len(s) - 1 and s[i] == char:
                i += 1
            while j > 0 and s[j] == char:
                j -= 1
        return 1 if i == j else max(0, j - i + 1)
