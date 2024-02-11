# https://leetcode.com/problems/cherry-pickup-ii/description/?envType=daily-question&envId=2024-02-11


# my first solution passed 50/59 test cases, but i had to ref user solutions to handle all cases
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        l1, l2 = len(grid), len(grid[0])
        # very unique (and strange) dp approach that seems to be required for this one.
        dp = [[[-1] * l2 for _ in range(l2)] for _ in range(l1)]
        dp[0][0][l2 - 1] = grid[0][0] + grid[0][l2 - 1]

        for i in range(1, l1):
            for j in range(l2):
                for k in range(j + 1, l2):
                    # looking at possible options for robots (diag_l, down, diag_r)
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if 0 <= j + x < l2 and 0 < k + y < l2:
                                # update dp array with new largest possible val
                                prev = dp[i - 1][j + x][k + y]
                                if prev == -1:
                                    continue
                                new_val = (
                                    prev + grid[i][j] + (grid[i][k] if j != k else 0)
                                )
                                dp[i][j][k] = max(dp[i][j][k], new_val)
        # largest sums at end of dp array
        sums = [max(row) for row in dp[l1 - 1]]
        res = max(sums)
        # if res is -1 (original val of all cells in dp array), return 0 instead
        return max(res, 0)
