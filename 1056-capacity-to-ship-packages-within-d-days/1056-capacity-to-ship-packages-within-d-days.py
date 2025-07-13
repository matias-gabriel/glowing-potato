import bisect


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check_can_ship(capacity):
            day = 1
            value = 0
            for weight in weights:
                value += weight

                if value > capacity:
                    day += 1
                    value = weight

            return day <= days

        left = max(weights)
        right = sum(weights)
        capacities = range(left, right + 1)
        index = bisect.bisect_left(capacities, True, key=check_can_ship)

        return capacities[index]
