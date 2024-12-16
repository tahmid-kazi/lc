class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # DP/memoization + backtracking is O(n*k) 
        wordset = set(wordDict)
        memo = {}
        # 12/16/24) Mon) 1204-1212pm) tk)  
        def dfs(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return [""]
            result = []
            for end in range(index+1, len(s)+1):
                word = s[index:end]
                if word in wordset:
                    sub_sentence = dfs(end)
                    for sub in sub_sentence:
                        if sub:
                            result.append(word + " " + sub)
                        else:
                            result.append(word)
            memo[index] = result
            return result
        return dfs(0)