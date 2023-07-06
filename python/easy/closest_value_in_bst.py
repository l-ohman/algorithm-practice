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

# more efficient solution
def findClosestValueInBst2(tree, target):
    node = tree
    closest = float("inf")
    while (node is not None):
        if node.value == target: return node.value
        closest = node.value if abs(target - node.value) < abs(target - closest) else closest
        if (node.value < target):
            node = node.right
        else:
            node = node.left
    return closest
