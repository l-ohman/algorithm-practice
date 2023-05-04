# https://leetcode.com/problems/ugly-number/
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

def isUgly(n):
    if n <= 0:
        return False
    for i in [2, 3, 5]:
        while n % i == 0: n /= i
    return n == 1
