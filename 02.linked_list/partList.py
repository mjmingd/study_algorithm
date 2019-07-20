# Partition List
# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        greater =  greater_head = ListNode(0)
        less = less_head = ListNode(0)
        
       
        while head :
            if head.val < x :
                less.next = head
                less = less.next
                
            else:
                greater.next = head
                greater = greater.next
        
            head = head.next
            
        greater.next = None
        
        less.next = greater_head.next
        
        return less_head.next
