class Solution:
    def longestPalindrome(self, s: str) -> str:
        # manacher algorithm is the most optimal (time, space = O(n), O(n))
        # using two pointers (O(n^2), space = O(1)), brute force is O(n^3)

        if not s:
            return ""
        # 11/24/24) Sun) tk) 254-305pm) makerlab)
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right-left-1
        
        start, end = 0, 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i+1)
            max_len = max(odd, even)

            if max_len > end-start:
                start = i - (max_len-1)//2
                end = i + max_len//2
        return s[start:end+1]