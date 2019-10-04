# Merge Intervals
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    '''
    time complexity : O(NlogN)
    space complexity : O(N)
    '''
    
        sorted_intervals = sorted(intervals, key= lambda x : x[0])
        ret = []
        for i in sorted_intervals :
            if not ret or ret[-1][1] < i[0] :
                ret.append(i)
            else :
                ret[-1][1] = max(ret[-1][1], i[1])
        return ret
