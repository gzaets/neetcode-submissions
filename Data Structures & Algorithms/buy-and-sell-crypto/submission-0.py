class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bigMoney = 0
        buy = 999
        for price in prices:
            if price < buy:
                buy = price
            else:
                bigMoney=max(bigMoney, price - buy)
        
        return bigMoney