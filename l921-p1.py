class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # 11/11/24) Mon) 1130-1140pm) tk) 50th problem done!
        s = list(s)
        stack1 = []
        unmatched_closing = 0

        for j in s:
            if j == "(":
                stack1.append(j)
            elif j == ")":
                if stack1:
                    stack1.pop()
                else:
                    unmatched_closing += 1
            
        return len(stack1)+unmatched_closing