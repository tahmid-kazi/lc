# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # 11/11/24) Mon) 824-844pm) tk)
        items = []
        # use preorder traversal
        def dfs(node, str1):
            if not node:
                return
            str1 += str(node.val) # this was the key missing piece  

            if not node.left and not node.right:
                items.append(int(str1))
                return 
              
            if node.left:
                dfs(node.left, str1)
            if node.right:
                dfs(node.right, str1)
        
        dfs(root, "")
        return sum(items)
        