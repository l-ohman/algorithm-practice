# https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=daily-question&envId=2024-03-02


# first attempt -- not pretty, but beats 60% time and 85% space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # identify point where list goes from negative to positive
        neg = pos = 0
        while pos < len(nums) and nums[pos] <= 0:
            pos += 1
        neg = pos - 1

        res = []
        while len(res) < len(nums):
            # first check list boundaries
            if pos >= len(nums):
                res.append(nums[neg] ** 2)
                neg -= 1
            elif neg < 0:
                res.append(nums[pos] ** 2)
                pos += 1
            # if both indicies are in limits, compare abs vals
            else:
                a, b = nums[pos], nums[neg]
                if abs(a) < abs(b):
                    res.append(a**2)
                    pos += 1
                else:
                    res.append(b**2)
                    neg -= 1
        return res


# attempt 2 -- thought this iteration would be faster, but it only beats 34% time...?
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        i, j, k = 0, len(nums) - 1, len(res) - 1
        while k >= 0:
            a, b = nums[i], nums[j]
            if abs(a) > abs(b):
                res[k] = a**2
                i += 1
            else:
                res[k] = b**2
                j -= 1
            k -= 1
        return res


# looked at the "faster" solutions, they are actually slower--
# but it may have been when the test cases were different (since it's an old problem).
# i think my solutions are fine for now, just gonna move on.
