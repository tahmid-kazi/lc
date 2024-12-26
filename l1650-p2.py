"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # 12/25/24) Wed) 949-953pm) tk) did it on own)
        tracker = set()
        while p:
            tracker.add(p.val)
            p = p.parent

        while q:
            if q.val in tracker:
                return q
            q = q.parent
        return None