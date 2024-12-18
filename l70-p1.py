class Solution:
    def climbStairs(self, n: int) -> int:
        # foundational dynamic programming problem, basically fibonacci
        # 12/17/24) tk) Tue) 936/946 - 948pm) 
        memo = {1:1, 2:2}
        def dp(num):
            if num in memo:
                return memo[num]
            else:
                memo[num] = dp(num-1) + dp(num-2)
                return memo[num]
        return dp(n)