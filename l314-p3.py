# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # 12/25/24) 930 to 949pm) Wed) tk) did it on my own) 
        if not root:
            return []
        
        #first setup the column tracker and the BFS queue
        queue1 = deque([(root, 0)])
        col_tracker = defaultdict(list)

        while queue1:
            node, col = queue1.popleft()
            col_tracker[col].append(node.val)

            if node.left:
                queue1.append((node.left, col-1))
            if node.right:
                queue1.append((node.right, col+1))
        result = []
        for i in sorted(col_tracker.keys()):
            result.append(col_tracker[i])
        return result