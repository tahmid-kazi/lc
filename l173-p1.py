# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # 11/14/24) 1210 to 1215pm) Thurs) tk)
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.current_idx = 0
        self.in_order(root)

    # needs inorder traversal
    def in_order(self, root): #run this to fill the array
        if not root:
            return
        self.in_order(root.left)
        self.arr.append(root.val)
        self.in_order(root.right)

    def next(self) -> int: # then move idx by and iterate over the BST_array
        val = self.arr[self.current_idx]
        self.current_idx += 1
        return val

    def hasNext(self) -> bool: # the checker
        return self.current_idx <= len(self.arr)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()