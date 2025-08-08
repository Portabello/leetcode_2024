class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = None
        maxprofit = 0
        for x in prices:
            if buy == None:
                buy = x
            else:
                maxprofit = max(maxprofit, x-buy)
                if x < buy:
                    buy = x
        return maxprofit
