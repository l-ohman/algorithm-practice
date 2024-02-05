# https://leetcode.com/problems/sequential-digits/?envType=daily-question&envId=2024-02-02


# not a great solution, but i found this one very challenging--will look at into better solutions
class Solution:
    def sequentialDigits(self, low: int, high: int):
        res = []
        curr = low
        while curr >= low and curr < high:
            next_val = [c for c in str(curr)]
            if 10 - int(next_val[0]) < len(next_val):
                curr += 10 ** (len(next_val) - 1)
                continue

            for i in range(1, len(next_val)):
                next_val[i] = str(int(next_val[0]) + i)
            next_val = int("".join(next_val))
            if next_val >= low and next_val <= high:
                res.append(next_val)

            # add to first index
            next_val = [char for char in str(next_val)]
            next_val[0] = str(int(next_val[0]) + 1)
            curr = int("".join(next_val))
        return res
