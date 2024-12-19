class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # after pasta, 12/19/24) tk) Wed night) 220 to 227am)
        # runtime: O(M*N), space = O(1)
        if not board or not board[0]:
            return 0
        rows, cols = len(board), len(board[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    if r > 0 and board[r-1][c] == "X":
                        continue
                    if c > 0 and board[r][c-1] == "X":
                        continue
                    count +=1 
        return count 