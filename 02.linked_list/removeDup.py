# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None :
            return head
        
        res = tmp =  ListNode(-1)
        tmp.next = head
        CN = head
        
        while CN :
            if CN.next and CN.val == CN.next.val :
                val = CN.val
                while CN and val == CN.val :
                    CN = CN.next
                tmp.next = CN
            else :
                tmp = tmp.next
                CN = CN.next
            
        return res.next
                
            


