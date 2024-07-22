# beats 55% time and 89% memory
# not very well written, but need to de-rust a bit

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        num, highest = float("inf"), 0
        for i,n in enumerate(divisors):
            score = 0
            for a in nums:
                if a%n==0:
                    score += 1
            if score>=highest:
                num = min(n,num) if score==highest else n
                highest = score
        return num 
