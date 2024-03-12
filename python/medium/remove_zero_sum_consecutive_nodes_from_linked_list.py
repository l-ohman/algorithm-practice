# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/?envType=daily-question&envId=2024-03-12


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = start = ListNode(0, head)
        while start:
            p_sum = 0
            end = start.next
            while end:
                p_sum += end.val
                if p_sum == 0:
                    start.next = end.next
                end = end.next
            start = start.next

        return dummy.next
