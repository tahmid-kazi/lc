"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # bruh this is exact similar to leetcode 116 that I did yesterday
        # BFS, 11/21/24 - thurs) 1043-1048pm) tk)

        if not root:
            return
        head = root
        while head:
            temp = Node()
            cur = temp
            while head:
                if head.left:
                    cur.next = head.left
                    cur = cur.next
                if head.right:
                    cur.next = head.right
                    cur = cur.next
                head = head.next
            head = temp.next
        return root