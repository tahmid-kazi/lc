# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 11/13/24) Wed) 1040 to 1046pm) tk)
        #binary search problem, two pointers
        first, last = 1, n
        while first < last:
            mid = first+(last-first)//2
            if isBadVersion(mid):
                last = mid
            else:
                first = mid+1
        return first