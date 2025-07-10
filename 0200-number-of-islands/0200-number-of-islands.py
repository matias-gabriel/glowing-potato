class Solution:
    def traverse(self, grid, position):
      position_i, position_j = position
      if grid[position_i][position_j] != "1":
        return
      else:
        grid[position_i][position_j] = 0

      len_grid_i = len(grid)
      len_grid_j = len(grid[0])

      positions_to_visit = []

      if position_i + 1 < len_grid_i:
         self.traverse(grid, (position_i + 1, position_j))
      if position_j + 1 < len_grid_j:
         self.traverse(grid, (position_i, position_j + 1))
      if position_i - 1 >= 0:
         self.traverse(grid, (position_i - 1, position_j))
      if position_j - 1 >= 0:
         self.traverse(grid, (position_i, position_j - 1))
      
    def numIslands(self, grid: List[List[str]]) -> int:
      result = 0
      for i, _ in enumerate(grid):
        for j, value in enumerate(grid[i]):
          if value == "1":
            result +=1
            self.traverse(grid, (i,j))

      return result
