# https://leetcode.com/problems/integer-break/
# math explanation: https://leetcode.com/problems/integer-break/solutions/80689/a-simple-explanation-of-the-math-part-and-a-o-n-solution/comments/85242


def integerBreak(n: int):
    if n == 2: return 1
    if n == 3: return 2
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    return product * n
