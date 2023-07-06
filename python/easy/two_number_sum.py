def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while (left < right):
        new_sum = array[left] + array[right]
        if (new_sum < targetSum):
            left += 1
        elif (new_sum > targetSum):
            right -= 1
        else:
            return [array[left], array[right]]
    return []

def twoNumberSum2(array, targetSum):
    set_array = set(array)
    for num in set_array:
        target = targetSum - num
        if target in set_array and target is not num:
            return [num, target]
    return []
