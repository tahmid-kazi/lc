# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Reverse Nodes in k-Group - LeetCode
    # Time Complexity: O(n), Space Complexity: O(1)

    # 12/23/24) sun night) 134-138am) gtk) 12J
        def reverse(head, k):
            prev, curr = None, head
            while k:
                next_temp = curr.next
                curr.next = prev
                prev, curr = curr, next_temp
                k -= 1
            return prev

        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            prev, curr = kth.next, group_prev.next
            for _ in range(k):
                next_temp = curr.next
                curr.next = prev
                prev, curr = curr, next_temp
            temp = group_prev.next
            group_prev.next = prev
            group_prev = temp