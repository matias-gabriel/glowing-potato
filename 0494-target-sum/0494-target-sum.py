class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
      n = len(nums)
      def r(idx, target, memo):
        if idx == n and target == 0:
          return 1
        if idx == n:
          return 0
        if (idx, target) in memo:
          return memo[(idx, target)]

        result = r(idx + 1, target + -1 * nums[idx], memo) + r(idx + 1, target + nums[idx], memo)
        memo[(idx, target)] = result
        return result

      

      return r(0, target, {}) 