# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root):
        curr = [root]
        sums = []
        while len(curr) > 0:
            new_sum = 0
            next_level = []
            for node in curr:
                if not node:
                    continue
                new_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            sums.append(new_sum)
            curr = next_level

        level = 0
        maximum = float("-inf")
        for i in range(len(sums)):
            if sums[i] > maximum:
                maximum = sums[i]
                level = i+1
        return level
