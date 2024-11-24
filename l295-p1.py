class MedianFinder:
    # 11/24/24) Sat night) 1246-108am) tk)
    def __init__(self):
        self.minheap = [] #for larger half
        self.maxheap = [] # for smaller half (invert numbers to use max heap)

    def addNum(self, num: int) -> None:
        if len(self.maxheap) == 0 or -self.maxheap[0] >= num:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        #balance heaps
        if len(self.maxheap) > len(self.minheap)+1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0])/2.0
        else:
            return -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()