# https://leetcode.com/problems/find-the-pivot-integer/?envType=daily-question&envId=2024-03-13


class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n + 1):
            left = i * (i + 1) // 2
            right = n * (n + 1) // 2 - i * (i - 1) // 2
            if left == right:
                return i
        return -1
