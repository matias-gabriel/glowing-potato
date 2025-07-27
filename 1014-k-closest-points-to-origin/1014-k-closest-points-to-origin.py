import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0, 0]
        min_heap = []

        for point in points:
          heapq.heappush(min_heap, (math.dist(origin, point), point))

        result = []

        for i in range(k):
          result.append(heapq.heappop(min_heap)[1])

        return result
        