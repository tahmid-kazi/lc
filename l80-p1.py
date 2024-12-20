class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        # O(n) time, O(1) space
        # 12/20/24) Thurs night) tk) 320 to 325am)
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+= 1
        return k
        