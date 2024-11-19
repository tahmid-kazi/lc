class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 100th problem/Meta list
        # Union Find! wtf
        # 11/18/24) Mon) 1121-1144pm) tk)
        self.island_id = -1
        self.island_areas = {}

        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    island_area = self.dfs(grid, m, n)
                    self.island_areas[self.island_id] = island_area
                    self.island_id -= 1
        max_area = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if not grid[m][n]:
                    area = 1
                    surrounding = set()
                    for m_inc, n_inc in self.directions:
                        new_m = m + m_inc
                        new_n = n + n_inc
                        if (0 <= new_m < len(grid)) and (0 <= new_n < len(grid[0])) and grid[new_m][new_n] != 0:
                            surrounding.add(grid[new_m][new_n])
        
                    for island_id in surrounding:
                        area += self.island_areas[island_id]
                    max_area = max(max_area, area)
        return max_area if max_area else len(grid) ** 2
    
    def dfs(self, grid, m, n):
        if (0 <= m < len(grid)) and (0 <= n < len(grid[m])) and grid[m][n] == 1:
            grid[m][n] = self.island_id
            area = 1

            for m_inc, n_inc in self.directions:
                area += self.dfs(grid, m + m_inc, n + n_inc)
            return area
        else:
            return 0