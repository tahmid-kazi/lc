class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # 11/11/24) Mon) 220 to 234pm) tk)
        
        list_of_lists = []
        #base case
        if len(nums) == 0:
            return [[lower,upper]]
        
        # beginning case
        if lower < nums[0]:
            item1 = [lower, nums[0]-1]
            list_of_lists.append(item1)
        
        for j in range(0, len(nums)-1):
            
            #first check if the nums are consecutive
            if nums[j+1]-nums[j] <= 1:
                continue
            #else:
            list_of_lists.append([nums[j]+1, nums[j+1]-1])

        # last case    
        if upper > nums[len(nums)-1]:
            item2 = [nums[len(nums)-1]+1, upper]
            list_of_lists.append(item2)
        
        return list_of_lists
        
