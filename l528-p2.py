import random

    # most optimal solution: prefix sum + binary search
    # runtime:  O(n) = calculate prefix sum 
    #           O(log(n)) = for each query
    #           this is for q queries
    # Overall:  O(n + q*log(n))
    # space = O(n) for the list 

    # 12/25/24) Wed) 1142-1153am) gtk) 12J

class Solution:
    def __init__(self, w: list[int]):
        self.prefix_sums = list(accumulate(w))  # Create prefix sums
        self.total_sum = self.prefix_sums[-1]  # Total weight for normalization

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)  # Pick a random number
        # Find the index using binary search
        return bisect.bisect_left(self.prefix_sums, target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()