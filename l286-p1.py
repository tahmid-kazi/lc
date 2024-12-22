class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Djikstra (O(nm*logm) time, O(nm) space) vs BFS (O(nm) time, O(nm) space)
        # this is BFS (more optimal)
        # 12/21/24) 1129/1139 - 1150pm) tk) Sat)
        if not rooms or not rooms[0]:
            return
        
        rows, cols = len(rooms), len(rooms[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue1 = deque()

        # add all gates (0's) to the queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue1.append((r,c))
        
        # run BFS for all gates
        while queue1:
            r,c = queue1.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc]  = rooms[r][c] + 1
                    queue1.append((nr,nc))
