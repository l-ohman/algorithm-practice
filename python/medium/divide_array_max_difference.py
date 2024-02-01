# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2024-02-01


# first attempt, beats 93% time and  92% memory
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2, 3):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if abs(c - a) > k:
                return []
            res.append([a, b, c])
        return res
