# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS, recursion, backtracking; this shouldnt be a leetcode hard
        # 11/21/24-thurs, 1106-1112pm) tk) 16th problem of the day done
        def traverse(node, sum1):
            if not node:
                return 0
            left = traverse(node.left, sum1)
            right = traverse(node.right, sum1)
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            sum1.append(left+right+node.val)
            return max(left, right) + node.val
        res = []
        traverse(root, res)
        return max(res)
