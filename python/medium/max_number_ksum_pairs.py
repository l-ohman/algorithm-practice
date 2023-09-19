# https://leetcode.com/problems/max-number-of-k-sum-pairs

class Solution:
    def maxOperations1(self, nums: List[int], k: int) -> int:
        nums.sort()
        pairs, i, j = 0, 0, len(nums)-1
        while i < j:
            val = nums[i] + nums[j]
            if val == k:
                i += 1
                j -= 1
                pairs += 1
            elif val > k:
                j -= 1
            elif val < k:
                i += 1
        return pairs

    def maxOperations2(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        pairs = 0
        for n in nums:
            if hashmap[n] > 0:
                hashmap[n] -= 1
                pairs += 1
            else:
                hashmap[k-n] += 1
        return pairs
