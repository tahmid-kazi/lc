class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # last leetcode hard of the Meta list!
        # 8th and final leetcode hard of the day done
        # 11/24/24) Sat night) 326-334am) tk)
        result = []
        queue1 = deque()

        for i in range(len(nums)):
            if queue1 and queue1[0] < i-k+1:
                queue1.popleft()
            while queue1 and nums[queue1[-1]] < nums[i]:
                queue1.pop()
            queue1.append(i)

            if i >= k-1:
                result.append(nums[queue1[0]])
        return result