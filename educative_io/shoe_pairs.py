import unittest
from collections import Counter


def shoe_pairs(shoes):
    """
    Determines if a collection of shoes can be perfectly paired.

    Args:
        shoes: A list of lists, where each inner list represents a shoe
               as [type, size].
               - type is 0 for a left shoe.
               - type is 1 for a right shoe.
               - size is a positive integer.

    Returns:
        True if all shoes can be formed into pairs of a left and a right shoe
        of the same size. False otherwise.
    """
    shoes_hash = {}

    for shoe in shoes:
        s_tuple = (shoe[0], shoe[1])
        if s_tuple not in shoes_hash:
            shoes_hash[s_tuple] = 0

        shoes_hash[s_tuple] = shoes_hash[s_tuple] + 1

    for shoe in shoes:
        to_find = 0 if shoe[0] == 1 else 1
        s_tuple = (shoe[0], shoe[1])
        shoe_to_find = (to_find, shoe[1])

        if shoes_hash.get(s_tuple, 0) != shoes_hash.get(shoe_to_find, 0):
            return False

    return True


# --- Test Suite ---
# You can run this file to test your implementation of the shoe_pairs function.


class TestShoePairs(unittest.TestCase):
    def test_empty_list(self):
        """Test with an empty list of shoes."""
        self.assertTrue(
            shoe_pairs([]), "An empty list should be considered perfectly paired."
        )

    def test_single_perfect_pair(self):
        """Test with a single, valid pair of shoes."""
        self.assertTrue(
            shoe_pairs([[0, 25], [1, 25]]), "A single valid pair should return True."
        )

    def test_multiple_perfect_pairs(self):
        """Test with several valid pairs of different sizes."""
        shoes = [[0, 30], [1, 30], [0, 28], [1, 28], [0, 29], [1, 29]]
        self.assertTrue(shoe_pairs(shoes), "Multiple valid pairs should return True.")

    def test_mismatched_size(self):
        """Test with shoes of the same type but different sizes."""
        self.assertFalse(
            shoe_pairs([[0, 25], [1, 26]]),
            "A left and right of different sizes cannot form a pair.",
        )

    def test_two_left_shoes(self):
        """Test with two left shoes of the same size."""
        self.assertFalse(
            shoe_pairs([[0, 25], [0, 25]]), "Two left shoes cannot form a pair."
        )

    def test_two_right_shoes(self):
        """Test with two right shoes of the same size."""
        self.assertFalse(
            shoe_pairs([[1, 25], [1, 25]]), "Two right shoes cannot form a pair."
        )

    def test_uneven_number_of_shoes(self):
        """Test with an odd number of shoes, making pairing impossible."""
        shoes = [[0, 25], [1, 25], [0, 25]]
        self.assertFalse(
            shoe_pairs(shoes), "An odd number of shoes cannot be fully paired."
        )

    def test_uneven_pairs(self):
        """Test with an even number of shoes, but with unbalanced pairs."""
        shoes = [[0, 25], [1, 25], [0, 25], [1, 26]]
        self.assertFalse(
            shoe_pairs(shoes),
            "Should be False if counts for a size/type are not balanced.",
        )

    def test_complex_unbalanced_set(self):
        """Test a more complex case with multiple unbalanced pairs."""
        shoes = [[0, 30], [1, 30], [0, 30], [1, 30], [0, 30], [1, 28]]
        self.assertFalse(
            shoe_pairs(shoes), "Should be False with complex unbalanced sets."
        )

    def test_large_perfectly_matched_set(self):
        """Test with a large, but perfectly matched, set of shoes."""
        shoes = [
            [0, 42],
            [1, 42],
            [0, 38],
            [1, 38],
            [0, 40],
            [1, 40],
            [0, 42],
            [1, 42],
            [0, 39],
            [1, 39],
            [0, 41],
            [1, 41],
        ]
        self.assertTrue(
            shoe_pairs(shoes), "A large, perfectly matched set should return True."
        )

    def test_shuffled_order_perfect_match(self):
        """Test that order does not affect a perfect match."""
        shoes = [[0, 42], [0, 38], [1, 42], [1, 38], [0, 40], [1, 40]]
        self.assertTrue(
            shoe_pairs(shoes), "Shuffled order of a valid set should still return True."
        )

    def test_unbalanced_types_same_size(self):
        """Test with an even number of shoes, but unbalanced types for the same size."""
        shoes = [[0, 23], [1, 23], [0, 23], [0, 23]]
        self.assertFalse(
            shoe_pairs(shoes),
            "Should be False with three lefts and one right of the same size.",
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
