class SeatManager:
    # 11/25/24 - Mon - tk - bbus - (755-802pm) 2nd to last Meta 169 list done
    # Binary Search: O(M∗N)
    # Binary Heap: O((M+N)∗Log(N))
    # Binary Heap with checkpoint: O(M∗Log(N)) (mine)
    def __init__(self, n: int):
        self.minimum = 1
        self.heap = []        

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        self.minimum += 1
        return self.minimum-1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)