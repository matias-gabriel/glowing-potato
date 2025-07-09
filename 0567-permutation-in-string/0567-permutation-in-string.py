class Solution(object):
    def checkIsPermutation(self, n, m):
        """
        Checks if two strings are permutations of each other by comparing character counts.

        Args:
            n (str): First string to compare
            m (str): Second string to compare

        Returns:
            bool: True if strings are permutations, False otherwise

        Time Complexity: O(max(len(n), len(m))) / O(N)
        Space Complexity: O(1) (since there are at most 26 letters in English alphabet)
        """
        letters_m = {}
        letters_n = {}

        for letter in n:
            if letter in letters_n:
                letters_n[letter] = letters_n[letter] + 1
            else:
                letters_n[letter] = 1

        for letter in m:
            if letter in letters_m:
                letters_m[letter] = letters_m[letter] + 1
            else:
                letters_m[letter] = 1

        return letters_m == letters_n

    def checkInclusion(self, s1, s2):
        """
        Checks if any permutation of s1 exists as a substring in s2.

        Args:
            s1 (str): The string to find permutations of
            s2 (str): The string to search within

        Returns:
            bool: True if a permutation of s1 exists in s2, False otherwise

        Time Complexity: O(len(s2) * len(s1)) / O (N*M)
        Space Complexity: O(1) (uses constant space for character counts)
        """
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        for i, item in enumerate(s2):
            if i + s1_len > s2_len:
                return False

            s2_slice = s2[i : i + s1_len]

            if self.checkIsPermutation(s1, s2_slice):
                return True

        return False
