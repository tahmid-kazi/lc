class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # classic subarray
        # from blind 75 (this is where I got the roman to integer list back in august)
        # 11/20/24) 1041-1047pm) Wed) tk)
        res = nums[0]
        total = 0
        for n in nums:
            if total < 0:
                total = 0
            total += n
            res = max(res, total)
        return res