class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
    # Excel Sheet Column Title - LeetCode
    # Time Complexity: O(log n), Space Complexity: O(1)
    # 12/22/24) Sun) 1150pm) gtk) 12J
        result = []
        while columnNumber:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))