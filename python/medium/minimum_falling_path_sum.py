# https://leetcode.com/problems/minimum-falling-path-sum/?envType=daily-question&envId=2024-01-19


# first attempt, beats 92% time and 67% space
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        l = len(matrix)
        for i in range(1, l):
            for j in range(l):
                above = matrix[i - 1][j]
                diag_left = diag_right = float("inf")
                if j > 0:
                    diag_left = matrix[i - 1][j - 1]
                if j < l - 1:
                    diag_right = matrix[i - 1][j + 1]
                smallest = min(above, diag_left, diag_right)
                matrix[i][j] += smallest

        return min(matrix[l - 1])
