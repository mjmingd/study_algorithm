# Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
    '''
    time complexity : O(N)
    space complexity : O(1)
    '''
        if not head or not head.next : return head
        dummyH, dummy = ListNode(0), ListNode(0)
        
        # dummy -> curr -> nxt -> nxt.next
        # dummy -> nxt -> curr -> nxt.next
        #                 dummy -> curr ...
        
        dummyH.next, dummy.next = head.next, head
        while dummy.next and dummy.next.next :
            curr, nxt = dummy.next, dummy.next.next
            dummy.next, nxt.next, curr.next = nxt, curr, nxt.next
            dummy = curr
            
        return dummyH.next
    
