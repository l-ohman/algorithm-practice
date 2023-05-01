# dynamic programming / math (can use combinatorics to solve)
# https://leetcode.com/problems/unique-paths/

# dynamic programming solution:
# paths to square[i][j] = paths to square[i-1][j] + square[i][j-1]
def uniquePaths(m, n):
    if m == 1 or n == 1:
        return 1
    row = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            row[j] += row[j-1]
    return row[n-1]
