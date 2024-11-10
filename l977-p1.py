class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 11/10/24) 644-648pm) Sun) tk)
        nums1 = []
        for i in nums:
            nums1.append(i*i)
        return sorted(nums1)