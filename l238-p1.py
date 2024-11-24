class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # did this before, for google, blind 75
        # 11/24/24) Sun) 119-122pm) tk) makerlab)
        output = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= right
            right *= nums[i]
        
        return output