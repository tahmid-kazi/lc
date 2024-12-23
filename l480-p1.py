class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    # Sliding Window Median - LeetCode
    # Time Complexity: O(n log k), Space Complexity: O(k)
    
    # 12/23/24) sun night) 1213-1222am) gtk) 12J
    
        window = SortedList()
        res = []
        for i in range(len(nums)):
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k])
            if i >= k - 1:
                if k % 2 == 1:
                    res.append(window[k // 2])
                else:
                    res.append((window[k // 2 - 1] + window[k // 2]) / 2)
        return res