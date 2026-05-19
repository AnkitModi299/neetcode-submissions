class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxprofit = 0
        for r in prices:
            maxprofit = max(maxprofit, r - minBuy)
            minBuy = min(minBuy, r)
        return maxprofit


            


        