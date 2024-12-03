class SparseVector:
    # submitted at Oct 10, 2024 20:58
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.len = len(nums)

    def dotProduct(self, vec: 'SparseVector') -> int:

        sum1 = 0
        for i in range(vec.len):
            sum1 += self.nums[i] * vec.nums[i]        
        return sum1

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)