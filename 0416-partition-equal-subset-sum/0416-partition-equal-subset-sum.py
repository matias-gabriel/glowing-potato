class Solution:
    # canPart(idx, current) = canPart(idx - 1, current ) or canPart(idx - 1, current + nums[idx1])
    def canPart(self, idx, target, current, nums, memo):
        if target == current and idx > 0:
            memo[(idx, current)] = True
            return True
        elif current > target or idx < 0:
            memo[(idx, current)] = False
            return False

        if (idx, current) in memo:
            return memo[(idx, current)]

        result = self.canPart(
            idx - 1, target, current + nums[idx - 1], nums, memo
        ) or self.canPart(idx - 1, target, current, nums, memo)
        memo[(idx, current)] = result
        return result

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[len(nums)][target]
        # recursion: return self.canPart(len(nums), int(sum(nums) / 2), 0, nums, {})
