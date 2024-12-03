# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # 10/8/24 934 to 952pm Tue
        #why do we need the (res) parameter?
        def dfs(root, res):

            if not root:
                return 0
            
            left = dfs(root.left, res)
            right = dfs(root.right, res)

            self.res = max(self.res, left + right) 

            return max(left, right) + 1

        dfs(root, self.res)
        return self.res
