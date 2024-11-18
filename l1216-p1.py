class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # uses DFS/recursion + 2 pointers + DP/memoization
        # reuse the palindrome checker from Leetcode 680
        # 11/18/24) Mon) 417 to 440pm) tk)
        self.string = s
        if not k:
            return self.isPalindrome(0, len(s)-1)
        
        memoization = {}
        def helper(left, right, k):
            if (left,right,k) in memoization: # means we encountered it before
                return memoization[(left,right,k)]
            # 2 more edge cases left
            elif not k: #that means we used up all of our deletions quota
                memoization[(left,right,k)] = self.isPalindrome(left, right)
            else: # this is the main case
                while left < right:
                    if self.string[left] != self.string[right]:
                        memoization[(left,right,k)] = helper(left+1, right, k-1) or helper(left, right-1, k-1) # removing the left side makes a palindrome or removing the right side makes a palindrome
                        return memoization[(left, right, k)]
                    #else
                    left += 1
                    right -= 1
                memoization[(left,right,k)] = True
            return memoization[left, right, k]

        return helper(0, len(self.string)-1, k)
    
    def isPalindrome(self, left, right):
        while left < right:
            if self.string[left] != self.string[right]:
                return False
            left += 1
            right -= 1
        return True