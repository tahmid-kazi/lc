class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dont use the frequency count, use the Dutch national flag algorithm (3 pointers)
        # 11/24/24) Sun) 130-137pm) tk) makerlab)
        low, mid, high = 0, 0, len(nums)-1
        while mid<= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1