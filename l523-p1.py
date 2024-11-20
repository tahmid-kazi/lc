class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 918-935pm) 11/19/24) Tue) tk)
        remainders = {0:-1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k
            if remainder in remainders:
                if i-remainders[remainder] > 1: # this checks to see if its a valid index
                    return True
            else:
                remainders[remainder] = i
        
        return False 
        

        #subarray is contiguous, you'll never come across a subarray problem with multiple disjoint (non-adjacent) elements 
        # 11/19/24) Tue) 918 to 923pm) tk)
        # did this all on my own in the first try
        # for i in range(1,len(nums)):
        #     if (nums[i-1] + nums[i] % k == 0) or (sum(nums) % k == 0):
        #         return True
        # return False
