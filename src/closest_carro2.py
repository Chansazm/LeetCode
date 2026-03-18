from collections import deque
def closest_carrot(grid, starting_row, starting_column):
    visited = set([(starting_row, starting_column)])
    queue = deque([(starting_row,starting_column,0)])
    
    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == 'C':
            return distance
        deltas = [(1,0),(-1,0),(0,1),(0,-1)]
        for delta in deltas:
           delta_row, delta_col = delta
           neighbor_row = delta_row + row
           neighbor_col = delta_col + col
           pos = (neighbor_row, neighbor_col)
           
           row_inbounds = 0 <= neighbor_row < len(grid)
           col_inbounds = 0 <= neighbor_col < len(grid[0])
           
           if row_inbounds and col_inbounds and grid[neighbor_row][neighbor_col] != 'X':
               queue.append((neighbor_row, neighbor_col, distance + 1))
               
           
           if pos not in visited:
               visited.add(pos)
               
               
           
    
    
    return -1


grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # -> 4