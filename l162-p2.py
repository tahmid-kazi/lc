class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # most optimal code: binary search
        # runtime: O(log(n)), space: O(1)
        # 12/25/24) wed) 1142am) gtk)
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # Compare mid with the next element
            if nums[mid] > nums[mid + 1]:
                # Peak is on the left side or at mid
                right = mid
            else:
                # Peak is on the right side
                left = mid + 1
        
        return left
