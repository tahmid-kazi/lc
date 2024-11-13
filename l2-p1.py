# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 11/13/24) Tue) 353 to 408pm) tk)
        list1, list2 = [], []
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next
        
        int1 = int("".join(list1[::-1]))
        int2 = int("".join(list2[::-1]))
        total = int1 + int2
        
        # reverse again and turn it back into linked list
        dummy = ListNode(0)
        current = dummy
        for i in str(total)[::-1]:
            current.next = ListNode(int(i))
            current = current.next
        return dummy.next