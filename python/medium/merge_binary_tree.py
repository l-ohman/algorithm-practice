class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# First iteration
def mergeBinaryTrees(tree1, tree2):
    if not tree1 and not tree2:
        return None
    value = (tree1.value if tree1 else 0) + (tree2.value if tree2 else 0)
    tree = BinaryTree(value)
    
    left = [tree1.left if tree1 else None, tree2.left if tree2 else None]
    right = [tree1.right if tree1 else None, tree2.right if tree2 else None]
    
    tree.left = mergeBinaryTrees(left[0], left[1])
    tree.right = mergeBinaryTrees(right[0], right[1])
    return tree


# Second iteration (a better if-statement allows _much_ cleaner code)
def mergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2
    elif tree2 is None:
        return tree1

    tree = BinaryTree(tree1.value + tree2.value)
    tree.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree
