class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprices=prices[0]
        minp=0
        for i in range(len(prices)):
            if prices[i]<minprices:
                minprices=prices[i]
            if prices[i]-minprices>minp:
                minp=prices[i]-minprices
        return minp

       
        