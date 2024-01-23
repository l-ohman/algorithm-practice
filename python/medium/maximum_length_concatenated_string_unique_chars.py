# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/?envType=daily-question&envId=2024-01-23


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for s in arr:
            chars = set(s)
            if len(chars) < len(s):
                continue

            combinations = [(chars | x) for x in dp if not (chars & x)]
            dp.extend(combinations)

        max_len = 0
        for x in dp:
            if len(x) > max_len:
                max_len = len(x)
        return max_len
