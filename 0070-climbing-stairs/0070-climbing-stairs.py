class Solution:
    # cs(n) = 1 + cs(n-1), 1 + cs
    def climbStairs(self, n: int) -> int:
      def r(current, target, memo):
        if current in memo:
          return memo[current]

        if current == target:
          return 1

        result = 0

        if current + 2 <= target:
          result = r(current + 2, target, memo)

        if current + 1 <= target:
          result = result + r(current + 1, target, memo)

        memo[current] = result

        return result

      return r(0, n, {})