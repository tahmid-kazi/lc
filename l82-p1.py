# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 11/12/24) 4:00-4:15pm) Tue) tk)
        #first set up the dummy node and attach it to head
        dummy = ListNode(0)
        dummy.next = head

        #now set up the current and prev nodes for traversal
        current = head
        prev = dummy

        while current:
            if current.next and current.val == current.next.val:
                # forgot this while loop
                while current.next and current.val == current.next.val: #kep traversing the current while the previous stays the same
                    current = current.next
                prev.next = current.next # got this correct (now just bypass the duplicate nodes)
            else:
                prev = current
            current = current.next
        
        return dummy.next
