# https://leetcode.com/problems/majority-element/

def majorityElement(nums):
    num_set = set(nums)
    for num in num_set:
        if nums.count(num) > len(nums) / 2:
            return num
    return -1
