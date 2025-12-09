from collections import deque
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
      start = (0,0)
      visited = set([])
      added = set([])
      final = (len(obstacleGrid) - 1, len(obstacleGrid[0]) -1)

      def possible_directions(current):
        x,y = current
        directions = [(0,1), (1,0)]
        options = []
        
        for idx,direction in enumerate(directions):
          d_x, d_y = direction
          i, j = (x + d_x, y + d_y)

          if (0 <= i < len(obstacleGrid)) and (0 <= j < len(obstacleGrid[0])) and ((i,j) not in visited) and obstacleGrid[i][j] != 1:
            options.append((i,j,idx))

        return options
      
      if obstacleGrid[0][0] == 1 : return 0

      memo =  {}

      def unique_paths(current):
        if current == final:
          return 1

        if current in memo: 
          return memo[current]

        value = 0
        for direction in possible_directions(current):
          i,j,idx = direction
          if memo.get((current[0], current[1], idx)):
            returned = memo[(current[0], current[1], idx)] 
          else:
            returned = unique_paths((i,j))

          value += returned

        memo[current] = value

        return value

  
      return unique_paths((0,0))

        