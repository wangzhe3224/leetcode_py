class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for idx in range(1, len(prices)):
            p = prices[idx] - prices[idx-1]
            if p >= 0:
                profit += p
                
        return profit