class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # 11/11/24) Mon) 1118 to 1126pm) tk)
        # you can use the O(n^2) approach
        row, col = len(matrix), len(matrix[0])

        for r in range(1, row):
            for c in range(1, col):
                if matrix[r-1][c-1] != matrix[r][c]:
                    return False

        return True