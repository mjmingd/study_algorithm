# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        
        res = ListNode(-1)
        res.next = head
        dummy = head
        length = 0 
        
        # measure length of linked list
        while dummy:
            length += 1
            dummy = dummy.next
            
        # drop the n-th node
        idx = length-n
        dummy = res
        for _ in range(idx):
            dummy = dummy.next
        dummy.next = dummy.next.next
        
        return res.next
