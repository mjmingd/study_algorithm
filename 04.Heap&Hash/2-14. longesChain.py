# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
    '''
    Note: 1. 1 <= words.length <= 1000
          2. 1 <= words[i].length <= 16
          3. words[i] only consists of English lowercase letters.
          
    time complexity : O(N)
    space complexity : O(N)
    '''
    
        def dfs(word):
            if word in dp : return dp[word]
            chains = 1
            for i in range(len(word)) :
                nxt = word[:i] + word[i+1:]
                if nxt in words :
                    chains = max(chains, dfs(nxt)+1)
            dp[word] = chains
            return chains
        
        
        dp = {}
        for w in words :
            dfs(w)
            
        return max(dp.values())
