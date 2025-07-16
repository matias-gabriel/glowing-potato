class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        def canGrowMemo(position, mines, direction, memo):
            i, j = position

            if not (i >= 0 and j >= 0 and j < n and i < n):
                return 0

            if position in mines:
                memo[position[0]][position[1]][direction] = 0
                return 0

            if memo[position[0]][position[1]][direction] is not -1:
                return memo[position[0]][position[1]][direction]

            result = None
            if direction == 0:
                result = 1 + canGrowMemo((i - 1, j), mines, direction, memo)
            if direction == 1:
                result = 1 + canGrowMemo((i + 1, j), mines, direction, memo)

            if direction == 2:
                result = 1 + canGrowMemo((i, j + 1), mines, direction, memo)

            if direction == 3:
                result = 1 + canGrowMemo((i, j - 1), mines, direction, memo)

            dp[position[0]][position[1]][direction] = result
            return result

        def calcC(position, mines, memo, n):
            return min(
                canGrowMemo(position, mines, 0, memo),
                canGrowMemo(position, mines, 1, memo),
                canGrowMemo(position, mines, 2, memo),
                canGrowMemo(position, mines, 3, memo),
            )

        result = 0
        mines_set = set([(m[0], m[1]) for m in mines])
        memo = {}
        dp = [[[-1] * 4 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                result = max(calcC((i, j), mines_set, dp, n), result)

        return result
