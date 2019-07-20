# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_l = sum_h = ListNode(0)
        carry = 0
        
        while l1 or l2 :
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
            
            s = v1 + v2 + carry
            carry = int(s/10)
            s = int(s % 10)
            
            sum_l.next = ListNode(s)
            sum_l = sum_l.next
            
            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next
        if carry >= 1:
            sum_l.next = ListNode(carry)        
            
        return sum_h.next
        
