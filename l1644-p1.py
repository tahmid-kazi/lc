# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # similar to leetcode 236 - LCA-BT-I
        # in this case we have to also check if p and q even exist
        # 11/19/24) 109 to 113pm) Tue) tk)
        self.found_p = False
        self.found_q = False

        def dfs(node):
            if not node:
                return
            
            # traverse left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            # now check if you found p or q
            if node == p:
                self.found_p = True
                return node
            if node == q:
                self.found_q = True
                return node

            if left and right:
                return node
            
            return left if left else right
        lca =dfs(root)
        if self.found_p and self.found_q:
            return lca
        return None
        