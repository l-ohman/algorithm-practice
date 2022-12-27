# array | medium
# https://leetcode.com/problems/3sum/

# this method works (and is more readable) but time complexity is insufficient
def three_sum_first(nums: list) -> list:
    valid_triplets = {}
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            # only one possible value for k
            k = 0 - (nums[i] + nums[j])
            
            if k in nums[j+1:]:
                # sorting and using map to ensure combinations are unique
                valid_nums = sorted([nums[i], nums[j], k])
                valid_triplets[str(valid_nums)] = valid_nums
                    
    return list(valid_triplets.values())

# optimized solution using 'sliding window' pointers (achieved by sorting the input array)
# ref: https://leetcode.com/problems/3sum/solutions/7373/share-my-simple-java-solution/
def three_sum(nums: list) -> list:
    nums = sorted(nums)
    valid_triplets = []
    
    i = 0
    while (i < len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        
        # 'pointers beyond i to check possible values above i
        while(j < k):
            sum = nums[i] + nums[j] + nums[k]
            
            if sum == 0:
                valid_triplets.append([nums[i], nums[j], nums[k]])
            if sum <= 0:
                # if sum is too small, move j up to next value
                while j < k:
                    j += 1
                    if nums[j-1] != nums[j]:
                        break
                    
            if sum >= 0:
                # if sum is too large, move k down
                while j < k:
                    k -= 1
                    if nums[k+1] != nums[k]:
                        break
        
        # increment up to next i value (skipping duplicates) and continue
        while (i < len(nums) - 2):
            i += 1
            if (nums[i-1] != nums[i]):
                break
    return valid_triplets


if __name__ == "__main__":
    print(three_sum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(three_sum([0,1,1]))          # []
    print(three_sum([0,0,0]))          # [[0,0,0]]
