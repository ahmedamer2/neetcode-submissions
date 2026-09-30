class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, l= 0, 0
        #[7,1,5,3,6,4]
        for r in range(1, len(prices)):
            curr = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                r += 1
            profit = max(curr, profit)

            
        
        return profit