# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            a, b = curr, curr.next
            while b and a.val==b.val:
                b = b.next
            curr.next = b
            curr = curr.next
        return head
      
