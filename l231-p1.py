class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 11/13/24) Wed) 1031-1037pm) tk)
        for i in range(0,31,1):
            ans = 2 ** i
            if ans == n:
                return True
        return False
        