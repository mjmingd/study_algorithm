# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    '''
    time complexity : O(NlogN)
    space complexity : O(N)
    '''
    
        dict_ = Counter(nums)
        print(dict_)
        ret =  sorted(dict_, key= lambda x : dict_[x], reverse=True)
        return ret[:k]
        
            
        
