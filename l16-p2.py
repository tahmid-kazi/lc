# -------------------------------------------------------------------
# ------------------ TWO POINTER IS THE BEST SOLUTION ---------------
# -------------------------------------------------------------------


# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         # classic two pointers problem
#         # 11/24/24) Sun) 216-222pm) tk) makerlab)
#         # brute force is O(n^3), this is O(n^2)
#         nums.sort() # O(n logn)
#         closest_sum = float('inf')
        
#         for i in range(len(nums)-2):
#             left, right = i+1, len(nums)-1
            
#             while left < right:
#                 curr_sum = nums[i] + nums[left] + nums[right]

#                 if curr_sum == target:
#                     return curr_sum
                
#                 if abs(curr_sum-target) < abs(closest_sum-target):
#                     closest_sum = curr_sum
                
#                 if curr_sum < target:
#                     left+=1
#                 else:
#                     right-=1

#         return closest_sum




# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         # 11/24/24) Sun) tk) 222-254pm) makerlab)
#         def backtrack(start, k, target):
#             if k==1:
#                 closest = nums[start]
#                 for i in range(start, len(nums)):
#                     if abs(nums[i]-target) < abs(closest-target):
#                         closest = nums[i]
#                 return closest

#             closest = float('inf')

#             for i in range(start, len(nums)-k+1):
#                 if i > start and nums[i] == nums[i-1]:
#                     continue # skip duplicates
                
#                 current = backtrack(i+1, k-1, target-nums[i]) + nums[i]

#                 if abs(target-current) < abs(target-closest):
#                     closest = current
#                 if closest == target:
#                     return closest
#             return closest

#         return backtrack(0, 3, target) # 3Sum closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current
        
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i>0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest
        # this is the most optimal solution, figure it out later