# https://leetcode.com/problems/perfect-squares/
# Given an integer n, return the least number of perfect square numbers that sum to n.


# 05/03/23 -- 4677ms runtime
def numSquares(n):
    dp = [i for i in range(n + 1)]
    for i in range(n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[-1]


# https://leetcode.com/problems/perfect-squares/description/?envType=daily-question&envId=2024-02-08
# 02/08/24 -- 2729ms runtime
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(len(dp)):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]
