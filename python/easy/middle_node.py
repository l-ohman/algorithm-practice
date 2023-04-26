# easy, linked lists

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    index = 0
    current = linkedList
    middle = linkedList

    while current.next:
        current = current.next
        if index % 2 == 0:
            middle = middle.next
        index += 1
    return middle
