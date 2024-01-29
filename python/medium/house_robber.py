# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75


# yeah i think i need to practice dp more because what is this
class Solution:
    def rob(self, nums: List[int]) -> int:
        starts = {}
        for i in range(len(nums) - 1, -1, -1):
            if i + 1 not in starts:
                starts[i] = nums[i]
            elif i + 2 not in starts:
                starts[i] = max(nums[i], starts[i + 1])
            elif i + 3 not in starts:
                starts[i] = max(nums[i] + nums[i + 2], nums[i + 1])
            else:
                starts[i] = nums[i] + max(starts[i + 2], starts[i + 3])
        return max(starts.values())
