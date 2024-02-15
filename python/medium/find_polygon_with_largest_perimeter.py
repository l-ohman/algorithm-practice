# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/?envType=daily-question&envId=2024-02-15

# first attempt, beats 95% time and 91% space
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) >= 3:
            largest = nums[-1]
            perimeter = sum(nums)
            if largest < perimeter - largest:
                return perimeter
            nums = nums[:-1]
        return -1
