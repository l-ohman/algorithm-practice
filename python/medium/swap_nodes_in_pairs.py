# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        prev, curr, res = None, head, head.next
        while curr and curr.next:
            tmp = curr.next
            if prev: prev.next = tmp
            curr.next, tmp.next = tmp.next, curr
            prev, curr = curr, curr.next
        return res or head
