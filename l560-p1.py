class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 11/12/24) Tue) 652-659pm) tk)
        hashmap = {0: 1}
        sum1 = 0
        count = 0
        for j in nums:
            sum1 += j
            if (sum1 - k) in hashmap:
                count += hashmap[sum1-k]
            if sum1 in hashmap:
                hashmap[sum1] += 1
            else:
                hashmap[sum1] = 1
        return count
        