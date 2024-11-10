class Solution:
    def calculate(self, s: str) -> int:
        # 11/10/24) Sun) 240-335pm) tk)
        # tried iterative approach but this is incorrect
        # now going to try the stack-based approach
        s = s.strip() #first get rid of whitespaces
        parts = []
        current_num = ""
        for j in s:
            #first you want to seperate the operators and the numbers
            if j.isdigit(): #its a number
                current_num += j
            elif j in "+-*/": #its an operator
                if current_num:
                    parts.append(current_num)
                    current_num = ""
                parts.append(j) #add the operator
        
        if current_num:
            parts.append(current_num)
        #print(parts)

        final_num = int(parts[0])
        temp_num = 0
        #now run the operation
        for k in range(1, len(parts), 2):
            operator = parts[k]
            next_num = int(parts[k+1])
            if operator == "*":
                final_num *= next_num
            elif operator == "/":
                final_num = int(final_num/next_num)
            elif operator == "+":
                final_num += next_num
            elif operator == "-":
                final_num -= next_num
        return final_num
        