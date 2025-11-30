class Solution:
  def spiralOrder(self, matrix):
    # What makes me change the direction?
    # out of bound, or visited, or visited directions
    # [0, 1] -> right
    # [1, 0] -> down
    # [0, -1] -> left
    # [-1, 0] -> up
    
    # right-> 1,2,3, down -> 6,9 -> left, 8, 7 -> up -> 4
    directions = [[0,1], [1,0], [0, -1], [-1, 0]]
    direction = [0,1]
    position = (0,0)

    output = []
    visited = set([])

    def is_valid(pos):
      return pos not in visited and 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0])

    def get_next_direction(pos):
      directions.append(directions.pop(0))

      while direction != directions[0]:
        new_direction = directions[0]
        new_position = (pos[0] + new_direction[0], pos[1] + new_direction[1])
        if is_valid(new_position):
          return new_direction

        directions.append(directions.pop(0))

      return None

    while position:
      visited.add(position)
      output.append(matrix[position[0]][position[1]])

      print(direction)
      if direction:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if is_valid(new_position):
          position = new_position
          continue
        else:
          direction = get_next_direction(position)
          if direction:
            position = (position[0] + direction[0], position[1] + direction[1])
          else:
            break
      else:
        break

    return output

      
    
      