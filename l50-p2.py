class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 11/7/24) tk) Thurs) 1130 to 1155pm)
        # first handle negative case for n (i.e. 1/x)
        if n < 0:
            x = 1/x
            n = -n #flip it to (+) for the rest of the computation
        
        res = 1 
        while n > 0:
            #res *= x #multiply by itself (O(n) runtime)

            #exponentiation by squaring (O(log(n)))
            if n%2 == 1:
                res *= x
            x *= x
            n //= 2

        return res