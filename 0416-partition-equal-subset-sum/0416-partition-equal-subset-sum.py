class Solution:
    def canPart(self, idx, target, current, nums, memo):
        if target == current and idx > 0:
            memo[(idx, current)] = True
            return True
        elif current > target or idx < 0:
            memo[(idx, current)] = False
            return False
        
        if (idx, current) in memo:
            return memo[(idx, current)]

        result =  self.canPart(idx - 1, target, current + nums[idx-1], nums, memo) or  self.canPart(idx - 1, target, current, nums, memo)
        memo[(idx, current)] = result
        return result


    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        return self.canPart(len(nums), int(sum(nums) / 2), 0, nums, {})