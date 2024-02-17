# https://leetcode.com/problems/number-of-atoms/


# deceptively difficult question...first attempt -- beats 28% time and 67% memory
# i'm okay with this solution for now, but it'd be nice to refactor it eventually
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # will use a stack of defaultdicts to manage nested parens
        count = defaultdict(int)
        stack = [count]

        i, n = 0, len(formula)
        while i < n:
            char = formula[i]
            if char == "(":
                # starting a subsequence--create new entry in stack
                count = defaultdict(int)
                stack.append(count)
                i += 1
            elif char == ")":
                # ending a subsequence--get the number after this paren (if it exists)
                start, end = i+1, i+2
                if start<n and formula[start].isdigit():
                    while end<n and formula[end].isdigit():
                        end += 1
                    factor = int(formula[start:end])
                else:
                    factor = 1
                
                # multiply nums and update count in stack
                subcount = stack.pop()
                for atom,num in subcount.items():
                    stack[-1][atom] += num * factor

                i = end if start<n and formula[start].isdigit() else start
                count = stack[-1]
            else:
                # if it's not a paren, it must be an atom--identify the atom and its count
                start, end = i, i+1
                while end < n and formula[end].islower():
                    end += 1
                atom = formula[start:end]

                # get the count (amount) of this atom if it exists
                start, end = end, end+1
                if start<n and formula[start].isdigit():
                    while end < n and formula[end].isdigit():
                        end += 1
                    amount = int(formula[start:end])
                else:
                    amount = 1
                
                # update the counter in the respective stack
                stack[-1][atom] += amount
                i = end if start<n and formula[start].isdigit() else start
        
        # conv into output string
        res = ""
        for atom in sorted(stack[0].keys()):
            res += atom
            num = stack[0][atom]
            if num>1:
                res += str(num)
        return res
