class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 12/18/24) Wed) 834-840pm) tk)
        # this trick is insane
        # O(m*n) runtime, O(1) space
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1