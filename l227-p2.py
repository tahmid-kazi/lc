class Solution:
    def calculate(self, s: str) -> int:
        # try stack based approach
        # try2 - 12/1/24) Sun) 422-430pm) tk)
        stack1 = []
        s = s.strip() # first get rid of any whitespaces
        num = 0
        operator = "+"
        for i in range(len(s)):
            char = s[i]
            # first check and construct the num
            if char.isdigit():
                num = num*10 + int(char)
            # now run the operations
            if char in "*/+-" or i == len(s)-1:

                # but first check the operators
                if operator == "+":
                    stack1.append(num)
                if operator == "-":
                    stack1.append(-num)
                if operator == "*":
                    stack1[-1] = stack1[-1]*num
                if operator == "/":
                    stack1[-1] = int(stack1[-1]/num)

                # set the operator
                operator = char
                num = 0
        return sum(stack1)
