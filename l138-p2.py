"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1137am - msg'd about 3d printer bed leveling
        # 12/26/24) thurs) 1122-1147am) tk) 12J
        if not head: return None
        hashmap = {}
        current = head
        while current: # first fill up the hashmap {Node:Node}
            hashmap[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            hashmap[current].next = hashmap.get(current.next)
            hashmap[current].random = hashmap.get(current.random)
            current = current.next
        return hashmap[head] # forgot this one

