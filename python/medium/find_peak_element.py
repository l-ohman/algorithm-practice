# https://leetcode.com/problems/find-peak-element
# straightforward problem , but difficult time complexity requirement


# first attempt - beats 81% time, 79% space
def findPeakElement(nums):
    if len(nums) == 1 or nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums) - 1

    idx = 1
    while idx < len(nums) - 1:
        if nums[idx] > nums[idx + 1]:
            return idx
        elif nums[idx] == nums[idx + 1]:
            idx += 2
        elif nums[idx] < nums[idx + 1]:
            idx += 1
    return idx
