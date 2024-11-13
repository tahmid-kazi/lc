# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 11/12/24) Tue) 1117 to 1124pm) tk)
        node = None
        while head:
            dummy = head.next
            head.next = node
            node = head
            head = dummy
        return node