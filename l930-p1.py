class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # sliding window (O(n) time and O(1) space) 
        # is more efficient than prefix sum + hashmap (O(n) time and 0(n) space)

        # 1015/1030 to 1040pm) tk) Thurs) 12/19/24)
        # this is sliding window (O(n) time and O(1) space) 
        def atMost(nums, goal):
            tail = total = result = 0
            for head in range(len(nums)):
                total += nums[head]
                while total > goal and tail <= head:
                    total -= nums[tail]
                    tail += 1
                result += head-tail+1
            return result
        return atMost(nums, goal)-atMost(nums, goal-1)
