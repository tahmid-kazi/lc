class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        sign_value = 1
        result = 0
        ops = []
        # 11/26/24) tue) 916-921am) ffx) tk)
        for c in s:
            if c.isdigit():
                number = number*10 + int(c)
            elif c in "+-":
                result += number*sign_value
                sign_value = -1 if c == '-' else 1
                number = 0
            elif c == "(":
                ops.append(result)
                ops.append(sign_value)
                result = 0
                sign_value = 1
            elif c == ")":
                result += sign_value * number
                result *= ops.pop()
                result += ops.pop()
                number = 0
        return result + number * sign_value