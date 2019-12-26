# Redundant Connection
# https://leetcode.com/problems/redundant-connection/


'''
solution 2 : using Union-Find
time complexity : O(N)
space complexity : O(N)
'''

class DSU :
    def __init__(self) :
        self.parent = [x for x in range(1001)]
        self.rank = [0] * 1001
    
    def find(self, x) :
        if self.parent[x] != x :
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y) :
        xrank, yrank = self.find(x), self.find(y)
        if xrank == yrank :
            return False
        elif self.rank[xrank] < self.rank[yrank] :
            self.parent[xrank] = yrank
        elif self.rank[yrank] < self.rank[xrank] :
            self.parent[yrank] = xrank
        else :
            self.parent[yrank] = xrank
            self.rank[xrank] += 1
        return True
    
   
class Solution:
    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for u, v in edges :
            if not dsu.union(u,v):
                return u, v
        


'''
solution 1 : dfs
time complexity : O(N^2)
space complexity : O(N)

from collections import defaultdict

class Solution:
    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        def dfs(src, tgt) :
            if src not in seen :
                seen.add(src)
                if src==tgt : return True
                return any(dfs(nei, tgt) for nei in graph[src])
            
        for u, v in edges :
            seen = set()
            if u in graph and v in graph and dfs(u,v): return u, v
            graph[u].add(v)
            graph[v].add(u)
