class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # 11/24/24) Sat) 108-119am) tk)
        rows, cols = len(grid), len(grid[0])
        row_counts, col_counts = [0]*rows, [0]*cols
        houses = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
                    houses.append((r,c))
        h = len(houses)

        def find_mid(counts):
            target = ceil(h/2)
            seen = 0
            for i in range(len(counts)):
                seen += counts[i]
                if seen >= target:
                    return i
        
        meet_r, meet_c = find_mid(row_counts), find_mid(col_counts)
        return sum(abs(r-meet_r) + abs(c-meet_c) for r,c in houses)