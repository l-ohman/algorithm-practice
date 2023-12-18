# https://leetcode.com/problems/invert-binary-tree/

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# first attempt (BFS) roughly 1min - beats 47% time and 84% memory
def invertTree(root):
    q = deque([root])
    while len(q):
        node = q.popleft()
        if node == None:
            continue
        left, right = node.left, node.right
        node.left = right
        node.right = left
        q.append(left)
        q.append(right)
    return root


# second attempt (DFS) - beats 53% time and 19% memory
def invertTree2(root):
    if root is not None:
        root.left, root.right = root.right, root.left
        invertTree2(root.left)
        invertTree2(root.right)
    return root
