# Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        time complexity : O(max(M,N))
        space complexity : O(1)
        '''
        
        x, p1 = 0, l1
        while p1 :
            x = x*10 + p1.val
            p1 = p1.next
        
        y, p2 = 0, l2
        while p2 :
            y = y*10 + p2.val
            p2 = p2.next
        
        ans, dummy = x+y, ListNode(0)
    
        if ans == 0 : return dummy
        while ans :
            v, ans = ans%10, ans//10
            dummy.next, dummy.next.next = ListNode(v), dummy.next
            
        return dummy.next

            
        
            
        
        
            
