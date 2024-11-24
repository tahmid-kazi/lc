class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # classic two pointers problem
        # 11/24/24) Sun) 216-222pm) tk) makerlab)
        # brute force is O(n^3), this is O(n^2)
        nums.sort() # O(n logn)
        closest_sum = float('inf')
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == target:
                    return curr_sum
                
                if abs(curr_sum-target) < abs(closest_sum-target):
                    closest_sum = curr_sum
                
                if curr_sum < target:
                    left+=1
                else:
                    right-=1

        return closest_sum