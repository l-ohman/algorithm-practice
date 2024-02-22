# https://leetcode.com/problems/find-the-town-judge/?envType=daily-question&envId=2024-02-22


# first attempt -- beats 59% time and  67% space
# don't love this solution too much, but it's alright
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts_no_one = set([i for i in range(1, n + 1)])
        trusted_by = defaultdict(int)
        for truster, trustee in trust:
            if truster in trusts_no_one:
                trusts_no_one.remove(truster)
            trusted_by[trustee] += 1
        for p in trusts_no_one:
            if trusted_by[p] == n - 1:
                return p
        return -1


# second attempt -- beats 94% time and 86% space
# simply inverting the first set saved quite a lot of time on this
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts_someone = set()
        trusted_by = defaultdict(int)
        for truster, trustee in trust:
            trusts_someone.add(truster)
            trusted_by[trustee] += 1
        for p in range(1, n + 1):
            if p not in trusts_someone and trusted_by[p] == n - 1:
                return p
        return -1
