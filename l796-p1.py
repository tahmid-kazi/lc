class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 11/14/24) Thurs) 130 - 139pm) tk)
        if len(s) == len(goal) and (s+s).find(goal) != -1:
            return True
        else:
            return False