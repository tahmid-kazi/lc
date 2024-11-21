class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bruh dynamic programming (meta probably wont ask this)
        # 1047-1052pm) 11/20/24) Wed) tk)
        aboveRow = [1] * n
        for _ in range(m-1):
            currRow = [1] * n
            for i in range(1, n):
                currRow[i] = currRow[i-1] + aboveRow[i]
            aboveRow = currRow
        return aboveRow[-1]