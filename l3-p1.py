class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window + set()
        # 11/21/24 - thurs) 1048-1054pm) tk)
        # this is basically what I got in my Amazon SDE II interview (July 2024) (L3 & L219)
        left = max_len = 0
        charset = set()
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len