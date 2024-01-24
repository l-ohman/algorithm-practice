# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/?envType=daily-question&envId=2024-01-24

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# second attempt -- had another working solutions but exceeded memory constraints
class Solution:
    def __init__(self):
        self.count = 0

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, pairs=set()):
            if node.val in pairs:
                pairs.remove(node.val)
            else:
                pairs.add(node.val)

            if node.left:
                dfs(node.left, set(pairs))
            if node.right:
                dfs(node.right, set(pairs))

            if not node.left and not node.right:
                palindromic = len(pairs) <= 1
                if palindromic:
                    self.count += 1

        dfs(root)
        return self.count


# slightly refined version
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, pairs=set()):
            # remove if there would be a pair, otherwise add this val
            if node.val in pairs:
                pairs.remove(node.val)
            else:
                pairs.add(node.val)

            # if leaf node, return whether or not its pseudo-palindromic
            if not node.left and not node.right:
                palindromic = len(pairs) <= 1
                return 1 if palindromic else 0

            # if it's not a leaf, return sum of left/right branches
            left = right = 0
            if node.left:
                left = dfs(node.left, set(pairs))
            if node.right:
                right = dfs(node.right, set(pairs))
            return left + right

        return dfs(root)
