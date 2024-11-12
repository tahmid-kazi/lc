class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 11/11/24) Mon) 734-804pm) tk)
        n = len(nums)
        pivot = 0
        for i in range(n-1, 0, -1): # find the pivot point
            if nums[i-1] < nums[i]:
                pivot = i-1
                break
        else: # if no pivot point found, just reverse the list
            nums = nums.reverse()
            return
        # now that you have the pivot, do the swap
        swap = n-1
        while nums[swap] <= nums[pivot]:
            swap -= 1    
        nums[pivot], nums[swap] = nums[swap], nums[pivot]
        # huh
        nums[pivot+1:] = reversed(nums[pivot+1:])
        return