class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell,buy=1,0
        profit=0
        while sell < len(prices):
            if prices[sell]<prices[buy]:
                buy = sell
            if prices[sell] - prices[buy] > profit:
                profit = prices[sell] - prices[buy]
            sell += 1
        return profit if profit>0 else 0
