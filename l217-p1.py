class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    # Contains Duplicate - LeetCode
    # Time Complexity: O(n), Space Complexity: O(n)

    # 12/23/24) mon) 604-608pm) gtk) last one)
        return len(nums) != len(set(nums))
