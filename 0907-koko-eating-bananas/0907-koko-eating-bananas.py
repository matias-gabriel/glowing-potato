import bisect
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      """
      Calculates the minimum integer eating speed (k) to consume all bananas within h hours.

      This function determines the slowest possible eating speed where all piles of
      bananas can be finished within the given time limit 'h'. The problem is solved
      using a binary search approach on the possible eating speeds. The range of
      possible speeds is from 1 to the size of the largest pile.

      For a given speed 'k', if Koko can finish all bananas in 'h' hours, she can
      also finish them with any speed greater than 'k'. This monotonic property
      allows for the use of binary search to efficiently find the minimum required speed.

      Args:
        piles: A list of integers representing the number of bananas in each pile.
        h: An integer representing the total hours available to eat all bananas.

      Returns:
        The minimum integer eating speed (k) required to eat all bananas within h hours.
      """
      min_k = 1
      max_k = max(piles)

      def check_can_eat(k: int) -> bool:
        """
        Checks if it's possible to eat all bananas with a given speed 'k' within 'h' hours.

        Args:
          k: The eating speed in bananas per hour.

        Returns:
          True if all bananas can be eaten within the time limit, False otherwise.
        """
        hour_count = 0
        for pile in piles:
          # Calculate the time to eat a pile, rounding up to the nearest integer.
          # For example, if a pile has 7 bananas and speed is 3, it will take
          # math.ceil(7 / 3) = 3 hours.
          hours_needed = math.ceil(pile / k)
          hour_count += hours_needed
          # Early exit if the time limit is already exceeded.
          if hour_count > h:
            return False
        return True

      # The range of possible eating speeds to search.
      eat_range = range(min_k, max_k + 1)
      
      # bisect_left finds the first value in eat_range for which check_can_eat is True.
      # It efficiently performs a binary search to find this minimum speed.
      result_index = bisect.bisect_left(eat_range, True, key=check_can_eat)
      
      return eat_range[result_index]