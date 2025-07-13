import bisect
import math


class Solution:
    # piles [3,6,7,11]
    # 4,1 , 4,2, 2,3 , 4,4, 3,5, 4,6, 4,7, 3,8
    # this is a monotonic condition bc,
    # [3,6,7,11] h=8, result = 4
    #  k's = [3,4,5,6,7,8,9,10,11]
    #         [not, yes, yes, yes ... yes]
    # if i can eat 4 per hour and finish before or in h=8
    # for sure if I eat more I'll end before taht
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)

        def check_can_eat(k):
            hour_count = 0

            for pile in piles:
                hours_needed = math.ceil(pile / k)
                hour_count += hours_needed

                if hour_count > h:
                    return False
            return hour_count <= h

        eat_range = range(min_k, max_k + 1)
        result = bisect.bisect_left(eat_range, True, key=check_can_eat)
        return eat_range[result]
