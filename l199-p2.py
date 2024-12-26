# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        # 12/26/24) 232 to 252am) tk) wed night)
        queue1 = deque([root])
        result = []
        if not root: return []
        
        while queue1:
            level_len = len(queue1) # usually length is 2 b.c. binary tree
            for i in range(level_len):            
                node = queue1.popleft()
                # now find the rightmost
                if i == level_len-1:
                    result.append(node.val)
                
                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
        return result # thi indent was goobering it up