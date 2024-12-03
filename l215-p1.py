class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # submitted at Oct 07, 2024 23:57
        return sorted(nums, reverse=True)[k-1]
        # 10/3/24 1145pm