# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 11/25/24) Sun night) 111-118am) tk)
        if not head:
            return
        slow = fast = head 
        # find the middle node now
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reversing the second part of the list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            #merge the 2 sorted lists
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next