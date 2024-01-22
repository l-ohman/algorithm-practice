# https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22


# first attempt, beats 91% time
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = missing = -1

        unique = set()
        for i in range(len(nums)):
            if nums[i] in unique:
                duplicate = nums[i]
            unique.add(nums[i])

        for i in range(1, len(nums) + 1):
            if i not in unique:
                missing = i
                break

        return [duplicate, missing]
