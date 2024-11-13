# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = float("inf")
        node = root
        # 11/12/24) Tue) 1052-1104pm) tk)
        while node:
            if root.val == target:
                return root.val
            
            if abs(node.val - target) < abs(closest - target):
                closest = node.val

            if abs(node.val - target) == abs(closest - target):
                closest = min(node.val, closest)
            
            if target < node.val:
                node = node.left
            else:
                node = node.right
                
        return closest