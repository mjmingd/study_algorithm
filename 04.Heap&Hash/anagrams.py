# Group Anagrams
# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        alpha ={}
        for s in strs :
            key = tuple(sorted(s))
            if key in alpha :
                val = alpha[key]
                val.append(s)
                
            else :
                val = [s]
                
            alpha[key] = val
        
        return alpha.values()
            
