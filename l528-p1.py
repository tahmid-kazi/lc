import random

class Solution:
    # 10/10/24 (1008 to 1034pm) (Thurs)
    def __init__(self, w: List[int]):
        self.w = w
        self.len = len(w)
        self.weighted_sum = []

        rolling_sum = 0
        #first task is to create the cumulative sum array:
        for i in range(len(w)):
            rolling_sum += w[i]
            self.weighted_sum.append(rolling_sum)

    def pickIndex(self) -> int:
        
        #find a number between 1 and the largest num
        random_number = random.randint(1, self.weighted_sum[-1])

        #then run binary search to find the index of that num
        left1, right1 = 0, self.len-1

        while left1 < right1:
            middle = left1 + (right1-left1)// 2

            if random_number <= self.weighted_sum[middle]: 
                right1 = middle
            else:
                left1 = middle + 1
        #this is assuming that the answer exists in the array
        return left1
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()