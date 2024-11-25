class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = [0] * 2
        
    # 11/25/24) tk) Mon) 1022-1029am)
    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col: 
                self.diagonal[0] += 1
            if row+col == self.n-1:
                self.diagonal[1] += 1
            if self.row[row] == self.n or self.col[col] == self.n or self.diagonal[0] == self.n or self.diagonal[1] == self.n:
                return 1
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col: 
                self.diagonal[0] -= 1
            if row+col == self.n-1:
                self.diagonal[1] -= 1
            if self.row[row] == -self.n or self.col[col] == -self.n or self.diagonal[0] == -self.n or self.diagonal[1] == -self.n:
                return 2
        return 0
            



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)