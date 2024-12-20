class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking, time O(n*2^n), space O(n) 
        # 12/20/24) Fri) 123-134pm) tk)
        def is_palindrome(sub):
            return sub == sub[::-1]
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:]) # store copy of current list
                return
            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):
                    path.append(s[start:end+1]) #choose
                    backtrack(end+1, path) #explore
                    path.pop()
        result = []
        backtrack(0, [])
        return result