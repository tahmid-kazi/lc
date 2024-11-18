class Solution:
    def decodeString(self, s: str) -> str:
        # way simpler than leetcode 329
        # you can use DFS, but better way is to use stack
        # there should really be an until function, similar to a if/while/for

        # 11/18/24) 610/639-649pm) Mon) tk)

        stack1 = []

        for i in range(len(s)):
            if s[i] != "]":
                stack1.append(s[i])
            else:
                substring = ""
                while stack1[-1] != "[":
                    substring = stack1.pop() + substring #add the popped item to the front due to the stack reversal
                stack1.pop() #remove the opening bracket

                # now get the integer in front of the opening bracket
                k = ""
                while stack1 and stack1[-1].isdigit():
                    k = stack1.pop() + k
                
                stack1.append(int(k) * substring)
        
        return "".join(stack1) 