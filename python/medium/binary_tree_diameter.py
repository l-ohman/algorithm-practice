# "diameter" -> length of longest path
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# ... new keyword, "global"
def longestPath(tree):
    global longest
    if tree is None:
        return 0
    left = longestPath(tree.left)
    right = longestPath(tree.right)
    longest = max(longest, left + right)
    return max(left, right) + 1


def binaryTreeDiameter(tree):
    global longest
    longest = 0
    longestPath(tree)
    return longest
