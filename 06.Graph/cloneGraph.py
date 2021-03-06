# Clone Graph
# https://leetcode.com/problems/clone-graph/

# DFS (iterative) 

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node :
            return 
        copy = Node(node.val, [])
        visited = {node : copy}
        stack = [node]
            
        while stack :
            node = stack.pop()
            for neighbor in node.neighbors :
                if neighbor not in visited :
                    copyNeib = Node(neighbor.val, [])
                    visited[neighbor] = copyNeib
                    visited[node].neighbors.append(copyNeib)
                    stack.append(neighbor)
                else :
                    visited[node].neighbors.append(visited[neighbor])
        return copy
