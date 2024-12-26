class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # did it on my own (12/25/24)(918 to 930pm)(Wed) tk) 12J
        
        s = list(s)
        stack1 = []
        for i in range(len(s)):
            if s[i] == "(":
                stack1.append(i)
            if s[i] == ")":
                if stack1:
                    stack1.pop()
                else:
                    s[i] = ""
        while stack1:
            s[stack1.pop()] = ""
        return "".join(s)