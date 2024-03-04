# https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-03-04


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens) - 1
        highest = score = 0
        while i <= j:
            a, b = tokens[i], tokens[j]
            if power >= a:
                power -= a
                score += 1
                i += 1
            elif score >= 1:
                power += b
                score -= 1
                j -= 1
            else:
                break
            highest = max(highest, score)
        return highest
