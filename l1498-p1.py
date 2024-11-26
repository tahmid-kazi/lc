class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # sorting + 2 pointers
        # 11/25/24) tk) bbus) Mon) 748-755pm)
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        left, right = 0, n-1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += pow(2, right-left, mod) # compute on the fly, O(1) memory efficient vs O(n) if you stored precomputes
                left += 1
        return ans%mod
