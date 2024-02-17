# https://leetcode.com/problems/super-washing-machines/


# first attempt - passes maybe 50% of test cases
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        d, l = sum(machines), len(machines)
        # check if a solution exists
        if d % l != 0:
            return -1
        # ideal number of dresses in each machine
        ideal = int(d / l)

        count = 0
        for i in range(len(machines)):
            num = machines[i]
            if num<ideal:
                continue
            # check adjacents to see if they need moving
            # if not, we can do this same time as another operation
            adjacents = 0
            if i>0 and machines[i-1]>ideal:
                adjacents = machines[i-1] - ideal
            elif i<len(machines)-1 and machines[i+1]>ideal:
                adjacents = max(adjacents, machines[i+1] - ideal)
            
            amount = num-ideal
            if adjacents<amount:
                amount = 0 if count>=amount else amount - count 
            count += amount 
        return count


# close, but couldn't quite find the prefix sum idea without reading an explanation
# beats 66% time, 95% space
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        d, l = sum(machines), len(machines)
        # check if a solution exists
        if d % l != 0:
            return -1
        # ideal number of dresses in each machine
        ideal = d // l

        # set baseline as 0 to use prefix sum
        machines = [m - ideal for m in machines]
        res = max(machines)
        prefix = 0
        for m in machines:
            prefix += m
            res = max(res, abs(prefix))
        return res
