class MovingAverage:
    
    # wait amazon asked me this back in July 2024!
    # try2 - most optimal code (O(1) runtime, O(k) space (k=size of window))
    # 12/25/24) Wed) 110pm) gtk)

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()
        return self.sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)