# https://leetcode.com/problems/longest-common-prefix/


# first attempt - beats 55% time and 95% space
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != char:
                    return res
            res += char
        return res


# second attempt - beats 87% time and 71% space
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i, res = 0, ""
        while i < len(strs[0]):
            char = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return res
            res += char
            i += 1
        return res


# third attempt - beats 95% time and 95% space (how is zip this fast?)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for letters in zip(*strs):
            char = letters[0]
            for l in letters:
                if l != char:
                    return res
            res += letters[0]
        return res
