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
        
        # trick: this uses inorder traversal
        # you also need to figure out a way to link the last node with the next one
        # 11/4/24) Mon) 723 to 734pm) tk)
        if not root:
            return

        first, last = None, None
        
        def dfs_linker(node):
            nonlocal first, last
            if not node:
                return
            
            #now run the inorder traversal:
            dfs_linker(node.left) # left
            # middle
            if last is None:
                first = node
            else:
                node.left = last
                last.right = node
            last = node

            dfs_linker(node.right) # right

        dfs_linker(root)

        last.right = first
        first.left = last
        
        return first
        
        
