# https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root):
        def dfs(node, largest):
            if not node:
                return 0
            count = 0
            if node.val >= largest:
                count += 1
                largest = node.val
            count += dfs(node.left, largest)
            count += dfs(node.right, largest)
            return count
        return dfs(root, float("-inf"))
