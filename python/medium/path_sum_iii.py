# https://leetcode.com/problems/path-sum-iii/


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# first attempt, beats 14% time and 83% memory
def pathSum(root: TreeNode, targetSum: int) -> int:
    def countPaths(node, target):
        count = 0
        if node is None:
            return count
        if node.val == target:
            count += 1
        count += countPaths(node.left, target - node.val)
        count += countPaths(node.right, target - node.val)
        return count

    count = 0
    q = deque([root])
    while len(q):
        node = q.popleft()
        if node is None:
            continue
        count += countPaths(node, targetSum)
        q.extend([node.left, node.right])
    return count
