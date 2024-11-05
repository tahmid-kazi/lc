"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 11/4/24) Mon) 738 too 754pm) tk)
        if not root:
            return
        first, last = None, None
        # now define the function that 
        def dfs_linker(node):
            nonlocal first, last # make local vars accessible
            if not node:
                return
            
            dfs_linker(node.left) # left
            #middle
            if not last: # if last node is not set, we're at the first node
                first = node 
            else: # start linking nodes
                node.left = last 
                last.right = node 
            last = node 
            dfs_linker(node.right) # right
        
        # call the dfs linker
        dfs_linker(root)
        #now handle the first and last pointers
        last.right = first # --> connection; connect the last pointer to the first pointer 
        first.left = last  # <-- connection; connect the first pointer to the last pointer

        return first #return the first item in the linked list