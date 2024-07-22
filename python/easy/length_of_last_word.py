class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        for i, char in enumerate(s[::-1]):
            if char==" ":
                return i
        return len(s)
