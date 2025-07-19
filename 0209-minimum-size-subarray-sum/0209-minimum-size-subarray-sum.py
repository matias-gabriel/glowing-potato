class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # idea
        # l, r = 1
        # [2,3,1,2,4,3]
        #
        n = len(nums)
        l = 0

        if n == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0

        result = float("inf")
        current_sum = 0

        for r in range(n):
            current_sum += nums[r]
            while current_sum >= target:
                result = min(r - l + 1, result)
                current_sum -= nums[l]
                l += 1

        return result if result != float("inf") else 0
