# Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
    '''
    time complexity : O(N)
    space complexity : O(1)
    '''
    
        i, ordered = 0, {}
        for cha in order :
            ordered[cha] = i
            i += 1
        
        for i in range(len(words)-1) :
            w1, w2 = words[i], words[i+1]
            for l in range(min(len(w1), len(w2))) :
                if w1[l] != w2[l] :
                    if ordered[w1[l]] > ordered[w2[l]] :
                        return False
                    break
                else :
                    if len(w1) > len(w2) : return False
            
        return True
          
                
                
        
            
        
