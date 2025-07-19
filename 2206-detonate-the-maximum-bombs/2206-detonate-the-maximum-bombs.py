from collections import deque
import math


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def circles_intersect(xi, yi, ri, xj, yj, rj):
            dist_sq = (xi - xj) ** 2 + (yi - yj) ** 2
            return dist_sq <= ri**2

        graph = {}
        for i, bomb1 in enumerate(bombs):
            graph[i] = []
            for j, bomb2 in enumerate(bombs):
                if i == j:
                    continue
                if circles_intersect(
                    bomb1[0], bomb1[1], bomb1[2], bomb2[0], bomb2[1], bomb2[2]
                ):
                    graph[i].append(j)

        result = 0
        for key in graph.keys():
            visited = set([key])
            queue = deque([(key, 1)])
            while queue:
                k, w = queue.popleft()
                for n in graph[k]:
                    if n not in visited:
                        visited.add(n)
                        queue.append((n, w + 1))

            result = max(result, len(visited))

        return result

        return 0
