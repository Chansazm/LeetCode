from collections import deque
def closest_carrot(grid,r,c):
    visited = set(r,c)
  
    minimum_distance = float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            distance = explore(grid, r,c)
            if distance < minimum_distance:
                minimum_distance = distance
    return distance
    

def explore(grid, r,c, visited):
    pos = (r,c)
    queue = deque([pos,0])
    
    while queue:
        current, distance = queue.popleft()
        
        #already visited
        if current in visited:
            return 0
        if current == 'X':
            return 0
        if current == 'O':
            return 0
        if current == 'C':
            return distance
        for neighbor in grid[current]:
            queue.append(neighbor, distance + 1)
    return 0

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # -> 4
            
        
    
    
    
    