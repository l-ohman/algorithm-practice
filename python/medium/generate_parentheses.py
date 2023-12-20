# https://leetcode.com/problems/generate-parentheses/description/


# first attempt - beats 68% time and 6% memory
def generateParenthesis(n):
    if n == 1:
        return ["()"]
    if n == 2:
        return ["()()", "(())"]

    combinations = generateParenthesis(n - 1)
    res = set([])
    for c in combinations:
        # for each combination, add all possible variants with +1 paren
        res.update(["(" + c + ")", "()" + c, c + "()"])
        for i in range(len(c) - 1):
            res.add(c[: i + 1] + "()" + c[i + 1 :])
    return list(res)
