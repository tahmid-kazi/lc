class Solution:
    def countSubstrings(self, s: str) -> int:
        # similar to leetcode 5 - longest palindromic substring
        # this is from Blind 75
        # 11/19/24) Tue) 451-455pm) tk)
        res = 0
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]: #we found a odd length palindrome
                res += 1
                left -= 1
                right += 1 # spread out

            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]: #we found an even length palindrome
                res += 1
                left -= 1
                right += 1
        
        return res