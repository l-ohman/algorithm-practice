# hashmap | medium
# https://leetcode.com/problems/top-k-frequent-elements/submissions/865467905/

# top 10% time complexity ... ? not sure how this solution is efficient
def top_k_frequent(nums: list, k: int) -> list:
    freq_count = {} # key = value:int, val = count:int
    
    for i in range(len(nums)):
        if nums[i] not in freq_count:
            freq_count[nums[i]] = 0
        freq_count[nums[i]] += 1
    
    grouped_by_count = {} # key = count: int, val = values:list[int]
    for val, count in freq_count.items():
        if count not in grouped_by_count:
            grouped_by_count[count] = []
        grouped_by_count[count].append(val)
    grouped_by_count = sorted(grouped_by_count.items())
    print(grouped_by_count)
    
    output = []
    count = len(grouped_by_count) - 1
    m = k
    while m > 0:
        output += grouped_by_count[count][1]
        count -= 1
        m -= len(grouped_by_count[count][1])
    
    return output[:k]

if __name__ == "__main__":
    print(top_k_frequent([1,1,1,2,2,3], 2))
    # [1, 2]
