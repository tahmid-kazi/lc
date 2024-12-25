class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 12/25/24) Wed) 1157am) gtk) 12J
        # most optimal code (O(n) time, O(1) space)

        # Two-pointer approach
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
