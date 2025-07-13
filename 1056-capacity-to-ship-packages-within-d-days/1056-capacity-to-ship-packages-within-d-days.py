import bisect
from typing import List


class Solution:
    """
    Solves the 'Ship Within Days' problem using binary search on the answer space.
    """

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Calculates the minimum weight capacity of a ship that can ship all packages
        within a specified number of days.

        The core strategy is to binary search for the smallest possible capacity. The
        search space for the capacity ranges from the heaviest single package to the
        sum of all package weights. A helper function, `check_can_ship`, determines
        if a given capacity is feasible.

        Args:
            weights: A list of integers representing the weights of the packages.
            days: An integer representing the number of days within which to ship
                  all packages.

        Returns:
            The minimum capacity required to ship all packages within the given days.
        """

        def check_can_ship(capacity: int) -> bool:
            """
            Checks if it's possible to ship all packages within the allowed `days`
            given a certain `capacity`.

            This function simulates the loading process. It iterates through the
            weights, adding them to a running total. If adding a weight exceeds the
            ship's capacity, it counts as a new day and the new weight becomes the
            start of the next shipment.

            Args:
                capacity: The ship's weight capacity to test.

            Returns:
                True if the packages can be shipped within `days`, False otherwise.
            """
            day_count = 1
            current_load = 0
            for weight in weights:
                current_load += weight
                if current_load > capacity:
                    day_count += 1
                    current_load = weight  # Start a new day with the current weight

            return day_count <= days

        # The search space for the capacity is between the largest single item
        # and the sum of all items.
        left = max(weights)
        right = sum(weights)

        # We can conceptualize a range of all possible capacities.
        # Note: We don't actually create this list in memory.
        # It's just a conceptual range for bisect.
        possible_capacities = range(left, right + 1)

        # bisect_left finds the first value (capacity) for which the `key` function
        # (check_can_ship) returns True. This is the essence of finding the
        # minimum valid capacity.
        # We are searching for `True` in the conceptual boolean array:
        # [False, False, ..., False, True, True, True]
        index = bisect.bisect_left(possible_capacities, True, key=check_can_ship)

        return possible_capacities[index]
