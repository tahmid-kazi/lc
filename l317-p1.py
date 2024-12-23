class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
    # Shortest Distance from All Buildings - LeetCode - optimized
    # Time Complexity: O(k * m * n), Space Complexity: O(m * n)

    # 12/23/24) Sun night) 1240am/131-134am) gtk) 12J

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        distances = [[0] * n for _ in range(m)]
        reachable = [[0] * n for _ in range(m)]
        building_count = 0  # Count of buildings in the grid

        # Multi-source BFS initialization
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    building_count += 1
                    queue = deque([(r, c, 0)])  # Start BFS from this building
                    visited = [[False] * n for _ in range(m)]
                    visited[r][c] = True

                    while queue:
                        x, y, dist = queue.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                                visited[nx][ny] = True
                                distances[nx][ny] += dist + 1
                                reachable[nx][ny] += 1
                                queue.append((nx, ny, dist + 1))

        # Find the minimum distance to all buildings
        min_distance = float('inf')
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and reachable[r][c] == building_count:
                    min_distance = min(min_distance, distances[r][c])

        return min_distance if min_distance != float('inf') else -1