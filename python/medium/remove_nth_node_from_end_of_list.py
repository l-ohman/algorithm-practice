# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=daily-question&envId=2024-03-03


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        before = end = head
        for _ in range(n):
            end = end.next
        if not end:
            return head.next

        while end.next:
            before = before.next
            end = end.next
        before.next = before.next.next
        return head
