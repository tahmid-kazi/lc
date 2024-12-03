class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 11/14/24) Thurs) 833-854pm) tk) (in g14 + maker lab!)
        # g14 laptop
        # if k=2, return the top 2 most frequent elements
        frequency = Counter(nums) #O(n)
        result = heapq.nlargest(k, frequency.keys(), key = frequency.get) #O(n log k)
        return result