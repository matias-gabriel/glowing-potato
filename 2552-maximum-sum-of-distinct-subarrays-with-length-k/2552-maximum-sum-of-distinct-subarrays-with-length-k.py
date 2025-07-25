def add_number(i, quantity_dict):
    if i in quantity_dict:
        quantity_dict[i] += 1
    else:
        quantity_dict[i] = 1


def remove_number(i, quantity_dict):
    if i in quantity_dict:
        quantity_dict[i] -= 1
        if quantity_dict[i] == 0:
            quantity_dict.pop(i)


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        result = 0

        last_sub_array_sum = sum(nums[0:k])
        quantity_dict = {}

        for i in nums[0:k]:
            add_number(i, quantity_dict)

        if len(quantity_dict) == k:
            result = last_sub_array_sum

        for i in range(1, len(nums) - k + 1):
            removed_n = nums[i - 1]
            added_n = nums[i + k - 1]
            last_sub_array_sum = last_sub_array_sum - removed_n + added_n

            add_number(added_n, quantity_dict)
            remove_number(removed_n, quantity_dict)

            if len(quantity_dict) == k:
                result = max(result, last_sub_array_sum)

        return result
