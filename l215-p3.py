class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # this is the most optimal solution
        # 12/25/24) 1129am) Wed) gtk) 
        # runtime O(nlog(k)), space: O(k) 

        # Maintain a min-heap of size k
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]
