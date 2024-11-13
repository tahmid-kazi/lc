class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 11/13/24) Wed) 305 to 335pm) tk)
        rows = len(mat)
        cols = len(mat[0])
        result = []
        going_up = True
        row, col = 0, 0

        while len(result) != rows * cols:
            if going_up: #going up
                while row >= 0 and col < cols:
                    result.append(mat[row][col])
                    row -= 1 # move up
                    col += 1 # move to the right
                
                if col == cols:
                    col -= 1
                    row += 2
                else:
                    row += 1
                going_up = False
            else: #going down
                while row < rows and col >= 0:
                    result.append(mat[row][col])
                    row += 1 #move down
                    col -= 1 #move left
                if row == rows:
                    row -= 1
                    col += 2
                else:
                    col += 1
                going_up = True
        return result