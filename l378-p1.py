class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # use min heap (or a reverse max heap)
        max_heap = []
        # 11/19/24) Tue) 909-915pm) tk)
        for row in matrix:
            for num in row:
                heapq.heappush(max_heap, -num)
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
        # bruh this is so clever
        return -max_heap[0]