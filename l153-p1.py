class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search O(logn)
        left, right = 0, len(nums)-1
        # 12/18/24) tk) Wed) 428-451pm)
        while left < right:
            mid = (left+right)//2

            # example of a rotated sorted array:
            [ 3, 4, 5, 6, 1, 2]
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]
