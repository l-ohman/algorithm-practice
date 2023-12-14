# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/


def countHillValley(nums):
    res = 0
    for i in range(1, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = nums[i - 1]
        elif (nums[i] > nums[i + 1] and nums[i] > nums[i - 1]) or (
            nums[i] < nums[i + 1] and nums[i] < nums[i - 1]
        ):
            res += 1
    return res


def countHillValley2(nums):
    j = res = 0
    for i in range(1, len(nums) - 1):
        if (nums[i] > nums[i + 1] and nums[i] > nums[j]) or (
            nums[i] < nums[i + 1] and nums[i] < nums[j]
        ):
            res += 1
            j = i
    return res
