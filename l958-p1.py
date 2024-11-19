# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # 11/18/24) Mon) 1003 - 1008pm) tk)
        # use BFS (level tracking)
        queue1 = deque([(root, 0, 0)])
        position = 1
        while queue1:
            node, level, column = queue1.popleft()
            if position != 2 ** level + column: #check the calculation
                return False
            
            if node.left:
                queue1.append((node.left, level+1, column*2)) # check the column calculation
            if node.right:
                queue1.append((node.right, level+1, column*2+1))
            position += 1
        return True