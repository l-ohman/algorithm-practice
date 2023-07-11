# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    for i in range(1, left):
        prev = prev.next
    curr = prev.next

    # ex: [1,2,3,4,5],2,4 - prev=1, curr=2
    for i in range(right-left):
        tmp = curr.next         # tmp -> 3              | tmp -> 4
        curr.next = tmp.next    # curr (2) next -> 4    | curr (2) next -> 5
        tmp.next = prev.next    # tmp (3) next -> 2     | tmp (4) next -> 3
        prev.next = tmp         # prev (1) next -> 3    | prev (1) next -> 4
    return dummy.next


def test(input, left, right):
    expected = input[:left-1] + input[left-1:right][::-1] + input[right:]
    # print(expected)
    nodes = []
    for i in range(len(input)):
        nodes.append(ListNode(input[i]))
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    head = reverseBetween(nodes[0], left, right)
    duplicate = []
    curr = head
    while curr:
        duplicate.append(curr.val)
        curr = curr.next
    print("Pass" if duplicate == expected else "Fail")


input, left, right = [1, 2, 3, 4, 5], 2, 4
test(input, left, right)
input, left, right = [3, 5], 1, 2
test(input, left, right)
