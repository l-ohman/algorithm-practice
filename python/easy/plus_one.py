class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        for i in range(l-1, -1, -1):
            if digits[i]!=9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
      
