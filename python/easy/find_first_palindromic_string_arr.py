# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/?envType=daily-question&envId=2024-02-13


# first attempt (<2min), pretty straightforward
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    break
                i += 1
                j -= 1
            if i >= j:
                return word
        return ""


# not much faster but looks better i guess
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
