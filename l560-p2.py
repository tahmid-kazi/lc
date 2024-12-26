class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 12/25/24) Wed) 1136-1156pm) tk)
        hashmap = {0:1}
        sum1, count = 0, 0
        for i in nums:
            sum1 += i
            if (sum1-k) in hashmap: # still dont get this part
                count += hashmap[sum1-k] 
            if sum1 in hashmap:
                hashmap[sum1] += 1
            else:
                hashmap[sum1] = 1
        return count