# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # floyd's tortoise and hare, O(N) time, O(1) space, most optimal and answers the O(1) followup question
        # 614/628 - 639pm) 12/21/24) sat) tk)
        # step 1 = detect if a cycle exists
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break # cycle detected
        else:
            return None # no cycle
        
        # step 2 = find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow