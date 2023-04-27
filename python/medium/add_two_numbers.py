# medium, linked list
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first attempt - unnecessary recursion, adding an extra variable to fn
def addTwoNumbersRecursive(l1, l2, add1=False):
    if (l1 is None) and (l2 is None):
        return None if not add1 else ListNode(1)
    
    val1 = 0 if l1 is None else l1.val
    val2 = 0 if l2 is None else l2.val
    result = val1 + val2 + (1 if add1 else 0)

    single_digit = result < 10
    if not single_digit:
        result -= 10
    
    if l1 is not None:
        l1 = l1.next
    if l2 is not None:
        l2 = l2.next
    return ListNode(result, addTwoNumbers(l1, l2, (not single_digit)))

# second attempt - while loop instead of recursion
def addTwoNumbers(l1, l2):
    head = current = ListNode(0)
    value = 0
    while l1 or l2 or value:
        if l1:
            value += l1.val
            l1 = l1.next
        if l2:
            value += l2.val
            l2 = l2.next
        current.next = ListNode(value % 10)
        value = value // 10
        current = current.next
    return head.next
