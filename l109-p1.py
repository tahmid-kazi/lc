# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        #turn linkedlist into BST (very similar to leetcode 108 - convert sorted arr into BST)
        # basically find the middle (fast and slow pointer!!), make it root node
        # 11/19/24) Tue) 559-610pm) tk)
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)
        if prev:
            prev.next = None
        
        root.left = self.sortedListToBST(head) # left subtree
        root.right = self.sortedListToBST(slow.next) # right subtree
        return root
        
        