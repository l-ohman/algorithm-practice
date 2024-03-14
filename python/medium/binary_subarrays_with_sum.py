# https://leetcode.com/problems/binary-subarrays-with-sum/?envType=daily-question&envId=2024-03-14


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sums = {0: 1}
        curr = res = 0
        for num in nums:
            curr += num
            if curr - goal in sums:
                res += sums[curr - goal]
            if curr not in sums:
                sums[curr] = 0
            sums[curr] += 1
        return res
