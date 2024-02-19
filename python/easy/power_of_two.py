# easy, math
# https://leetcode.com/problems/power-of-two/


def isPowerOfTwo(n):
    if n <= 0:
        return False
    while n > 0.5:
        n = n / 2
    while n < 0.5:
        n = n * 2
    return n == 0.5


def isPowerOfTwoBitwise(n):
    return n > 0 and n & (n - 1) == 0


# "&" operator in python is "bitwise-and" operator
# if n is a power of two, it will be a binary value such as "1000 0000"
# and n-1 would be "0111 1111"
# ex: n&(n-1) == 1000 0000 & (0111 1111)
# these have 0 digits in common, so the output would be 0


# 02/19/24
# the binary stuff is cool, but can't say i'd ever code like that in a real application
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        t = 1
        while n > t:
            t *= 2
        return n == t
