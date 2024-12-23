class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 12/20/24) Fri) 123-134pm) tk) try1
    
    # try2:
    # Palindrome Partitioning - Optimized
    # Time Complexity: O(n * 2^n), Space Complexity: O(n^2)

    # 12/23/24) gtk) sun night) 1231-1234am) 12J
        n = len(s)
        # Precompute palindrome substrings
        is_palindrome = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True

        def backtrack(start, path):
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if is_palindrome[start][end]:  # Use precomputed palindrome information
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        res = []
        backtrack(0, [])
        return res
