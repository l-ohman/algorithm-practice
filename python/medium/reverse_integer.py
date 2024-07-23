# https://leetcode.com/problems/reverse-integer/

# somewhat odd solution, but works as a first attempt
class Solution:
    def reverse(self, x: int) -> int:
        limit = 2**31
        is_negative = x<0
        val = str(abs(x))
        res = 0
        for i, digit in enumerate(val):
            add = int(digit)*(10**i)
            if res + add >= limit:
                return 0
            res += add
        return res * (-1 if is_negative else 1)

# attempt 2 -- beats 87% time, 78% memory
class Solution:
    def reverse(self, x: int) -> int:
        limit, negative = str(2**31), x<0
        val = str(abs(x))[::-1]
        
        if len(val)>len(limit):
            return 0
        elif len(val)==len(limit):
            for i in range(len(val)):
                if int(val[i])<int(limit[i]):
                    break
                elif int(val[i])>int(limit[i]):
                    return 0
        return int(val)*(-1 if negative else 1)
        
