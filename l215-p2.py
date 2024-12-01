# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # 10/9/24 (1256 - 101am) (Tue night)
#         return sorted(nums, reverse=True)[k-1]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # try2 - tk) Sun) 12/1/24) 610-612pm)
        heap1 = heapq.nlargest(k, nums)[-1]
        return heap1