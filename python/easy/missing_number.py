# https://leetcode.com/problems/missing-number/?envType=daily-question&envId=2024-02-20


# first attempt - beats 87% time and 34% space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


# second attempt - beats 64% time and 99% space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        for i in range(len(nums) + 1):
            if len(nums) == 0 or i != heapq.heappop(nums):
                return i
