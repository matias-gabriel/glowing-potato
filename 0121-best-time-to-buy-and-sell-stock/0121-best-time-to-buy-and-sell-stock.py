class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # buy
        # sell

        result = float("-inf")
        l = 0

        # [7 , 3, 5,3,6,4, 2, 10000]
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r

            result = max(result, prices[r] - prices[l])

        
        return result
        