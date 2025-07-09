def is_strobogrammatic(num):
    """
    Checks if a number is strobogrammatic.

    A strobogrammatic number is a number that appears the same when rotated
    180 degrees. Examples include 69, 96, 88, and 101.

    This is determined by checking characters from both ends of the number's
    string representation, moving inwards.

    Note:
        This function correctly validates numbers composed of strobogrammatic
        digits (0, 1, 6, 8, 9). However, it does not validate that the digits
        themselves are strobogrammatic. For example, it will incorrectly return
        True for inputs like 22 or 55, because the outer digits match. The
        middle digit in an odd-length number is also not checked for being
        a valid strobogrammatic digit (0, 1, or 8).

    Args:
        num (int or str): The number to check.

    Returns:
        bool: True if the number is strobogrammatic according to the implemented
              logic, False otherwise.
    """
    # Convert the number to a list of characters to easily access individual digits.
    num_list = list(str(num))

    # Initialize pointers for the left and right ends of the number.
    left_pointer = 0
    right_pointer = len(num_list) - 1

    # A dictionary to define the digits that map to each other when rotated.
    # '6' becomes '9' and '9' becomes '6'.
    equivalence_dict = {
        "6": "9",
        "9": "6",
    }

    # Loop until the pointers meet or cross, checking pairs of digits.
    while left_pointer < right_pointer:
        # Get the digits at the current left and right positions.
        left_value = num_list[left_pointer]
        right_value = num_list[right_pointer]

        # Check if the digits are valid as a pair. A pair is valid if:
        # 1. The digits are the same (e.g., '8' == '8', '1' == '1').
        # 2. The digits are rotational equivalents (e.g., '6' and '9').
        if (left_value == right_value) or (
            equivalence_dict.get(left_value, -1) == right_value
        ):
            # If the pair is valid, move the pointers inward.
            left_pointer += 1
            right_pointer -= 1
        else:
            # If a pair is not valid, the number is not strobogrammatic.
            return False

    # If the loop completes without finding any invalid pairs, the number is strobogrammatic.
    return True
