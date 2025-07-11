from collections import deque


class Solution:
    def calcIslandArea(self, position, grid):
        node_queue = deque([position])

        result = 0
        while node_queue:
            i, j = node_queue.popleft()
            if grid[i][j] == 1:
                grid[i][j] = 0
                result += 1
            else:
                continue

            if i + 1 < len(grid):
                node_queue.append((i + 1, j))
            if i - 1 >= 0:
                node_queue.append((i - 1, j))
            if j + 1 < len(grid[i]):
                node_queue.append((i, j + 1))
            if j - 1 >= 0:
                node_queue.append((i, j - 1))

        return result

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for i, _ in enumerate(grid):
            for j, value in enumerate(grid[i]):
                if value == 1:
                    result = max(result, self.calcIslandArea((i, j), grid))

        return result
