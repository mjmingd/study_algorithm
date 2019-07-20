# Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        
        #find the mid
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        #flipped slow
        pre = None
        while slow :
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt
        
        while pre :
            if pre.val != head.val :
                return False
            pre = pre.next
            head = head.next
        return True
