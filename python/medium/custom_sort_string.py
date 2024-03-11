# https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11


# first attempt -- beats 58% time and 26% space
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = ""
        for letter in order:
            if letter in count:
                for i in range(count[letter]):
                    res += letter
        order = set(order)
        for l in s:
            if l not in order:
                res += l
        return res


# second attempt -- beats 74% time and 16% space
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res, count = "", Counter(s)
        for l in order:
            if l in count:
                res += l * count[l]
                del count[l]
        for l in count.keys():
            res += l * count[l]
        return res
