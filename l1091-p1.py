class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 11/11/24) Mon) 240-315pm) tk)
        n = len(grid) # its nxn so same length of row and cols
        # do a basic BFS (On^2, size of the grid)
        queue1 = deque([(0,0,1)]) # (row, col, length) 
        visited = set((0,0)) # the visited set
        eight_directions = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]

        while queue1:
            row, col, length = queue1.popleft()
            # out of bounds check
            # also check if its been visited and check if the current loc is valid    
            if (min(row, col) < 0 or max(row,col) >= n or grid[row][col]): 
                continue #just skip this position
            
            # check if you reached the end
            if row == n-1 and col == n-1:
                return length
            
            #otherwise, do the path by checking the neighbors
            # check the 8 directions
            for r2,c2 in eight_directions:
                if (row+r2,col+c2) not in visited:
                    queue1.append((row+r2, col+c2, length+1))
                    visited.add((row+r2, col+c2))
            
        return -1
        