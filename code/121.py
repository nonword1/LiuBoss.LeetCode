class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        l = len(prices)
        for i in range(l):
            m = max(m,max(prices[i:l])-prices[i])
        return m
