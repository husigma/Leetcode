class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        while len(prices) != 1:
            if prices[0]> prices[1]:
                del prices[0]
            else:
                profit = profit if profit > prices[1] - prices[0] else prices[1] - prices[0]
                del prices[1]
        return profit