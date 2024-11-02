# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # 11/2/2024) 950am - 1000am) Sat) tk)
        # the trick: 
        # - use BFS, use a queue
        # - keep a column tracker (defaultdict)
        # - fill the column tracker relative to root
        # - then return the items from the defaultdict in sorted order (O(nlogn))

        # check edge case
        if not root:
            return []
        
        # use queue and dictionary of lists
        queue1 = deque([(root, 0)]) #first value - store the root (use this to anchor the rest of the cols)
        col_tracker = defaultdict(list)

        while queue1:
            node, col = queue1.popleft()
            col_tracker[col].append(node.val)

            # now run BFS/add to queue
            if node.left:
                queue1.append((node.left, col-1))
            if node.right:
                queue1.append((node.right, col+1))
            
        result = []
        for value in sorted(col_tracker.keys()):
            result.append(col_tracker[value])
        
        return result


