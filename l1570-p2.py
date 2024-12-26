class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.len = len(nums)
    # 12/26/24) Thurs) 1100-1104am) tk) 12J
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum1 = 0
        for i in range(vec.len):
            sum1 += vec.nums[i] * self.nums[i] 
        return sum1
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)