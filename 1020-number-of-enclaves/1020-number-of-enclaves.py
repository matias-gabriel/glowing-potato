class Solution:
    ## Strategy
    ## We are going to run a dfs for each 1
    ## We can cache some with 2
    ## We want to run a dfs for e
    def numEnclaves(self, grid: List[List[int]]) -> int:
      visited = set({})

      def not_out_of_bounds(r,c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

      def get_valid_moves(r,c):
        moves = []
        is_enclaved = False
        directions = [(0,1), (1,0),(0,-1), (-1,0)]

        for x, y in directions:
          new_r= r+x
          new_c = c+y

          if not_out_of_bounds(new_r,new_c):
            if grid[new_r][new_c] != 0:
              moves.append((new_r , new_c))
          else:
            is_enclaved = True

        return (is_enclaved, moves)

      def dfs(r,c, visited):
        visited.add((r,c))

        is_enclaved, moves = get_valid_moves(r,c)

        total = 0
        for x,y in moves:
          if (x,y) not in visited:
            is_e, count = dfs(x,y,visited) 
            is_enclaved = is_e or is_enclaved
            total+= count

        if not is_enclaved: return (is_enclaved, total+1)

        return (is_enclaved, 0)


      results = 0

      for r, _ in enumerate(grid):
        for c, value in enumerate(grid[r]):
          if value != 0 and (r,c) not in visited:
            visited.add((r,c))
            is_enclaved, count = dfs(r,c,visited)
            results+= count 

      return results








        


        