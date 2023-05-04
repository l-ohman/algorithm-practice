# https://leetcode.com/problems/ugly-number-ii/
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

def nthUglyNumber(n):
    ugly = [1]
    a2 = a3 = a5 = 0
    while len(ugly) < n:
        next_num = min(ugly[a2] * 2, ugly[a3] * 3, ugly[a5] * 5)
        ugly.append(next_num)
        if next_num == ugly[a2] * 2: a2 += 1
        if next_num == ugly[a3] * 3: a3 += 1
        if next_num == ugly[a5] * 5: a5 += 1
    return ugly[n-1]
