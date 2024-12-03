# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 10/7/24 1133 to 1152pm (i dont get it)
        dummy = ListNode(0,head) #the next is set to the head

        left = dummy
        right = head

        # first create the distance between left and right
        while n > 0 and right != None:
            right = right.next
            n-=1
        
        # now move the 2 pointers together
        while right != None:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        
