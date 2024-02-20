# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


# first attempt -- beats 15% time, and probably not a good solution for an interview anyway
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# second attempt -- beats 95% time and 95% space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] != needle[0]:
                continue
            valid = True
            for j in range(len(needle)):
                if i + j >= len(haystack) or haystack[i + j] != needle[j]:
                    valid = False
                    break
            if valid:
                return i
        return -1
