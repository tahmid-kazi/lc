# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 12/22/24) Sun) tk) (1027-1041am + 1111-1125am) 12J)
    # O(h) time, O(1) space, iterative

    def findSuccessor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        while root.left is not None:
            root = root.left
        return root
    def Replace(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left: # if no left, return right child
            return root.right
        if not root.right: # if no right, return left child
            return root.left
        # node has 2 children, find successor (in-order traversal)
        successor = self.findSuccessor(root.right)
        # attach left subtree to successor
        successor.left = root.left
        return root.right # return right subtree (which now has successor as root)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        current = root # node 
        parent = None # parent of the current node
        # find node to delete
        while current and current.val != key:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right
        # if the node to delete is not found, return the OG tree
        if not current:
            return root
        
        if not parent: # delete the target node
            return self.Replace(current) # deleting the root node

        if parent.left == current:
            parent.left = self.Replace(current)
        else:
            parent.right = self.Replace(current)
        
        return root