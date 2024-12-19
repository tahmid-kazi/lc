class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS + graphs, similar to L200/blind75 classic/foundational graph problem
        # time: O(m * n), Space: O(m * n)
        # 12/19/24) Wed night) tk) 227 to 242am)
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c]==0:
                return 0 #all edge cases covered
            grid[r][c] = 0
            area = 1
            area += dfs(r+1, c) #down
            area += dfs(r-1, c) # up
            area += dfs(r, c+1) # right
            area += dfs(r, c-1) # left
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        return max_area
        