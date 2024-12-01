class Solution:
    def calculate(self, s: str) -> int:
        # try3 - 12/1/24) tk) Sun) 516-524pm)
        result = 0 # no stack (O(n) space), now computing in place (O(1) space)
        operator = "+"
        num = 0
        last_val = 0
        s = s.strip()
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num*10 + int(char)
            if char in "*/+-" or i == len(s)-1:
                if operator == "+":
                    result += last_val #this is because * and / have higher precedence
                    last_val = num
                if operator == "-":
                    result += last_val
                    last_val = -num
                if operator == "*":
                    last_val *= num
                if operator == "/":
                    last_val = int(last_val/num)
                operator = char
                num = 0
        result += last_val
        return result