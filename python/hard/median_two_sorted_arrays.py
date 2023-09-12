# https: // leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        combined = []
        i = j = 0
        while i+j < length//2+1:
            # validate the index - also handles case where the list is empty
            if i > len(nums1) - 1:
                combined.append(nums2[j])
                j += 1
            elif j > len(nums2) - 1:
                combined.append(nums1[i])
                i += 1
            # add the smaller number to the 'combined' list
            elif nums1[i] >= nums2[j]:
                combined.append(nums2[j])
                j += 1
            elif nums2[j] > nums1[i]:
                combined.append(nums1[i])
                i += 1
        # return median based on the total length
        if len(combined) == 0:
            return 0
        elif length % 2 == 0:
            return (combined[-1] + combined[-2])/2
        else:
            return combined[-1]
