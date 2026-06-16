class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        min_price=prices[0]
        for i in prices:
            min_price=min(min_price,i)
            profit=i-min_price
            if profit>max_profit:
                max_profit=profit
        return max_profit        

        