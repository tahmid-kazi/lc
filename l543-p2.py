# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # try2: beats 97%, 12/4/24 - wed - (1227 to 1238pm) tk)
        def dfs(root): # postorder traversal
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], left + right) 

            return max(left, right) + 1
        res = [0]
        dfs(root)
        return res[0]
