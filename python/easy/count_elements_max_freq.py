# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2024-03-08


# beats 92% time and 100% memory
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        amount = max_freq = 0
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > max_freq:
                amount = 1
                max_freq = hashmap[num]
            elif hashmap[num] == max_freq:
                amount += 1
        return amount * max_freq
