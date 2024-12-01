class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # round 2 - 12/1/24) Sun) 114-119pm) tk)
        s = list(s)
        stack1 = []

        for i in range(len(s)):
            if s[i] == "(":
                #opening bracket, add it to the stack
                stack1.append(i)
            if s[i] == ")":
                # closing bracket
                if stack1:
                    # if theres a corresponding opening bracket with this closed one, then pop from stack
                    stack1.pop()
                else:
                    # if theres no corresponding opening bracket, then just remove the ) from the string
                    s[i] = ""

        while stack1:
            # now if you have any extra ( left on the stack, remove them from the string
            # since we stored the index of the ('s on the stack, use that
            s[stack1.pop()] = ""
        
        return "".join(s)