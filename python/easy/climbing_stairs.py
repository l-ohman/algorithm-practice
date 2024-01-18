# https://leetcode.com/problems/climbing-stairs/?envType=daily-question&envId=2024-01-18


# first attempt - beats 93% time, 34% memory
class Solution:
    def climbStairs(self, n: int) -> int:
        curr, ways = 2, [1, 2]
        while curr <= n:
            ways.append(ways[curr - 2] + ways[curr - 1])
            curr += 1
        return ways[n - 1]
