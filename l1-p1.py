class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hashmap
        # 11/4/24) Mon) 801-811pm) tk)
        hashmap = defaultdict()

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i