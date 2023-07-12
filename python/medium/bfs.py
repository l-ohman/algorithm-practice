class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        stack = [self]
        while stack:
            node = stack.pop(0)
            array.append(node.name)
            stack += node.children
        return array
