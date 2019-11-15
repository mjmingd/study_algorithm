# Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(idx,target, res=list()) :
            if target == 0 : 
                if res not in ret :
                    ret.append(res)
                return
            for i in range(idx, len(candidates)) :
                if target-candidates[i] < 0 :
                    break
                helper(i, target-candidates[i], res+[candidates[i]])
            
    
        ret= []
        candidates.sort()
        helper(0, target)

        return ret
       
