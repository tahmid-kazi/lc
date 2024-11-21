class Solution:
    def reverseWords(self, s: str) -> str:
        # 11/21/24) thurs) 530-532pm) tk)
        return " ".join(s.split()[::-1])