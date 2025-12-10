class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        final = (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)

        def possible_directions(current):
            x, y = current
            directions = [(0, 1), (1, 0)]
            options = []

            for idx, direction in enumerate(directions):
                d_x, d_y = direction
                i, j = (x + d_x, y + d_y)

                if (
                    (0 <= i < len(obstacleGrid))
                    and (0 <= j < len(obstacleGrid[0]))
                    and obstacleGrid[i][j] != 1
                ):
                    options.append((i, j))

            return options

        if obstacleGrid[0][0] == 1:
            return 0

        memo = {}

        def unique_paths(current):
            if current == final:
                return 1

            if current in memo:
                return memo[current]

            value = 0
            for direction in possible_directions(current):
                i, j = direction
                returned = unique_paths((i, j))

                value += returned

            memo[current] = value

            return value

        return unique_paths((0, 0))
