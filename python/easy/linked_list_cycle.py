# https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        curr = head
        while curr and curr not in nodes:
            nodes.add(curr)
            curr = curr.next
        return curr is not None


# "hare and tortoise" algorithim, haven't seen this before
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
