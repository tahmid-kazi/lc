# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        # uses DFS + Postorder traversal
        # 1211am to 1230am) 12/19/24) Wed night) tk)
        # time: O(n), space: O(H) (height)
        def postorder(node):
            if not node:
                # (is_bst, min_val, max_val, size_of_bst)
                return (True, float('inf'), float('-inf'), 0)

            # dfs left
            left_bst, left_min, left_max, left_size = postorder(node.left)
            # dfs right
            right_bst, right_min, right_max, right_size = postorder(node.right)
            # do postorder work

            is_current_bst = left_bst and right_bst and (left_max < node.val < right_min)
            if is_current_bst:
                current_size = 1 + left_size + right_size
                min_val= min(node.val, left_min)
                max_val= max(node.val, right_max)
                return (True, min_val, max_val, current_size)
            else:
                return (False, 0,0,max(left_size, right_size))

        return postorder(root)[3] # the 4th item gives you the size of the largest subtree
        