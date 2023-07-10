# https://www.hackerrank.com/challenges/one-week-preparation-kit-tree-preorder-traversal

def preOrder(root):
    if root:
        print(root, end=" ")
        preOrder(root.left)
        preOrder(root.right)
