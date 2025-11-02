def subgrid_maximuns(grid):
    def valid_cells(i, j, pos):
        def is_valid(a, b):
            if a < 0 or b < 0:
                return False
            if a >= len(grid) or b >= len(grid[0]):
                return False

            return True

        for i in range(len(grid) - 1, 0, -1):
            for j in range(len(grid[0]) - 1, 0, -1):




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

assert subgrid_maximuns([[1, 5, 3], [4, -1, 0], [2, 0, 2]]) == [
    [5, 5, 3],
    [4, 2, 2],
    [2, 2, 2],
]
assert subgrid_maximuns([[5]]) == [[5]]
assert subgrid_maximuns([[1, 2, 3]]) == [[3, 3, 3]]
assert subgrid_maximuns([[1], [2], [3]]) == [[3], [3], [3]]
assert subgrid_maximuns([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9],
]
