class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 11/10/24) Sun) 530 to 557pm) tk)
        # ues the two-pointer approach
        last_zero = 0
        i = 0

        while i < len(nums):
            if nums[i] != 0:
                nums[last_zero], nums[i] = nums[i], nums[last_zero] #simultaneous swapping, this is the key trick
                last_zero += 1 #last zero only increments by 1 because the magic of this swapping makes sure its always in the path of a zero
            i+=1
