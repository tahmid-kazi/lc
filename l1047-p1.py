class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 11/12/24) Tue) 927/934 to 939pm) tk)
        stack1 = []
        for i in s:
            if stack1 and i == stack1[-1]:
                stack1.pop()
            else:
                stack1.append(i)
        return "".join(stack1)    