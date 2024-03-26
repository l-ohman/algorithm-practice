# https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-03-26


# didn't really understand this one without referencing a solution. link to original here:
# https://leetcode.com/problems/first-missing-positive/solutions/4925619/hard-easy-positioning-elements-at-correct-index
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
