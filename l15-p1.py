class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 11/13/24) 900/905-908pm) Wed) tk)
        # this problem is easy to understand
        nums.sort()
        temp = set()

        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1
            while j < k:
                tempsum = nums[i] + nums[j] + nums[k]
                if tempsum == 0:
                    temp.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif tempsum < 0:
                    j += 1
                else:
                    k -= 1
        result = list(temp)
        return result