import math


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        n_max = math.floor(n / 3)
        result = set([])

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] = freq[i] + 1

            if freq[i] > n_max:
                result.add(i)
        return list(result)
