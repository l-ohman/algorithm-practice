# hashmap | medium
# https://leetcode.com/problems/longest-consecutive-sequence/

# top 5% time, bottom 10% space
def longest_consecutive_sequence(nums: list) -> int:
    if len(nums) == 0: return 0
    # remove duplicates and sort, then iterate thru and keep track of largest num
    sequence_map = {}
    for num in nums:
        sequence_map[num] = True
    sequence_map = sorted(sequence_map.keys())
    
    longest = current = 1
    for i in range(1, len(sequence_map)):
        if sequence_map[i] - sequence_map[i-1] == 1:
            current += 1
        else:
            current = 1
        
        if current > longest:
            longest = current
    return longest

if __name__ == "__main__":
    print(longest_consecutive_sequence([100,4,200,1,3,2])) # 4
    print(longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1])) # 9
    print(longest_consecutive_sequence([])) # 0
    print(longest_consecutive_sequence([5])) # 1
