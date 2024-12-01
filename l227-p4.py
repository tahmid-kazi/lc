class Solution:
    def calculate(self, s: str) -> int:
        current, result, num, operator = 0, 0, 0, "+"
        # try4 - 12/1/24) tk) Sun) 531-549pm)
        for i in s+"+":
            if i.isdigit():
                num = num*10+int(i)
            if i in "*/+-":
                if operator == "+":
                    current += num
                if operator == "-":
                    current -= num
                if operator == "*":
                    current *= num
                if operator == "/":
                    current = int(current/num)
                
                if i in "+-":
                    result += current
                    current = 0

                operator = i
                num = 0
        return result