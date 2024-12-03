# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 10/10/24 913 to 919am to 927am @ capital one cafe!!
        if not root:
            return 
 
        if root == q or root == p:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: # that means both recursion trees are null, hence root is the LCA
            return root
        return left or right # otherwise left OR right is the LCA
