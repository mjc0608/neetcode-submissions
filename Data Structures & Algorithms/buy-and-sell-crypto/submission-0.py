class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            res = max(res, profit)
            min_price = min(prices[i], min_price)
        return res