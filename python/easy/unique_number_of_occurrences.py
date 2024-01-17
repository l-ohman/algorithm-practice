# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=daily-question&envId=2024-01-17

from collections import defaultdict


# first solution -- 2 minutes or so, but only beats 25%
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = defaultdict(int)
        for num in arr:
            hashmap[num] += 1
        nums_list = list(hashmap.values())
        nums_set = set(nums_list)
        return len(nums_list) == len(nums_set)


# second solution -- faster than 97%, and only replaced the defaultdict
# i guess defaultdict is much slower than i originally thought...
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for num in arr:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        nums_list = list(counter.values())
        nums_set = set(nums_list)
        return len(nums_list) == len(nums_set)
