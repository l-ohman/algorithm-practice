# easy
from math import trunc, floor


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# first solution
def evaluateExpressionTreeFirst(tree):
    if tree.value >= 0:
        return tree.value

    val1 = evaluateExpressionTreeFirst(tree.left)
    val2 = evaluateExpressionTreeFirst(tree.right)
    if tree.value == -1:
        return val1 + val2
    elif tree.value == -2:
        return val1 - val2
    elif tree.value == -3:
        result = val1 / val2
        if result < 0:
            return -floor(-result)
        return floor(result)
    elif tree.value == -4:
        return val1 * val2


# second solution
def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value

    operators = {
        -1: lambda x, y: x + y,
        -2: lambda x, y: x - y,
        -3: lambda x, y: trunc(x / y),
        -4: lambda x, y: x * y
    }
    val1 = evaluateExpressionTree(tree.left)
    val2 = evaluateExpressionTree(tree.right)
    return operators[tree.value](val1, val2)
