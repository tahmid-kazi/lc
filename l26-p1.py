class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 11/5/24) Tue) 754 to 800am) tk)
        unique_nums = 1
        i = 1 

        while i < len(nums):

            if nums[i] == nums[i-1]: #because its a sorted array
                del nums[i] # remove in-place
            else:
                unique_nums += 1
                i += 1
        return unique_nums