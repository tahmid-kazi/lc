    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
            # backtracking + DFS + path sum + recursion
            # 12/18/24 - 840 to 900pm) Wed) tk) 
            # O(N*H) runtime, O(H) space
            result, path = [], []
            def dfs_backtrack(node, current_sum):
                if not node:
                    return
                path.append(node.val)
                current_sum += node.val

                #check if leaf node
                if not node.left and not node.right and current_sum == targetSum:
                    result.append(list(path)) # add all possible paths to the result array
                
                # now check left and right subtree (recursion)
                # hence, preorder traversal
                if node.left:
                    dfs_backtrack(node.left, current_sum)
                if node.right:
                    dfs_backtrack(node.right, current_sum)
                
                path.pop() # remove the last node from the path (why?)
            # main()
            dfs_backtrack(root, 0)
            return result