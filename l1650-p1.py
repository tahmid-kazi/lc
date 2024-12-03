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

        # 10/11/24 - 1204 to 1218am) (thurs night) 
        # set-based approach         
        tracker = set()

        while p:
            tracker.add(p)
            p = p.parent
        
        while q:
            if q in tracker:
                return q
            q = q.parent
