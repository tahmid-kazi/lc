class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 11/7/24) tk) Thurs) 1130 to 1145pm)
        # first handle negative case for n (i.e. 1/x)
        if n < 0:
            x = 1/x
            n = -n #flip it to (+) for the rest of the computation
        
        res = 1 #placeholder
        for j in range(n): # if 2^4, that means multiply 2 by itself 4 times
            res *= x #multiply by itself (O(n) runtime)
        
        return res