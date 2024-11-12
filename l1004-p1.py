class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 11/11/24) Mon) tk) 912/921-942pm)
        # subarray problem, two pointer/sliding window approach
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0: # this if statement keeps iterating until k is no longer < 0!
                if nums[left] == 0:
                    k += 1    
                left += 1
        return right - left + 1