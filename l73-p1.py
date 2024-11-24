class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_col_zero, first_row_zero = False, False
        # 11/24/24) Sun) 148-155pm) tk) makerlab)
        for c in range(cols): 
            if matrix[0][c] == 0: # check if first row contains zero
                first_row_zero = True
                break
        for r in range(rows):
            if matrix[r][0] == 0: # check if first col contains zero
                first_col_zero = True
                break
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols): # set marked rows as zero
                    matrix[r][c] = 0

        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1,rows): # set marked cols as zero
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
