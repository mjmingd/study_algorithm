# Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
    '''
    time complexity : O(NlogN)
    space complexity : O(N)
    '''
    
        def sorting(log) :
            identifier, letter = log.split(" ", 1)
            return (letter, identifier)
        
        digits, letters = list(), list()
        for log in logs :
            if log.split()[1].isdigit() :
                digits += log,
            else :
                letters += log,
        
        sorted_letters = sorted(letters, key = sorting)

        return sorted_letters + digits
                
