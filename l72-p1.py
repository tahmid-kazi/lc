class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Edit Distance - LeetCode
        # Time Complexity: O(m * n), Space Complexity: O(min(m, n))

        # 12/22/24) Sun night) 1159pm-1200am) gtk) 12J

        m, n = len(word1), len(word2)
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m

        prev = list(range(n + 1))
        for i in range(1, m + 1):
            curr = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
            prev = curr
        return prev[-1]