# https://leetcode.com/problems/reorder-list/submissions/1211953769/?envType=daily-question&envId=2024-03-23


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# first attempt--beats 99% time (!) and 87% space
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # store all nodes
        nodes = deque([])
        curr = head
        while curr:
            if curr != head:
                nodes.append(curr)
            curr = curr.next

        # restructure list
        curr = head
        while nodes:
            curr.next = nodes.pop()
            curr = curr.next
            if len(nodes) > 0:
                curr.next = nodes.popleft()
                curr = curr.next

            # ensure no cycle in linked-list
            curr.next = None

        return head
