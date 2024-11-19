class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        dict1 = defaultdict(list)
        # 11/19/24) Tue) 113/120-123pm) tk)
        for i in range(len(nums)):
            dict1[nums[i]].append(i)
            
        if target in dict1:
            idx = dict1[target]
            return [idx[0], idx[-1]]
        return [-1,-1]