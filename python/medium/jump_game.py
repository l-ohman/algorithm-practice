# https://leetcode.com/problems/jump-game/description/


# first attempt - beats 97% time 7% memory
def canJump(nums):
    # curr is idx we are on, next is idx we might jump to
    curr = next = 0
    # value of next + nums[next]
    while curr <= len(nums) - 1:
        if curr + nums[curr] >= len(nums) - 1:
            return True
        if nums[curr] == 0:
            return False

        jump = curr + nums[curr]
        next = jump
        for i in range(curr + 1, curr + nums[curr] + 1):
            if i + nums[i] >= len(nums) - 1:
                return True
            if i + nums[i] > jump:
                next = i
                jump = i + nums[i]
        curr = next
    return False


# second attempt, a bit cleaner - beats 99.93% time (!) and 7% space
def canJump(nums):
    max_dist = 0
    for i in range(len(nums)):
        if i <= max_dist:
            max_dist = max(max_dist, i + nums[i])
        if max_dist >= len(nums) - 1:
            return True
    return False
