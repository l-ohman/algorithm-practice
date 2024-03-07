# https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=daily-question&envId=2024-03-07


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = end = head
        while end and end.next:
            middle = middle.next
            end = end.next.next
        return middle
