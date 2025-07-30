class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items_dict = {}

        for idx, num in enumerate(nums):
            if target - num in items_dict:
                return [idx, items_dict[target - num]]

            items_dict[num] = idx
