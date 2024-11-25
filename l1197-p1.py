class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # theres an O(1) optimal way via math induction but for interviews just use BFS
        # 11/25/24) Sun night) 1231-1248am) tk)
        x, y = abs(x), abs(y)
        directions = [
            (2,1), (1,2), (-1,2), (-2,1), 
            (-2,-1), (-1,-2), (1, -2), (2,-1)
        ]
        queue1 = deque([(0,0,0)]) # (curr_x, curr_y, steps)
        visited = set((0,0))

        while queue1:
            curr_x, curr_y, steps = queue1.popleft()
            if curr_x == x and curr_y == y:
                return steps
            
            for dx, dy in directions:
                new_x, new_y = curr_x + dx, curr_y + dy
                if (new_x, new_y) not in visited and new_x >= -1 and new_y >= -1:
                    visited.add((new_x, new_y))
                    queue1.append((new_x, new_y, steps+1))
        return -1
