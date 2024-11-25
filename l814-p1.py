# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # postorder traversal
        # 11/25/24) Mon) 510-512pm) tk) on bestbus)
        if not root:
            return
        
        if not self.pruneTree(root.left):
            root.left = None
        if not self.pruneTree(root.right):
            root.right = None
        
        if root.val != 1 and root.left is None and root.right is None:
            root = None
        return root