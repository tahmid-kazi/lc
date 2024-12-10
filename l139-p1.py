class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # this is DP theyre not gonna ask this
        cache = [True] + [False] * len(s)
        # 12/09/24) 1109 - 1121pm) tk) Mon) t115)
        for i in range(1, len(s)+1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and cache[start] and s[start:i] == w:
                    cache[i] = True
                    break
        return cache[-1]