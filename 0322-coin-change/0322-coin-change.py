class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def r(idx, target, memo):
            if (idx, target) in memo:
                return memo[(idx, target)]
            if target == amount and idx < len(coins):
                return 0
            if idx >= len(coins) or target > amount:
                return float("inf")

            result = min(
                r(idx, target + coins[idx], memo) + 1, r(idx + 1, target, memo)
            )

            memo[(idx, target)] = result

            return result

        result = r(0, 0, {})

        if result == float("inf"):
            return -1
        else:
            return result
