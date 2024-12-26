class MovingAverage:
    # 12/26/24) Thurs) 1221 to 1240pm) + notes + food) 12J)
    # 1240 to 1258pm) lunch done
    def __init__(self, size: int):
        self.queue1 = deque()
        self.sum = 0
        self.size = size # you forgot this

    def next(self, val: int) -> float:
        self.queue1.append(val)
        self.sum += val                 # you forgot this
        if len(self.queue1) > self.size:
            pp = self.queue1.popleft()
            self.sum -= pp
        return self.sum/len(self.queue1)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)