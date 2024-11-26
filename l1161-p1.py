# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # use BFS + queue
        # 11/25/24) tk) Mon) 735-739pm) bbus)
        minlevel = 1
        maxsum = float('-inf')
        queue1 = deque()
        queue1.append(root)
        level = 1
        while queue1:
            levelsum = 0
            size = len(queue1)

            for _ in range(size):
                node = queue1.popleft()
                levelsum += node.val

                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
            if levelsum > maxsum:
                maxsum = levelsum
                minlevel = level
            level += 1
        return minlevel