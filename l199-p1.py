# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 11/4/24) Mon) 705 to 715pm) tk)
        return_list = []
        queue1 = deque()
        
        # first check for these edge cases
        if not root: # check no node
            return []
        
        # start
        queue1.append(root)
        # run bfs
        while queue1:            
            level_len = len(queue1)
            for i in range(level_len):
                node = queue1.popleft()
                if i == level_len - 1: #last item on the queue at this level is the first rightmost
                    return_list.append(node.val)

                if node.left is not None:
                    queue1.append(node.left)
                if node.right is not None:
                    queue1.append(node.right)                

        return return_list