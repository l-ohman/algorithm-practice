# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

# terrible solution ... but it works
def removeDuplicates(nums):
    write = 1
    val = nums[0]
    seen_twice = False
    for i in range(1, len(nums)):
        print(val, nums[i], seen_twice)
        if nums[i] == val:
            if not seen_twice:
                seen_twice = True
                nums[write] = nums[i]
                write += 1
        else:
            seen_twice = False
            val = nums[i]
            nums[write] = nums[i]
            write += 1
    return write
