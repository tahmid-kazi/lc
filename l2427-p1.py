class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # 11/24/24) Sun) 116-119pm) tk) makerlab)
        count = 0
        temp = min(a,b)
        for i in range(1, temp+1):
            if a%i==0 and b%i==0:
                count += 1
        return count