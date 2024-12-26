class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # textbook binary search
        # 12/25/24) 1040-1045pm) Wed) tk) 
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left