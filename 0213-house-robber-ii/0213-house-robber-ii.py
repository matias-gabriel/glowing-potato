class Solution:
    def rob(self, nums: List[int]) -> int:
      # def r_recursive(idx, sub_arr, memo):
      #   if idx >= len(sub_arr):
      #     return 0
      #   if idx in memo:
      #     return memo[idx]
      #
      #   result = max( r_recursive(idx + 1, sub_arr, memo), sub_arr[idx] + r_recursive(idx + 2, sub_arr, memo))
      #   memo[idx] = result
      #
      #   return memo[idx]
      #
      # if len(nums) == 1: return nums[0]
      # return max(r_recursive(0, nums[:len(nums) - 1], {}), r_recursive(0, nums[1:], {}))


      # iterative solution
      if len(nums) == 1: return nums[0]

      def r_iterative(sub_array):
        result_array = [0] * len(sub_array)
  
        for i in range(len(sub_array)-1, -1, -1):
          # result_i
          results_i = []
          if i + 1 < len(sub_array):
            results_i.append(result_array[i+1])
          
          if i + 2 < len(sub_array):
            results_i.append(result_array[i+2] + sub_array[i])
          else:
            results_i.append(sub_array[i])

          result_array[i] = max(results_i)

        return result_array[0]

      return max(r_iterative(nums[:len(nums) - 1]), r_iterative(nums[1:]))

