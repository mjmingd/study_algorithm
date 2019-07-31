# K Cloest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        points.sort(key = lambda p : p[0]**2+p[1]**2)
        
        return points[:K]
        
        
        
#solution using heap
    def kClosest2 (self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # using min heap
        heap = []
        
        for p in points:
            d = p[0]** 2 + p[1]**2
            heapq.heappush(heap, (d, p)) #(priority, value)
            
        return [heapq.heappop(heap)[1] for _ in range(K)]
