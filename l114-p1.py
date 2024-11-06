# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 11/6/24) Tue night) 1201 to 1222am) tk)
        #explanation done 1222 to 1247am
        if not root:
            return None
        
        left = self.flatten(root.left)
        right = self.flatten(root.right)

        if left is not None:
            flat = left # now flat is the flattened left subtree 
            while flat.right is not None: 
                flat = flat.right # move to the rightmost edge of the left subtree
            flat.right = right # attach right subtree to rightmost of left subtree

            root.right = left # now take that constructed linked list and set root to it
            root.left = None
        return root