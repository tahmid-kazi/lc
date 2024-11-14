class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 11/13/24) Wed) 1138 to 1143pm) tk)
        nums.sort()
        return nums[len(nums)//2]