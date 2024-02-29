# https://leetcode.com/problems/even-odd-tree/description/?envType=daily-question&envId=2024-02-29


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# First attempt -- not written very well, but beats 78% time and 75% space
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([[root, 0]])
        p_val = p_lvl = None
        while q:
            curr, lvl = q.popleft()
            even = curr.val % 2 == 0
            # ensure odd/even is on correct level
            if (even and lvl % 2 == 0) or (not even and lvl % 2 == 1):
                return False
            # ensure order of vals in row is asc/dec correctly
            if lvl == p_lvl and (
                (even and curr.val >= p_val) or (not even and curr.val <= p_val)
            ):
                return False
            # update prev values
            p_val, p_lvl = curr.val, lvl

            if curr.left:
                q.append([curr.left, lvl + 1])
            if curr.right:
                q.append([curr.right, lvl + 1])
        return True
