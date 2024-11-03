class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # process:
        # construct a stack and make the input str a list
        # fill the stack with a net "(",
        # then once entire string is traversed, delete the extra "("
        # then return the string 

        # 11/2/24) Sat) 620-645pm) tk)

        stack1 = []
        s = list(s)

        for i in range(len(s)):
            if s[i] == "(":
                stack1.append(i)
            if s[i] == ")":
                if stack1:
                    stack1.pop()
                else:
                    s[i] = ''
        
        while stack1:
            s[stack1.pop()] = ''
        
        return "".join(s)
        
