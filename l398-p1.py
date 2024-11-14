class Solution:
    # 11/14/24) Thurs) 1240 to 1245pm) tk)
    def __init__(self, nums: List[int]):
        self.idx_tracker = defaultdict(list)
        idx = 0
        for j in nums:
            self.idx_tracker[j].append(idx) #fill up a dictionary of all the unique values in the array and all the indexes where they appear
            idx += 1

    def pick(self, target: int) -> int:
        return random.choice(self.idx_tracker[target]) #then just randomly pick one of the indexes from the dictionary that pertains to the specific target number


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)