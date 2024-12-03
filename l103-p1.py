# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # use BFS (left to right, then right to left)
        # this is basically a variation of BFS with the alternating left and right movements (zigzag)
        # 12/3/24) Tue) 1225 to 1239pm) tk) 2F study room)
        result = []
        queue1 = deque([root])
        left_to_right = True
        while queue1:
            level = []
            for _ in range(len(queue1)): # per level
                node = queue1.popleft()
                # process the zigzag, determine what order it needs to be added in
                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                # now do the BFS
                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
            result.append(level) #add each level of the zigzag one level by one level
            left_to_right = not left_to_right # now do right to left
        return result