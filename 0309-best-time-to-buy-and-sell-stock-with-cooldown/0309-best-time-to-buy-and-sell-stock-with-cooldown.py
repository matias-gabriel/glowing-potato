class Solution:
    # [1,2,3,0,2]
    # maxP(idx, sold) =  max(idx+1) or max(idx+1, profit-prices[idx], sold)
    def maxProfit(self, prices: List[int]) -> int:
        def r(idx, stock, memo):
            if idx >= len(prices):
                return 0
            if (idx, stock) in memo:
              return memo[idx, stock]
            do_nothing=r(idx+1, stock, memo)
            if not stock:
                # buy
                result=max(do_nothing, -prices[idx] + r(idx+1, True, memo))
            else:
                # sell
                result=max(do_nothing, prices[idx] + r(idx+2, False, memo))

            memo[(idx, stock)] = result

            return result

        result = r(0, False,  {})
        return result

        