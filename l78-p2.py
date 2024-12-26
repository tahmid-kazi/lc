class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       
        # 100-124pm (H1B tweets)
        # 12/26/24) 125-143pm) Thurs) tk) 12J) idgi) 
        res = [] 
        subset = []
        def create_subset(i):
            if i == len(nums):
                res.append(subset[:]) # once all subsets are explored, add to result array and return
                return
            subset.append(nums[i]) # start creating the subset
            create_subset(i+1) 
            subset.pop() # remove the previous subset to now work on the current subset
            create_subset(i+1) 
            # this function works on 2 possibilities at each step
        create_subset(0)
        return res
