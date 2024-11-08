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
        # 11/7/24) 1113 to 1123pm) Thurs) tk)
        # keep track of visited nodes with a dictionary
        visited = defaultdict()

        # perform a deep copy with DFS
        def dfs(node):
            if node in visited:
                return visited[node] #if this node has already been visited, return that node and all of its neighbors
            
            deep_copy = Node(node.val)
            visited[node] = deep_copy # now set the mapping of the node to its deep copy in the dictionary
            for nei in node.neighbors: # now just populate the neighbors
                deep_copy.neighbors.append(dfs(nei))
            return deep_copy #once done with all the work for that node, return it

        # now call the function
        if node:
            return (dfs(node))
        else:
            return None