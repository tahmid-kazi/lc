class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Modify board in-place to solve the Sudoku puzzle.
        """

        # Sudoku Solver - Optimized
        # Time Complexity: O(n), Space Complexity: O(n)    

        # 12/23/24) sun night) 157-209am) gtk) 12J

        rows, cols, blocks = defaultdict(set), defaultdict(set), defaultdict(set)
        empty_cells = []

        # Initialize constraints and empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i // 3, j // 3)].add(board[i][j])
                else:
                    empty_cells.append((i, j))

        # Sort empty cells by the number of possibilities (MRV heuristic)
        def count_candidates(cell):
            r, c = cell
            block_key = (r // 3, c // 3)
            return len({'1', '2', '3', '4', '5', '6', '7', '8', '9'} - (rows[r] | cols[c] | blocks[block_key]))

        empty_cells.sort(key=count_candidates)

        def dfs(index=0):
            if index == len(empty_cells):
                return True  # All cells filled

            r, c = empty_cells[index]
            block_key = (r // 3, c // 3)

            for num in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                if num not in rows[r] and num not in cols[c] and num not in blocks[block_key]:
                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    blocks[block_key].add(num)

                    # Recurse to the next cell
                    if dfs(index + 1):
                        return True

                    # Backtrack
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    blocks[block_key].remove(num)

            return False

        dfs()
