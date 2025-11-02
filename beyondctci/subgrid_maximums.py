import math


def subgrid_maximums(grid: list[list[int]]) -> list[list[int]]:
    """
    For a MxN grid, this function computes the maximum value in each subgrid
    starting at (i, j) and extending to the bottom-right corner.
    Time Complexity: O(N*M)
    Space Complexity: O(N*M)

    https://start.interviewing.io/login?nextPath=%2Fbeyond-ctci%2Fpart-vii-catalog%2Fgrids-and-matrices
    """
    rows, cols = len(grid), len(grid[0])
    matrix = [[-math.inf for _ in range(cols)] for _ in range(rows)]

    def is_valid(a: int, b: int) -> bool:
        if a < 0 or b < 0:
            return False
        if a >= rows or b >= cols:
            return False
        return True

    # matrix[i][j] = max(grid[i][j], matrix[i+1][j], matrix[i][j+1])
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            options = [grid[i][j]]
            if is_valid(i + 1, j):
                options.append(matrix[i + 1][j])
            if is_valid(i, j + 1):
                options.append(matrix[i][j + 1])
            matrix[i][j] = max(options)

    return matrix


# Example 1:
# grid =  [[1, 5, 3],
#          [4,-1, 0],
#          [2, 0, 2]]
# Output: [[5, 5, 3],
#          [4, 2, 2],
#          [2, 2, 2]]
#
# Example 2:
# grid =  [[5]]
# Output: [[5]]
# Explanation: For a 1x1 grid, each cell's subgrid is just itself.
#
# Example 3:
# grid =  [[1, 2, 3]]
# Output: [[3, 3, 3]]
# Explanation: For a single row, each cell's subgrid includes all elements to its right.
#
# Constraints:

assert subgrid_maximums([[1, 5, 3], [4, -1, 0], [2, 0, 2]]) == [
    [5, 5, 3],
    [4, 2, 2],
    [2, 2, 2],
]
assert subgrid_maximums([[5]]) == [[5]]
assert subgrid_maximums([[1, 2, 3]]) == [[3, 3, 3]]
assert subgrid_maximums([[1], [2], [3]]) == [[3], [3], [3]]
assert subgrid_maximums([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9],
]
