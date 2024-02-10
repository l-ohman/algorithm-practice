# https://leetcode.com/problems/palindromic-substrings/description/?envType=daily-question&envId=2024-02-10


# had to reference a user solution, but was finally able to grasp this one. very challenging but interesting problem
class Solution:
    def countSubstrings(self, s: str) -> int:
        # will look at each index and pair of indicies as a central pivot point
        # and count based on the length of the largest palindrome centered at a specific point
        palindrome_count = 0

        for i in range(len(s)):
            # using each index and pair of indicies as pivot points
            # this handles both even/odd length palindromes
            for a, b in [(i, i), (i, i + 1)]:
                # expand outwards as far as possible while it's still a palindrome
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    a -= 1
                    b += 1
                # for each palindrome, we are counting all sub-palindromes at the same time
                # ex: if we are counting for "racecar", we also include: "aceca", "cec", and "c"
                # so we use (len+1)//2 to get sub-palindrome count
                palindrome_count += (b - a) // 2

        return palindrome_count


# solution referenced:
# https://leetcode.com/problems/palindromic-substrings/solutions/392119/solution-in-python-3-beats-94-six-lines-with-detaiiled-explanation/?envType=daily-question&envId=2024-02-10
