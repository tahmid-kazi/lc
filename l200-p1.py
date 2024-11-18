class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # foundational graph problem
        # use BFS
        # 11/18/24) 931-1001am) Mon) tk)
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        directions = [(1,0),(-1,0), (0,1), (0,-1)] # only define it once without having to redefine it 
         
        def bfs (r, c): # BFS section
            queue1 = deque()
            visited.add((r,c))
            queue1.append((r,c))
            while queue1:
                row, col = queue1.popleft()
                for dr, dc in directions:
                    r1, c1 = (row + dr), (col + dc)
                    if (r1 in range(rows) and 
                    c1 in range(cols) and 
                    grid[r1][c1] == "1" and 
                    (r1,c1) not in visited):
                        visited.add((r1, c1))
                        queue1.append((r1,c1))


        # main algorithm
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # runs BFS
                    bfs (r,c)
                    islands += 1
        return islands