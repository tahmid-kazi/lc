class Solution:
    def validPalindrome(self, s: str) -> bool:

        # 10/9/24, 718 to 730pm, Wed, still at Starbucks
        def check_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                check_left = check_palindrome(left, right-1)
                check_right = check_palindrome(left+1, right)
                return check_left or check_right
            left += 1
            right -= 1
        return True