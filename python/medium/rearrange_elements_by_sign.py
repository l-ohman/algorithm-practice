# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14


# first solution (5min) -- pretty stupid, would never write code like this in a real app...
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = neg = 0
        res = []
        while len(res) < len(nums):
            l = len(res)
            # if it is even length, we want a positive number (else a negative)
            if l % 2 == 0:
                while l == len(res):
                    if nums[pos] > 0:
                        res.append(nums[pos])
                    pos += 1
            else:
                while l == len(res):
                    if nums[neg] < 0:
                        res.append(nums[neg])
                    neg += 1
        return res


# second solution (1min) --i thought this would be faster at the expense of memory, but it's somehow worse for space AND time complexity
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            arr = pos if num > 0 else neg
            arr.append(num)

        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res


# third solution (1min) -- it finally hit me! beats 98% time and 63% space
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        i, j = 0, 1
        for num in nums:
            if num > 0:
                res[i] = num
                i += 2
            else:
                res[j] = num
                j += 2
        return res
