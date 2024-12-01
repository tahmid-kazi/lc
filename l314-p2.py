# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use BFS + column tracker
        if not root:
            return []
        # try2 - 12/1/24) Sun) tk) 119-128pm)
        queue1 = deque([(root, 0)]) #(node, col)
        col_tracker = defaultdict(list)

        while queue1:
            node, col = queue1.popleft()
            # now store into column tracker
            col_tracker[col].append(node.val)
            # NOW run the BFS shit
            if node.left:
                queue1.append((node.left, col-1))
            if node.right:
                queue1.append((node.right, col+1))
        
        # now that the column tracker dictionary is made, make an array of arrays to return it
        result = []
        for i in sorted(col_tracker.keys()): # O(nlog(n))
            result.append(col_tracker[i]) # this is the area where you are prone to make a mistake
        return result