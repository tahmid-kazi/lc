class Solution:
    def reverse(self, x: int) -> int:
        # int to string to int 
        # wait I actually got it, this is easy
        # 12/17/24) Tue) 854 to 856pm) tk)
        sign = 0
        if x < 0: sign = -1
        else: sign = 1
        
        reversed_int = int(str(abs(x))[::-1])
        result = sign * reversed_int
        if reversed_int < -2**31 or reversed_int > 2**31-1:
            return 0
        return result