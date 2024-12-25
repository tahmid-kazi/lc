class Solution:
    def validPalindrome(self, s: str) -> bool:

        # most optimal code
        # 12/25/24) Wed) 1132am) gtk) 12J
        # O(n) runtime, O(1) space

        def is_palindrome_range(left: int, right: int) -> bool:
            """Check if s[left:right+1] is a palindrome."""
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # If mismatch, check the two possible substrings by skipping one character
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1

        return True
