# Time Based Key-value Store
# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
    '''
    time complexity : O(1)
    space complexity : O(N)
    '''
            self.t_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
    '''
    time complexity : O(logN)
    '''
    
        candi, l, r = self.t_map[key], 0, len(self.t_map[key])-1
        if key not in self.t_map or timestamp < candi[0][1] : return ''
        while l <= r:
            m = (l + r) // 2
            if candi[m][1] == timestamp: return candi[m][0]
            if candi[m][1] < timestamp: l = m + 1
            else: r = m - 1
        return candi[r][0]
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
