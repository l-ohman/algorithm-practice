# https://leetcode.com/problems/4sum/description/
# very slow, but didn't have to check any hints/solutions !

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        i, j = 0, len(nums)-1
        while i<j-2:
            quads = []
            for k in range(i, j-2):
                r = self.helper(nums[k:j+1], target)
                quads += r
            for l in range(j, i+2, -1):
                r = self.helper(nums[i:l+1], target)
                quads += r

            for q in quads:
                if q in res:
                    continue
                res.append(q)

            i += 1
            j -= 1

        return res
        
    def helper(self, nums, target):
        res = []
        i, j = 0, len(nums)-1
        k, l = i+1, j-1
        while l>k:
            curr = [nums[i], nums[k], nums[l], nums[j]]
            s = sum(curr)
            if s == target and curr not in res:
                res.append(curr)
            if s >= target:
                l -= 1
            if s <= target:
                k += 1
        return res
