# https://leetcode.com/problems/remove-duplicates-from-sorted-array

def removeDuplicates(nums):
    write = 1
    val = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != val:
            nums[write] = val = nums[i]
            write += 1
    return write
