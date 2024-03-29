# https://leetcode.com/problems/decompress-run-length-encoded-list/submissions/1155623272/


# beats 95% time, 5% space
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            res.extend([val] * freq)
        return res
