# merge two sorted lists
# https://leetcode.com/problems/merge-two-sorted-lists/

"""
time complexity : O(max(M,N))
spare complexity : O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        head = return_list = ListNode(0)
        point1, point2 = l1, l2
        
        while point1 and point2 :
            if point1.val >= point2.val :
                head.next = point2
                head = head.next
                point2 = point2.next
                
            elif point1.val < point2.val :
                head.next = point1
                head = head.next
                point1 = point1.next
                
        # if the lengths of two lists are not the same
        
        if point1 != None :
            head.next = point1
            
        elif point2 != None :
            head.next = point2
            
        return return_list.next
