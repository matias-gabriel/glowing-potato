def valid_word_abbreviation(word, abbr):
    """
    Checks if a given string is a valid abbreviation of a word.

    An abbreviation's character sequence should match the word's sequence.
    A number in the abbreviation represents a count of skipped characters
    in the word. Leading zeros in these numbers are not permitted.

    Args:
        word (str): The original word, consisting of lowercase English letters.
        abbr (str): The abbreviation to validate, consisting of lowercase
                    English letters and digits.

    Returns:
        bool: True if `abbr` is a valid abbreviation of `word`, otherwise False.

    Examples:
        >>> valid_word_abbreviation("internationalization", "i12iz4n")
        True
        >>> valid_word_abbreviation("apple", "a2e")
        False
        >>> valid_word_abbreviation("word", "w0rd")
        False
        >>> valid_word_abbreviation("a", "2")
        False
    """
    word_list = list(word)
    abbr_list = list(abbr)

    word_pointer = 0
    abbr_pointer = 0
    check_number = ""

    while abbr_pointer < len(abbr_list):
        current_abbr_letter = abbr_list[abbr_pointer]

        if current_abbr_letter == "0":
            return False

        if word_pointer >= len(word_list):
            return False

        while current_abbr_letter.isnumeric() and abbr_pointer < len(abbr_list):
            check_number += current_abbr_letter
            abbr_pointer += 1
            if not abbr_pointer < len(abbr_list):
                continue
            current_abbr_letter = abbr_list[abbr_pointer]

        if len(check_number):
            int_check_number = int(check_number)
            new_word_pointer = word_pointer + int_check_number
            if int_check_number > len(word):
                return False
            word_pointer = new_word_pointer
        else:
            if word_list[word_pointer] != abbr_list[abbr_pointer]:
                return False
            word_pointer += 1
            abbr_pointer += 1

        check_number = ""

    if word_pointer < len(word_list):
        return False

    return True
