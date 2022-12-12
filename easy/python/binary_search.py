# string / easy
# input: sorted array of integers, target integer
# output: index of target integer in input array (else -1)
# note: must use binary search algorithm.

# O(log(n)) time | O(log(n)) space
def binary_search(array, target):
    return compare_midpoint(array, target, 0, len(array)-1)

def compare_midpoint(array, target, left, right):
    midpoint = (right + left) // 2

    if array[midpoint] == target:
        return midpoint
    elif left >= right:
        # this could be (left > right) and placed at start of fn
        return -1
    elif array[midpoint] > target:
        return compare_midpoint(array, target, left, midpoint-1)
    elif array[midpoint] < target:
        return compare_midpoint(array, target, midpoint+1, right)

# note: optimized solution has same time complexity, but O(1) space
# it uses a while loop instead of recursion (while left <= right: ...)
