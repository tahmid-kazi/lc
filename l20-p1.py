class Solution:
    def isValid(self, s: str) -> bool:
        # submitted at Oct 09, 2024 00:56
        stack1 = []
        bracket_map = {
            ")":"(",
            "}":"{",
            "]":"[", #the key is the CLOSING bracket not the opening one!!
        }

        for i in s:
            if i in bracket_map.values():
                stack1.append(i)
            if i in bracket_map.keys():
                if not(stack1 and bracket_map[i] == stack1.pop()):
                    return False

        #after all is said and done, return based on the state of the stack
        if stack1:
            return False
        else:
            return True
            