class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
    # Contiguous Array - LeetCode
    # Time Complexity: O(n), Space Complexity: O(n)
    
    # 12/23/24) Sun night) 1201 to 1204am) gtk) 12J
    
        count = 0
        max_len = 0
        table = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in table:
                max_len = max(max_len, i - table[count])
            else:
                table[count] = i
        return max_len