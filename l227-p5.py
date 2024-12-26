class Solution:
    def calculate(self, s: str) -> int:
        # (958-1008pm)+(1018pm-1029pm)(12/25/24)(Tue)
        current, result, operator, num = 0, 0, "+", 0
        for i in s+"+": #this last "+" is to ensure that the last number gets computed
            if i.isdigit():
                num = num*10 + int(i)
            if i in "*/+-":
                if operator == "+":
                    current += num
                if operator == "-":
                    current += -num
                if operator == "*":
                    current *= num
                if operator == "/":
                    current = int(current/num)

                if i in "+-":
                    result += current
                    current = 0

                operator = i #now you set the operator so that its used for the next number (thats why we added the "+" in the end)
                num=0 # reset it for next computation
        return result