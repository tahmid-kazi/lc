class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window + hashmap
        # 11/15/24) Fri) 738 to 804pm) tk)
        # build a hashmap of char frequencies in t
        freq_count_t = {}
        for i in t:
            if i in freq_count_t:
                freq_count_t[i] += 1
            else:
                freq_count_t[i] = 1
        
        # now run the sliding window
        left, right = 0, 0
        window_count = {}
        formed = 0
        min_len = float('inf')
        result = [0,0] # the two indices to make the substring

        while right < len(s):
            char = s[right]
            if char in window_count:
                window_count[char] += 1
            else:
                window_count[char] = 1
            
            if char in freq_count_t and freq_count_t[char] == window_count[char]:
                formed += 1

            # now run the shrinking logic
            t_count = len(freq_count_t)
            while left <= right and formed == t_count:
                char = s[left]

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = [left, right]
                
                window_count[char] -= 1
                if char in freq_count_t and window_count[char] < freq_count_t[char]:
                    formed -= 1

                left += 1
            right += 1
        start, end = result
        return "" if min_len == float('inf') else s[start:end+1]