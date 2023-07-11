# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# 3min

def twoSum(numbers, target):
    i = 0; j = len(numbers) - 1
    while i <= j:
        new_sum = numbers[i] + numbers[j]
        if new_sum > target: j -= 1
        elif new_sum < target: i += 1
        else: return [i+1, j+1]

numbers = [2,7,11,15]; target = 9
print(twoSum(numbers, target) == [1,2])
