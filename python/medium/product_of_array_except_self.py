# medium | array
# https://leetcode.com/problems/product-of-array-except-self/solutions/

# 12-25-22
def product_except_self(nums: list) -> list:
    output = [1] * len(nums)
    
    # don't need to cache product iterating forwards
    for i in range(1, len(nums)):
        output[i] = output[i-1] * nums[i-1]
    
    product = nums[len(nums)-1]
    for i in range(len(nums) - 2, -1, -1):
        output[i] *= product
        product *= nums[i]
    return output

if __name__ == "__main__":
    print(product_except_self([1,2,3,4])) # [24, 12, 8, 6]
    print(product_except_self([-1,-1,0,-3,-3])) # [0, 0, 9, 0, 0]


# 03-15-24
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left = right = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

