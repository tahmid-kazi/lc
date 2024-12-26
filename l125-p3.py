class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, skip spaces, punctuation and ignore uppercase
        # 1206 to 1232am) 12/26/24) Wed) tk)
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower(): #you forgot .lower()
                return False
            left +=1
            right -=1
        return True