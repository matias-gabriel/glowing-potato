from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_queue = deque([])
        max_minutes = 0

        for i,_ in enumerate(grid):
            for j, value in enumerate(grid[i]):
                if value == 2:
                    rotten_queue.append((i,j, 0))

        while rotten_queue:
            current = rotten_queue.popleft()
            i,j, t = current
            max_minutes = max(max_minutes, t)

            to_visit = []

            if i + 1 < len(grid):
                to_visit.append((i+1, j))
            if j + 1 < len(grid[0]):
                to_visit.append((i, j+1))
            if i - 1 >= 0:
                to_visit.append((i-1, j))
            if j - 1 >= 0 :
                to_visit.append((i, j-1))

            for v in to_visit:
                if grid[v[0]][v[1]] == 1:
                    grid[v[0]][v[1]] = 2
                    rotten_queue.append((v[0], v[1], t + 1))


        for i in grid:
            for j in i:
                if j == 1:
                    return -1

        return max_minutes

            


        

        
        