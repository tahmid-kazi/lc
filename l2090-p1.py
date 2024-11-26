class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # sliding window + prefix sum
        # 11/25/24) Mon) tk) bbus) 802-809pm) last problem dome from meta last 30days list (169Q)
        n = len(nums)
        result = [-1] * n
        window_sum = 0
        window_size = 2*k+1

        for i in range(n):
            window_sum += nums[i]
            if i >= window_size:
                window_sum -= nums[i-window_size]
            if i >= window_size-1:
                result[i-k] = window_sum//window_size
        return result