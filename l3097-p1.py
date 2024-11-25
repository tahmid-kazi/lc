class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # sliding window with bit manipulation
        # 11/25/24) 1224 to 1231am) Sunday night) tk)

        n = len(nums)
        count = [0] * 32 #count the occurrence of each bit position
        ans = n+1
        s, i = 0, 0 #i is the left pointer

        for j in range(n):
            x = nums[j]
            s |= x
            for h in range(32):
                if x >> h & 1:
                    count[h] += 1
            while s >= k and i <= j:
                ans = min(ans, j-i+1)
                y = nums[i]
                for h in range(32):
                    if y >> h & 1:
                        count[h] -= 1
                        if count[h] == 0:
                            s ^= 1 << h
                i += 1
        return -1 if ans > n else ans
