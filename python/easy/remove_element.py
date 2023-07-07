# https://leetcode.com/problems/remove-element/

def removeElement(nums, val) -> int:
    count = len(nums)
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = float("inf")
            count -= 1
    nums.sort()
    return count

def removeElement2(nums, val):
    i = 0
    for num in nums:
        if num != val:
            nums[i] = num
            i += 1
    return i
