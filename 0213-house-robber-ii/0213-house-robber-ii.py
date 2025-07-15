class Solution:
    def rob(self, nums: List[int]) -> int:
      def r(idx, sub_arr, memo):
        if idx >= len(sub_arr):
          return 0
        if idx in memo:
          return memo[idx]
        
        result = max( r(idx + 1, sub_arr, memo), sub_arr[idx] + r(idx + 2, sub_arr, memo))
        memo[idx] = result

        return memo[idx]
      
      if len(nums) == 1: return nums[0]
      return max(r(0, nums[:len(nums) - 1], {}), r(0, nums[1:], {}))