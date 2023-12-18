# https://leetcode.com/problems/same-tree/description/

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS - beats 30%
def isSameTree(p, q):
    if p is None or q is None:
        return p == q
    if p.val != q.val:
        return False
    if not isSameTree(p.left, q.left):
        return False
    if not isSameTree(p.right, q.right):
        return False
    return True


# BFS approach - beats 83% (but is written somewhat poorly)
def isSameTree2(p, q):
    p_queue, q_queue = deque([p]), deque([q])
    while len(p_queue) > 0 and len(q_queue) > 0:
        p, q = p_queue.popleft(), q_queue.popleft()
        if p == None or q == None:
            if p != q:
                return False
        elif p.val != q.val:
            return False
        else:
            p_queue.append(p.left)
            p_queue.append(p.right)
            q_queue.append(q.left)
            q_queue.append(q.right)
    return len(p_queue) == 0 and len(q_queue) == 0
