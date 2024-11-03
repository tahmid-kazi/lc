# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        counter = [0]

        # 11/3/24) Sun) 613-617pm) tk)
        def dfs(node):
            if not node:
                return

            if low <= node.val <= high:
                counter[0] += node.val
            if low < node.val:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        
        dfs(root)
        return counter[0]
        
        