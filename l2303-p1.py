class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # 11/24/24) Sun) 114-116pm) tk) makerlab) 2nd problem of the day
        tax = 0
        last_upper = 0
        for b in brackets:
            rate = b[1]/100
            upper = min(b[0], income)
            tax += (upper-last_upper) * rate
            last_upper = upper
        return tax