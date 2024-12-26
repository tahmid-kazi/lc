class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 12/26/24) Wed night) 1243 to 1252am) tk)
        hashmap = defaultdict()
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in hashmap:
                return [hashmap[complement], i] # you forgot this
            hashmap[nums[i]] = i # and this
        return []