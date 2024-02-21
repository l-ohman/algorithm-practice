# https://leetcode.com/problems/bitwise-and-of-numbers-range/?envType=daily-question&envId=2024-02-21
# cant say i enjoy bitwise problems...


# beats 73% time and 56% space
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right = right & right - 1
        return left & right
