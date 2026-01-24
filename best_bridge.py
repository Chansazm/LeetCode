from collections import deque

def best_bridge(grid):
    main_island = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            potential_island = traverse(grid, r, c, set())
            if len(potential_island) > 0:
                main_island = potential_island
                break
    
    visited = set(main_island)
    queue = deque([])
    
    
    for pos in main_island:
        r, c = pos
        queue.append((r,c, 0))
        
    while queue:
        r, c , distance = queue.popleft()
        if grid[r][c] == 'L' and (r,c) not in main_island:
            return distance - 1
        
        deltas = [(1,0),(-1,0),(0,1),(0,-1)]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = delta_row + r
            neighbor_col = delta_col + c
            neighbor_pos = (neighbor_row, neighbor_col)
            
            if is_inbounds(grid, neighbor_row, neighbor_col) and neighbor_pos not in visited:
                queue.append((neighbor_row, neighbor_col, distance + 1))
                visited.add(neighbor_pos)
                
    

def is_inbounds(grid,row,col):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])
    return row_inbounds and col_inbounds

def traverse(grid,row, col, visited):
    if not is_inbounds(grid, row, col) or grid[row][col] == 'W':
        return visited
    
    pos = row, col
    if pos in visited:
        return visited
    visited.add(pos)
    
    traverse(grid, row + 1, col, visited)
    traverse(grid, row - 1, col, visited)
    traverse(grid, row, col + 1, visited)
    traverse(grid, row, col - 1, visited)
    
    return visited

grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]

print(best_bridge(grid))# --> 1
    
    
    
    
    
    