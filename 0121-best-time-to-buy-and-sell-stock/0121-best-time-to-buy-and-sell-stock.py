class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        maxprofit=0
        for i in range(len(prices)):
            if prices[i]<minp:
                minp=prices[i]
            if prices[i]-minp>maxprofit:
                maxprofit=prices[i]-minp
        return maxprofit
       
        