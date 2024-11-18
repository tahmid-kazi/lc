class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DFS + DP memoization (an easier Leetcode Hard) (probably won't show up)
        # 11/18/24) Mon) 543/550-610pm) tk)
        rows, cols = len(matrix), len(matrix[0])
        cache = {} # r,c -> longest increasing path

        def dfs(r,c, previous):
            if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= previous:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            result = 1
            result = max(result, 1 + dfs(r+1, c, matrix[r][c])) #down
            result = max(result, 1 + dfs(r-1, c, matrix[r][c])) #up
            result = max(result, 1 + dfs(r, c+1, matrix[r][c])) #right
            result = max(result, 1 + dfs(r, c-1, matrix[r][c])) #left
            cache[(r,c)] = result
            return result

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,-1)
        return max(cache.values()) #this can be optimized