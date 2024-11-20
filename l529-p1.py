class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,1), (1,1), (1,-1), (-1,-1)]

        # (945/1030pm - 1041pm) 11/19/24) Tue) tk)
        def dfs(r,c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != "E":
                return
            
            mine_count = sum(0 <= r+dr < rows and 0 <= c+dc < cols and board[r+dr][c+dc] == "M" for dr, dc in directions)

            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for dr, dc in directions:
                    dfs(r+dr, c+dc)
        
        click_r, click_c = click
        if board[click_r][click_c] == 'M':
            board[click_r][click_c] = 'X'
        else:
            dfs(click_r, click_c)

        return board        