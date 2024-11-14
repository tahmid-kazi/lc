class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 11/13/24) Wed) 1037 - 1040pm) tk)
        set1 = set()
        for char in s:
            if char not in set1:
                set1.add(char)
            else:
                set1.remove(char)
        return (len(set1) <= 1)