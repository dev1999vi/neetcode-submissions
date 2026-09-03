class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        max_profit = 0
        
        for i, val in enumerate(prices):
            current_profit = val - prices[j]
            while prices[j] > val:
                j += 1

            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit