class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 11/13/24) 1100 to 1106pm) Wed) 
        string1 = str(x)
        if string1 == string1[::-1]:
            return True
        else:
            return False