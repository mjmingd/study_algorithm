# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    '''
    time complexity : O(N)
    space complexity : O(1)
    '''
        if not prices :
            return 0
            
        maxProfit, minPrice = 0, max(prices)
        
        for p in prices :
            if p < minPrice :
                minPrice = p
            if p - minPrice > maxProfit :
                maxProfit = p - minPrice
        
        return maxProfit
