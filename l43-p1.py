class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 11/24/24) Sun) 155-157pm) tk) makerlab)
        a = b = 0
        for i in num1:
            a = a * 10 + (ord(i)-48)
        for k in num2:
            b = b * 10 + (ord(k)-48)

        return str(a*b)