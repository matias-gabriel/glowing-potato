
def calc_best_rob(current_idx, nums, memo):
    if current_idx >= len(nums):
        return 0
    if current_idx in memo:
        return memo[current_idx]

    value = max(
        calc_best_rob(current_idx + 2, nums, memo) + nums[current_idx],
        calc_best_rob(current_idx + 1, nums, memo),
        nums[current_idx]
    )

    memo[current_idx] = value
    return memo[current_idx]


class Solution:

    def rob(self, nums: List[int]) -> int:
        
        return calc_best_rob(0, nums, {})
