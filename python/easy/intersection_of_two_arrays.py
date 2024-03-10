# https://leetcode.com/problems/intersection-of-two-arrays/?envType=daily-question&envId=2024-03-10

# first attempt, beats 93% time and 91% space
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))
