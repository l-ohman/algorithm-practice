# https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=daily-question&envId=2024-03-27


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        i = 0
        count, curr = 0, 1
        for j in range(len(nums)):
            curr *= nums[j]
            while curr >= k:
                curr /= nums[i]
                i += 1
            count += j - i + 1
        return count
