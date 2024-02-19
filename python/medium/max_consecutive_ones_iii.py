# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75
# guess i need to pracitce sliding window problems more


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # use sliding window, and only allow its size to increase
        # i, j as left, right edges
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                i += 1
                if nums[i - 1] == 0:
                    k += 1
        return len(nums) - i
