# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 11/14/24) Thurs) 915 to 929pm) tk) (still in makerlab!)
        # g14 laptop
        min_heap = []
        for l in lists:
            if l: #fill the minheap
                heapq.heappush(min_heap, (l.val, id(l), l)) # revisit
        dummy = ListNode()
        current = dummy
        while min_heap:
            val, _, node = heapq.heappop(min_heap) #pop from the heap
            current.next = node #and add it to the linkedlist
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, id(node.next), node.next))
        return dummy.next