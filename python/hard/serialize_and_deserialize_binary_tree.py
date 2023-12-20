# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# first (and only) attempt - took ~45min
# beats 99.5% time and 99.5% memory (new pb!)
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        s = ""
        q = deque([root])
        while len(q) > 0:
            node = q.popleft()
            if node is not None:
                q.extend([node.left, node.right])
                s += str(node.val)
            else:
                s += "n"
            s += ","
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def create_node(val):
            if val == "n":
                return None
            else:
                return TreeNode(int(val))

        data = data.split(",")

        root = create_node(data[0])
        q = deque([root])
        for i in range(1, len(data) - 1, 2):
            node_left = create_node(data[i])
            node_right = create_node(data[i + 1])

            current_node = q.popleft()
            current_node.left = node_left
            current_node.right = node_right

            if node_left is not None:
                q.append(node_left)
            if node_right is not None:
                q.append(node_right)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
