class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # stared at in and did it on own (12/25/24)(Wed)(636/644-656pm) tk) 12J 
        minheap = nums[:k]
        heapq.heapify(minheap)
        for i in nums[k:]:
            if i > minheap[0]:
                heapq.heappushpop(minheap, i)
        return minheap[0]