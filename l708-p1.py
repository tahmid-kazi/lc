"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # 11/13/24) Wed) 528 to 600pm) tk)
        prop = Node(insertVal)
        # if its zero nodes
        if head is None:
            prop.next = prop
            return prop
        # if its only 1 node
        if head.next == head:
            head.next = prop
            prop.next = head
            return head
        # general case
        current = head
        while True:

            if current.val <= insertVal <= current.next.val:
                break
            
            if current.val > current.next.val:
                if insertVal >= current.val or insertVal <= current.next.val:
                    break
            
            current = current.next
        
            if current == head:
                break
            
        prop.next = current.next
        current.next = prop

        return head