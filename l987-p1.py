# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 11/5/24) 756 to 815pm) Tue) tk)
        # use BFS, use a queue
        queue1 = deque([(root, 0, 0)]) #for this one, you need to track (val, row, col)!
        col_tracker = defaultdict(list)

        while queue1:
            node, row, col = queue1.popleft()
            col_tracker[col].append((row, node.val))

            if node.left:
                queue1.append((node.left, row+1, col-1))
            if node.right:
                queue1.append((node.right, row+1, col+1))
        
        res = []
        for col in sorted(col_tracker.keys()):
            #---------------------------------------
            col_vals = []
            for row, val in sorted(col_tracker[col]):
                col_vals.append(val)
            #---------------------------------------
            res.append(col_vals)
        return res