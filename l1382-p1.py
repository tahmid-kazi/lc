# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # inorder traversal + greedy
        # 11/25/24) Mon) tk) bbus) 739-748pm)
        def traverse(root): # inorder traversal
            if not root:
                return
            traverse(root.left)
            tree.append(root.val)
            traverse(root.right)
        def construct(left, right):
            if left > right:
                return
            mid = (left+right)//2
            return TreeNode(tree[mid], construct(left, mid-1), construct(mid+1, right))
        tree = []
        traverse(root)
        return construct(0, len(tree)-1)