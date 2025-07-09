def get_sum_of_the_digit_squares(n):
    str_n = str(n)
    result = 0
    for digit in list(str_n):
        result = result + (int(digit) ** 2)

    return result


class Solution:
    def isHappy(self, n: int) -> bool:
        first_pointer = get_sum_of_the_digit_squares(n)
        second_pointer = get_sum_of_the_digit_squares(first_pointer)

        while (
            first_pointer != 1
            and second_pointer != 1
            and second_pointer != first_pointer
        ):
            first_pointer = get_sum_of_the_digit_squares(first_pointer)
            second_pointer = get_sum_of_the_digit_squares(second_pointer)
            second_pointer = get_sum_of_the_digit_squares(second_pointer)

        return second_pointer == 1 or first_pointer == 1
