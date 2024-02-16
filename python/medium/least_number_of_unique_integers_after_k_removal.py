# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/?envType=daily-question&envId=2024-02-16


# first attempt, beats 58% time and 94% space
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # first attempt, will be quite slow but should work
        # count all values
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        # then remove the ones with lower counts
        counts = list(count.values())
        heapq.heapify(counts)
        while len(counts)>0 and k>0:
            x = heapq.heappop(counts)
            k -= x
            if k<0:
                return len(counts)+1
        return len(counts)


# cleaned up a bit but pretty much the same solution--yet somehow it's faster? beats 69% time and 85% space
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1

        count = list(count.values())
        heapq.heapify(count)
        while k>0 and len(count)>0:
            k -= heapq.heappop(count)
        
        return len(count)+1 if k<0 else len(count)


# turns out the heap isn't as necessary as i thought--beats 94% time and 71% space
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)
        counts = sorted(c.values())

        for i in range(len(counts)):
            if k >= counts[i]:
                k -= counts[i]
            else:
                return len(counts)-i
        return 0
