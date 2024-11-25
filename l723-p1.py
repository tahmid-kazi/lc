class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows, cols = len(board), len(board[0]) # this is a matrix problem
        stable = False
        # 11/25/24) tk) Mon) 1051-1105am)
        while True:
            stable = True
            crushable = set()
            # part 1 = horizontal crushables
            for row in range(rows):
                for col in range(cols-2):
                    if board[row][col] == board[row][col+1] == board[row][col+2] != 0:
                        stable = False
                        crushable.update([(row, col), (row, col+1), (row, col+2)])
            # part 2 = vertical crushables
            for row in range(rows-2):
                for col in range(cols):
                    if board[row][col] == board[row+1][col] == board[row+2][col] != 0:
                        stable = False
                        crushable.update([(row, col), (row+1, col), (row+2, col)])
            if stable: # if board is stable, no candies to crush, return the board
                return board
            # step 4 = crush the candies by setting them to 0
            for row, col in crushable:
                board[row][col] = 0
            # step 5 = let the candies fall (gravity simulation)
            for col in range(cols):
                write_row = rows-1
                for row in range(rows-1, -1, -1):
                    if board[row][col] != 0:
                        board[write_row][col] = board[row][col]
                        write_row -= 1
                for row in range(write_row, -1, -1):
                    board[row][col] = 0
            