class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [0] * (len(nums) + 1)

        for i in range(1, n+1):
            lis_i = 0
            for j in range(1, i):
                if nums[i-1] < nums[j-1]:
                    continue
                else:
                    curr = lis[j]
                    if nums[j-1] < nums[i-1]:
                        curr+=1 

                lis_i = max(curr, lis_i )

            lis[i] = max(lis_i, 1)

        return max(lis)
                
        