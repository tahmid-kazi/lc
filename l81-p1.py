class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # very similar to Leetcode 33 - blind75, but may have DUPLICATES
        # basically binary search with extra checks for pivot and duplicates
        # 11/21/24-thurs) 1054-1106pm) tk)
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            # check for duplicates
            while mid < right and nums[right] == nums[mid]:
                right -= 1
            
            if nums[mid] <= nums[right]: # check for pivot point for rotation
                if nums[right] < target or target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target or target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False




        #this is the essence of binary search:
        # if target < right:
        #     right = mid
        # if target > mid:
        #     left = mid