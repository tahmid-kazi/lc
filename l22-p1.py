class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # DFS + classic backtracking problem
        # 11/24/24) 157-209pm) Sun) tk) makerlab)
        res = []
        def dfs_backtrack(current, open_count, close_count):
            if len(current) == 2*n:
                res.append(current)
                return
            
            if open_count < n:
                dfs_backtrack(current + "(", open_count+1, close_count)

            if close_count<open_count:
                dfs_backtrack(current + ")", open_count, close_count+1)
        dfs_backtrack("",0,0)
        return res