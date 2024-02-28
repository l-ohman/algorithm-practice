# https://leetcode.com/problems/find-bottom-left-tree-value/description/?envType=daily-question&envId=2024-02-28


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# First attempt (5min) -- beats 13% time and 40% space
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 0]])
        lowest, res = 0, root
        while q:
            curr, level = q.popleft()
            if curr is None:
                continue
            if level < lowest:
                lowest = level
                res = curr
            q.append([curr.left, level - 1])
            q.append([curr.right, level - 1])
        return res.val


# Small change to the queue...beats 64% time and 80% space
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 0]])
        lowest, res = 0, root
        while q:
            curr, level = q.popleft()
            if level < lowest:
                lowest = level
                res = curr

            if curr.left is not None:
                q.append([curr.left, level - 1])
            if curr.right is not None:
                q.append([curr.right, level - 1])
        return res.val
