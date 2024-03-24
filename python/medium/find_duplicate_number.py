# https://leetcode.com/problems/find-the-duplicate-number/description/?envType=daily-question&envId=2024-03-24


# first attempt--beats 68% time, 21% space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)
