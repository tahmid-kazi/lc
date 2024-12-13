class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 12/12/24 - Thurs - 809 to 818pm) makerlab) tk)
        left = 0
        right = len(nums)-1
        # basically use modified binary search
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            # determine if the left side is sorted
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                # means right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
