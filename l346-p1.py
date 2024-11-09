class MovingAverage:
    
    # wait amazon asked me this back in July 2024!
    # 11/8/24) Fri) 1123 to 1136pm) tk)
    def __init__(self, size: int):
        self.queue = deque(maxlen=size)
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        return sum(self.queue)/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)