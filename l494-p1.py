class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # similar to leetcode 282 - expression add operators
        # use decision tree here (recursion tree/backtracking) + DP cache (FFS another dynamic programming problem)
        
        # 11/18/24) 650-710pm) Mon) tk)
        cache = {} #(index, total) -> number of expressions you can build
        def dfs_backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in cache: #if you found the value
                return cache[(i, total)]
            
            cache[(i,total)] = (dfs_backtrack(i+1, total+nums[i]) + dfs_backtrack(i+1, total-nums[i])) # revisit
            return cache[(i,total)]

        return dfs_backtrack(0,0)