class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def r(idx, target, memo):
            if target == amount:
                return 1
            if target > amount:
                return 0
            if (idx, target) in memo:
                return memo[(idx, target)]
            if idx >= len(coins):
                return 0
            

            result = r(idx, target + coins[idx], memo) + r(idx + 1, target, memo) 

            memo[(idx, target)] = result

            return result

        return r(0, 0, {})

        