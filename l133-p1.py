"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 11/7/24) 1103-1113pm) Thurs) tk)
        #keep a dictionary to keep track of all the nodes already visited
        visited = {}

        # use dfs to perform a deep copy
        def dfs(node):

            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone
            for j in node.neighbors:
                clone.neighbors.append(dfs(j))
            return clone
        
        return dfs(node) if node else None
            
