# https://leetcode.com/problems/furthest-building-you-can-reach/?envType=daily-question&envId=2024-02-17


# first attempt -- recursive brute force(ish), passes some tests but is too slow for larger cases (pretty sloppy code, too)
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # trying recursion for first attempt
        if len(heights)==1:
            return 0
        
        if heights[1] <= heights[0]:
            return self.furthestBuilding(heights[1:], bricks, ladders) + 1
        # try both options
        else:
            # ladders
            use_ladders = self.furthestBuilding(heights[1:], bricks, ladders-1) if ladders>0 else -1
            # bricks
            bricks -= heights[1] - heights[0]
            use_bricks = self.furthestBuilding(heights[1:], bricks, ladders) if bricks>=0 else -1
            
            # can't progress further from this building
            if use_ladders==-1 and use_bricks==-1:
                return 0
            return max(use_ladders, use_bricks) + 1


# trick is to use a ladder for each jump, and only go back and change the method later if it could get you further
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # heap keeps which jumps are using ladders
        heap = []
        heapq.heapify(heap)

        # start by using a ladder for each jump
        for i in range(len(heights)-1):
            gap = heights[i+1] - heights[i]
            if gap<=0:
                continue
            
            if len(heap)<ladders:
                heapq.heappush(heap, gap)
            else:
                if not heap or gap<=heap[0]:
                    bricks -= gap
                else:
                    bricks -= heapq.heappop(heap)
                    heapq.heappush(heap, gap)
                if bricks<0:
                    return i
        return len(heights)-1
  
