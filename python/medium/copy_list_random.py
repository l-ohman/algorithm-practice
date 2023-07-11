# https://leetcode.com/problems/copy-list-with-random-pointer/
# top 0.5% on memory usage....but bottom 5% on runtime 🤔

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    original = []
    duplicate = []
    current = head
    while current:
        original.append(current)
        duplicate.append(Node(current.val))
        current = current.next
    for i in range(len(original)):
        node = original[i]
        if node.random:
            idx = original.index(node.random)
            duplicate[i].random = duplicate[idx]
        if node.next:
            duplicate[i].next = duplicate[i+1]
    return duplicate[0] if duplicate else None
