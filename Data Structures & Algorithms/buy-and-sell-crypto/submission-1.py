class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        low=prices[0]
        recent=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<recent:
                low=min(prices[i],low)
            if prices[i]>recent:
                profit=max(profit, prices[i]-low)
            recent=prices[i]
        return profit