# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# first solution - beats 63% time and 75% memory, but is messy code
def longestZigZag(root: TreeNode) -> int:
    global longest
    longest = 0

    def zigzag(node, go_left, distance=0):
        if node is None: return
        global longest
        longest = max(distance, longest)

        if node.left is not None:
            if go_left:
                zigzag(node.left, False, distance + 1)
            else:
                zigzag(node.left, False, 1)
        if node.right is not None:
            if not go_left:
                zigzag(node.right, True, distance + 1)
            else:
                zigzag(node.right, True, 1)

    zigzag(root, True)
    return longest
