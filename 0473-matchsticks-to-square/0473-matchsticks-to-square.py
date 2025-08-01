import math


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks = sorted(matchsticks, reverse=True)
        max_side = math.ceil(sum(matchsticks) / 4)

        def r(position, s1, s2, s3, s4, memo):
            result_tuple = (position, s1, s2, s3, s4)
            if result_tuple in memo:
                return memo[result_tuple]
            if s1 > max_side or s2 > max_side or s3 > max_side or s4 > max_side:
                memo[result_tuple] = False
                return memo[result_tuple]

            if position == len(matchsticks):
                return s1 == s2 == s3 == s4

            if r(position + 1, s1 + matchsticks[position], s2, s3, s4, memo):
                return True
            if r(position + 1, s1, s2 + matchsticks[position], s3, s4, memo):
                return True
            if r(position + 1, s1, s2, s3 + matchsticks[position], s4, memo):
                return True
            if r(position + 1, s1, s2, s3, s4 + matchsticks[position], memo):
                return True

            memo[result_tuple] = False

            return False

        positions = set([i for i in range(len(matchsticks))])
        return r(0, 0, 0, 0, 0, {})
