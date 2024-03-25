# https://leetcode.com/problems/find-all-duplicates-in-an-array/?envType=daily-question&envId=2024-03-25


# first attempt--beats 82% time and 34% space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s, res = set(), []
        for n in nums:
            if n in s:
                res.append(n)
            s.add(n)
        return res


# meeting space constraint with...weird solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        # marking "seen" as negative for constant space constraint
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                res.append(n)
            nums[n - 1] *= -1
        return res
