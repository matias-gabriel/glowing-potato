class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes_position_set = set([])
        [1,2, 0 ,3, 0,4]

        product = 1

        for idx, num in enumerate(nums):
            if num == 0:
                zeroes_position_set.add(idx) 
            else:
                product = product * num

        result = []
        if len(zeroes_position_set) > 1:
            return [0] * len(nums)

        if len(zeroes_position_set) == 1:
            result = [0] * len(nums)
            result[list(zeroes_position_set)[0]] = product

            return result

        for i in nums:
            result.append(int(product / i))

        return result

                

