class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        result = []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

        # O(m * n) time, O(1) space
        # 12/20/24) tk) Thurs night) 237-257am)
        while top <= bottom and left <= right:
            # traverse from left to right in the top row
            for col in range(left, right+1):
                result.append(matrix[top][col])
            top += 1

            #traverse from top to bottom on the rightmost column
            for row in range(top, bottom+1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                # traverse from right to left on the bottom row
                for col in range(right, left-1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                # traverse from bottom to top on leftmost column
                for row in range(bottom, top-1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result