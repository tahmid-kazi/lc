class Solution:
    def numDecodings(self, s: str) -> int:
        # did before for google/blind75 - aug/sept 2024
        # dynamic programming, probably wont be asked
        # O(n) time, O(1) space
        # 12/20/24) tk) thurs night) 349 to 357am) 
        if not s or s[0] == '0':
            return 0

        prev1, prev2 = 1, 1 # base cases
        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current += prev1
            if 10 <= int(s[i-1:i+1]) <= 26:
                current += prev2
            
            prev2, prev1 = prev1, current # update state
        return prev1