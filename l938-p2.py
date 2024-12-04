# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # try2 - 12/3/24) tue) 745-755pm) tk) 
        def dfs(node):
            nonlocal counter 
            if not node:
                return

            if low <= node.val <= high:
                counter += node.val
            if low < node.val:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        counter = 0
        dfs(root)
        return counter
        
        