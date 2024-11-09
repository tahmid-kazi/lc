class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 11/8/24) Fri) 1136-1152pm) tk)
        left, right = 0,0
        maxProfit = 0

        while right < len(prices):
            profit = prices[right]-prices[left]
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit