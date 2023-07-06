# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if not root:
        return []
    branches = branchSums(root.left) + branchSums(root.right)
    if branches:
        return [x + root.value for x in branches]
    else:
        return [root.value]
