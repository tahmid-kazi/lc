class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        # most optimal code: dynamic programming
        # O(n^2) time and O(n^2) space
        # 12/25/24) Wed) 119pm) gtk) 12J
        
        n = len(s)
        
        # Create a DP table to store lengths of longest palindromic subsequences
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the DP table
        for length in range(2, n + 1):  # Substring lengths from 2 to n
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # The length of the longest palindromic subsequence is in dp[0][n-1]
        lps_length = dp[0][n - 1]
        
        # Check if the number of deletions is within k
        return (n - lps_length) <= k
