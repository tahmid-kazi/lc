class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 11/12/24) Tue) 547 to 555pm) tk)
        hashmap = defaultdict()
        for j in range(len(nums)):
            if nums[j] in hashmap and abs(j - hashmap[nums[j]]) <= k:
                return True
            hashmap[nums[j]] = j
        return False