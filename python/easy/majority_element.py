# https://leetcode.com/problems/majority-element/


# 07-07-23
def majorityElement(nums):
    num_set = set(nums)
    for num in num_set:
        if nums.count(num) > len(nums) / 2:
            return num
    return -1


# 02-12-24
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, count = None, 0
        for num in nums:
            if count == 0:
                ans = num
            count += 1 if num == ans else -1
        return ans
