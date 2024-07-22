# i mean......technically this works
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while True:
            square = i*i
            if square==x:
                return i
            elif square>x:
                return i-1
            i += 1

# real solution
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1: return 1
        i, j = 2, x//2
        while i <= j:
            midpoint = (i+j)//2
            square = midpoint * midpoint

            if square==x:
                return midpoint
            elif square>x:
                j = midpoint-1
            elif square<x:
                i = midpoint+1
        return j
  
