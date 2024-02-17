# https://leetcode.com/problems/make-array-empty/


# first attempt - able to pass 500/515 tests pretty easily, but too slow for the large scale cases
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        min_heap = nums[:]
        heapq.heapify(min_heap)
        res = 0
        while len(nums)>0:
            smallest = heapq.heappop(min_heap)
            idx = nums.index(smallest)
            nums = nums[idx+1:] + nums[:idx]
            res += idx + 1
        return res        


# second attempt -- passed large scale tests, but failed the smaller but more complex cases
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        # sort by number, but keep idx with it when sorting
        s_nums = sorted(enumerate(nums), key=lambda x: x[1])
        res = 0
        
        last_seen = 0
        for i in range(len(s_nums)):
            removed = i
            idx = s_nums[i][0]
            num = s_nums[i][1]

            if idx<last_seen:
                amount = (len(nums) - last_seen + idx) - removed
            else:
                amount = idx - last_seen
            last_seen = idx
            
            res += amount + 1
        return res        


# the key was to track of loop subtracts individually instead of as just "removed" variable
# can't help but feel there's something better here--i'll have to come back to this in a few months
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        # sort by number, but keep idx with it when sorting
        s_nums = sorted(enumerate(nums), key=lambda x: x[1])
        res = 0
        
        curr_loop_sub = loop_sub = 0
        last_seen = 0
        for i in range(len(s_nums)):
            idx = s_nums[i][0]
            num = s_nums[i][1]

            if idx<last_seen:
                amount = (len(nums) - last_seen + idx)
                amount -= loop_sub
                loop_sub += curr_loop_sub
                curr_loop_sub = 1
            else:
                amount = idx - last_seen
                curr_loop_sub += 1
            last_seen = idx
            res += amount
        
        res -= last_seen - curr_loop_sub
        return res        
