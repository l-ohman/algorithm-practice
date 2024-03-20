# https://leetcode.com/problems/merge-in-between-linked-lists/?envType=daily-question&envId=2024-03-20


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# first attempt--beats 99% (!) time and 71% memory
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        curr = list1
        for _ in range(a - 1):
            curr = curr.next
        skip = curr.next
        curr.next = list2

        for _ in range(b - a + 1):
            skip = skip.next
        while curr.next:
            curr = curr.next
        curr.next = skip

        return list1
