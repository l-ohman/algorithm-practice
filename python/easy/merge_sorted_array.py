# https://leetcode.com/problems/merge-sorted-array/

def merge(nums1, m, nums2, n) -> None:
    i, j, write = m-1, n-1, m+n-1
    while (j >= 0):
        if (i >= 0 and nums1[i] >= nums2[j]):
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1
