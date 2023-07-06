class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def distance(value, target):
    return float("inf") if value is None else abs(target - value)

def findClosestValueInBst(tree, target):
    if tree is None: return None
    value1 = findClosestValueInBst(tree.left, target)
    value2 = findClosestValueInBst(tree.right, target)
    closer = value1 if distance(value1, target) < distance(value2, target) else value2
    return closer if distance(closer, target) < distance(tree.value, target) else tree.value
