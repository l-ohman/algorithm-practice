# https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75


# first attempt ~2min, beats 92% time and 60% space
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for letter in s:
            if letter == "*":
                res.pop()
            else:
                res.append(letter)
        return "".join(res)
