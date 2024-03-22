# https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-22


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# first attempt--beats 95% time and 41% space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        for i in range(len(vals) // 2):
            j = len(vals) - 1 - i
            if vals[i] != vals[j]:
                return False
        return True
