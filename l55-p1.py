class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Optimal code, Greedy (O(n))
        # 12/17/24) tk) Tue) 927 to 936pm) 
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i+nums[i])

            if max_reachable >= len(nums)-1:
                return True
        return False