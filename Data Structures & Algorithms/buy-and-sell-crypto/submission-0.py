class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        days = len(prices)
        for bday in range(days):
            for sday in range(bday, days):
                diff = prices[sday] - prices[bday]
                if diff > res:
                    res = diff
        return res