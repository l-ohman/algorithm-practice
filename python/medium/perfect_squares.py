# https://leetcode.com/problems/perfect-squares/
# Given an integer n, return the least number of perfect square numbers that sum to n.

def numSquares(n):
    dp = [i for i in range(n+1)]
    for i in range(n+1):
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i-j*j] + 1)
            j += 1
    return dp[-1]
