def minimum_island_count(grid):
    visited = set()
    count = 1
    minimum_count = float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited) == True:
                count += 1
                if count < minimum_count:
                    minimum_count = count
    return minimum_count
            

def explore(grid, r, c, visited):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])
    
    if not row_inbound or not col_inbound:
        return False
    
    if grid[r][c] == 'W':
        return False
    
    pos = r, c
    if pos in visited:
        return False
    visited.add(pos)
    
    explore(grid, r+1, c, visited)
    explore(grid, r-1, c, visited)
    explore(grid, r, c+1, visited)
    explore(grid, r, c-1, visited)
    
    return True
    

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island_count(grid)) # -> 2
    