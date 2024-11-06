# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #11/6/24) Tue night) 133 to 143am) tk)
        arr = [] #bruh this is so easy, but bad on memory
        # since its BST, use inorder traversal
        def dfs(node, arr):
            if not node:
                return
            else:
                dfs(node.left, arr)
                # ----- now do the actual work ------
                arr.append(node.val)
                # -----------------------------------
                dfs(node.right, arr)
        dfs(root, arr)
        return arr[k-1]
        