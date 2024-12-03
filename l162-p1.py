class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # 10/9/24 644 to 652pm in starbucks on 35th st 5th ave!!
        # waiting for sk-ghc-2024
        # two pointers, start from the ends, meet in the middle
        left, right = 0, len(nums) - 1

        while left < right:
            #do the midpoint calculation 
            mid = left + ((right-left)//2)

            # basically this check is there to break the while loop
            if nums[mid] < nums [mid+1]:
                left = mid + 1
            
            else:
                right = mid
        
        return left