# https://leetcode.com/problems/two-sum/description/


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSums2(nums, target):
    seen = {}
    for i in range(len(nums)):
        seen[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in seen:
            j = seen[target - nums[i]]
            if i == j:
                continue
            return [i, j]
