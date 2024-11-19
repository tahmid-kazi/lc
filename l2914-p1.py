class Solution:
    def minChanges(self, s: str) -> int:
        # 11/18/24) Mon) 1017-1018pm) tk) 99th problem/Meta
        # basically all youre trying to do is get pairs of twins
        changes = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                changes += 1
        return changes