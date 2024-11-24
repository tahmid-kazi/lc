class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[""]*3 for _ in range(3)]
        for i in range(len(moves)):
            r,c = moves[i]
            board[r][c] = "A" if i % 2 == 0 else "B"
        # 11/24/24) Sun) 103-114pm) tk) makerlab)
        def check_winner(player):
            for r in range(3): # check rows
                if board[r][0] == player and board[r][1] == player and board[r][2] == player:
                    return True
            for c in range(3): #check cols
                if board[0][c] == player and board[1][c] == player and board[2][c] == player:
                    return True
            # check main diagonal
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            # check anti-diagonal
            if board[0][2] == player and board[1][1] == player and board[2][0] == player:
                return True
            return False
                    
        #main
        if check_winner("A"):
            return "A"
        if check_winner("B"):
            return "B"
        #else
        return "Draw" if len(moves) == 9 else "Pending"