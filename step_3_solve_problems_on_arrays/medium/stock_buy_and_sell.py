#https://takeuforward.org/data-structure/stock-buy-and-sell/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]
        prof = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            if prices[i] - min_price > prof:
                prof = prices[i] - min_price
        return prof

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))  # Output should be 5