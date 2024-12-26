# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # 1150am) buy white cardstock ffx 
        # 12/26/24) 1155 to 1202pm) Thurs) tk) done (4th problem in 1hr) 12J
        def dfs(node):
            nonlocal counter
            if not node: return

            if low <= node.val <= high: # forgot this
                counter += node.val
            if low < node.val: # forgot this
                dfs(node.left)
            if high > node.val: # forgot this
                dfs(node.right)
        counter = 0
        dfs(root)
        return counter