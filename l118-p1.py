class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    # Pascal's Triangle - LeetCode
    # Time Complexity: O(n^2), Space Complexity: O(n^2)
    
    # 12/23/24) gtk) 1211 to 1213am) Sun night) 12J
    
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res

