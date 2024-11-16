# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # foundational BFS problem
        # 11/15/24) 729-739pm) Fri) tk)
        result = []
        queue1 = deque()
        queue1.append(root)
        while queue1:
            level = []
            for i in range(len(queue1)):
                node = queue1.popleft()
                level.append(node.val)

                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
            result.append(level)

        return result