class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    # Word Search - LeetCode
    # Time Complexity: O(m * n * 4^len(word)), Space Complexity: O(len(word))

    # 12/23/24) sun night) 209-212am) gtk) 12J

        def backtrack(r, c, index):
            if index == len(word):
                return True
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])) or board[r][c] != word[index]:
                return False
            temp, board[r][c] = board[r][c], '#'
            found = (backtrack(r + 1, c, index + 1) or backtrack(r - 1, c, index + 1) or
                    backtrack(r, c + 1, index + 1) or backtrack(r, c - 1, index + 1))
            board[r][c] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False