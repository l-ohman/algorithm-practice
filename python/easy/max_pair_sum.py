# https://leetcode.com/problems/max-pair-sum-in-an-array/
from collections import defaultdict


def maxSum(nums):
    def maxDigit(num):
        if num < 10:
            return num
        return max(int(d) for d in str(num))

    res = -1
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] <= res:
                continue
            if maxDigit(nums[i]) == maxDigit(nums[j]):
                res = nums[i] + nums[j]
    return res


def maxSum2(nums):
    digit_map = defaultdict(lambda: [-1, -1])
    # o(n) * log(m)
    for num in nums:
        digit = num if num < 10 else max(int(d) for d in str(num))
        # we want digit map to contain the 2 highest vals for this max_digit
        # placing manually so we don't have to do any sorting
        if digit_map[digit][1] >= num:
            continue
        elif digit_map[digit][0] >= num:
            digit_map[digit][1] = num
        else:
            digit_map[digit][1] = digit_map[digit][0]
            digit_map[digit][0] = num

    # o(1) - there is a max of 9 keys in this hash
    res = -1
    for pair in digit_map.values():
        a, b = pair[0], pair[1]
        if b != -1:
            res = max(res, a + b)
    return res


def maxSum3(nums):
    res = -1
    # key as max_digit of a num, val as the highest seen
    digit_map = {}
    for num in nums:
        digit = max(str(num))
        if digit in digit_map:
            res = max(res, num + digit_map[digit])
            digit_map[digit] = max(num, digit_map[digit])
        else:
            digit_map[digit] = num
    return res
