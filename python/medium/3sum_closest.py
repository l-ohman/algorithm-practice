# https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)==3: return sum(nums)
        nums.sort()
        diff=float("inf")
        for i in range(len(nums)-1):
            j, k = i+1, len(nums)-1
            while j<k:
                res = nums[i]+nums[j]+nums[k]
                if res==target:
                    return res
                if abs(diff)>abs(res-target):
                    diff = res-target

                if res>target:
                    k -= 1
                else:
                    j += 1
        return target+diff
      
