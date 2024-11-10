class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip() 
        
        #stack-based approach (11/10/24) (Sun) (335 to 405pm) tk)
        operator = "+"
        num = 0
        stack1 = []
        for j in range(len(s)):
            char = s[j]
            if char.isdigit():
                num = 10*num + int(char)
            if char in "*/+-" or j == len(s)-1:
                
                #check the operators
                if operator == "+":
                    stack1.append(num)
                if operator == "-":
                    stack1.append(-num)
                
                if operator == "*":
                    # for multiply and divides, run the operation immediately
                    stack1[-1] = stack1[-1]*num
                    
                if operator == "/":
                    stack1[-1] = int(stack1[-1]/num)
                    
                #set the operator
                operator = char
                num = 0
        return sum(stack1)

            