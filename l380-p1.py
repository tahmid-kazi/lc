class RandomizedSet:
    # 11/17/24) Sun) 808/822-830pm) Sun) tk)
    def __init__(self):
        self.list1 = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.list1.append(val)
        self.index_map[val] = len(self.list1)-1
        return True
    
    def remove(self, val: int) -> bool: 
        if not val in self.index_map:
            return False
        index = self.index_map[val]
        self.list1[index] = self.list1[-1]
        self.index_map[self.list1[-1]] = index
        self.list1.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list1)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()