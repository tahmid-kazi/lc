class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s is in t then return true
        # use 2 pointers, O(n) time
        # 12/18/24) tk) Wed) 504 to 507pm)
        s_ptr = t_ptr = 0 # its like a race between these 2 pointers
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1
        return s_ptr == len(s) # that means you made it to the end, meaning theres a valid subsequence
        