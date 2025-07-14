class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = 0
        current_min = 0
        values = [0] * len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                current_max = num
                current_min = num
                values[0] = current_max

                continue

            current_max = current_max * num
            current_min = current_min * num

            if current_max < current_min:
                aux = current_max
                current_max = current_min
                current_min = aux

            current_max = max(num, current_max)
            current_min = min(num, current_min)

            values[i] = current_max

        return max(values)
        
        