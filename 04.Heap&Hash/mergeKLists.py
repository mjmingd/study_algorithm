# Merge k sorted lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):

# Divide and Conquer
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            
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
    
        if len(lists) == 0 :
            return None
        elif len(lists) == 1 :
            return lists[0]
        else :
            while len(lists) > 1  :
                l1 = lists.pop()
                l2 = lists.pop()
                l = mergeTwoLists(l1, l2)
                lists.append(l)
            return lists[0]
    
    
    # Heap
    # Time Limit Exceeded
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        heap = []
        res = dummy = ListNode(0)
        
        for l in lists :
            while l :
                heapq.heappush(heap, (l.val, l))
                l = l.next
                
        while heap != [] :   
            n = heapq.heappop(heap)[1]
            dummy.next = n
            dummy = dummy.next
            
        return res.next
    
        
