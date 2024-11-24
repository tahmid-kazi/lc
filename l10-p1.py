class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # this is dynamic programming as well, probably wont be asked
        # 310am-318am) 11/24/24) Sat night) 
        m, n = len(s), len(p)
        cache = [[False] * (n+1) for _ in range(m+1)]
        cache[0][0] = True
        for j in range(2, n+1):
            if p[j-1] == "*":
                cache[0][j] = cache[0][j-2]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == "*":
                    cache[i][j] = cache[i][j-2] or ( cache[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                else:
                    cache[i][j] = cache[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        return cache[m][n]