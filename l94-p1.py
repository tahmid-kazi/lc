# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # 11/5/24) Tue) 806 to 808am) tk)
        # nailed in on my own in 2mins!
        res = []
        def dfs(node):
            if not node:
                return
            #left            
            if node.left:
                dfs(node.left)
            # middle
            res.append(node.val)
            #right
            if node.right:
                dfs(node.right)
        dfs(root)
        return res