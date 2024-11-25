class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # use hashmap; 11/25/24) Mon) 1010-1022am) tk) 1st problem of the day done
        prefix_sums = {0:-1}
        current_sum = 0
        max_length = 0
        n = len(nums)

        for i in range(n):
            current_sum += nums[i]

            if current_sum == k:
                max_length = i+1

            if current_sum-k in prefix_sums:
                max_length = max(max_length, i-prefix_sums[current_sum-k])
            
            if current_sum not in prefix_sums:
                prefix_sums[current_sum] = i
        return max_length
