# https://leetcode.com/problems/jump-game-ii/description/


# bfs
def jump(nums):
    count = furthest = i = 0
    for j in range(len(nums) - 1):
        furthest = max(furthest, j + nums[j])
        if furthest >= len(nums) - 1:
            return count + 1
        if j == i:
            count += 1
            i = furthest
    return count
