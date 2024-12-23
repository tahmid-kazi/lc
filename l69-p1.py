class Solution:
    def mySqrt(self, x: int) -> int:        
    # Sqrt(x) - LeetCode
    # Time Complexity: O(log x), Space Complexity: O(1)

    # 12/22/24) gtk) Sun) 1158-1159pm) 12J
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right