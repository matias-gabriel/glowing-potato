class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        n_string = str(x)
        len_n_string = len(n_string)
        # 1 2 1
        # j: 0 1 2
        # i: 2 1 0

        for i, letter_i in enumerate(n_string):
          j = len_n_string - 1 - i
          if i >= j:
            return True

          letter_j = n_string[j]
          if letter_j != letter_i:
            return False

        return False

        