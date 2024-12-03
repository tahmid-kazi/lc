class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # this is binary search but with a twist: return middle or left pointer
        # 12/3/24 - Tue - tk - 1220 to 1225pm) 2F study room)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid-1
            if target > nums[mid]:
                left = mid+1
        return left  
        