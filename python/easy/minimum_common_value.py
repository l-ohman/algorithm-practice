# https://leetcode.com/problems/minimum-common-value/?envType=daily-question&envId=2024-03-09


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            a, b = nums1[i], nums2[j]
            if a == b:
                return a
            elif a > b:
                j += 1
            else:
                i += 1
        return -1
