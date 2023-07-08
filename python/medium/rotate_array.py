# https://leetcode.com/problems/rotate-array

# Most straightforward solution, with O(n) space
def rotate(nums, k):
    copy = list(nums)
    k = k % len(nums)
    for i in range(len(nums)):
        nums[i] = copy[i-k]

# Attempting a solution with O(1) space
def rotate(nums, k):
    k = k % len(nums)

    def rotateOne(nums):
        last_val = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            nums[i] = nums[i-1]
        nums[0] = last_val
    for i in range(k):
        rotateOne(nums)

# Optimal solution - reverses entire array, then reverses parts before/after index k
def rotate(nums, k):
    length = len(nums)
    k = k % length
    nums.reverse()
    for i in range(k//2):
        nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
    for i in range(k, (length+k)//2):
        nums[i], nums[length-i+k-1] = nums[length-i+k-1], nums[i]


# Testcases
nums1 = [1, 2, 3, 4, 5, 6, 7]
rotate(nums1, 3)
nums2 = [-1, -100, 3, 99]
rotate(nums2, 2)
def test(x): return "Pass" if x else "Fail"

print(f"Test 1: {test(nums1 == [5, 6, 7, 1, 2, 3, 4])}")
print(f"Test 2: {test(nums2 == [3, 99, -1, -100])}")
