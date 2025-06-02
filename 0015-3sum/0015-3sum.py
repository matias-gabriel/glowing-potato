class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        sorted_array = sorted(nums)
        result_array = []

        for index, number in enumerate(sorted_array):
            if index >= len(sorted_array) - 2:
                break
            if number > 0:
                break
            if index > 0 and number == sorted_array[index-1]:
                continue

            left_pointer = index + 1
            right_pointer = len(sorted_array) - 1

            # -2, 0, 1, 1 , 2
            while left_pointer < right_pointer:
                current_result = [number, sorted_array[left_pointer], sorted_array[right_pointer]]
                current_sum = sum(current_result)
                
                if current_sum == 0:
                    result_array.append(current_result)
                    right_pointer = right_pointer - 1
                    left_pointer = left_pointer + 1
                    while left_pointer < right_pointer and sorted_array[right_pointer] == sorted_array[right_pointer+1]:
                        right_pointer = right_pointer - 1
                    while left_pointer < right_pointer and sorted_array[left_pointer] == sorted_array[left_pointer-1]:
                        left_pointer = left_pointer + 1
                elif current_sum > 0:
                    right_pointer = right_pointer - 1
                else:
                    left_pointer = left_pointer + 1

        return result_array




                
        