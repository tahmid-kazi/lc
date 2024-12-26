class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 12/25/24) wed) 1112/1124-1131pm) tk)
        if n < 0:
            x = 1/x
            n = -n
        res = 1
        while n > 0: # you forgot the while loop
            if n % 2 == 1: #this is meant as the final step
                res *= x
            x *= x
            n //= 2
        return res