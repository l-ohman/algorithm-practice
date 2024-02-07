# https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=daily-question&envId=2024-02-07


# first attempt, beats 65% time and 68% space
class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.defaultdict(int)
        for l in s:
            count[l] += 1

        vals = [(k, v) for k, v in count.items()]
        vals.sort(key=lambda x: -x[1])

        res = ""
        for letter, count in vals:
            for _ in range(count):
                res += letter
        return res


# 87% time, 93% space
class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s).most_common()
        res = ""
        for letter, count in c:
            res += letter * count
        return res
