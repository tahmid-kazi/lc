class Solution:
    def isMatch(self, s: str, p: str) -> bool:
    # Wildcard Matching - Optimized x2
    # Time Complexity: O(s * p), Space Complexity: O(1)
    # two pointer approach is the most optimal!

    # 12/23/24) Sun night) 138-149am) gtk) 12J
        s1, p1, mat, star_idx = 0, 0, 0, -1

        while s1 < len(s):
            if p1 < len(p) and (p[p1] == '?' or p[p1] == s[s1]):
                s1 += 1
                p1 += 1
            elif p1 < len(p) and p[p1] == '*':
                star_idx = p1
                mat = s1
                p1 += 1
            elif star_idx != -1:
                p1 = star_idx + 1
                mat += 1
                s1 = mat
            else:
                return False

        while p1 < len(p) and p[p1] == '*':
            p1 += 1

        return p1 == len(p)


