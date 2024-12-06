class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 10/3/24 1220 to 1230am
        return sorted(s) == sorted(t)

        # bruh, all of this is unnecessary if you just sort it!

        # char_freq_s = {}
        # char_freq_t = {}

        # for i in s:
        #     if i not in char_freq_s:
        #         char_freq_s[i] = 1
        #     else:
        #         char_freq_s[i] += 1
        
        # for j in t:
        #     if i not in char_freq_t:
        #         char_freq_t[j] = 1
        #     else:
        #         char_freq_t[j] += 1
        
        # if len(char_freq_s) != len(char_freq_t):
        #     return False
        