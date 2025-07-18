class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      # logic behind that
      # you can see the future
      # the logic is, can I profit tommorow [i+1] if I buy today[i]?

      profit = 0

      if len(prices) == 1:
        return 0

      for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
          profit+= prices[i+1]-prices[i]

      return profit



