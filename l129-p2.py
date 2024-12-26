# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # 12/26/24) 1104/1112-1121am) Thurs) tk)
        results = []
        def dfs(node, str1):
            if not node: return 0
            # use preorder traversal

            str1+= str(node.val)
            if not node.left and not node.right:
                results.append(int(str1))

            if node.left:
                dfs(node.left, str1)
            if node.right:
                dfs(node.right, str1)
        dfs(root, "")
        return sum(results)