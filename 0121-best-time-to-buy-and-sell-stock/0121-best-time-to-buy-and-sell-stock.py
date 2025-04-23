class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprices=prices[0]
        maxp=0
        for i in range(len(prices)):
            if minprices>prices[i]:
                minprices=prices[i]
            if prices[i]-minprices>maxp:
                maxp=prices[i]-minprices
        return maxp

       
        