class Solution {
    public int maxProfit(int[] prices) {
        int minprice = Integer.MAX_VALUE; // Initialize minprice to the highest possible value
        int maxprofit = 0;                // Initialize maxprofit to 0 (no profit)

        for (int i = 0; i < prices.length; i++) {
            // Update minprice if the current price is less than minprice
            if (prices[i] < minprice) {
                minprice = prices[i];
            } 
            
            // Calculate the profit by selling on the current day and compare with maxprofit
            int profit = prices[i] - minprice;
            if (profit > maxprofit) {
                maxprofit = profit;
            }
        }
        return maxprofit; // Return the maximum profit found
    }
}
